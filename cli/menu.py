
import sys
import datetime
import time
from colorama import init, Fore, Style
from models.team import Team
from models.driver import Driver
from models.race import Race
from models.result import Result
from database import Session
from tabulate import tabulate

init(autoreset=True)

import sys
import time
import random
from colorama import init, Fore, Style

init(autoreset=True)

def print_neon_banner():
    neon_colors = [Fore.CYAN, Fore.MAGENTA, Fore.YELLOW, Fore.GREEN, Fore.BLUE]
    banner_lines = [
        "   ________  ___      ___  ________  ________  ________  ________  ________  ________     ",
        "  |\\   __  \\|\\  \\    /  /||\\   __  \\|\\   __  \\|\\   __  \\|\\   __  \\|\\   __  \\|\\   __  \\    ",
        "  \\ \\  \\|\\  \\ \\  \\  /  / /\\ \\  \\|\\  \\ \\  \\|\\  \\ \\  \\|\\  \\ \\  \\|\\  \\ \\  \\|\\  \\ \\  \\|\\  \\   ",
        "   \\ \\   __  \\ \\  \\/  / /  \\ \\   __  \\ \\   _  _\\ \\   __  \\ \\   _  _\\ \\   __  \\ \\   _  _\\  ",
        "    \\ \\  \\ \\  \\ \\    / /    \\ \\  \\ \\  \\ \\  \\\\  \\\\ \\  \\ \\  \\ \\  \\\\  \\\\ \\  \\ \\  \\ \\  \\\\  \\| ",
        "     \\ \\__\\ \\__\\ \\__/ /      \\ \\__\\ \\__\\ \\__\\\\ _\\\\ \\__\\ \\__\\ \\__\\\\ _\\\\ \\__\\ \\__\\ \\__\\\\ _\\ ",
        "      \\|__|\\|__|\\|__|/        \\|__|\\|__|\\|__|\\|__|\\|__|\\|__|\\|__|\\|__|\\|__|\\|__|\\|__|\\|__|",
        "",
        "🏁  🏎️  🏆  FORMULA 1 Management CLI  🏆  🏎️  🏁"
    ]
    for line in banner_lines:
        color = random.choice(neon_colors)
        print(color + Style.BRIGHT, end="")
        for char in line:
            print(char, end='', flush=True)
            time.sleep(0.0005)
        print(Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "✨ © 2025 Captain 23. All rights reserved. ✨\n" + Style.RESET_ALL)


def motorsport_cheer():
    print(Fore.CYAN + "Engines are roaring! Get ready for the race!\n" + Style.RESET_ALL)
    print(Fore.GREEN + "Welcome to the Formula 1 Management CLI!\n" + Style.RESET_ALL)

def main_menu():    
    while True:
        print_neon_banner()
        motorsport_cheer()
        print("Main Menu:")
        print("1. Teams")
        print("2. Drivers")
        print("3. Races")
        print("4. View Options")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            teams_menu()
        elif choice == '2':
            drivers_menu()
        elif choice == '3':
            races_menu()
        elif choice == '4':
            view_menu()
        elif choice == '5':
            print("It's Lights Out And Away You Go. Ciao!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

def teams_menu():
    while True:
        print("\n--- Teams Menu ---")
        print("1. List Teams")
        print("2. Add Team")
        print("3. Update Team")
        print("4. Delete Team")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        session = Session()
        if choice == '1':
            teams = session.query(Team).all()
            if not teams:
                print("No teams found in the database.")
            else:
                headers = ["#", "Name", "Base", "Principal", "Championships", "Points"]
                table = [
                    [idx, team.name, team.base, team.Team_principal, team.championships_won, team.points]
                    for idx, team in enumerate(teams, 1)
                ]
                print(tabulate(table, headers, tablefmt="grid"))
        elif choice == '2':
            while True:
                name = input("Enter new team name: ").strip()
                if not name:
                    print("Team name cannot be empty.")
                    continue
                base = input("Enter team base: ").strip()
                if not base:
                    print("Team base cannot be empty.")
                    continue
                principal = input("Enter team principal: ").strip()
                if not principal:
                    print("Team principal cannot be empty.")
                    continue
                try:
                    championships = int(input("Enter championships won (number): ").strip())
                except ValueError:
                    print("Championships must be a number.")
                    continue
                try:
                    points = int(input("Enter points (number): ").strip())
                except ValueError:
                    print("Points must be a number.")
                    continue

                if session.query(Team).filter_by(name=name).first():
                    print("Team already exists.")
                    break
                team = Team(
                    name=name,
                    base=base,
                    Team_principal=principal,
                    championships_won=championships,
                    points=points
                )
                session.add(team)
                session.commit()
                print(f"Team '{name}' added.")
                break
        elif choice == '3':
            teams = session.query(Team).all()
            if not teams:
                print("No teams to update.")
                continue
            for idx, team in enumerate(teams, 1):
                print(f"{idx}. {team.name}")
            try:
                num = int(input("Enter team number to update: "))
                if 1 <= num <= len(teams):
                    team = teams[num-1]
                    new_name = input(f"Enter new team name [{team.name}]: ").strip() or team.name
                    new_base = input(f"Enter new team base [{team.base}]: ").strip() or team.base
                    new_principal = input(f"Enter new team principal [{team.Team_principal}]: ").strip() or team.Team_principal
                    try:
                        new_championships = input(f"Enter new championships won [{team.championships_won}]: ").strip()
                        new_championships = int(new_championships) if new_championships else team.championships_won
                    except ValueError:
                        print("Championships must be a number.")
                        continue
                    try:
                        new_points = input(f"Enter new points [{team.points}]: ").strip()
                        new_points = int(new_points) if new_points else team.points
                    except ValueError:
                        print("Points must be a number.")
                        continue
                    team.name = new_name
                    team.base = new_base
                    team.Team_principal = new_principal
                    team.championships_won = new_championships
                    team.points = new_points
                    session.commit()
                    print("Team updated.")
                else:
                    print("Invalid team number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            teams = session.query(Team).all()
            if not teams:
                print("No teams to delete.")
                continue
            for idx, team in enumerate(teams, 1):
                print(f"{idx}. {team.name}")
            try:
                num = int(input("Enter team number to delete: "))
                if 1 <= num <= len(teams):
                    team = teams[num-1]
                    # Delete all results for drivers in this team
                    drivers = session.query(Driver).filter_by(team_id=team.id).all()
                    for driver in drivers:
                        session.query(Result).filter_by(driver_id=driver.id).delete()
                        session.delete(driver)
                    session.delete(team)
                    session.commit()
                    print(f"Team '{team.name}' and its drivers/results deleted.")
                else:
                    print("Invalid team number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            session.close()
            break
        else:
            print("Invalid choice. Please try again.")
        session.close()

def drivers_menu():
    while True:
        print("\n--- Drivers Menu ---")
        print("1. List Drivers")
        print("2. Add Driver")
        print("3. Update Driver")
        print("4. Delete Driver")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        session = Session()
        if choice == '1':
            drivers = session.query(Driver).all()
            if not drivers:
                print("No drivers found in the database.")
            else:
                headers = ["#", "Name", "Age", "Nationality", "Titles", "Points", "Role", "Team ID"]
                table = [
                    [idx, d.name, d.age, d.nationality, d.titles_won, d.points_scored, d.role, d.team_id]
                    for idx, d in enumerate(drivers, 1)
                ]
                print(tabulate(table, headers, tablefmt="grid"))
        elif choice == '2':
            while True:
                name = input("Enter new driver name: ").strip()
                if not name:
                    print("Driver name cannot be empty.")
                    continue
                try:
                    age = int(input("Enter driver age: ").strip())
                except ValueError:
                    print("Age must be a number.")
                    continue
                nationality = input("Enter driver nationality: ").strip()
                if not nationality:
                    print("Driver nationality cannot be empty.")
                    continue
                try:
                    titles_won = int(input("Enter number of titles won: ").strip())
                except ValueError:
                    print("Titles won must be a number.")
                    continue
                try:
                    points_scored = int(input("Enter points scored: ").strip())
                except ValueError:
                    print("Points scored must be a number.")
                    continue
                role = input("Enter driver role (optional): ").strip() or None
                # Team assignment (optional)
                team_id = None
                teams = session.query(Team).all()
                if teams:
                    print("Select team for this driver:")
                    for idx, team in enumerate(teams, 1):
                        print(f"{idx}. {team.name}")
                    team_choice = input("Enter team number or leave blank for none: ").strip()
                    if team_choice:
                        try:
                            team_num = int(team_choice)
                            if 1 <= team_num <= len(teams):
                                team_id = teams[team_num-1].id
                        except ValueError:
                            print("Invalid team number. Skipping team assignment.")

                if session.query(Driver).filter_by(name=name).first():
                    print("Driver already exists.")
                    break
                driver = Driver(
                    name=name,
                    age=age,
                    nationality=nationality,
                    titles_won=titles_won,
                    points_scored=points_scored,
                    role=role,
                    team_id=team_id
                )
                session.add(driver)
                session.commit()
                print(f"Driver '{name}' added.")
                break
        elif choice == '3':
            drivers = session.query(Driver).all()
            if not drivers:
                print("No drivers to update.")
                continue
            for idx, driver in enumerate(drivers, 1):
                print(f"{idx}. {driver.name}")
            try:
                num = int(input("Enter driver number to update: "))
                if 1 <= num <= len(drivers):
                    driver = drivers[num-1]
                    new_name = input(f"Enter new driver name [{driver.name}]: ").strip() or driver.name
                    try:
                        new_age = input(f"Enter new age [{driver.age}]: ").strip()
                        new_age = int(new_age) if new_age else driver.age
                    except ValueError:
                        print("Age must be a number.")
                        continue
                    new_nationality = input(f"Enter new nationality [{driver.nationality}]: ").strip() or driver.nationality
                    try:
                        new_titles = input(f"Enter new titles won [{driver.titles_won}]: ").strip()
                        new_titles = int(new_titles) if new_titles else driver.titles_won
                    except ValueError:
                        print("Titles won must be a number.")
                        continue
                    try:
                        new_points = input(f"Enter new points scored [{driver.points_scored}]: ").strip()
                        new_points = int(new_points) if new_points else driver.points_scored
                    except ValueError:
                        print("Points scored must be a number.")
                        continue
                    new_role = input(f"Enter new role [{driver.role}]: ").strip() or driver.role
                    # Team assignment (optional)
                    team_id = driver.team_id
                    teams = session.query(Team).all()
                    if teams:
                        print("Select team for this driver:")
                        for idx, team in enumerate(teams, 1):
                            print(f"{idx}. {team.name}")
                        team_choice = input(f"Enter team number or leave blank to keep [{driver.team_id}]: ").strip()
                        if team_choice:
                            try:
                                team_num = int(team_choice)
                                if 1 <= team_num <= len(teams):
                                    team_id = teams[team_num-1].id
                            except ValueError:
                                print("Invalid team number. Keeping previous assignment.")
                    driver.name = new_name
                    driver.age = new_age
                    driver.nationality = new_nationality
                    driver.titles_won = new_titles
                    driver.points_scored = new_points
                    driver.role = new_role
                    driver.team_id = team_id
                    session.commit()
                    print("Driver updated.")
                else:
                    print("Invalid driver number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            drivers = session.query(Driver).all()
            if not drivers:
                print("No drivers to delete.")
                continue
            for idx, driver in enumerate(drivers, 1):
                print(f"{idx}. {driver.name}")
            try:
                num = int(input("Enter driver number to delete: "))
                if 1 <= num <= len(drivers):
                    driver = drivers[num-1]
                    # Delete all results for this driver before deleting the driver
                    session.query(Result).filter_by(driver_id=driver.id).delete()
                    session.delete(driver)
                    session.commit()
                    print(f"Driver '{driver.name}' and their results deleted.")
                else:
                    print("Invalid driver number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            session.close()
            break
        else:
            print("Invalid choice. Please try again.")
        session.close()

def races_menu():
    while True:
        print("\n--- Races Menu ---")
        print("1. List Races")
        print("2. Add Race")
        print("3. Update Race")
        print("4. Delete Race")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        session = Session()
        if choice == '1':
            races = session.query(Race).all()
            if not races:
                print("No races found in the database.")
            else:
                headers = ["#", "Name", "Circuit", "Location", "Date", "Laps", "Distance (km)", "Weather"]
                table = [
                    [idx, r.name, r.circuit, r.location, r.date, r.laps, r.distance_km, r.weather]
                    for idx, r in enumerate(races, 1)
                ]
                print(tabulate(table, headers, tablefmt="grid"))
        elif choice == '2':
            while True:
                name = input("Enter new race name: ").strip()
                if not name:
                    print("Race name cannot be empty.")
                    continue
                circuit = input("Enter circuit name: ").strip()
                if not circuit:
                    print("Circuit cannot be empty.")
                    continue
                location = input("Enter race location: ").strip()
                if not location:
                    print("Race location cannot be empty.")
                    continue
                date_str = input("Enter race date (YYYY-MM-DD): ").strip()
                if not date_str:
                    print("Race date cannot be empty.")
                    continue
                try:
                    race_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                except ValueError:
                    print("Date must be in YYYY-MM-DD format.")
                    continue
                try:
                    laps = int(input("Enter number of laps: ").strip())
                except ValueError:
                    print("Laps must be a number.")
                    continue
                try:
                    distance_km = float(input("Enter race distance in km: ").strip())
                except ValueError:
                    print("Distance must be a number.")
                    continue
                weather = input("Enter weather (optional): ").strip() or None

                if session.query(Race).filter_by(name=name).first():
                    print("Race already exists.")
                    break
                race = Race(
                    name=name,
                    circuit=circuit,
                    location=location,
                    date=race_date,
                    laps=laps,
                    distance_km=distance_km,
                    weather=weather
                )
                session.add(race)
                session.commit()
                print(f"Race '{name}' added.")

                # Prompt to add results immediately
                add_results = input("Would you like to add results for this race now? (y/n): ").strip().lower()
                if add_results == 'y':
                    drivers = session.query(Driver).all()
                    if not drivers:
                        print("No drivers found. Please add drivers first.")
                    else:
                        for driver in drivers:
                            print(f"\nEntering result for driver: {driver.name} (Team ID: {driver.team_id})")
                            try:
                                points = int(input("Points earned: ").strip())
                            except ValueError:
                                print("Invalid points, setting to 0.")
                                points = 0
                            status = input("Status (e.g., Finished, DNF): ").strip() or "Finished"
                            result = Result(
                                race_id=race.id,
                                driver_id=driver.id,
                                points=points,
                                status=status
                            )
                            session.add(result)
                        session.commit()
                        print("Results added for all drivers.")
                break
        elif choice == '3':
            races = session.query(Race).all()
            if not races:
                print("No races to update.")
                continue
            for idx, race in enumerate(races, 1):
                print(f"{idx}. {race.name}")
            try:
                num = int(input("Enter race number to update: "))
                if 1 <= num <= len(races):
                    race = races[num-1]
                    new_name = input(f"Enter new race name [{race.name}]: ").strip() or race.name
                    new_circuit = input(f"Enter new circuit [{race.circuit}]: ").strip() or race.circuit
                    new_location = input(f"Enter new location [{race.location}]: ").strip() or race.location
                    new_date_str = input(f"Enter new date [{race.date}]: ").strip()
                    if new_date_str:
                        try:
                            new_date = datetime.datetime.strptime(new_date_str, "%Y-%m-%d").date()
                        except ValueError:
                            print("Date must be in YYYY-MM-DD format.")
                            continue
                    else:
                        new_date = race.date
                    try:
                        new_laps = input(f"Enter new laps [{race.laps}]: ").strip()
                        new_laps = int(new_laps) if new_laps else race.laps
                    except ValueError:
                        print("Laps must be a number.")
                        continue
                    try:
                        new_distance = input(f"Enter new distance_km [{race.distance_km}]: ").strip()
                        new_distance = float(new_distance) if new_distance else race.distance_km
                    except ValueError:
                        print("Distance must be a number.")
                        continue
                    new_weather = input(f"Enter new weather [{race.weather}]: ").strip() or race.weather
                    race.name = new_name
                    race.circuit = new_circuit
                    race.location = new_location
                    race.date = new_date
                    race.laps = new_laps
                    race.distance_km = new_distance
                    race.weather = new_weather
                    session.commit()
                    print("Race updated.")
                else:
                    print("Invalid race number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            races = session.query(Race).all()
            if not races:
                print("No races to delete.")
                continue
            for idx, race in enumerate(races, 1):
                print(f"{idx}. {race.name}")
            try:
                num = int(input("Enter race number to delete: "))
                if 1 <= num <= len(races):
                    race = races[num-1]
                    # Delete all results for this race before deleting the race
                    session.query(Result).filter_by(race_id=race.id).delete()
                    session.delete(race)
                    session.commit()
                    print(f"Race '{race.name}' and its results deleted.")
                else:
                    print("Invalid race number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            session.close()
            break
        else:
            print("Invalid choice. Please try again.")
        session.close()

def view_menu():
    while True:
        print("\n--- View Options ---")
        print("1. View Team Standings")
        print("2. View Driver Standings")
        print("3. View Race Results")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")
        session = Session()
        if choice == '1':
            teams = session.query(Team).order_by(Team.points.desc()).all()
            if not teams:
                print("No teams found.")
            else:
                headers = ["#", "Name", "Team Principal", "Points"]
                table = [
                    [idx, t.name, t.Team_principal, t.points]
                    for idx, t in enumerate(teams, 1)
                ]
                print(tabulate(table, headers, tablefmt="grid"))
        elif choice == '2':
            drivers = session.query(Driver).order_by(Driver.points_scored.desc()).all()
            if not drivers:
                print("No drivers found.")
            else:
                headers = ["#", "Name", "Team", "Points"]
                table = []
                teams_dict = {team.id: team.name for team in session.query(Team).all()}
                for idx, d in enumerate(drivers, 1):
                    team_name = teams_dict.get(d.team_id, "None")
                    table.append([idx, d.name, team_name, d.points_scored])
                print(tabulate(table, headers, tablefmt="grid"))
        elif choice == '3':
            races = session.query(Race).order_by(Race.date.desc()).all()
            if not races:
                print("No races found.")
            else:
                print("Select a race to view results:")
                for idx, race in enumerate(races, 1):
                    print(f"{idx}. {race.name} ({race.date})")
                try:
                    race_choice = int(input("Enter race number: "))
                    if 1 <= race_choice <= len(races):
                        selected_race = races[race_choice - 1]
                        # Query results for this race, join with driver and team
                        results = (
                            session.query(Result, Driver, Team)
                            .join(Driver, Result.driver_id == Driver.id)
                            .join(Team, Driver.team_id == Team.id)
                            .filter(Result.race_id == selected_race.id)
                            .order_by(Result.points.desc())
                            .all()
                        )
                        headers = ["#", "Driver Name", "Team", "Points Earned", "Status"]
                        table = []
                        for idx, (result, driver, team) in enumerate(results, 1):
                            table.append([
                                idx,
                                driver.name,
                                team.name,
                                result.points,
                                result.status
                            ])
                        print(f"\nResults for {selected_race.name} ({selected_race.date}):")
                        print(tabulate(table, headers, tablefmt="grid"))
                    else:
                        print("Invalid race number.")
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == '4':
            session.close()
            break
        else:
            print("Invalid choice. Please try again.")
        session.close()

if __name__ == "__main__":
    main_menu()