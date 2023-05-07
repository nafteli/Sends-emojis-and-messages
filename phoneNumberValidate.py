import logging
import re

logging.basicConfig(
    level=logging.INFO,
    filename="log.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def phoneNumber() -> int | str:
    """
    This function prompts the user to enter a phone number, validates it against an Israeli phone number pattern, and then
    cleans and formats the phone number to be returned. If the phone number is invalid, the function returns -1.

    Args:
        None.

    Returns:
        Either an integer or string: The cleaned and formatted phone number (int or str) or -1 if the phone number is invalid.

    Raises:
        None.

    Example:
        >>> phoneNumber()
        The phone number of the recipient of the messages?
        +972-53-700-5116
        972537005116

    """
    try:
        # Ask for user input and clean the phone number of non-ASCII characters
        phone_number = (
            input("The phone number of the recipient of the messages?\n")
            .encode("ascii", "ignore")
            .decode()
        )
        # Define the regular expression pattern to match the phone number format
        pattern = r"^(?:\+972|972|0)(?:[- ])?(?:[23489]|5[023458]|77|81)(?:[- ])?(?:\d{3})(?:[- ])?(?:\d{4})$"
        # If the phone number matches the pattern, clean it and return it.
        if bool(re.match(pattern, phone_number)):
            clean_number = re.sub(r"[+ -]", "", phone_number)
            return re.sub(r"^0", "972", clean_number)
        else:
            return -1
    # If an exception occurs, log it and return -1 as an error code.
    except Exception as Error:
        logging.error(f"error {Error}")
        return -1
