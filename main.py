from auth.login import log_in
from auth.logout import logout
from auth.register import register
from config.models import create_all_tables
from queries.districts import insert_districts
from queries.regions import insert_regions


def auth_menu():
    user_input = input("""
        1. Register
        2. Login
        3. Exit
        
        Enter your choice:  
        """)

    if user_input == '1':
        register()
        auth_menu()

    elif user_input == '2':
        user = log_in()
        if user:
            if user == 'admin':
                admin_menu()
            else:
                user_menu(user[0])
    elif user_input == '3':
        return None
    else:
        print("Invalid input! Try again.")
        auth_menu()


def admin_menu():
    user_input = input("""
        1. Create initiative
        2. Update initiative
        3. Start initiative
        4. Moderation
        5. Show statistics
        6. Logout
        """)
    if user_input == '1':
        pass
    elif user_input == '2':
        pass
    elif user_input == '3':
        pass
    elif user_input == '4':
        pass
    elif user_input == '5':
        pass
    elif user_input == '6':
        auth_menu()
    else:
        print("Invalid input! Try again.")
        admin_menu()


def user_menu(uuid):
    user_input = input("""
        1. Send an appeal
        2. All appeals
        3. My all appeals
        4. My new appeals
        5. My accepted appeals
        6. My rejected appeals
        7. Vote
        8. All initiatives
        8. Logout
        """)
    if user_input == '1':
        pass
    elif user_input == '2':
        pass
    elif user_input == '3':
        pass
    elif user_input == '4':
        pass
    elif user_input == '5':
        pass
    elif user_input == '6':
        pass
    elif user_input == '7':
        pass
    elif user_input == '8':
        pass
    elif user_input == '9':
        logout(uuid)
        auth_menu()
    else:
        print("Invalid input! Try again.")
        user_menu(uuid)



if __name__ == '__main__':
    create_all_tables()
    insert_regions()
    insert_districts()

    auth_menu()
