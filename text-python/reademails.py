import json
import imaplib
import email
import imaplib
import email

SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

class email_reader():

  def __init__(self) -> None:

    with open("ignored/credentials.JSON") as f:
      data = json.load(f)

    self.mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    self.mail.login(data['email'], data['password'])
    self.mail.select('inbox')

  def single_email_check(self) -> tuple:
    """ Uses the logged in email and returns the latest email. Returns sender, body """
    data = self.mail.search(None, "ALL")
    mail_ids = data[1]
    id_list = mail_ids[0].split()
    latest_email_id = int(id_list[-1])

    data = self.mail.fetch(str(latest_email_id), '(RFC822)')
    for response_part in data:
      arr = response_part[0]
      if isinstance(arr, tuple):
        body = ""
        msg = email.message_from_string(str(arr[1],'utf-8'))
        email_from = msg['from']
        print('From : ' + email_from + '\n')
        if msg.is_multipart():
          for part in msg.walk():
            ctype = part.get_content_type()
            cdispo = str(part.get('Content-Disposition'))

            # skip any text/plain (txt) attachments
            if ctype == 'text/plain' and 'attachment' not in cdispo:
              body = part.get_payload(decode=True)  # decode
              break
        # not multipart - i.e. plain text, no attachments, keeping fingers crossed
        else:
          body = msg.get_payload(decode=True)
        
    return email_from, body