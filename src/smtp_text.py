import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage

class smtp_text:
    def __init__(self, GMAIL_EMAIL, GMAIL_PASSWORD):
        self.GMAIL_EMAIL = GMAIL_EMAIL
        self.GMAIL_PASSWORD = GMAIL_PASSWORD
        self.server = None

        self.SmsGateways = [
                            'tmomail.net',                  # tmobile
                            'mms.att.net',                  # at&t
                            'vtext.com',                    # verizon
                            'pm.sprint.com',                # sprint
                            'sms.mycricket.com',            # cricket 
                            'sms.myboostmobile.com'         # boost
                            ]

    # Establish a secure session with gmail's outgoing SMTP server using your gmail account
    def reconnect(self):
        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.starttls()
        self.server.login(self.GMAIL_EMAIL, self.GMAIL_PASSWORD)

    def send_message(self, phone, message):
        message += "\n\nTweet powered by VIRU coins"

        # Due to company acquisitions, multiple gateways for a single number might work
        for gateway in self.SmsGateways:
            destination = f"{phone}@{gateway}"
            
            msg_with_header = f"From: {self.GMAIL_EMAIL}\r\nTo: {destination}\r\nSubject: \r\n\r\n{message}"
            mimed_msg = MIMEText(msg_with_header.encode('utf-8'), _charset='utf-8')
            try:
                self.server.sendmail(self.GMAIL_EMAIL, destination, mimed_msg.as_string())
            except Exception as e:
                print(e)
                continue
    