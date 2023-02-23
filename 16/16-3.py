import imaplib
import email
from email import policy
import json
import requests

def find_encoding_info(txt):
    info = email.header.decode_header(txt)
    subject, encode = info[0]
    return subject, encode

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

imap = imaplib.IMAP4_SSL('imap.naver.com')
sender_email = '@naver.com'
sender_pwd = '!@'

imap.login(sender_email, sender_pwd)
imap.select('INBOX')
resp, data = imap.uid('search', None, 'All')
all_email = data[0].split()
last_email = all_email[-100:]

for mail in reversed(last_email):
    result, data = imap.uid('fetch', mail, '(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email, policy=policy.default)

    email_from = email_message["From"]
    email_date = email_message["Date"]
    email_subject, encode = find_encoding_info(email_message['Subject'])

    subject_str = str(email_subject)
    if subject_str.find('내역') > 0:
        print(email_subject)
        message = ''
        if email_message.is_multipart():
            for part in email_message.get_payload():
                if part.get_content_type() == 'text/plain':
                    bytes = part.get_payload(decode=True)
                    encode = part.get_content_charset()
                    message = message + str(bytes,encode)
        slack_msg = email_from + '\n' + email_date + '\n' + message
        print(slack_msg)
        send_msg_slack_webhook(slack_msg)

imap.close()
imap.logout()