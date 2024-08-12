"Functions to use dialog flow"

import json
from pathlib import Path
from django.conf import settings

from google.api_core import exceptions
from google.cloud.dialogflow import (AgentsClient, Intent, IntentsClient,
                                     QueryInput, SessionsClient, TextInput)


def create_fallback_intent(message_texts: str = "Fallback text message"):
    """Create a fallback intent with custom messages."""
    intents_client = IntentsClient()
    parent = AgentsClient.agent_path(settings.GOOGLE_PROJECT_ID)
    message = Intent.Message(text=Intent.Message.Text(text=[message_texts]))

    intent = Intent(
        display_name="Fallback intent",
        messages=[message],
        is_fallback=True
    )

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )


def detect_intent_texts(project_id: str,
                        session_id: str,
                        text: str,
                        fallback: bool) -> str:
    """Returns the result of detect intent with text.
    Using the same `session_id` between requests allows continuation
    of the conversation.

    If there are no scripts in dialog flow for recived message and
        - fallback = True returns "Try one more time" text
        - fallback = False returns "We've forwarded your request"
    """

    session_client = SessionsClient()
    session_cl_path = session_client.session_path(project_id, session_id)
    text_input = TextInput(text=text, language_code="ru-RU")
    query_input = QueryInput(text=text_input)
    response = session_client.detect_intent(
        request={
            "session": session_cl_path,
            "query_input": query_input
        }
    )
    print(response)
    if fallback:
        return response.query_result.fulfillment_text
    else:
        if not response.query_result.intent.is_fallback:
            return response.query_result.fulfillment_text
        else:
            return "Ваш запрос передан оператору службы поддержки"


def create_intents() -> None:
    """Creates an intents with adding training script from json file
    named train_dialog_flow.json located in bot app"""
    intents_client = IntentsClient()
    parent = AgentsClient.agent_path(settings.GOOGLE_PROJECT_ID)
    create_fallback_intent()

    with open(Path("tg_bot", "train_dialogflow.json"), "r") as f:
        training_scripts = json.load(f)
    for intent_name, qa in training_scripts.items():
        training_phrases: list[str] = qa.get("questions")
        reply_text: str = qa.get("answer")
        df_training_phrases = [
            Intent.TrainingPhrase(parts=[
                Intent.TrainingPhrase.Part(text=phrase)
            ])
            for phrase in training_phrases
        ]
        reply_message = Intent.Message(
            text=Intent.Message.Text(text=[reply_text])
        )
        try:
            intent = Intent(display_name=intent_name,
                            training_phrases=df_training_phrases,
                            messages=[reply_message])
            response = intents_client.create_intent(
                request={"parent": parent, "intent": intent}
            )
        except exceptions.InvalidArgument:
            print(f"Intent with display name '{intent_name}' already exists")
            continue
        print(f"Intent created: {response}")