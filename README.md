# Gen AI Playground

A small LangChain-based GenAI project for experimenting with chat models, structured extraction, and embeddings using Mistral, OpenAI, and Hugging Face models.

This workspace includes multiple demo scripts and Streamlit interfaces for testing different AI workflows in a lightweight setup.

## Overview

The project is organized into a few key areas:

- `chatmodels/` — conversational AI experiments and interactive chat apps.
- `CineSage/` — movie information extraction demos.
- `embeddingmodels/` — embedding generation experiments.
- `requirements.txt` — Python dependencies.

## Project Structure

```text
Gen AI/
├── README.md
├── requirements.txt
├── .env
├── chatmodels/
│   ├── chat.py
│   ├── chatbot.py
│   ├── localmodel.py
│   ├── UI_chatbot.py
│   └── hugging_face.py
├── CineSage/
│   ├── core.py
│   └── UI_core.py
└── embeddingmodels/
    ├── embeddings.py
    └── huggingface_embeddings.py
```

## Features

### 1. Mood-based AI chat agent
The project includes a CLI chat experience and a Streamlit UI where the model can respond in different moods:

- Angry
- Funny
- Sad

Files:
- `chatmodels/chatbot.py`
- `chatmodels/UI_chatbot.py`

### 2. Movie information extraction
A LangChain prompt + Pydantic schema is used to extract movie details from a paragraph and return structured JSON-like output.

Files:
- `CineSage/core.py`
- `CineSage/UI_core.py`

### 3. Embedding experiments
The project tests embedding generation with OpenAI and Hugging Face models for semantic similarity tasks and vector representation experiments.

Files:
- `embeddingmodels/embeddings.py`
- `embeddingmodels/huggingface_embeddings.py`

### 4. Local Hugging Face model experimentation
A local pipeline example is included to run a Hugging Face text-generation model.

File:
- `chatmodels/localmodel.py`

## Tech Stack

- Python 3.x
- LangChain
- LangChain Community
- LangChain OpenAI
- LangChain Mistral
- LangChain Hugging Face
- Streamlit
- Pydantic
- Python-dotenv

## Setup

1. Clone the repository.
2. Create a virtual environment (optional but recommended):

```bash
python -m venv .venv
```

3. Activate the environment:

On Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root and add your API keys as needed. This project uses models from Mistral and OpenAI, so your environment may need keys such as:

```env
OPENAI_API_KEY=your_openai_key
MISTRAL_API_KEY=your_mistral_key
```

Depending on the script, additional provider-specific keys may also be required.

## Running the Applications

### CLI chat bot
```bash
python chatmodels/chatbot.py
```

### Simple Mistral chat example
```bash
python chatmodels/chat.py
```

### Hugging Face text generation example
```bash
python chatmodels/hugging_face.py
```

### Local Hugging Face pipeline
```bash
python chatmodels/localmodel.py
```

### Streamlit mood chat app
```bash
streamlit run chatmodels/UI_chatbot.py
```

### Streamlit movie extractor
```bash
streamlit run CineSage/UI_core.py
```

### Embedding examples
```bash
python embeddingmodels/embeddings.py
python embeddingmodels/huggingface_embeddings.py
```

## Notes

- Some scripts are experimental and intended for learning or prototyping.
- Model availability depends on your API keys and internet connectivity.
- The project includes both terminal-based and UI-based examples for testing different LLM integration patterns.
- If you are using a local or restricted environment, some model providers may require authentication or quota access.

## Use Cases

This repository is useful for:

- Testing LangChain model integrations
- Building simple AI chat interfaces
- Running prompt-based structured extraction
- Exploring text embeddings and semantic representations
- Prototyping GenAI ideas quickly in Python

## License

This project does not currently include a specific license file. If you plan to share or distribute it publicly, consider adding a license such as MIT or Apache 2.0.

## Future Improvements

Potential next steps:

- Add a unified app interface
- Add error handling and configuration management
- Add a database or vector store for retrieval systems
- Add tests for model wrappers and prompt logic
- Add documentation for each module

## Contributing

This project is a learning/demo workspace. Contributions are welcome if you want to expand model support, improve UI design, or add reusable utilities.
