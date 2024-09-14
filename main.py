from admin_and_user_functions.admin.crud_categories import create_category, update_the_category, \
    delete_category_from_table, show_all_categories, show_categories_by_project_type
from admin_and_user_functions.admin.crud_initiatives import create_initiative, update_unstarted_initiative, \
    start_initiative, show_unstarted_initiatives, show_started_initiative, show_ended_initiatives, show_all_initiatives
from admin_and_user_functions.admin.crud_project_types import create_project_type, update_project_type, \
    delete_project_type, show_all_project_types
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
            1. Initiatives
            2. Project types
            3. Categories
            4. Moderation
            5. Show statistics
            6. Logout

            Enter your choice:  
            """)
    if user_input == '1':
        initiative_menu()

    elif user_input == '2':
        project_type_menu()

    elif user_input == '3':
        category_menu()

    elif user_input == '4':
        pass

    elif user_input == '5':
        admin_statistics()

    elif user_input == '6':
        auth_menu()

    else:
        print("Invalid input! Try again.")
        admin_menu()


def initiative_menu():
    user_input = input("""
        1. Create initiative
        2. Update initiative
        3. Start initiative
        4. Show all initiatives
        5. Go to back
        
        Enter your choice:  
        """)
    if user_input == '1':
        create_initiative()
        initiative_menu()

    elif user_input == '2':
        update_unstarted_initiative()  # admin can update only unstarted initiatives
        initiative_menu()

    elif user_input == '3':
        start_initiative()
        initiative_menu()

    elif user_input == '4':
        show_all_initiatives()
        initiative_menu()

    elif user_input == '5':
        admin_menu()

    else:
        print("Invalid input! Try again.")
        initiative_menu()


def project_type_menu():
    user_input = input("""
        1. Create project type
        2. Update project type
        3. Delete project type
        4. Show all project types
        5. Go to back

        Enter your choice:  
        """)
    if user_input == '1':
        create_project_type()
        project_type_menu()

    elif user_input == '2':
        update_project_type()
        project_type_menu()

    elif user_input == '3':
        delete_project_type()
        project_type_menu()

    elif user_input == '4':
        show_all_project_types()
        project_type_menu()

    elif user_input == '5':
        admin_menu()

    else:
        print("Invalid input! Try again.")
        category_menu()


def category_menu():
    user_input = input("""
        1. Create category
        2. Update category
        3. Delete category
        4. Show all categories
        5. View categories by project type
        6. Go to back

        Enter your choice:  
        """)
    if user_input == '1':
        create_category()
        category_menu()

    elif user_input == '2':
        update_the_category()
        category_menu()

    elif user_input == '3':
        delete_category_from_table()
        category_menu()

    elif user_input == '4':
        show_all_categories()
        category_menu()

    elif user_input == '5':
        show_categories_by_project_type()
        category_menu()

    elif user_input == '6':
        admin_menu()

    else:
        print("Invalid input! Try again.")
        category_menu()


def admin_statistics():
    user_input = input("""
        1. Show unstarted initiatives
        2. Show initiative in the process
        3. Show ended initiatives
        4. Projects with the most votes
        5. Projects with the most votes in an initiative
        
        Enter your choice:  
        """)
    if user_input == '1':
        if not show_unstarted_initiatives():
            print("Unstarted initiatives not found.")
        admin_statistics()

    elif user_input == '2':
        show_started_initiative()
        admin_statistics()

    elif user_input == '3':
        show_ended_initiatives()
        admin_statistics()

    elif user_input == '4':
        pass

    elif user_input == '5':
        pass

    else:
        print("Invalid input! Try again.")
        admin_statistics()


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

    # auth_menu()
    admin_menu()
