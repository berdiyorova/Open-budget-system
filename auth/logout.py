from queries.users import update_user


def logout(id):
    update_user(id, 'is_login', False)
