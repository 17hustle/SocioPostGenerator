# PostGen: Automated Post Generator

## Overview
PostGen is a Python-based project designed to generate social media posts using a few-shot learning approach. The project processes raw posts, extracts metadata, and uses an LLM (Large Language Model) to generate new posts.

## Features
- **Few-Shot Learning**: Utilize existing post examples for style and content.
- **LLM Integration**: Powered by Groq's ChatGPT API for generating posts.
- **Metadata Extraction**: Automatically extracts tags, language, and line counts from raw posts.


## Setup Instructions
1. Clone the repository.
2. Install dependencies:
  pip install -r requirements.txt
3. Set up environment variables:
  GROQ_API_KEY=your_api_key_here
4. Run the main script:
  python src/main.py

