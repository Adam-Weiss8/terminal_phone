# buttons need to be "Contacts", "Internet Browser"
# "Manage Tasks and Subtasks"

# "Contacts" dropdown should have Create, update, Delete, and Read
# "Internet" Browser just links directly to browser
# "Tasks and Subtasks" dropdown should have Create, Update, Delete, Read

# get input from user, if contacts, link to contacts, etc.
from feature_internet_search import search_system
from feature_manage_contacts import manage_contacts
from terminal_phone_tasks import phone_tasks

contacts = {}
tasks = []

print("Hello, and welcome to your phone main menu. Please make a selection.")
user_input = ''
while user_input != "Quit":
 print("""
    Enter the number for your selection or "Quit"
     1. Contacts
     2. Internet
     3. Tasks and Subtasks
 """)
 user_input = input("Enter your selection: ")
 if user_input == "1":
  contacts = manage_contacts(contacts)
 elif user_input == "2":
  search_system(1)
 elif user_input == "3":
  tasks = phone_tasks(tasks)
 elif user_input == "Quit":
  print("Exiting Menu")
 else:
  print("Invalid Selection")

