# Support Telegram bot

## How to install

- Create virtula environment and install all dependencies:
  ```console
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```
- [Create a DialogFlow Agent](https://dialogflow.cloud.google.com/#/newAgent) to communicate with users [Docs](https://cloud.google.com/dialogflow/es/docs/quick/build-agent).
- [Install the gcloud CLI](https://cloud.google.com/sdk/docs/install)
- [Initialize the Google Cloud CLI](https://cloud.google.com/dialogflow/es/docs/quick/setup#sdk)
- [Enable API](https://cloud.google.com/dialogflow/es/docs/quick/setup#api) for your newly created DialogFLow agent.
- Create an [API key](https://cloud.google.com/docs/authentication/api-keys#create)
- [Provide user credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc#google-idp) for your Google Account
- Run your project:
  ```console
  python3 manage.py runserver
  python3 migrate
  ```
- [Enable API](https://console.cloud.google.com/apis/api/apikeys.googleapis.com/)
- Create API key and save it to `.env` with Google App credentials:
  ```console
  python3 manage.py create_api_key
  ```
