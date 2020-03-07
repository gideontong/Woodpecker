import smtplib, ssl

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465
password = "password"

sender_email = "example@example.com"  # Enter your address
receiver_email = "example@example.com"  # Enter receiver address
message = MIMEMultipart("alternative")
message["Subject"] = "test"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
This is a test by Gideon"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("example.com", port, context=context) as server:
    server.login(username, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )