import datetime

from queries.initiatives import get_started_initiative
from queries.votes import get_appeals_with_the_most_votes_on_initiative


def get_winners():
    initiative = get_started_initiative()

    #  start_date + application_period + moderation_period + voting_period
    end_time = initiative[2] + initiative[3] + initiative[4] + initiative[5]
    if datetime.datetime.now() >= end_time:
        appeals = get_appeals_with_the_most_votes_on_initiative(initiative[0])
        total_amount = 0
        winners = []

        for appeal in appeals:
            if total_amount < initiative[7]:  # compare total amount and allocated funds for initiative
                total_amount += appeal[9]  # add approved funds
                winners.append(appeal)
            else:
                break

        return winners
