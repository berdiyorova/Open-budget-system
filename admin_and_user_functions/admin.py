from queries.initiatives import add_initiative, get_unstarted_initiatives, update_initiative
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
    initiatives = get_unstarted_initiatives()
    if initiatives:
        print_list(initiatives)

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
