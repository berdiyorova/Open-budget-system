from admin_and_user_functions.admin.crud_categories import create_category, update_the_category, \
    delete_category_from_table, show_all_categories, show_categories_by_project_type
from admin_and_user_functions.admin.crud_initiatives import create_initiative, update_unstarted_initiative, \
    start_initiative, show_unstarted_initiatives, show_started_initiative, show_ended_initiatives, show_all_initiatives
from admin_and_user_functions.admin.crud_project_types import create_project_type, update_project_type, \
    delete_project_type, show_all_project_types
from admin_and_user_functions.admin.get_winners import get_winners
from admin_and_user_functions.admin.moderation import moderation
from admin_and_user_functions.show_statistics import show_count_all_votes, show_count_votes_on_initiatives, \
    show_count_votes_on_appeal, show_users_voted_on_appeal, show_appeals_with_the_most_votes, \
    show_appeals_with_the_most_votes_on_initiative
from admin_and_user_functions.user import send_appeal, show_all_appeals, show_my_all_appeals, show_my_new_appeals, \
    show_my_accepted_appeals, show_my_rejected_appeals, show_my_winner_appeals, vote_on_the_project, \
    show_initiative_in_process, show_my_voted_appeals
from auth.login import log_in
from auth.logout import logout
from auth.register import register
from config.models import create_all_tables
from queries.districts import insert_districts
from queries.regions import insert_regions
from utils.common import print_list


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
            5. Get winners
            6. Show statistics
            7. Logout

            Enter your choice:  
            """)
    if user_input == '1':
        initiative_menu()

    elif user_input == '2':
        project_type_menu()

    elif user_input == '3':
        category_menu()

    elif user_input == '4':
        moderation()
        admin_menu()

    elif user_input == '5':
        print_list(get_winners())
        admin_menu()

    elif user_input == '6':
        statistics_menu()

    elif user_input == '7':
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


def statistics_menu():
    user_input = input("""
        1. Show unstarted initiatives
        2. Show initiative in the process
        3. Show ended initiatives
        4. Count all votes
        5. Count votes on initiatives
        6. Count votes on appeals
        7. Show users voted on appeal
        8. Show appeals with the most votes
        9. Show appeals with the most votes on the initiative
        10. Go to back
        
        Enter your choice:  
        """)
    if user_input == '1':
        if not show_unstarted_initiatives():
            print("Unstarted initiatives not found.")
        statistics_menu()

    elif user_input == '2':
        show_started_initiative()
        statistics_menu()

    elif user_input == '3':
        show_ended_initiatives()
        statistics_menu()

    elif user_input == '4':
        show_count_all_votes()
        statistics_menu()

    elif user_input == '5':
        show_count_votes_on_initiatives()
        statistics_menu()

    elif user_input == '6':
        show_count_votes_on_appeal()
        statistics_menu()

    elif user_input == '7':
        show_users_voted_on_appeal()
        statistics_menu()

    elif user_input == '8':
        show_appeals_with_the_most_votes()
        statistics_menu()

    elif user_input == '9':
        show_appeals_with_the_most_votes_on_initiative()
        statistics_menu()

    elif user_input == '10':
        admin_menu()

    else:
        print("Invalid input! Try again.")
        statistics_menu()


def user_menu(uuid):
    user_input = input("""
        1. Send an appeal
        2. All appeals
        3. My all appeals
        4. My new appeals
        5. My accepted appeals
        6. My rejected appeals
        7. My winner appeals
        8. Vote
        9. All initiatives
        10. Show my voted appeals
        11. Logout
        """)
    if user_input == '1':
        send_appeal(uuid)
        user_menu(uuid)

    elif user_input == '2':
        show_all_appeals()
        user_menu(uuid)

    elif user_input == '3':
        show_my_all_appeals(uuid)
        user_menu(uuid)

    elif user_input == '4':
        show_my_new_appeals(uuid)
        user_menu(uuid)

    elif user_input == '5':
        show_my_accepted_appeals(uuid)
        user_menu(uuid)

    elif user_input == '6':
        show_my_rejected_appeals(uuid)
        user_menu(uuid)

    elif user_input == '7':
        show_my_winner_appeals(uuid)
        user_menu(uuid)

    elif user_input == '8':
        vote_on_the_project(uuid)
        user_menu(uuid)

    elif user_input == '9':
        show_all_initiatives()
        user_menu(uuid)

    elif user_input == '10':
        show_my_voted_appeals(uuid)
        user_menu(uuid)

    elif user_input == '11':
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
    # admin_menu()
