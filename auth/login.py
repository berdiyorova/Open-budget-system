from logs.logs import log_decorator
from queries.users import get_user, update_user
from utils.check_users import check_admin, check_user
from utils.validation import validate_phone


@log_decorator
def log_in():
    phone = input("Enter your phone:  ")
    if not validate_phone(phone):
        print("Invalid phone number. Please, try again.")
        log_in()

    if check_admin(phone):
        return 'admin'

    elif check_user(phone):
        user = get_user(phone)
        update_user(user[0], 'is_login', True)
        return user

    else:
        print("Invalid phone number. Please, try again.")
        log_in()

