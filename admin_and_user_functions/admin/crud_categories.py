from admin_and_user_functions.admin.crud_project_types import show_all_project_types
from queries.categories import add_category, get_all_categories, update_category, delete_category
from utils.common import print_list


def create_category():
    if show_all_project_types():
        project_type_id = input("Enter project type id:  ")
        name = input("Enter category name:  ")
        add_category(project_type_id=project_type_id, name=name)


def show_all_categories():
    categories = get_all_categories()
    if categories:
        print_list(categories)
        return True
    else:
        print("There is no category")
        return None


def update_category_name():
    if show_all_categories():
        id = input("Enter category id you want to update:  ")
        new_name = input("Change the category name:  ")
        update_category(id=id, field='name', new_value=new_name)
        print("Successfully updated the category.")


def update_project_id():
    if show_all_categories():
        id = input("Enter category id you want to update:  ")
        if show_all_project_types():
            project_type_id = input("Change project type id:  ")
            update_category(id=id, field='project_type_id', new_value=project_type_id)
            print("Successfully updated the category.")


def delete_category_from_table():
    if show_all_categories():
        id = input("Enter category id you want to delete:  ")
        delete_category(id=id)
        print("Successfully deleted the category.")
