from queries.project_types import add_project_type, get_all_project_types, update_pr_type, delete_pr_type
from utils.common import print_list


def create_project_type():
    name = input("Enter project type name:  ")
    add_project_type(name)


def show_all_project_types():
    pr_types = get_all_project_types()
    if pr_types:
        print_list(pr_types)
        return True
    else:
        print("There is no project type")
        return None


def update_project_type():
    if show_all_project_types():
        id = input("Enter project type id you want to update:  ")
        new_name = input("Change the project type name:  ")
        update_pr_type(id=id, field='name', new_value=new_name)
        print("Successfully updated the project type name.")


def delete_project_type():
    if show_all_project_types():
        id = input("Enter project type id you want to delete:  ")
        delete_pr_type(id=id)
        print("Successfully deleted the project type.")
