def build_conversation_prompt(
    history: list,
    current_question: str,
):
    """
    Build an LLM prompt using conversation history.
    The current question is excluded from history to avoid duplication.
    """

    prompt = (
        "You are a helpful AI assistant.\n\n"
        "Use the previous conversation when answering.\n\n"
    )

    if history:

        prompt += "Previous Conversation:\n\n"

        # Exclude the latest user message
        previous_history = history[:-1]

        for message in previous_history:

            role = message["role"].capitalize()

            prompt += (
                f"{role}: "
                f"{message['content']}\n\n"
            )

    prompt += (
        "Current User Question:\n"
        f"{current_question}"
    )

    return prompt