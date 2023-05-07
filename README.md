# &lt;Emoji And Messages Sender&gt;

## A simple python code to send a list of emojis to a user in a WhatsApp chat.

### The script offers the following functionalities:

- Send all emojis
- Send a list of pre-defined love emojis
- Send a list of emojis given by the user as unicode
- Send a given number of same emoji in one message
- Send a given number of same emoji in many messages

## Usage

##### Install required apt packages

```bash
sudo apt install scrot && sudo apt install python3-tk && sudo apt install python3-dev && sudo apt install xclip
```

##### clone the repository

###### using ssh

```bash
git clone git@github.com:nafteli/Sends-emojis-and-messages.git && cd Sends-emojis-and-messages/
```

###### using https

```bash
git clone https://github.com/nafteli/Sends-emojis-and-messages.git && cd Sends-emojis-and-messages/
```

##### create a virtual environment

```bash
python3 -m venv Naftali_nonsense
```

##### start the virtual environment

```bash
source Naftali_nonsense/bin/activate
```

##### install the requirements file

```bash
pip3 install -r requirements.txt
```

##### start the project

```bash
python3 main.py
```
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

### Functionalities

- sendListOfAllEmoji()
    ```
    sendListOfAllEmoji(): This function sends a list of all emojis to a user in a WhatsApp chat. 
    It prompts the user to confirm the number of emojis to be sent and then opens the WhatsApp Web page for the specified phone number. 
    The emojis are sent using the emojisSend function.
    ```
  
- sendListOfLoveEmoji()
    ```
    sendListOfLoveEmoji(): This function sends a list of love emojis to a user in a WhatsApp chat. 
    It opens the WhatsApp Web page for the specified phone number and then sends the love emojis using the emojisSend function.
    ```

- sendManyEmojisInManyMessages()
    ```
   sendManyEmojisInManyMessages(): This function sends a given list of emojis as individual messages. 
   It starts by sleeping for 5 seconds, to give time for the user to switch to a different application. 
   Then it splits the list of emojis into individual emojis, copies each emoji to the clipboard, 
   pastes it in the current application using PyAutoGUI, and finally sends the message using the 'enter' key.
   ```
