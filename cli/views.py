def create_menu(title, options, actions):
    while True:
        print(f"\n--- {title} ---")
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")
        choice = input("Enter your choice: ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            action = actions.get(choice)
            if action:
                action()
            if options[int(choice)-1].lower().startswith("back"):
                break
        else:
            print("Invalid choice. Please try again.")

# Example usage for a view menu:
def view_team_standings():
    print("TODO: Display team standings")

def view_driver_standings():
    print("TODO: Display driver standings")

def view_race_results():
    print("TODO: Display race results")

def view_menu():
    options = [
        "View Team Standings",
        "View Driver Standings",
        "View Race Results",
        "Back to Main Menu"
    ]
    actions = {
        "1": view_team_standings,
        "2": view_driver_standings,
        "3": view_race_results,
        "4": lambda: None  # No action, just returns to main menu
    }
    create_menu("View Options", options, actions)