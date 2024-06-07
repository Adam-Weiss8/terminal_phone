def search_engine_choice():
    choice = input("Select a search engine:\n1 for Google\n2 for Bing\n")
    if choice == "1":
        return "google"
    elif choice == "2":
        return "bing"
    else:
        print("Invalid input")
        search_engine_choice()

search_engine_choice()