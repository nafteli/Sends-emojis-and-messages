# &lt;README for emoji and messages sender script&gt;

## Overview
###### This script is designed to send emojis through WhatsApp Web. The script uses the pyautogui and pyperclip libraries to automate the process of sending messages.

### The script offers the following functionalities:

- Send all emojis
- Send a list of pre-defined love emojis
- Send a list of emojis given by the user as unicode
- Send a given number of same emoji in one message
- Send a given number of same emoji in many messages
## Installation
```
$ python3 -m pip install pyautogui 
or 
$ pip install pyautogui
```
```bash
sudo apt install scrot
```
```bash
sudo apt install python3-tk
```
```bash
sudo apt install python3-dev
```

##### For sending emoji you need an additional library
```bash
pip install pyperclip
sudo apt install xclip
```

### imports

```python
import pyautogui
import pyperclip
from time import sleep
import os
```

### send all emojis 

```python
def sendListOfAllEmoji() -> str:
    """
    This function sends a list of all emojis to a user in a WhatsApp chat.
    """

    # Import the emoji data from the `EMOJI_DATA` dictionary in the `data_dict` module
    from data_dict import EMOJI_DATA

    # Prompt the user to confirm that they want to send the number of emojis specified in the `EMOJI_DATA` dictionary
    input(f'Are you sure you want to send {len(EMOJI_DATA.keys())} emojis?')

    # Get the phone number of the recipient
    PhoneNumber = phoneNumber()

    # Open the WhatsApp Web page for the specified phone number
    os.system(f"google-chrome https://web.whatsapp.com/send?phone={PhoneNumber} &")

    # Wait 10 seconds to allow the page to load
    sleep(10)

    # Loop through each emoji in the `EMOJI_DATA` dictionary
    for emoji in EMOJI_DATA.keys():
        # because it is unicode of emoji need to copy and paste all string together
        # must use pyperclip for copy the string
        # Copy the emoji string to the clipboard
        pyperclip.copy(emoji)

        # Use the `pyautogui` library to paste the emoji in the chat and send it
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        
    # Return a message indicating that the function has finished sending the emojis
    return 'done'
```

### send list of love emojis

```python
def sendListOfLoveEmoji() -> str:
    """
    This function sends a list of love emojis to a user in a WhatsApp chat.
    """

    # Get the phone number of the recipient
    PhoneNumber = phoneNumber()

    # Open the WhatsApp Web page for the specified phone number
    os.system(f"google-chrome https://web.whatsapp.com/send?phone={PhoneNumber} &")
    
    # list of encode love emoji
    emojis_love = ['\U0001F60D', '\U0001F970', '\U0001F618', '\U0001F48C',
                   '\U00002763', '\U00002764\U0000FE0F\U0000200D\U0001FA79',
                   '\U0001F49F', '\U0001F48B', '\U0001F498', '\U0001F49D',
                   '\U0001F496', '\U0001F497', '\U0001F493', '\U0001F49E',
                   '\U0001F495', '\U00002764\U0000FE0F\U0000200D\U0001F525',
                   '\U00002764', '\U0001F9E1', '\U0001F49B', '\U0001F49A',
                   '\U0001F499', '\U0001F49C', '\U0001F90E', '\U0001F5A4',
                   '\U0001F90D']
    sleep(10)
    for emoji in emojis_love:
        # because it is unicode of emoji need to copy and paste all string together
        # must use pyperclip for copy the string
        pyperclip.copy(emoji)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
    return 'done'
```

### send a given list of emojis

```python
def sendManyEmojisInManyMessages() -> str:
    """
    This function sends a given list of emojis as individual messages.
    It starts by sleeping for 5 seconds, to give time for the user to switch to a different application.
    Then it splits the `emojisList` string into a list of emojis, and iterates over the list.
    For each emoji in the list, it copies the emoji to the clipboard using the `pyperclip` module.
    Then it simulates pressing the 'ctrl' and 'v' keys to paste the emoji in the current application using the `pyautogui` module.
    Finally, it simulates pressing the 'enter' key to send the message in the current application using the `pyautogui` module.
    :return: None
    """
    emojisFromUser = input(
        r'Bring me the unicodes of the emojis you want to send (should look like \U00000000 \U00011111)''\n')
    emojis = emojisFromUser.encode("utf-8").decode("unicode_escape")

    PhoneNumber = phoneNumber()
    os.system(f"google-chrome https://web.whatsapp.com/send?phone={PhoneNumber} &")

    sleep(10)
    for emoji in emojis.split(' '):
        # because it is unicode of emoji need to copy and paste all string together
        # must use pyperclip for copy the string
        pyperclip.copy(emoji)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
    return 'done'
```

### send same emojis in one message

```python
def sendManyEmojisInOneMessage() -> str:
    """
    This function sends a given number of same emojis in one message.
    It starts by sleeping for 5 seconds, to give time for the user to switch to a different application.
    Then it uses a for loop to iterate 'numberOfEmojisToSend' number of times,
    in each iteration it copies the 'emojiToPaste' to the clipboard using the 'pyperclip' module.
    Then it simulates pressing the 'ctrl' and 'v' keys to paste the emoji in the current application
     using the 'pyautogui' module.
    Finally, it simulates pressing the 'enter' key to send the message with all the emojis pasted in one message
    in the current application using the 'pyautogui' module.
    :return: None
    """

    emojiFromUsrer = input('Bring me the unicode of the emoji you want to send\n')
    numberOfEmojisToSend = input('How many emojis?\n')
    PhoneNumber = phoneNumber()
    os.system(f"google-chrome https://web.whatsapp.com/send?phone={PhoneNumber} &")
    if not numberOfEmojisToSend.isnumeric():
        message = 'times to send must to be a number'
        print(message)
        return message
    emoji = emojiFromUsrer.encode("utf-8").decode("unicode_escape")

    sleep(10)
    for _ in range(int(numberOfEmojisToSend)):
        pyperclip.copy(emoji)
        pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    return 'done'
```

### sends a given message multiple times

```python
def sendManyTextMessage() -> str:
    """
    This function sends a given message multiple times.
    It starts by sleeping for 5 seconds, to give time for the user to switch to a different application.
    Then it uses a for loop to iterate 'timesToSend' number of times, in each iteration it writes the message
    and a counter indicating the current message number and total number of messages
    to be sent using the 'pyautogui' module.
    Then it simulates pressing the 'enter' key to send the message using the 'pyautogui' module.
    After sending each message, it sleeps for 0.2 seconds using the 'sleep()' function from the built-in 'time' module.
    :return: None
    """

    messageToSend = input('What message do you want to send?\n')
    timesToSend = input('How many times to send?\n')
    PhoneNumber = phoneNumber()
    os.system(f"google-chrome https://web.whatsapp.com/send?phone={PhoneNumber} &")
    if not timesToSend.isnumeric():
        message = 'times to send must to be a number'
        print(message)
        return message

    sleep(10)
    for msg in range(int(timesToSend) + 1):
        pyautogui.write(f'{messageToSend}:  {msg}/{timesToSend}')
        pyautogui.press('enter')
        sleep(0.2)
    return 'done'
```

### sends a message

```python
def sendOneTextMessage() -> str:
    """
    This function sends a given message.
    It writes the message using the 'write()' method of the 'pyautogui' module.
    Then it simulates pressing the 'enter' key to send the message using the 'press()' method of the 'pyautogui' module.
    :return: None
    """

    textMessage = input('What message do you want to send?\n')
    PhoneNumber = phoneNumber()
    os.system(f"google-chrome https://web.whatsapp.com/send?phone={PhoneNumber} &")
    sleep(10)
    pyautogui.write(textMessage)
    pyautogui.press('enter')
    return 'done'
```

### get the phone number

```python
def phoneNumber():
    """Returns the phone number"""
    PhoneNumber = input('The phone number of the recipient of the messages?\n')
    # check if it's number
    if not PhoneNumber[1:].isnumeric():
        return f'{PhoneNumber} is not number'
    # check if it's a valid phone number'
    if all([len(PhoneNumber) != 13, len(PhoneNumber) != 10]):
        return f'the number {PhoneNumber} is Invalid'
    # replace the 0 in country code
    if len(PhoneNumber) == 10:
        PhoneNumber = "972" + PhoneNumber[1:]
    # delete the "+"
    if len(PhoneNumber) == 13:
        PhoneNumber = PhoneNumber[1:]
    return PhoneNumber
```

## Usage 

##### Install required apt packages
```bash
sudo apt install scrot && sudo apt install python3-tk && sudo apt install python3-dev && sudo apt install xclip
```

##### clone the repository 
###### to using ssh
```bash
git clone git@github.com:nafteli/Sends-emojis-and-messages.git && cd Sends-emojis-and-messages/
```
###### to using https
```bash
git clone https://github.com/nafteli/Sends-emojis-and-messages.git && cd Sends-emojis-and-messages/
```

##### create a virtual environment
```bash
$ python3 -m vene <name of venv>
```

##### start the virtual environment
```bash
source venv/bin/activate
```

##### install the requirements file
```bash
pip3 install -r requirements.txt
```

##### start the project
```bash
python3 main.py
```
