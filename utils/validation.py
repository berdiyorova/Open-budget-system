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


def check_phone():
    phone = input("Enter your phone number:  ")
    if not validate_phone(phone):
        print("Invalid phone number")
        check_phone()

    return phone


def check_email():
    email = input("Enter your email:  ")
    if not validate_email(email):
        print("Invalid email address")
        check_email()

    return email
