from queries.users import get_user, get_user_by_email
from utils.validation import check_phone, check_email


def print_list(objs, page_size=5):
    """Display List with Pagination"""
    total_objs = len(objs)
    total_pages = (total_objs + page_size - 1) // page_size  # Calculate total pages

    current_page = 0

    while True:
        start_index = current_page * page_size
        end_index = start_index + page_size

        for obj in objs[start_index:end_index]:
            print(f"- {obj}")

        print("\nPage", current_page + 1, "of", total_pages)
        print("<-- [p] Previous,      [q] Quit,      [n] Next -->")
        command = input("Enter command: ").strip().lower()

        if command == 'n':
            if current_page < total_pages - 1:
                current_page += 1
            else:
                print("You are already on the last page.")
        elif command == 'p':
            if current_page > 0:
                current_page -= 1
            else:
                print("You are already on the first page.")
        elif command == 'q':
            print("Exiting...")
            break
        else:
            print("Invalid command. Please try again.")


def get_phone():
    phone = check_phone()
    if get_user(phone):
        print(f"This phone number already exists!\n")
        phone = get_phone()
        get_phone()

    return phone


def get_email():
    email = check_email()
    if get_user_by_email(email):
        print(f"This email already exists!\n")
        get_email()

    return email


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
