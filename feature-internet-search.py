import webbrowser
import os.path
import datetime

def search_engine_choice():
    choice = input("Select a search engine:\n1 for Google\n2 for Bing\n")
    if choice == "1":
        return "google"
    elif choice == "2":
        print("Seriously?")
        return "bing"
    else:
        print("Invalid input")
        search_engine_choice()

def search_terms():
    search_raw = input("Enter search:\n")
    time_log = str(datetime.datetime.now()[:19])
    search_filtered = ""
    for i in search_raw:
        if i == " ":
            search_filtered += "+"
        else:
            search_filtered += i
    search_history(search_raw, time_log)
    return search_filtered

def search_history(search, time):
    file_path = os.path.abspath(".") + "/history.txt"
    if not os.path.isfile(file_path):
        open("history.txt", "x")
    with open(file_path, "r+") as file:
        file_data = file.read()
        file.seek(0, 0)
        file.write(time + " " + search + "\n" + file_data)

def get_search_history():
    file_path = os.path.abspath(".") + "/history.txt"
    if not os.path.isfile(file_path):
        print("You have no history")
        search_engine_choice()
    print("Last 10 searches:")
    index = 0
    with open(file_path) as file:
        for line in file:
            if index < 10:
                print(line)
            index += 1
        


def search_system():
    browser = search_engine_choice()
    search_term = search_terms()
    #webbrowser.open(f"https://www.{browser}.com/search?q=" + search_term, new=2)

search_history("bbb", str(datetime.datetime.now())[:19])