import smtplib
from email.message import EmailMessage

email = EmailMessage()

email_content = '''
Dear Rodrigo,

Your Rolex already arrived. Apreciate your product!

Kind regards, Rolex Team.
'''

email['Subject'] = 'Test email'
email['From'] = 'marcus.h.retr0@gmail.com'
email['To'] = 'altac.rlins@gmail.com'

email.set_content(email_content)

smtp_connector = smtplib.SMTP(host='smtp.gmail.com', port=587)
smtp_connector.starttls()
smtp_connector.login('marcus.h.retr0@gmail.com', '14m4g0d@@wh04m1')

smtp_connector.send_message(email)
smtp_connector.quit()
