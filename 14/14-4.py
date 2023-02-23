import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

sender_email = '@naver.com'
sender_pwd = ''
recver_email = '@naver.com'

smtp_name = "smtp.naver.com"
smtp_port = 587

msg = MIMEMultipart()

html="""
<!-- #######  THIS IS A COMMENT - Visible only in the source editor #########-->
<h2>이렇게 이쁜 메일도 쓸 수가 있습니다.&nbsp;</h2>
<p>메일 보내는 서버를 만들어 두면, 죽고나서도 <strong>메일을 보낼 수 있겠구나.&nbsp;</strong></p>
<p><strong>야.. 그런데 양식이 나쁘지 않은데? 첨부도 여기서 하면 되나?&nbsp;</strong></p>
<p style="font-size: 1.5em;">You can <strong style="background-color: #317399; padding: 0 5px; color: #fff;">type your text</strong> directly in the editor or paste it from a Word Doc, PDF, Excel etc.</p>
<p style="font-size: 1.5em;">The <strong>visual editor</strong> on the right and the <strong>source editor</strong> on the left are linked together and the changes are reflected in the other one as you type! <img src="https://html5-editor.net/images/smiley.png" alt="smiley" /></p>
<table class="editorDemoTable">
<tbody>
<tr>
<td><strong>Name</strong></td>
<td><strong>City</strong></td>
<td><strong>Age</strong></td>
</tr>
<tr>
<td>John</td>
<td>Chicago</td>
<td>23. Face recognition</td>
</tr>
<tr>
<td>Lucy</td>
<td>Wisconsin</td>
<td>19</td>
</tr>
<tr>
<td>Amanda</td>
<td>Madison</td>
<td>22. OCR</td>
</tr>
</tbody>
</table>
<p>This is a table you can experiment with.</p>
<p>&nbsp;</p>
"""
msg.attach(MIMEText(html, 'html'))
msg['Subject'] = '자동으로 보내는 편지2'
msg['From'] = sender_email
msg['To'] = recver_email

with open('attach_file.txt', 'rb') as f:
    etc_part = MIMEApplication(f.read())
    etc_part.add_header('Content-Dispostion', 'attachment', filename='attach_file.txt')
    msg.attach(etc_part)

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(sender_email, sender_pwd)
s.sendmail(sender_email, recver_email, msg.as_string())
s.quit()



