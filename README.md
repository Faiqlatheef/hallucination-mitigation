# Hallucination Mitigation in Large Language Models

## Overview

This project implements techniques to reduce hallucinations in Large Language Models (LLMs) by integrating Grounded Generation, Fact Verification, Output Calibration, and Prompt Engineering.

## Features

- **Grounded Generation**: Retrieves relevant information from Wikipedia to ground the LLM's responses.
- **Fact Verification**: Cross-checks generated statements against reliable sources.
- **Output Calibration**: Allows the model to express uncertainty when necessary.
- **Prompt Engineering**: Crafts prompts that guide the LLM towards accurate and reliable responses.

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Faiqlatheef/hallucination-mitigation.git
   cd hallucination-mitigation

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

3. **Configure Environment Variables**
   
   Set your OpenAI API key:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'

4. **Usage**

   Run the main script with predefined test prompts:
    ```bash
    python main.py

