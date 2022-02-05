import smtplib
import json

carriers = {
	'att':    '@mms.att.net',
	'tmobile':' @tmomail.net',
	'verizon':  '@vtext.com',
	'sprint':   '@page.nextel.com'
}

def send_to_number(message, number):
  data = {}
  with open("ignored/credentials.JSON") as f:
    data = json.load(f)
  
  auth = (data['email'], data['password'])
  
  server = smtplib.SMTP( "smtp.gmail.com", 587 )
  server.starttls()
  server.login(auth[0], auth[1])

  server.sendmail( auth[0], number, message)

def send(message):
  data = {}
  with open("ignored/credentials.JSON") as f:
    data = json.load(f)
  
  to_number = f"{data['phone']}{carriers['tmobile']}"
  auth = (data['email'], data['password'])
  
  server = smtplib.SMTP( "smtp.gmail.com", 587 )
  server.starttls()
  server.login(auth[0], auth[1])

  server.sendmail(auth[0], to_number, message)