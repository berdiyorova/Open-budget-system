from logs.logs import log_decorator
from queries.users import get_user, update_user
from utils.check_users import check_admin, check_user
from utils.validation import get_phone


@log_decorator
def log_in():
    phone = get_phone()

    if check_admin(phone):
        return 'admin'

    elif check_user(phone):
        user = get_user(phone)
        update_user(user[0], 'is_login', True)
        return user

    else:
        print("Invalid phone or code. Please, try again.")
        log_in()

