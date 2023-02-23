import smtplib
from email.mime.text import MIMEText

send_email = '@naver.com'
send_pwd = ''

recv_email = '@naver.com'

smtp_name = 'smtp.naver.com'
smtp_port = 587

text = """
안녕하신가!
오늘도 좋은 하루 보내셨는지? 
조금더 성공하고 싶구나.
"""

msg = MIMEText(text)

msg['Subject'] = "나에게 보내는 편지"
msg['From'] = send_email
msg['To'] = recv_email
print(msg.as_string())

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()

