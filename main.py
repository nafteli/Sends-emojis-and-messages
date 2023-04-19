# from phoneNumberValidate import phoneNumber
# import send_with_selenum
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="log.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s",
)


from opsions import *


def main():
    """Main function to handle user input and call appropriate function.

    Returns:
        str: 'exit' if the user chooses to exit.
             errorMessage if the input is not numeric or not in optionsList.
    """
    optionsList = [0, 1, 2, 3, 4, 5, 6]
    try:
        while True:
            userInput = input(
                "What do you want to do?\n\n"
                "I know how to send one message or many messages"
                "one emoji many times in one message or many emojis in many messages\n\n"
                "    Press 1 end enter to send a single message\n"
                "    Press 2 end enter to send many messages\n"
                "    Press 3 end enter to send many emoji in one message\n"
                "    Press 4 end enter to send many emojis\n"
                "    Press 5 end enter to send List of love emoji\n"
                "    Press 6 end enter to send all emojis\n"
                "    Press 0 end enter to exit\n"
            )
            optionToRun = int(userInput)
            errorMessage = f"I only know how to work with one of the four options {optionToRun} not in {optionsList}"
            if not userInput.isnumeric():
                print(errorMessage)
                return errorMessage
            match optionToRun if optionToRun in optionsList else "":
                case 0:
                    print("exit")
                    send_with_selenum.closeBrowser()
                    return "exit"
                case 1:
                    sendOneTextMessage()
                case 2:
                    sendManyTextMessage()
                case 3:
                    sendManyEmojisInOneMessage()
                case 4:
                    sendManyEmojisInManyMessages()
                case 5:
                    sendListOfLoveEmoji()
                case 6:
                    sendListOfAllEmoji()
                case _:
                    print(errorMessage)
    except Exception as e:
        print(e)
        logging.error(f"the error is {e}")
        return -1


if __name__ == "__main__":
    # input(
    #     f'\u001b[41m \u001b[7m {"#" * 40} important!!! {"#" * 40} \u001b[00m\n'
    #     "\u001b[41m \u001b[7m Do not close the opened browser if it needs to be restarted \u001b[00m"
    # )
    main()
