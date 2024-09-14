import datetime

from queries.initiatives import add_initiative, get_unstarted_initiatives, update_initiative, get_started_initiative, \
    get_initiative_by_id, get_ended_initiatives, get_all_initiatives
from utils.common import print_list


def create_initiative():
    name = input("Initiative name:  ")
    application_period = input("Application period: (days):  ")
    moderation_period = input("Moderation period: (days):  ")
    voting_period = input("Voting period: (days):  ")
    allocated_funds = float(input("Allocated funds:  "))

    add_initiative(
        name=name,
        application_period=f"{application_period} days",
        moderation_period=f"{moderation_period} days",
        voting_period=f"{voting_period} days",
        allocated_funds=allocated_funds
    )


def update_unstarted_initiative():
    if show_unstarted_initiatives():

        id = int(input("\nEnter initiative id you want to update:  "))
        field = choose_field()
        new_value = input(f"Enter new value for {field}:  ")

        if field == 'allocated_funds':
            new_value = float(new_value)

        update_initiative(id=id, field=field, new_value=new_value)

    else:
        print("Unstarted initiatives not found.")




def choose_field():
    choice = input("""
        1. Name
        2. Application period
        3. Moderation period
        4. Voting period
        5. Allocated funds

        Choose field you want to update:  """)

    if choice == '1':
        return 'name'
    elif choice == '2':
        return 'application_period'
    elif choice == '3':
        return 'moderation_period'
    elif choice == '4':
        return 'voting_period'
    elif choice == '5':
        return 'allocated_funds'
    else:
        print("Invalid input. Try again.")
        choose_field()


def start_initiative():
    initiatives = get_unstarted_initiatives()
    initiative = get_started_initiative()

    if not initiatives:
        print("Unstarted initiatives not found.")
        return None

    elif initiative:
        print("Sorry, there is an unfinished initiative.")
        return None

    else:
        id = int(input("\nEnter initiative id you want to start:  "))

        date = datetime.datetime.now()
        update_initiative(id=id, field='start_time', new_value=date)
        update_initiative(id=id, field='status', new_value=True)

        initiative = get_initiative_by_id(id)

        print(f"{initiative[1]} initiative has started.")


def show_unstarted_initiatives():
    initiatives = get_unstarted_initiatives()
    if initiatives:
        print_list(initiatives)
        return True

    return None


def show_started_initiative():
    initiative = get_started_initiative()
    if initiative:
        print(initiative)
    else:
        print("There is no initiative in the process.")


def show_ended_initiatives():
    initiatives = get_ended_initiatives()
    if initiatives:
        print_list(initiatives)
    else:
        print("Ended initiatives not found.")


def show_all_initiatives():
    initiatives = get_all_initiatives()
    if initiatives:
        print_list(initiatives)
    else:
        print("Initiatives not found.")
