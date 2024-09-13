def print_enumerate(objs) -> None:
    for index, obj in enumerate(objs):
        print(f"{index + 1}. {obj}")


def select_option(objs) -> int:
    print_enumerate(objs)
    choice = int(input("Select an option:  "))
    return choice-1
