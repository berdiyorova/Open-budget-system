from logs.logs import log_decorator
from queries.districts import get_districts
from queries.regions import get_regions
from queries.users import add_user
from utils.common import print_list
from utils.send_email import verify_code_menu
from utils.validation import get_phone, ask_gender, get_email


@log_decorator
def register():
    first_name = input("Enter your first name:  ")
    last_name = input("Enter your last name:  ")
    birth_date = input("Enter your birth date (format: YYYY-MM-DD):  ")
    profession = input("Enter your profession:  ")

    phone = get_phone()
    email = get_email()
    gender = ask_gender()

    print_list(get_regions())
    region_id = int(input("\nSelect your region where you live:  "))
    print_list(get_districts(region_id))
    district_id = int(input("\nSelect your district where you live:  "))

    verify_code_menu(email)

    add_user(first_name, last_name, birth_date, profession, phone, email, gender, region_id, district_id)
    print("You have successfully registered.")
