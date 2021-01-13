import smtplib
import email
from email.mime.text import MIMEText


class smtp_text:
    def __init__(self, GMAIL_EMAIL, GMAIL_PASSWORD):
        self.GMAIL_EMAIL = GMAIL_EMAIL

        # Establish a secure session with gmail's outgoing SMTP server using your gmail account
        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.starttls()
        self.server.login(self.GMAIL_EMAIL, GMAIL_PASSWORD)

        self.SmsGateways = [
                            'tmomail.net',             # tmobile
                            'mms.att.net',             # at&t
                            'vtext.com',               # verizon
                            'pm.sprint.com',           # sprint
                            'sms.mycricket.com',       # cricket 
                            'vmobl.com',               # virgin mobile US
                            'sms.myboostmobile.com'    # boost mobile
                            ]

    def send_message(self, phone, message):
        mime_msg = MIMEText(message.encode('utf-8'), _charset='utf-8')
        print(mime_msg.as_string())
        for gateway in self.SmsGateways:
            destination = f"{phone}@{gateway}"
            try:
                self.server.sendmail(self.GMAIL_EMAIL, destination, mime_msg.as_string())
                print("HERE")
            except Exception as e:
                continue