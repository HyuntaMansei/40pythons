import requests
import json

def send_msg_slack_webhook(msg):
    slack_webhook_url = \
        'https://hooks.slack.com/services/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'
    headers = {
        'Content-type' : 'application/json'
    }
    data = {
        'text' : msg
    }
    req = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))
    
    if req.status_code == 200:
        return "Ok"
    else:
        return "Error"

send_msg_slack_webhook("Yeah, me too")