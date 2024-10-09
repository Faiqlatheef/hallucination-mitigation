from utils import get_wikipedia_summary

def grounded_generation(user_prompt):
    """
    Retrieves relevant information from Wikipedia based on the user prompt.
    """
    # Simple keyword extraction could be implemented here
    # For demonstration, using the first noun as the query
    # In production, consider more robust methods or user input
    query = user_prompt.split()[0]  # Simplistic approach
    summary = get_wikipedia_summary(query)
    return summary
