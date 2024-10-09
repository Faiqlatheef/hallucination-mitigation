from utils import get_wikipedia_summary
import re

def extract_factual_statements(text):
    """
    Extracts factual statements from the generated text.
    This is a simplistic approach using sentence tokenization.
    """
    sentences = sent_tokenize(text)
    # In production, use more sophisticated methods or NLP techniques
    return sentences

def verify_facts(statements):
    """
    Verifies each statement by checking its presence in Wikipedia summaries.
    Returns a list of verified statements.
    """
    verified = []
    for stmt in statements:
        # Extract key entities or keywords for verification
        # Simplistic approach: use the first noun phrase
        words = stmt.split()
        if not words:
            continue
        query = words[0]
        retrieved = get_wikipedia_summary(query)
        # Check if the statement is a substring of the retrieved info
        if stmt in retrieved:
            verified.append(stmt)
        else:
            verified.append(f"UNVERIFIED: {stmt}")
    return verified
