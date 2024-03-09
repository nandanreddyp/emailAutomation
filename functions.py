import csv
import smtplib, configparser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Read configuration from config file
config = configparser.ConfigParser()
config.read('config.ini')

# Email configuration
email_config = config['Email']
smtp_server = 'google.gmail.com'
smtp_port = 25  # Update this according to your SMTP server
sender_email = email_config['sender_email']
sender_password = email_config['sender_password']

def send_email(receiver_email, subject, message):
    try:
        # Set up the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        # Create a multipart message and set headers
        email_message = MIMEMultipart()
        email_message['From'] = sender_email
        email_message['To'] = receiver_email
        email_message['Subject'] = subject

        # Add message body
        email_message.attach(MIMEText(message, 'plain'))

        # Send the email
        server.sendmail(sender_email, receiver_email, email_message.as_string())

        # Close the SMTP server
        server.quit()
        print(f"Email sent successfully to {receiver_email}")

    except Exception as e:
        print(f"Failed to send email to {receiver_email}: {str(e)}")