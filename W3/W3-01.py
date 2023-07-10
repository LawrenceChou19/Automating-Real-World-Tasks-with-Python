import smtplib

from email.message import EmailMessage
message = EmailMessage()
# message['Subject'] = "test mail"
print(message)
sender = "me@example.com"
recipient = "you@example.com"


message['From'] = sender
message['To'] = recipient
print(message)
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
print(message)
body = """Hey there!
...
... I'm learning to send emails using Python!"""
message.set_content(body)
print(message)