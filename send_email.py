import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration for iChat (replace with your iChat settings)
smtp_server = 'smtp-mail.outlook.com'  # Replace with your iChat SMTP server
smtp_port = 587  # Replace with the recommended port for iChat
sender_email = 'kitwei18.20@ichat.sp.edu.sg'  # Replace with your iChat email address
sender_password = 'password'  # Replace with your iChat email password
receiver_email = 'ongkitwei@gmail.com'  # Replace with the recipient's email address

# Create a message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'Subject of your email'

# Add the email body
message_text = "This is the body of your email."
message.attach(MIMEText(message_text, 'plain'))

# Connect to the SMTP server
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Start TLS encryption (use server.ehlo() if not supported)
    server.login(sender_email, sender_password)  # Log in to your iChat email account
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)  # Send the email
    server.quit()
    print("Email sent successfully")

except Exception as e:
    print("An error occurred:", str(e))