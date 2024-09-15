from admin_and_user_functions.admin.crud_initiatives import show_all_initiatives
from queries.appeals import get_all_appeals_in_initiative
from queries.initiatives import get_all_initiatives
from queries.votes import count_all_votes, count_votes_on_initiatives, count_votes_on_appeal, get_users_voted_on_appeal, \
    get_appeals_with_the_most_votes, get_appeals_with_the_most_votes_on_initiative
from utils.common import print_list


def show_count_all_votes():
    print(count_all_votes())


def show_count_votes_on_initiatives():
    initiatives = get_all_initiatives()
    if initiatives:
        print_list(initiatives)
        initiative_id = int(input("Enter initiative id:  "))
        print(count_votes_on_initiatives(initiative_id))


def show_count_votes_on_appeal():
    show_all_initiatives()
    initiative_id = int(input("Enter initiative id:  "))
    appeals = get_all_appeals_in_initiative(initiative_id)
    if appeals:
        print_list(appeals)
        appeal_id = int(input("Enter appeal id:  "))
        print(count_votes_on_appeal(appeal_id))


def show_users_voted_on_appeal():
    show_all_initiatives()
    initiative_id = int(input("Enter initiative id:  "))
    appeals = get_all_appeals_in_initiative(initiative_id)
    if appeals:
        print_list(appeals)
        appeal_id = int(input("Enter appeal id:  "))
        print_list(get_users_voted_on_appeal(appeal_id))


def show_appeals_with_the_most_votes():  # show 10 appeals
    appeals = get_appeals_with_the_most_votes()
    print_list(appeals)


def show_appeals_with_the_most_votes_on_initiative():
    show_all_initiatives()
    initiative_id = int(input("Enter initiative id:  "))
    appeals = get_appeals_with_the_most_votes_on_initiative(initiative_id)
    print_list(appeals)
