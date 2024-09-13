import re


def validate_phone(phone):
    """
        check phone
        :param phone:
        :return:
        """
    # Define the phone number pattern
    pattern = r"^\+?[1-9]\d{0,2}[-.\s]?(\(?\d{1,4}?\)?[-.\s]?)?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"

    # Use re.match to validate the phone number
    if re.match(pattern, phone):
        return True
    return False


def validate_email(email):
    """
    check email
    :param email:
    :return:
    """
    # Define the email pattern
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    # Use re.match to validate the email
    if re.match(pattern, email):
        return True
    return False


def ask_gender():
    choice = input("""
            Gender:
            1. Male
            2. Female

            """)
    if choice == '1':
        return 'male'

    elif choice == '2':
        return 'female'

    else:
        print("Invalid input. Try again.")
        ask_gender()
