from time import sleep
import sms
from reademails import email_reader
import json
import os

def main():
  valid_phone = ""

  with open("ignored/credentials.JSON") as f:
    data = json.load(f)
    valid_phone = data['phone']
  


  reader = email_reader()

  print("Logged in, monitoring emails")

  while(True):
    sender, body = reader.single_email_check()

    # make sure we actually have a new email
    if (sender != ""):
      print(f"Email from: {sender}")
      print(f"msg: {body}")

      if (valid_phone in sender):

        # Replace this line with the command(s) you would like to run on a text from yourself
        # Alternatively, you have access to the body of the text, which would let you add some if-statements
        os.system('open /Users/taylor/Desktop/Aseprite.app/')
        
        print("Welcome. Opening app...")
        sms.send_to_number("Hello, I have recieved your request and opened your programs for you!", sender)

      else:
        try:
          sms.send_to_number("I don't even know who you are", sender)
        except:
          print("Error occurred in responding")
    
    # By default, only checks emails every 10 seconds
    sleep(10)  

if __name__ == '__main__':
  main()