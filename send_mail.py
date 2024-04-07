import email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import string

# read key from file key.txt
with open('key.txt', 'r') as file:
    KEY_SEQUENCE = file.read()

def encrypt_decrypt(message, key):
    key = key * (len(message) // len(key)) + key[:len(message) % len(key)]
    encrypted_message = ''.join(chr(ord(message_char) ^ ord(key_char)) for message_char, key_char in zip(message, key))
    return encrypted_message

def send_email(subject, message, to_email):
    from_email = 
    password = 
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    encrypted_message = encrypt_decrypt(message, KEY_SEQUENCE)
    
    msg.attach(MIMEText(encrypted_message, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Replace with SMTP server details
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

def receive_email():
    to_email = 
    password =  # Replace with Bob's email password
    
    server = smtplib.SMTP('imap.gmail.com', 993)  # Replace with IMAP server details
    server.starttls()
    server.login(to_email, password)
    
    server.select('inbox')
    
    status, messages = server.search(None, 'ALL')
    messages_ids = messages[0].split()
    
    if not messages_ids:
        print("No new messages.")
        return
    
    latest_email_id = messages_ids[-1]
    
    status, msg_data = server.fetch(latest_email_id, '(RFC822)')
    
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            subject = msg['subject']
            from_email = msg['from']
            message = msg.get_payload(decode=True).decode()
            
            decrypted_message = encrypt_decrypt(message, KEY_SEQUENCE)
            
            print(f"From: {from_email}")
            print(f"Subject: {subject}")
            print(f"Message: {decrypted_message}")

            with open('received_message.txt', 'w') as file:
                file.write(decrypted_message)
    
    server.logout()

# Send email from Alice to Bob
subject = 'Hello Bob'
message = 'This is a secret message from Alice to Bob'
to_email = 'b4713964@gmail.com'
send_email(subject, message, to_email)

# Receive email for Bob
receive_email()
