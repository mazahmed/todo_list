"""This is a Terminal-based program that allows a user to create and edit a to-do list.

The stub of each function has been provided. Read the docstrings for what each 
function should do and complete the body of the functions below.

You can run the script in your Terminal at any time using the command:

    >>> python todo_list.py

"""

def add_to_list(my_list):
    """Takes user input and adds it as a new item to the end of the list."""
    todo = (raw_input("What would you like to add? "))
    my_list.append(todo)


def view_list(my_list):
    """Print each item in the list."""
    for action in my_list:
        print action

def remove_first_item(my_list):
    """delete first item in list"""
    first = my_list[0]
    my_list.remove(first)


def index_add_to_list(my_list):
    """add user's answer to specific index, also user's answer"""
    todo = (raw_input("What would you like to add? "))
    index = int(raw_input("Where would you like to add it? "))
    #int(index)
    my_list.insert(index-1, todo)

def index_edit_list(my_list):
    """edit list at given index"""
    index = int(raw_input("What number item would you like to change? "))
    edit = (raw_input("What would you like to change it to? "))
    my_list[index-1] = edit


def display_main_menu(my_list):
    """Displays main options, takes in user input, and calls view or add function."""

    user_options = """
    \nWould you like to:
    A. Add a new item
    B. View list
    C. Quit the program
    D. Delete the first item
    E. Insert to specific index
    F. Change a particular list item
    >>> """

    while True:
        # Collect input and include your if/elif/else statements here.
        print user_options
        answer = raw_input("What would you like to do? ")
        if answer == "A":
            add_to_list(my_list)
        elif answer == "B":
            view_list(my_list)
        elif answer == "C":
            break
        elif answer == "D":
            remove_first_item(my_list)
        elif answer == "E":
            index_add_to_list(my_list)
        elif answer == "F":
            index_edit_list(my_list)
        else:
            print user_options

#-------------------------------------------------

my_list = []
display_main_menu(my_list)
