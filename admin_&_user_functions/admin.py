from queries.initiatives import add_initiative


def create_initiative():
    name = input("Initiative name:  ")
    application_period = input("Application period:  (days)")
    moderation_period = input("Moderation period:  (days)")
    voting_period = input("Voting period:  (days)")
    allocated_funds = float(input("Allocated funds:  "))

    add_initiative(
        name=name,
        application_period=application_period,
        moderation_period=moderation_period,
        voting_period=voting_period,
        allocated_funds=allocated_funds
    )
