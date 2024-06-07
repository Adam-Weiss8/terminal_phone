import webbrowser
import os.path

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
    search_filtered = ""
    for i in search_raw:
        if i == " ":
            search_filtered += "+"
        else:
            search_filtered += i
    search_history(search_raw)
    return search_filtered

def search_history(search):
    file_path = os.path.abspath(".") + "/history.txt"
    if not os.path.isfile(file_path):
        open("history.txt", "x")
    with open(file_path, "a") as file:
        file.write(search)


def search_system():
    browser = search_engine_choice()
    search_term = search_terms()
    #webbrowser.open(f"https://www.{browser}.com/search?q=" + search_term, new=2)

search_history("a")