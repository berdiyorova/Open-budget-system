from queries.districts import get_districts
from queries.regions import get_regions
from queries.users import add_user
from utils.common import select_option
from utils.validation import validate_phone, validate_email, ask_gender


def register():
    first_name = input("Enter your first name:  ")
    last_name = input("Enter your last name:  ")
    birth_date = input("Enter your birth date (format: YYYY-MM-DD):  ")
    profession = input("Enter your profession:  ")

    phone = input("Enter your phone number:  ")
    if not validate_phone(phone):
        register()

    email = input("Enter your email:  ")
    if not validate_email(email):
        register()

    gender = ask_gender()

    region_id = select_option(get_regions())
    district_id = select_option(get_districts())

    add_user(first_name, last_name, birth_date, profession, phone, email, gender, region_id, district_id)



