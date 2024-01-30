"Functions to use dialog flow"

from google.cloud import dialogflow


def detect_intent_texts(project_id: str, session_id: str, text: str) -> str:
    """Returns the result of detect intent with text.
    Using the same `session_id` between requests allows continuation
    of the conversation."""

    session_client = dialogflow.SessionsClient()
    session_path = session_client.session_path(project_id, session_id)
    text_input = dialogflow.TextInput(text=text,
                                      language_code="ru-RU")
    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session_path, "query_input": query_input}
    )
    return response.query_result.fulfillment_text
