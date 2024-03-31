# Support bot

## How to install
- Add Secret key for django
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
- [Enable API](https://console.cloud.google.com/apis/api/apikeys.googleapis.com/)
- Run your project:
  ```console
  python3 manage.py runserver
  python3 migrate
  ```


## How to run tg bot
- Create API key and save it to `.env` with Google App credentials.
  Run
  ```console
  python3 manage.py create_api_key
  ```

- If you want to train your own dialog flow by creating new intent:
  - Open `train_dialogflow.json`
  - Edit it like is shown in `train_dialogflow_example.json`.

  You can specify as many scripts as you need.

- Train dialog_flow.<br>
  Train with use of already written questions and answers or with use of file, you've edited on last step.
  ```console
  python3 manage.py train
  ```
  There is no need of retraining the dialog flow every time you run the telegram bot. This step must be repeted only when you want to update script (questions and answers) for your telegram bot.

- Create telegram bot using `@BotFather` bot in telegram and save it's token in an `.env` file under the name `TG_BOT_TOKEN`, as shown in `.env.example`.

- Run your telegram bot:
  ```
  python3 manage.py run_tg_bot
  ```

## How to run vk bot
- [Create your own vk](https://vk.com/) group and save the token in an `.env` file under the name `VK_GROUP_TOKEN`, as shown in `.env.example`.
- Allow your group to send messages in settings of the group.
- Run your vk bot
  ```console
  python3 manage.py run_vk_bot
  ```
