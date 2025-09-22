# slack_client.py
import os
import requests

# Pegue esse Webhook URL no seu app Slack (Incoming Webhook)
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL") or "https://hooks.slack.com/services/..."

def send_slack_message(text):
    payload = {"text": text}
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)
    if response.status_code == 200:
        print("📨 Mensagem enviada ao Slack!")
    else:
        print(f"Erro ao enviar mensagem Slack: {response.status_code} - {response.text}")