import webbrowser

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
    return search_filtered

def search_system():
    browser = search_engine_choice()
    search_term = search_terms()
    webbrowser.open(f"https://www.{browser}.com/search?q=" + search_term, new=2)
