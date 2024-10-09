import os
import openai
import wikipedia
import nltk
from nltk.tokenize import sent_tokenize

# Download NLTK data if not already present
nltk.download('punkt')

# Initialize OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_wikipedia_summary(query, sentences=3):
    try:
        summary = wikipedia.summary(query, sentences=sentences)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        # Choose the first option in case of ambiguity
        summary = wikipedia.summary(e.options[0], sentences=sentences)
        return summary
    except wikipedia.exceptions.PageError:
        return "No relevant Wikipedia page found."

def call_openai_api(prompt, temperature=0.2, max_tokens=500):
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can choose a suitable model
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()
