import datetime

from admin_and_user_functions.admin.crud_categories import show_categories_by_project_type
from queries.appeals import add_appeal, get_all_appeals, get_my_all_appeals, get_my_accepted_appeals, \
    get_my_rejected_appeals, get_my_winner_appeals, get_my_new_appeals, get_all_appeals_in_initiative
from queries.districts import get_districts
from queries.initiatives import get_started_initiative
from queries.regions import get_regions
from queries.votes import add_vote, get_my_voted_appeals
from utils.common import print_list, check_funds


def send_appeal(uuid):
    initiative = get_started_initiative()
    if initiative:
        start_application_period = initiative[2]
        now = datetime.datetime.now()
        end_application_period = initiative[2] + initiative[3]  # start_date + application_period
        if start_application_period < now < end_application_period:
            initiative_id = initiative[0]

            if show_categories_by_project_type():
                category_id = int(input("Enter category id:  "))

                regions = get_regions()
                print_list(regions)
                region_id = int(input("Enter region id:  "))

                districts = get_districts(region_id)
                print_list(districts)
                district_id = int(input("Enter district id:  "))

                title = input("Enter the contents of the appeal:  ")

                while True:
                    funds_offered = float(input("Enter the offer amount:  "))
                    if not check_funds(allocated=initiative[8], offered=funds_offered):
                        print(f"Allocated amount:  {initiative[8]}")
                        print("The offer must not exceed the allocated amount.")
                    else:
                        break

                add_appeal(
                    user_id=uuid,
                    initiative_id=initiative_id,
                    category_id=category_id,
                    region_id=region_id,
                    district_id=district_id,
                    title=title,
                    funds_offered=funds_offered
                )
        else:
            print("Application period ended.")



def show_all_appeals():
    appeals = get_all_appeals()
    if appeals:
        print_list(appeals)
    else:
        print("There is no appeal.")


def show_my_all_appeals(uuid):
    appeals = get_my_all_appeals(uuid)
    if appeals:
        print_list(appeals)
    else:
        print("There is no your appeal.")


def show_my_new_appeals(uuid):
    appeals = get_my_new_appeals(uuid)
    if appeals:
        print_list(appeals)
    else:
        print("There is no your new appeal.")


def show_my_accepted_appeals(uuid):
    appeals = get_my_accepted_appeals(uuid)
    if appeals:
        print_list(appeals)
    else:
        print("There is no your accepted appeal.")


def show_my_rejected_appeals(uuid):
    appeals = get_my_rejected_appeals(uuid)
    if appeals:
        print_list(appeals)
    else:
        print("There is no your rejected appeal.")


def show_my_winner_appeals(uuid):
    appeals = get_my_winner_appeals(uuid)
    if appeals:
        print_list(appeals)
    else:
        print("There is no your winner appeal.")


def show_initiative_in_process():
    initiative = get_started_initiative()
    if initiative:
        print(initiative)
    else:
        print("There is no initiative in process.")



def vote_on_the_project(uuid):
    initiative = get_started_initiative()
    if initiative:
        start_voting_period = initiative[2] + initiative[3] + initiative[4]  # start_date + application_period + moderation_period
        now = datetime.datetime.now()
        end_voting_period = start_voting_period + initiative[5]  # start_voting_period + voting_period
        if start_voting_period < now < end_voting_period:
            initiative_id = initiative[0]
            appeals = get_all_appeals_in_initiative(initiative_id)
            if appeals:
                print_list(appeals)
                appeal_id = int(input("Enter the appeal id you want to vote"))
                add_vote(initiative_id=initiative_id, appeal_id=appeal_id, user_id=uuid)
            else:
                print("There is no appeal")
        elif now < start_voting_period:
            print("Voting period has not started.")
        else:
            print("Voting period has ended.")


def show_my_voted_appeals(uuid):
    appeals = get_my_voted_appeals(uuid)
    if appeals:
        print_list(appeals)
    else:
        print("You have not voted.")
