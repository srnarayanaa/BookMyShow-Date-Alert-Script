import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests

MOVIE_URL = "https://in.bookmyshow.com/buytickets/oppenheimer-imax-bengaluru/movie-bang-ET00363396-MT/20230728"

#This ideally checks for validity of the URL to alert
#Change the URL date in the end to when you wanna get alerted for

# Email settings
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
GMAIL_USERNAME = 'YOURMAILID@gmail.com'
GMAIL_PASSWORD = 'GET YOUR APP PASSWORD'
SEND_TO_EMAIL = 'TARGETMAILID@gmail.com'

def send_email(subject, message):
    print("Starting ...")
    msg = MIMEMultipart()
    msg['From'] = GMAIL_USERNAME
    msg['To'] = SEND_TO_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(GMAIL_USERNAME, GMAIL_PASSWORD)
    text = msg.as_string()
    server.sendmail(GMAIL_USERNAME, SEND_TO_EMAIL, text)
    server.quit()

while True:
    response = requests.get(MOVIE_URL)
    print(response)
    
    if response.status_code == 200:
        send_email(
            subject="Movie Booking Available",
            message=f"Booking for the movie is now available. You can book your tickets at {MOVIE_URL}."
        )
    else:
        send_email(
            subject="Oppenheimer Not Available Yet",
            message=f"Booking for Oppenheimer is not open yet. Check later."
        )

    time.sleep(60)  #set your time accordingly
