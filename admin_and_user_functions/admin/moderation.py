import datetime

from queries.appeals import get_new_appeals, update_appeals
from queries.initiatives import get_started_initiative


def moderation():
    initiative = get_started_initiative()
    start_moderation_period = initiative[2] + initiative[3]  # start_date + application_period
    current_date = datetime.date.today()
    end_moderation_period = start_moderation_period + initiative[4]  # start_moderation_period + moderation_period

    if start_moderation_period < current_date < end_moderation_period:
        appeals = get_new_appeals()
        for appeal in appeals:
            while True:
                print(appeal)
                choice = input("""
                1. Accept
                2. Reject
                
                Choice an option:  
                """)
                if choice == '1':
                    update_appeals(appeal[0], 'status', 'accepted')
                    break
                elif choice == '2':
                    update_appeals(appeal[0], 'status', 'rejected')
                    break
                else:
                    print("Invalid input. Try again.")

    else:
        print("Not currently in moderation process.")
