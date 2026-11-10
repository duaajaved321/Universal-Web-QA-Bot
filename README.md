# Universal Web QA Bot

An interactive webpage question-answering prototype. A user provides a webpage URL and a question; the application fetches the page content, extracts readable text, and sends that context to an LLM to generate an answer.

**Live demo:** https://huggingface.co/spaces/duaajaved321/MSDSF24M005_ver1?logs=container

## How It Works

1. Accepts a webpage URL and a user question through a Gradio interface.
2. Uses the ZenRows API to retrieve the webpage, including JavaScript-rendered content.
3. Parses the returned HTML with BeautifulSoup and removes non-content elements such as scripts, styles, navigation, and footer sections.
4. Truncates the extracted text to a fixed 10,000-character context window.
5. Sends the page text and question to Groq's Llama model, with instructions to answer using the supplied context.
6. Displays the generated answer in the Gradio interface.

## Technology Stack

- Python
- Gradio
- Groq API — Llama 3.3 70B Versatile
- ZenRows API
- Requests
- BeautifulSoup4

## Run Locally

1. Clone this repository.
2. Install the dependencies used by the application:

   ```bash
   pip install gradio groq requests beautifulsoup4
   ```

3. Configure the following environment variables:

   - `ZENROWS_KEY`
   - `GROQ_KEY`

4. Run:

   ```bash
   python "app (1).py"
   ```

## Architecture and Scope

This implementation is a **context-grounded webpage Q&A prototype**, not a full vector-retrieval RAG pipeline. It does not currently implement document chunking, embedding generation, a vector database, top-k semantic retrieval, or retrieval evaluation. Instead, the extracted page text is passed directly to the LLM as context.

The system prompt encourages answers to stay grounded in the provided page text, but prompting alone cannot guarantee that every answer is correct or free from hallucinations.

## Limitations and Next Improvements

- Add URL validation and network access restrictions before accepting arbitrary URLs.
- Improve scraping and extraction error handling.
- Replace fixed character truncation with structure-aware chunking.
- Add embeddings, semantic retrieval, and source-level citations.
- Evaluate answer faithfulness and retrieval quality on a prepared test set.
- Add automated tests and a reproducible dependency file.

This is an educational prototype. Answers should be checked against the original webpage.
