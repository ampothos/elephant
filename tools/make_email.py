from email.message import EmailMessage
from smtplib import SMTP_SSL, SMTP_SSL_PORT


maildict = {'from_email' : "elephantclient1@gmail.com",
            'to_email': "thewateringholesender@gmail.com", 
            'subject' : 'Physical Therapy',
            'body' : 'Some stuff',
            'from_pass' : 'evatdawaocuiaief'}

def makeSendEmail(maildict):
    email_message = EmailMessage()
    email_message.add_header('From', maildict.from_email)
    email_message.add_header('To', maildict.to_email)
    email_message.add_header('Subject', maildict.subject)
    email_message.set_content(maildict.body)

    smtp_server = SMTP_SSL('imap.gmail.com', port=SMTP_SSL_PORT)
    smtp_server.set_debuglevel(1)  
    smtp_server.login(maildict.from_email, maildict.from_pass)
    smtp_server.sendmail(maildict.from_email, maildict.to_email, email_message.as_bytes())
    smtp_server.quit()
                