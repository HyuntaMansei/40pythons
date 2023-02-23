import imaplib
import email
from email import policy

def find_encoding_info(txt):
    info = email.header.decode_header(txt)
    subject, encode = info[0]
    return subject, encode

imap = imaplib.IMAP4_SSL('imap.naver.com')
sender_email = '@naver.com'
sender_pwd = '!'

imap.login(sender_email, sender_pwd)
imap.select('INBOX')
resp, data = imap.uid('search', None, 'All')
all_email = data[0].split()
last_email = all_email[-5:]

for mail in reversed(last_email):
    result, data = imap.uid('fetch', mail, '(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email, policy=policy.default)

    print('='*70)
    print('From:', email_message['From'])
    print('Sender:', email_message['Sender'])
    print('To:', email_message['To'])
    print('Date:', email_message['Date'])
    # print('Subject:', email_message['Subject'])
    subject, encode = find_encoding_info(email_message['Subject'])
    print('Subject:', subject)
    print("Contents")
    message = ''
    # if email_message.is_multipart():
    for part in email_message.get_payload():
        if part.get_content_type() == 'text/plain':
            bytes = part.get_payload(decode=True)
            encode = part.get_content_charset()
            message = message + str(bytes,encode)
    print(message)
    print('='*70)

imap.close()
imap.logout()