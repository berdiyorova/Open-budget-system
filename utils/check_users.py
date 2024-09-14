from queries.users import get_user_email
from utils.send_email import verify_code

admin_phone = "+998717020108"
admin_email = "baxromovna6974@gmail.com"


def check_admin(phone):
    if phone == admin_phone:
        return verify_code(admin_email)


def check_user(phone):
    email = get_user_email(phone)
    if email:
        return verify_code(email[0])
