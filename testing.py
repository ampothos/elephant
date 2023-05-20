import email 
import imaplib
from tools import retrieval


imap_server = "imap.gmail.com" 
email_address = "elephantclient1@gmail.com"
password = "evatdawaocuiaief"
# password = "elephantyikes"

imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_address, password)

imap.select("Inbox")

# str, arr
# is ok(OK, NO can't search that criteria or BAD arg invalid, command unknown)
isOk, msgnums = imap.search(None, 'SUBJECT', '"*"')
print(isOk, msgnums)

print(retrieval.parseEmails(msgnums, imap))

# for num in msgnums[0].split(): 
#     typ, data = imap.fetch(num, '(RFC822)')
#     message = email.message_from_bytes(data[0][1])

#     print(f"Message Number: {num}")
#     print(f"From: {message.get('From')}")
#     print(f"To: {message.get('To')}")
#     print(f"Date: {message.get('Date')}")
#     print(f"Subject: {message.get('Subject')}")
#     print()



imap.close()
imap.logout()