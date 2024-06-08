import webbrowser
import os.path
import datetime

def search_engine_choice():                                                 # Initial menu options for user
    choice = input("Select a search engine:\n1 for Google\n2 for Bing\n3 for search history\n9 to quit\n")
    if choice == "1":
        return "google"
    elif choice == "2":
        print("Seriously?")
        return "bing"
    elif choice == "3":
        get_search_history()
    elif choice == "9":
        return 0
    else:
        print("Invalid input")
        search_system(1)

def search_terms():                                                         # Takes user search input and formats it for link
    search_raw = input("Enter search:\n")
    time_log = str(datetime.datetime.now())[:19]                            # Track log for history
    search_filtered = ""
    for i in search_raw:
        if i == " ":
            search_filtered += "+"                                          # Search links use "+" as spaces
        else:
            search_filtered += i
    search_history(search_raw, time_log)                                    # Send to search_history() to log history
    return search_filtered

def search_history(search, time):                                           # Logs search history in a .txt file
    file_path = os.path.abspath(".") + "/history.txt"                       # Create file if it does not exist
    if not os.path.isfile(file_path):
        open("history.txt", "x")
    with open(file_path, "r+") as file:                                     # Write to the beginning of the file, log is most recent first
        file_data = file.read()
        file.seek(0, 0)
        file.write(time + " " + search + "\n" + file_data)

def get_search_history():                                                   # Reads last 5 searches and returns to user
    file_path = os.path.abspath(".") + "/history.txt"                       # Check existence of history.txt
    if not os.path.isfile(file_path):
        print("You have no history")
        search_engine_choice()
    print("Last 5 searches:")
    index = 0
    with open(file_path) as file:
        for line in file:
            if index < 5:
                print(line)
            index += 1
    search_system(1)                                                        # ***Need to add capability to read next 5 searches here

def search_system(run_code):                                                # Initial function
    if run_code == 0:
        print("Exiting")
        return 0
    browser = search_engine_choice()
    if browser == 0:
        print("Exiting")
        return 0
    search_term = search_terms()
    webbrowser.open(f"https://www.{browser}.com/search?q=" + search_term, new=2)
    while True:
        option = input("1 to return to menu\n9 to exit\n")
        if option == "1":
            search_system(1)
        elif option == "9":
            search_system(9)
        else:
            print("Invalid input")