"Functions to use dialog flow"

import json
from pathlib import Path

from google.api_core import exceptions
from google.cloud.dialogflow import (
    AgentsClient,
    Intent,
    IntentsClient,
    QueryInput,
    SessionsClient,
    TextInput,
)


def detect_intent_texts(project_id: str, session_id: str, text: str) -> str:
    """Returns the result of detect intent with text.
    Using the same `session_id` between requests allows continuation
    of the conversation."""

    session_client = SessionsClient()
    session_path = session_client.session_path(project_id, session_id)
    text_input = TextInput(text=text, language_code="ru-RU")
    query_input = QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session_path, "query_input": query_input}
    )
    return response.query_result.fulfillment_text


def create_intents(project_id: str) -> None:
    """Creates an intents with adding training script from json file
    named train_dialog_flow.json located in bot app"""
    intents_client = IntentsClient()
    parent = AgentsClient.agent_path(project_id)

    with open(Path("bot", "train_dialogflow.json"), "r") as f:
        training_scripts = json.load(f)
    for intent_name, qa in training_scripts.items():
        training_phrases: list[str] = qa.get("questions")
        reply_text: list[str] = qa.get("answer")
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
