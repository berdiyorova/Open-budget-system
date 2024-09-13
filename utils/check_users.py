from queries.users import get_user

admin_phone = "+998717020108"
admin_password = "Admin0101"


def check_admin(phone):
    if phone == admin_phone:
        password = input("Ender admin password:  ")
        if password == admin_password:
            return True
    return False


def check_user(phone):
    if get_user(phone):
        return True
    return False
