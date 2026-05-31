
import os
import requests
from bs4 import BeautifulSoup
from groq import Groq
import gradio as gr

# Setup using Hugging Face Secrets (Environment Variables)
ZENROWS_KEY = os.environ.get("ZENROWS_KEY")
GROQ_KEY = os.environ.get("GROQ_KEY")

client = Groq(api_key=GROQ_KEY)

def dynamic_scraper(url):
    params = {
        "apikey": ZENROWS_KEY,
        "url": url,
        "js_render": "true",
        "premium_proxy": "true",
    }
    try:
        response = requests.get("https://api.zenrows.com/v1/", params=params, timeout=30)
        if response.status_code != 200:
            return f"Error: Status code {response.status_code}"

        soup = BeautifulSoup(response.text, "html.parser")
        for junk in soup(["script", "style", "nav", "footer", "header"]):
            junk.decompose()

        text = soup.get_text(separator=" ")
        clean_lines = [line.strip() for line in text.splitlines() if line.strip()]
        return " ".join(clean_lines)[:10000]
    except Exception as e:
        return f"Failed to connect: {str(e)}"

def ask_about_url(url, question):
    if not url.startswith("http"):
        return "❌ Please enter a valid URL (https://...)"

    context = dynamic_scraper(url)
    if "Error" in context or "Failed" in context:
        return context

    system_prompt = f"You are a professional Web Analyst. Use ONLY the following content:\n\n{context}"

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]
    )
    return completion.choices[0].message.content

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🌐 Universal Web QA Bot (V1)")
    with gr.Row():
        url_box = gr.Textbox(label="Target URL")
        q_box = gr.Textbox(label="Your Question")
    output_box = gr.Textbox(label="AI Analysis", lines=10)
    submit_btn = gr.Button("Analyze Website", variant="primary")
    submit_btn.click(fn=ask_about_url, inputs=[url_box, q_box], outputs=output_box)

demo.launch()
