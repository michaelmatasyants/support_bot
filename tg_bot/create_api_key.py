from pathlib import Path

from django.conf import settings
from google.cloud import api_keys_v2


def create_api_key(project_id: str, suffix: str) -> api_keys_v2.Key:
    """
    Creates and restrict an API key. Add the suffix for uniqueness.

    TODO(Developer):
    1. Before running this sample,
      set up ADC as described in https://cloud.google.com/docs/authentication/external/set-up-adc
    2. Make sure you have the necessary permission to create API keys.

    Args:
        project_id: Google Cloud project id.

    Returns:
        response: Returns the created API Key.
    """
    client = api_keys_v2.ApiKeysClient()

    key = api_keys_v2.Key()
    key.display_name = f"My first API key - {suffix}"

    # Initialize request and set arguments.
    request = api_keys_v2.CreateKeyRequest()
    request.parent = f"projects/{project_id}/locations/global"
    request.key = key

    # Make the request and wait for the operation to complete.
    response = client.create_key(request=request).result()

    print(f"Successfully created an API key: {response.name}")
    # For authenticating with the API key, use the value in "response.key_string".
    # To restrict the usage of this API key, use the value in "response.name".
    return response


def main():
    api_key = create_api_key(project_id=settings.GOOGLE_PROJECT_ID,
                             suffix="Keyname")
    credential_path = Path(Path.home(),
                           ".config",
                           "gcloud",
                           "application_default_credentials.json")
    if credential_path.exists():
        with open(".env", "a") as file:
            file.write(f"\nDIALOGFLOW_TOKEN={api_key.key_string}")
            file.write(f"\nGOOGLE_APP_CREDENTIALS={credential_path}")
        print("DIALOGFLOW_TOKEN and GOOGLE_APP_CREDENTIALS",
              "have been saved to .env")
    else:
        print("Something went wrong.")
