#!/bin/sh

# Activate the virtual environment
source /opt/support_bot/venv/bin/activate

# install requiremnts for the venv
pip install -r requirements.txt

# Start Django
python3 /opt/support_bot/manage.py runserver &

# Train the dialog flow
python3 /opt/support_bot/manage.py train &

# Start Telegram Bot
python3 /opt/support_bot/manage.py run_tg_bot &

# Start VK Bot
python3 /opt/support_bot/manage.py run_vk_bot &

wait