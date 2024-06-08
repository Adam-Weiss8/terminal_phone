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

print("[green]Hello, and welcome to your phone main menu. Please make a selection.[/green]")
user_input = ''
while user_input != "Quit":
 print("""
    Enter the number for your selection or "Quit"
     [green]1.[/green] [blue]Contacts[/blue]
     [green]2.[/green] [red]Internet[/red]
     [green]3.[/green] [purple]Tasks and Subtasks[/purple]
 """)
 user_input = input("[green]Enter your selection:[/green] ")
 if user_input == "1":
  manage_contacts(contacts)
 elif user_input == "2":
  search_system(1)
 elif user_input == "3":
  phone_tasks(tasks)
 elif user_input == "Quit":
  print("Exiting Menu")
 else:
  print("[red]Invalid Selection[/red]")

