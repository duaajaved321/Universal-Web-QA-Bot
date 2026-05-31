# 🌐 Universal Web QA Bot (AI Research Assistant)

## Live Demo Link: https://huggingface.co/spaces/duaajaved321/MSDSF24M005_ver1?logs=container

## 📖 Project Overview
The Universal Web QA Bot is an interactive AI application that allows users to instantly chat with any webpage. By simply inputting a URL and a question, the system dynamically scrapes the target site, cleans the HTML payload, and leverages a Large Language Model (LLM) to provide highly accurate, context-aware answers based strictly on the webpage's content.

This project serves as a lightweight **Retrieval-Augmented Generation (RAG)** pipeline, demonstrating how to bridge the gap between live web data and generative AI.

## 🛠️ Tech Stack
* **Language:** Python
* **LLM Engine:** Groq API (Meta Llama 3.3 70B)
* **Web Scraping:** ZenRows API, `requests`
* **HTML Parsing:** BeautifulSoup4
* **User Interface:** Gradio

---

## 🚀 How It Works (The Pipeline)

### 1. Dynamic Web Scraping & Ingestion
* Utilizes the **ZenRows API** to execute JS-rendered scraping and bypass anti-bot protections (Cloudflare, CAPTCHAs) using premium proxies.
* Handles HTTP connection errors and timeouts gracefully to ensure pipeline stability.

### 2. Content Extraction & Sanitization
* Uses **BeautifulSoup4** to parse the raw DOM.
* Strips out noisy, non-content HTML tags (e.g., `<script>`, `<style>`, `<nav>`, `<footer>`) using `.decompose()`.
* Formats the remaining DOM into clean, continuous text strings and truncates the payload to ensure it fits within the LLM's maximum context window limit.

### 3. Context-Aware AI Generation
* Integrates the **Groq API** to utilize the ultra-fast `llama-3.3-70b-versatile` model.
* Uses precise **System Prompts** to restrict the AI's knowledge base. The model is instructed to act as a "Professional Web Analyst" and answer the user's question *only* using the dynamically scraped text context, effectively eliminating AI hallucinations.

### 4. Interactive User Interface
* Built a modern, responsive front-end using **Gradio** (`gr.Blocks`).
* Features a clean two-column layout for URL/Question inputs and an isolated output box for the AI's analytical response.

---

## 🧠 Key Concepts & Skills Learned
1. **LLM Integration & Prompt Engineering:** Learning how to constrain a Large Language Model's outputs by providing strict system prompts and dynamic context.
2. **Modern Web Scraping:** Moving beyond simple `requests.get()` to handle modern web architecture (JavaScript rendering and bot-protection) using specialized APIs like ZenRows.
3. **Data Sanitization:** Understanding that AI models perform better when HTML payloads are stripped of semantic noise and structural code.
4. **Rapid UI Prototyping:** Using Gradio to quickly deploy Python scripts into fully functional, sharable web applications without needing to write HTML/CSS/React.
