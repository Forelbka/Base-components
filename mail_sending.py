import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

to = 'ivan-8180@yandex.ru'
text = 'Hello'
subject = 'test'

Email_password = '"}Rr*:fQ3a2tQe,'

email_sender = 'no-reply@cos-podarok.ru'
msg = MIMEMultipart()
msg['From'] = email_sender
msg['To'] = to
msg['Subject'] = subject
msg.attach(MIMEText(text, 'plain'))
server = smtplib.SMTP_SSL('mail.cos-podarok.ru', 465)
server.login(email_sender, Email_password)
server.auth_plain()
server.send_message(msg)
server.quit()