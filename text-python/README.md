# Email Monitor/Texting

## What does it do?

This program monitors the most recent email you have received that is unread, checking every 10 seconds (default).

It can check for a specified phone number to text, and will respond and perform any OS calls that you set up in the code.

## How to use?

First, you need a gmail account that will be used by this program. This is to keep the clutter away from your regular email,
or feel free to stick to your regular if you don't mind.

1. You will need to create a JSON file that will contain your login information
  * This should be called/located in `./ignored/credentials.JSON`. You can name it what you want, just update the code if you name it something else
  * The JSON should take the following form:

```json
{"email": "email@gmail.com", "password": "myPassword", "phone": "1234567890"}
```

2. Once that is created, find the line in the `main.py` which calls `os.system()`.
  * This line is where code will be called after your specific number texts the email. Feel free to change this to whatever you like


That's about it in how to use it! Send me a message if there's anything else I can clarify!

