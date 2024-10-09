def construct_prompt(user_prompt, retrieved_info):
    """
    Constructs a prompt that includes retrieved information to ground the LLM's response.
    """
    prompt = (
        f"You are an AI assistant. Use the following information to answer the question accurately.\n\n"
        f"Retrieved Information:\n{retrieved_info}\n\n"
        f"Question: {user_prompt}\n\n"
        f"Answer:"
    )
    return prompt
