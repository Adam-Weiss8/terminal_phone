# buttons need to be "Contacts", "Internet Browser"
# "Manage Tasks and Subtasks"

# "Contacts" dropdown should have Create, update, Delete, and Read
# "Internet" Browser just links directly to browser
# "Tasks and Subtasks" dropdown should have Create, Update, Delete, Read

# get input from user, if contacts, link to contacts, etc.
from feature-internet-search import search_system
from feature-manage-contacts import manage_contacts
from tasks_features import phone_tasks

print("Hello, and welcome to your phone main menu. Please make a selection.")
user_input = ''
while user_input != "Quit":
 print("""
    Enter the number for your selection
     1. Contacts
     2. Internet
     3. Tasks and Subtasks
 """)
    user_input = input("Enter your selection: ")
 if user_input == "Contacts":
  manage_contacts()
 elif user_input == "Internet":
  search_system()
 elif user_input == "Tasks and Subtasks":
  phone_tasks()
 elif user_input == "Quit":
  print("Exiting Menu")
 else:
  print("Invalid Selection")

