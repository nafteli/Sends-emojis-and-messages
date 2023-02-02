#  for use pyautogui need to install pyautogui and scrot, python3-tk, python3-dev run the next line in terminal
#  python3 -m pip install pyautogui
#  sudo apt install scrot
#  sudo apt install python3-tk
#  sudo apt install python3-dev
import pyautogui
# pip install pyperclip
# sudo apt install xclip
import pyperclip
from time import sleep
import os

from phoneNumberValidate import phoneNumber


def sendListOfAllEmoji() -> str:
    """Sends a list of all emojis to a user in a WhatsApp chat.

    Returns:
        str: "no" if the user denies sending the emojis, "bay" if the user doesn't provide a valid input for confirmation,
             "number not found" if the recipient's phone number is not found, and the result of the emojisSend() function.
    """

    # Import the emoji data from the `EMOJI_DATA` dictionary in the `data_dict` module
    from data_dict import EMOJI_DATA

    # Prompt the user to confirm that they want to send the number of emojis specified in the `EMOJI_DATA` dictionary
    yesChoice = ['yes', 'YES', 'Yes', 'y', 'Y']
    noChoice = ['no', 'NO', 'No', 'n', 'N']
    angryEmoji = ['', '\U0001F61F', '\U0001F620', '\U0001F624', '\U0001F621', '\U0001F92C']
    angyCount = 0
    while True:
        seriousnessCheck = input(
            f'Are you sure you want to send {len(EMOJI_DATA.keys())} emojis?\nSelect yes or no (y/n)\n')
        if seriousnessCheck in noChoice:
            print("Too bad it could be nice \U0001F609\n\n")
            return "no"
        if seriousnessCheck in yesChoice:
            print('Remember you asked \U0001F479\n\n')
            break
        else:
            if angyCount >= len(angryEmoji):
                print("Im tired of you", '\U0001F47F' * angyCount, "\n\n")
                return "bay"
            print("Select yes or no (y/n)", angryEmoji[angyCount] * angyCount)
            angyCount += 1
    # Get the phone number of the recipient
    PhoneNumber = phoneNumber()
    if PhoneNumber == -1:
        return "number not found"

    send = emojisSend(EMOJI_DATA.keys(), PhoneNumber)
    return send


def sendListOfLoveEmoji() -> str:
    """
    Sends a list of love emojis to a user in a WhatsApp chat.

    Input: None

    Output:
      - If the phone number of the recipient is found, returns the result of calling `emojisSend` with the list of love emojis and the phone number.
      - If the phone number of the recipient is not found, returns the string "number not found".

    Dependencies:
      - `phoneNumber`: returns the phone number of the recipient.
      - `emojisSend`: sends a list of emojis to a specified phone number in a WhatsApp chat.
    """

    # Get the phone number of the recipient
    PhoneNumber = phoneNumber()
    if PhoneNumber == -1:
        return "number not found"

    # list of encode love emoji
    emojis_love = ['\U0001F60D', '\U0001F970', '\U0001F618', '\U0001F48C',
                   '\U00002763', '\U00002764\U0000FE0F\U0000200D\U0001FA79',
                   '\U0001F49F', '\U0001F48B', '\U0001F498', '\U0001F49D',
                   '\U0001F496', '\U0001F497', '\U0001F493', '\U0001F49E',
                   '\U0001F495', '\U00002764\U0000FE0F\U0000200D\U0001F525',
                   '\U00002764', '\U0001F9E1', '\U0001F49B', '\U0001F49A',
                   '\U0001F499', '\U0001F49C', '\U0001F90E', '\U0001F5A4',
                   '\U0001F90D']
    send = emojisSend(emojis_love, PhoneNumber)
    return send


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
    if PhoneNumber == -1:
        return "number not found"
    send = emojisSend(emojis.split(' '), PhoneNumber)
    return send


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
    if PhoneNumber == -1:
        return "number not found"

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
    if PhoneNumber == -1:
        return "number not found"

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


def sendOneTextMessage() -> str:
    """
    This function sends a given message.
    It writes the message using the 'write()' method of the 'pyautogui' module.
    Then it simulates pressing the 'enter' key to send the message using the 'press()' method of the 'pyautogui' module.
    :return: None
    """

    textMessage = input('What message do you want to send?\n')
    PhoneNumber = phoneNumber()
    if PhoneNumber == -1:
        return "number not found"

    os.system(f"google-chrome https://web.whatsapp.com/send?phone={PhoneNumber} &")
    sleep(10)
    pyautogui.write(textMessage)
    pyautogui.press('enter')
    return 'done'


def emojisSend(Emojis, PhoneNumber) -> str:
    """
    Sends a list of emojis to a specified phone number via WhatsApp Web.

    Inputs:
    - Emojis: List of emoji strings in unicode format to be sent.
    - PhoneNumber: The phone number of the recipient, formatted as a string (e.g. "1234567890").

    Output:
    - "done" if the emojis were successfully sent.
    """

    # Open the WhatsApp Web page for the specified phone number
    os.system(f"google-chrome https://web.whatsapp.com/send?phone={PhoneNumber} &")

    # Wait 10 seconds to allow the page to load
    sleep(10)

    # Loop through each emoji in the `EMOJI_DATA` dictionary
    for emoji in Emojis:
        # because it is unicode of emoji need to copy and paste all string together
        # must use pyperclip for copy the string
        # Copy the emoji string to the clipboard
        pyperclip.copy(emoji)

        # Use the `pyautogui` library to paste the emoji in the chat and send it
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')

    # Return a message indicating that the function has finished sending the emojis
    return 'done'


def main():
    """Main function to handle user input and call appropriate function.

    Returns:
        str: 'exit' if the user chooses to exit.
             errorMessage if the input is not numeric or not in optionsList.
    """
    optionsList = [0, 1, 2, 3, 4, 5, 6]
    while True:
        userInput = input('What do you want to do?\n\n'
                          'I know how to send one message or many messages'
                          'one emoji many times in one message or many emojis in many messages\n\n'
                          'Press 1 end enter to send a single message\n'
                          'Press 2 end enter to send many messages\n'
                          'Press 3 end enter to send many emoji in one message\n'
                          'Press 4 end enter to send many emojis\n'
                          'Press 5 end enter to send List of love emoji\n'
                          'Press 6 end enter to send all emojis\n'
                          'Press 0 end enter to exit\n')
        opsinToRun = int(userInput)
        errorMessage = f'I only know how to work with one of the four options {opsinToRun} not in {optionsList}'
        if not userInput.isnumeric():
            print(errorMessage)
            return errorMessage
        if opsinToRun not in optionsList:
            print(errorMessage)
            return errorMessage
        match opsinToRun:
            case 1:
                sendOneTextMessage()
            case 2:
                sendManyTextMessage()
            case 3:
                sendManyEmojisInOneMessage()
            case 4:
                sendManyEmojisInManyMessages()
            case 0:
                print('exit')
                return 'exit'
            case 5:
                sendListOfLoveEmoji()
            case 6:
                sendListOfAllEmoji()
            case _:
                return errorMessage


if __name__ == "__main__":
    input(f'\u001b[31m \u001b[7m {"#" * 40} important!!! {"#" * 40} \u001b[00m\n'
          '\u001b[31m \u001b[7m Before starting, make sure WhatsApp is connected to'
          '\u001b[31m \u001b[7m Chrome but closed Press Enter to confirm \u001b[00m')
    main()
