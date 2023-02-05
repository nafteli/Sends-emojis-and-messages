import logging
logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")


def phoneNumber() -> int | str:
    countryCode = "972"
    maxForPhoneNumber = 13
    minForPhoneNumber = 10
    emptyPhoneNumber = 1
    PhoneNumber = input('The phone number of the recipient of the messages?\n')
    try:
        if type(PhoneNumber) != str:
            print("Phone number must be a string")
            return -1
        if len(PhoneNumber) <= emptyPhoneNumber:
            print('the phone number is empty or too short')
            return -1
        PhoneNumber = PhoneNumber.replace("-", "").replace(' ', '')
        if not PhoneNumber[1:].isnumeric():
            print(f'{PhoneNumber} is not number')
            return -1
        # check if it's a valid phone number'
        if not maxForPhoneNumber >= len(PhoneNumber) >= minForPhoneNumber:
            print(f'the number {PhoneNumber} is Invalid')
            return -1
        # replace the 0 in country code
        if len(PhoneNumber) == minForPhoneNumber:
            PhoneNumber = countryCode + PhoneNumber[1:]
        # replace the 0O in country code
        if len(PhoneNumber) == maxForPhoneNumber + 1:
            PhoneNumber = countryCode + PhoneNumber[2:]
        # delete the "+"
        if len(PhoneNumber) == maxForPhoneNumber:
            PhoneNumber = PhoneNumber[1:]
        # The only option left is that it is max -1 and it is probably the correct number without +
        # or after corrections in the previous conditions
        return PhoneNumber
    except Exception as Error:
        logging.error(f'the error is {Error}')
        return -1


# test = ["phone_number", '', "+972537225919", "+972 53-722-5919", '0537225919', 12345678, 0, '  ', '1']
# for i in test:
#     print(phoneNumber(i))
