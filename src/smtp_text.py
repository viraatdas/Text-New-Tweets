import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage


class smtp_text:
    def __init__(self, GMAIL_EMAIL, GMAIL_PASSWORD):
        self.GMAIL_EMAIL = GMAIL_EMAIL

        # Establish a secure session with gmail's outgoing SMTP server using your gmail account
        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.starttls()
        self.server.login(self.GMAIL_EMAIL, GMAIL_PASSWORD)

        self.SmsGateways = [
                            'tmomail.net',                  # tmobile
                            'mms.att.net',                  # at&t
                            'vtext.com',                    # verizon
                            'pm.sprint.com',                # sprint
                            'sms.mycricket.com',            # cricket 
                            'sms.myboostmobile.com'         # boost
                            ]

    def send_message(self, phone, message):
        # Due to acquisiations
        message+="\n Contact Viraat if you are receiving duplicate messages."
        for gateway in self.SmsGateways:
            destination = f"{phone}@{gateway}"
            
            mimed_msg = f"From: {self.GMAIL_EMAIL}\r\nTo: {destination}\r\nSubject: \r\n\r\n{message}{destination}"

            try:
                self.server.sendmail(self.GMAIL_EMAIL, destination, mimed_msg)
            except Exception as e:
                print(e)
                continue