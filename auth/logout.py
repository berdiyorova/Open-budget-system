from logs.logs import log_decorator
from queries.users import update_user


@log_decorator
def logout(id):
    update_user(id, 'is_login', False)
