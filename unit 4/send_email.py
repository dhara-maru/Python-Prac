import smtplib
from email.mime.text import MIMEText

def send_email(sender_email, recipient_email, subject, message, smtp_server, smtp_port, smtp_username, smtp_password):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())

sender_email = "dharahetvimaru@gmail.com"
recipient_email = "dhaara47@gmail.com"
subject = "Test Subject"
message = "This is a test email."

smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "dharahetvimaru@gmail.com"
smtp_password = "123456"

send_email(sender_email, recipient_email, subject, message, smtp_server, smtp_port, smtp_username, smtp_password)
