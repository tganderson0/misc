import sms
from reademails import email_reader

def main():
  # print("sending message")
  # sms.send("hello there")
  # print("sent")

  reader = email_reader()

  while(True):
    sender, body = reader.single_email_check()

    

  reader.start_email_loop()
  



if __name__ == '__main__':
  main()