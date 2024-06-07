#

def manage_contacts(current_contact_dict):
    updated_contact_dict = current_contact_dict
    print("""Please make a selection: 
          'C' to create contact
          'U' to update contact
          'D' to delete contact
          'R' to read all contacts
          'Q' to return to main menu: """)

    user_input = ''

    while user_input != "Quit":

#show all contacts

#create contact
        if(user_input == 'C'):
            print("Creating Contact")
            

#update contact
        elif(user_input == 'U'):
            print("updating ")

#delete contact
        elif(user_input == 'D'):
            print("deleting")

#read contact
        elif(user_input == 'R'):
            print("reading")

#quit
        elif(user_input == 'Q'):
            return updated_contact_dict

#improper input

        else:
            print("Improper input")


