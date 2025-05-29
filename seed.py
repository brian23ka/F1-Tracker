from models.driver import Driver
from models.team import Team
from models.race import Race
from models.result import Result
from database import Session
from datetime import date

# --- Teams ---
teams = [
    Team(name="Mercedes", points=147, Team_principal="Toto Wolff", base="Brackley"),
    Team(name="Oracle Red Bull Racing", points=143, Team_principal="Christian Horner", base="Milton Keynes"),
    Team(name="Ferrari", points=142, Team_principal="Fred Vasseur", base="Maranello"),
    Team(name="McLaren", points=321, Team_principal="Andrea Stella", base="Woking"),
    Team(name="Alpine", points=7, Team_principal="Flavio Briatore", base="Enstone"),
    Team(name="Aston Martin", points=14, Team_principal="Mike Krack", base="Silverstone"),
    Team(name="Visa Cash app Racing Bulls", points=22, Team_principal="Franz Tost", base="Faenza"),
    Team(name="Haas F1 Team", points=6, Team_principal="Ayao Komatsu", base="Kannapolis"),
    Team(name="Stake Kick Sauber F1 Team", points=6, Team_principal="Alessandro Alunni Bravi", base="Hinwil"),
    Team(name="Williams Racing", points=54, Team_principal="James Vowles", base="Grove"),
]

session = Session()

for team in teams:
    if not session.query(Team).filter_by(name=team.name).first():
        session.add(team)
session.commit()
teams = [session.query(Team).filter_by(name=t.name).first() for t in teams]

# --- Drivers ---
Drivers = [
    # Mercedes
    Driver(name="George Russell", team_id=teams[0].id, nationality="British", age=25, titles_won=0, points_scored=99, role="main"),
    Driver(name="Kimi Antonelli", team_id=teams[0].id, nationality="Italian", age=18, titles_won=0, points_scored=48, role="reserve"),
    # Red Bull
    Driver(name="Max Verstappen", team_id=teams[1].id, nationality="Dutch", age=27, titles_won=4, points_scored=136, role="main"),
    Driver(name="Yuki Tsunoda", team_id=teams[1].id, nationality="Japanese", age=25, titles_won=0, points_scored=10, role="main"),
    Driver(name="Liam Lawson", team_id=teams[1].id, nationality="Australian", age=22, titles_won=0, points_scored=4, role="reserve"),
    # Ferrari
    Driver(name="Charles Leclerc", team_id=teams[2].id, nationality="Monegasque", age=27, titles_won=0, points_scored=79, role="main"),
    Driver(name="Lewis Hamilton", team_id=teams[2].id, nationality="British", age=38, titles_won=7, points_scored=63, role="main"),
    Driver(name="Oliver Bearman", team_id=teams[2].id, nationality="British", age=18, titles_won=0, points_scored=6, role="reserve"),
    # McLaren
    Driver(name="Lando Norris", team_id=teams[3].id, nationality="British", age=24, titles_won=0, points_scored=158, role="main"),
    Driver(name="Oscar Piastri", team_id=teams[3].id, nationality="Australian", age=22, titles_won=0, points_scored=163, role="main"),
    Driver(name="Ryo Hirakawa", team_id=teams[3].id, nationality="Japanese", age=30, titles_won=0, points_scored=0, role="reserve"),
    # Alpine
    Driver(name="Pierre Gasly", team_id=teams[4].id, nationality="French", age=23, titles_won=0, points_scored=7, role="main"),
    Driver(name="Franco Colapinto", team_id=teams[4].id, nationality="Argentinian", age=25, titles_won=0, points_scored=0, role="main"),
    Driver(name="Jack Doohan", team_id=teams[4].id, nationality="Australian", age=21, titles_won=0, points_scored=0, role="reserve"),
    # Aston Martin
    Driver(name="Fernando Alonso", team_id=teams[5].id, nationality="Spanish", age=40, titles_won=2, points_scored=0, role="main"),
    Driver(name="Lance Stroll", team_id=teams[5].id, nationality="Canadian", age=29, titles_won=0, points_scored=14, role="main"),
    Driver(name="Felipe Drugovich", team_id=teams[5].id, nationality="Brazilian", age=23, titles_won=0, points_scored=0, role="reserve"),
    # Visa Cash app Racing Bulls
    Driver(name="Isack Hadjar", team_id=teams[6].id, nationality="French", age=19, titles_won=0, points_scored=25, role="main"),
    Driver(name="Liam Lawson", team_id=teams[6].id, nationality="Australian", age=22, titles_won=0, points_scored=4, role="main"),
    Driver(name="Dennis Hauger", team_id=teams[6].id, nationality="Norwegian", age=21, titles_won=0, points_scored=0, role="reserve"),
    # Haas
    Driver(name="Nico Hulkenberg", team_id=teams[7].id, nationality="German", age=30, titles_won=0, points_scored=6, role="main"),
    Driver(name="Gabriel Bortoletto", team_id=teams[7].id, nationality="Brazilian", age=20, titles_won=0, points_scored=0, role="main"),
    Driver(name="Oliver Bearman", team_id=teams[7].id, nationality="British", age=18, titles_won=0, points_scored=6, role="reserve"),
    # Stake Kick Sauber
    Driver(name="Valtteri Bottas", team_id=teams[8].id, nationality="Finnish", age=34, titles_won=0, points_scored=0, role="main"),
    Driver(name="Zhou Guanyu", team_id=teams[8].id, nationality="Chinese", age=25, titles_won=0, points_scored=0, role="main"),
    Driver(name="Théo Pourchaire", team_id=teams[8].id, nationality="French", age=20, titles_won=0, points_scored=0, role="reserve"),
    # Williams
    Driver(name="Alexander Albon", team_id=teams[9].id, nationality="Thai", age=27, titles_won=0, points_scored=42, role="main"),
    Driver(name="Carlos Sainz", team_id=teams[9].id, nationality="Spanish", age=29, titles_won=0, points_scored=12, role="main"),
    Driver(name="Logan Sargeant", team_id=teams[9].id, nationality="American", age=23, titles_won=0, points_scored=0, role="reserve"),
]

for driver in Drivers:
    if not session.query(Driver).filter_by(name=driver.name, team_id=driver.team_id).first():
        session.add(driver)
session.commit()

# --- Races (2025 up to Monaco) ---
races = [
    Race(name="Australian Grand Prix", circuit="Melbourne Grand Prix Circuit", location="Melbourne , Australia", date=date(2025, 3, 16), laps=58, distance_km=306.124, weather="Sunny with possibility of rainshowers"),
    Race(name="Chinese Grand Prix", circuit="Shanghai International Circuit", location="Shanghai, China", date=date(2025, 3, 23), laps=56, distance_km=305.066, weather="Warm and humid"),
    Race(name="Japanese Grand Prix", circuit="Suzuka Circuit", location="Suzuka, Japan", date=date(2025, 4, 6), laps=53, distance_km=307.47, weather="Warm and dry"),
    Race(name="Bahrain Grand Prix", circuit="Bahrain International Circuit", location="Sakhir, Bahrain", date=date(2025, 4, 13), laps=57, distance_km=308.238, weather="Warm and dry"),
    Race(name="Saudi Arabian Grand Prix", circuit="Jeddah Corniche Circuit", location="Jeddah, Saudi Arabia", date=date(2025, 4, 20), laps=50, distance_km=308.45, weather="Warm and humid"),
    Race(name="Miami Grand Prix", circuit="Miami International Autodrome", location="Miami, USA", date=date(2025, 5, 4), laps=57, distance_km=308.326, weather="Warm and sunny"),
    Race(name="Emilia Romagna Grand Prix", circuit="Auto Enzo E Dino Ferari", location="Imola , Italy", date=date(2025, 5, 18), laps=63, distance_km=309.047, weather="Warm and dry"),
    Race(name="Monaco Grand Prix", circuit="Circuit de Monaco", location="Monaco, Monaco", date=date(2025, 5, 25), laps=78, distance_km=260.286, weather="Warm and sunny"),
]

for race in races:
    if not session.query(Race).filter_by(name=race.name, circuit=race.circuit, location=race.location, date=race.date).first():
        session.add(race)
session.commit()

# --- Results for each race ---
drivers_dict = {d.name: d for d in session.query(Driver).all()}
teams_dict = {t.name: t for t in session.query(Team).all()}
race_objs = {r.name: session.query(Race).filter_by(name=r.name, date=r.date).first() for r in races}

all_results = [
    # Australian Grand Prix
    ("Australian Grand Prix", date(2025, 3, 16), [
        ("Lando Norris", "McLaren", 1, 25),
        ("Max Verstappen", "Oracle Red Bull Racing", 2, 18),
        ("George Russell", "Mercedes", 3, 15),
        ("Kimi Antonelli", "Mercedes", 4, 12),
        ("Alexander Albon", "Williams Racing", 5, 10),
        ("Lance Stroll", "Aston Martin", 6, 8),
        ("Nico Hulkenberg", "Stake Kick Sauber F1 Team", 7, 6),
        ("Charles Leclerc", "Ferrari", 8, 4),
        ("Oscar Piastri", "McLaren", 9, 2),
        ("Lewis Hamilton", "Ferrari", 10, 1),
        ("Pierre Gasly", "Alpine", 11, 0),
        ("Yuki Tsunoda", "Visa Cash app Racing Bulls", 12, 0),
        ("Esteban Ocon", "Haas F1 Team", 13, 0),
        ("Oliver Bearman", "Haas F1 Team", 14, 0),
        ("Liam Lawson", "Oracle Red Bull Racing", 15, 0),
        ("Gabriel Bortoletto", "Stake Kick Sauber F1 Team", 16, 0),
        ("Fernando Alonso", "Aston Martin", 17, 0),
        ("Carlos Sainz", "Williams Racing", 18, 0),
        ("Jack Doohan", "Alpine", 19, 0),
        ("Isack Hadjar", "Visa Cash app Racing Bulls", 20, 0),
    ]),
    # Chinese Grand Prix
    ("Chinese Grand Prix", date(2025, 3, 23), [
        ("Oscar Piastri", "McLaren", 1, 25),
        ("Lando Norris", "McLaren", 2, 18),
        ("George Russell", "Mercedes", 3, 15),
        ("Max Verstappen", "Oracle Red Bull Racing", 4, 12),
        ("Charles Leclerc", "Ferrari", 5, 0),
        ("Lewis Hamilton", "Ferrari", 6, 0),
        ("Esteban Ocon", "Haas F1 Team", 7, 10),
        ("Kimi Antonelli", "Mercedes", 8, 8),
        ("Alexander Albon", "Williams Racing", 9, 6),
        ("Oliver Bearman", "Haas F1 Team", 10, 4),
        ("Pierre Gasly", "Alpine", 11, 0),
        ("Lance Stroll", "Aston Martin", 12, 2),
        ("Carlos Sainz", "Williams Racing", 13, 1),
        ("Isack Hadjar", "Visa Cash app Racing Bulls", 14, 0),
        ("Jack Doohan", "Alpine", 15, 0),
        ("Liam Lawson", "Oracle Red Bull Racing", 16, 0),
        ("Gabriel Bortoletto", "Stake Kick Sauber F1 Team", 17, 0),
        ("Nico Hulkenberg", "Stake Kick Sauber F1 Team", 18, 0),
        ("Yuki Tsunoda", "Visa Cash app Racing Bulls", 19, 0),
        ("Fernando Alonso", "Aston Martin", 20, 0),
    ]),
    # Japanese Grand Prix
    ("Japanese Grand Prix", date(2025, 4, 6), [
        ("Max Verstappen", "Oracle Red Bull Racing", 1, 25),
        ("Lando Norris", "McLaren", 2, 18),
        ("Oscar Piastri", "McLaren", 3, 15),
        ("Charles Leclerc", "Ferrari", 4, 12),
        ("George Russell", "Mercedes", 5, 10),
        ("Kimi Antonelli", "Mercedes", 6, 8),
        ("Lewis Hamilton", "Ferrari", 7, 6),
        ("Isack Hadjar", "Visa Cash app Racing Bulls", 8, 4),
        ("Alexander Albon", "Williams Racing", 9, 2),
        ("Oliver Bearman", "Haas F1 Team", 10, 1),
        ("Fernando Alonso", "Aston Martin", 11, 0),
        ("Yuki Tsunoda", "Visa Cash app Racing Bulls", 12, 0),
        ("Pierre Gasly", "Alpine", 13, 0),
        ("Carlos Sainz", "Williams Racing", 14, 0),
        ("Jack Doohan", "Alpine", 15, 0),
        ("Nico Hulkenberg", "Stake Kick Sauber F1 Team", 16, 0),
        ("Liam Lawson", "Visa Cash app Racing Bulls", 17, 0),
        ("Esteban Ocon", "Haas F1 Team", 18, 0),
        ("Gabriel Bortoletto", "Stake Kick Sauber F1 Team", 19, 0),
        ("Lance Stroll", "Aston Martin", 20, 0),
    ]),
    # Bahrain Grand Prix
    ("Bahrain Grand Prix", date(2025, 4, 13), [
        ("Oscar Piastri", "McLaren", 1, 25),
        ("George Russell", "Mercedes", 2, 18),
        ("Lando Norris", "McLaren", 3, 15),
        ("Charles Leclerc", "Ferrari", 4, 12),
        ("Lewis Hamilton", "Ferrari", 5, 10),
        ("Max Verstappen", "Oracle Red Bull Racing", 6, 8),
        ("Pierre Gasly", "Alpine", 7, 6),
        ("Esteban Ocon", "Haas F1 Team", 8, 4),
        ("Yuki Tsunoda", "Visa Cash app Racing Bulls", 9, 2),
        ("Oliver Bearman", "Haas F1 Team", 10, 1),
        ("Kimi Antonelli", "Mercedes", 11, 0),
        ("Alexander Albon", "Williams Racing", 12, 0),
        ("Isack Hadjar", "Visa Cash app Racing Bulls", 13, 0),
        ("Jack Doohan", "Alpine", 14, 0),
        ("Fernando Alonso", "Aston Martin", 15, 0),
        ("Liam Lawson", "Visa Cash app Racing Bulls", 16, 0),
        ("Lance Stroll", "Aston Martin", 17, 0),
        ("Gabriel Bortoletto", "Stake Kick Sauber F1 Team", 18, 0),
        ("Carlos Sainz", "Williams Racing", 19, 0),
        ("Nico Hulkenberg", "Stake Kick Sauber F1 Team", 20, 0),
    ]),
    # Saudi Arabian Grand Prix
    ("Saudi Arabian Grand Prix", date(2025, 4, 20), [
        ("Oscar Piastri", "McLaren", 1, 25),
        ("Max Verstappen", "Oracle Red Bull Racing", 2, 18),
        ("Charles Leclerc", "Ferrari", 3, 15),
        ("Lando Norris", "McLaren", 4, 12),
        ("George Russell", "Mercedes", 5, 10),
        ("Kimi Antonelli", "Mercedes", 6, 8),
        ("Lewis Hamilton", "Ferrari", 7, 6),
        ("Carlos Sainz", "Williams Racing", 8, 4),
        ("Alexander Albon", "Williams Racing", 9, 2),
        ("Isack Hadjar", "Visa Cash app Racing Bulls", 10, 1),
        ("Fernando Alonso", "Aston Martin", 11, 0),
        ("Liam Lawson", "Visa Cash app Racing Bulls", 12, 0),
        ("Oliver Bearman", "Haas F1 Team", 13, 0),
        ("Esteban Ocon", "Haas F1 Team", 14, 0),
        ("Nico Hulkenberg", "Stake Kick Sauber F1 Team", 15, 0),
        ("Lance Stroll", "Aston Martin", 16, 0),
        ("Jack Doohan", "Alpine", 17, 0),
        ("Gabriel Bortoletto", "Stake Kick Sauber F1 Team", 18, 0),
        ("Yuki Tsunoda", "Visa Cash app Racing Bulls", 19, 0),
        ("Pierre Gasly", "Alpine", 20, 0),
    ]),
    # Miami Grand Prix
    ("Miami Grand Prix", date(2025, 5, 4), [
        ("Oscar Piastri", "McLaren", 1, 25),
        ("Lando Norris", "McLaren", 2, 18),
        ("George Russell", "Mercedes", 3, 15),
        ("Max Verstappen", "Oracle Red Bull Racing", 4, 12),
        ("Alexander Albon", "Williams Racing", 5, 10),
        ("Kimi Antonelli", "Mercedes", 6, 8),
        ("Charles Leclerc", "Ferrari", 7, 6),
        ("Lewis Hamilton", "Ferrari", 8, 4),
        ("Carlos Sainz", "Williams Racing", 9, 2),
        ("Yuki Tsunoda", "Visa Cash app Racing Bulls", 10, 1),
        ("Isack Hadjar", "Visa Cash app Racing Bulls", 11, 0),
        ("Esteban Ocon", "Haas F1 Team", 12, 0),
        ("Pierre Gasly", "Alpine", 13, 0),
        ("Nico Hulkenberg", "Stake Kick Sauber F1 Team", 14, 0),
        ("Fernando Alonso", "Aston Martin", 15, 0),
        ("Lance Stroll", "Aston Martin", 16, 0),
        ("Liam Lawson", "Visa Cash app Racing Bulls", 17, 0),
        ("Gabriel Bortoletto", "Stake Kick Sauber F1 Team", 18, 0),
        ("Oliver Bearman", "Haas F1 Team", 19, 0),
        ("Jack Doohan", "Alpine", 20, 0),
    ]),
    # Emilia Romagna Grand Prix
    ("Emilia Romagna Grand Prix", date(2025, 5, 18), [
        ("Oscar Piastri", "McLaren", 1, 25),
        ("Lando Norris", "McLaren", 2, 18),
        ("George Russell", "Mercedes", 3, 15),
        ("Max Verstappen", "Oracle Red Bull Racing", 4, 12),
        ("Alexander Albon", "Williams Racing", 5, 10),
        ("Kimi Antonelli", "Mercedes", 6, 8),
        ("Charles Leclerc", "Ferrari", 7, 6),
        ("Lewis Hamilton", "Ferrari", 8, 4),
        ("Carlos Sainz", "Williams Racing", 9, 2),
        ("Yuki Tsunoda", "Visa Cash app Racing Bulls", 10, 1),
        ("Isack Hadjar", "Visa Cash app Racing Bulls", 11, 0),
        ("Esteban Ocon", "Haas F1 Team", 12, 0),
        ("Pierre Gasly", "Alpine", 13, 0),
        ("Nico Hulkenberg", "Stake Kick Sauber F1 Team", 14, 0),
        ("Fernando Alonso", "Aston Martin", 15, 0),
        ("Lance Stroll", "Aston Martin", 16, 0),
        ("Liam Lawson", "Visa Cash app Racing Bulls", 17, 0),
        ("Gabriel Bortoletto", "Stake Kick Sauber F1 Team", 18, 0),
        ("Oliver Bearman", "Haas F1 Team", 19, 0),
        ("Jack Doohan", "Alpine", 20, 0),
    ]),
    # Monaco Grand Prix
    ("Monaco Grand Prix", date(2025, 5, 25), [
        ("Lando Norris", "McLaren", 1, 25),
        ("Charles Leclerc", "Ferrari", 2, 18),
        ("Oscar Piastri", "McLaren", 3, 15),
        ("Max Verstappen", "Oracle Red Bull Racing", 4, 12),
        ("Lewis Hamilton", "Ferrari", 5, 10),
        ("Isack Hadjar", "Visa Cash app Racing Bulls", 6, 8),
        ("Esteban Ocon", "Haas F1 Team", 7, 6),
        ("Liam Lawson", "Visa Cash app Racing Bulls", 8, 4),
        ("Alexander Albon", "Williams Racing", 9, 2),
        ("Carlos Sainz", "Williams Racing", 10, 1),
        ("George Russell", "Mercedes", 11, 0),
        ("Oliver Bearman", "Haas F1 Team", 12, 0),
        ("Franco Colapinto", "Alpine", 13, 0),
        ("Gabriel Bortoletto", "Stake Kick Sauber F1 Team", 14, 0),
        ("Lance Stroll", "Aston Martin", 15, 0),
        ("Nico Hulkenberg", "Stake Kick Sauber F1 Team", 16, 0),
        ("Yuki Tsunoda", "Visa Cash app Racing Bulls", 17, 0),
        ("Kimi Antonelli", "Mercedes", 18, 0),
        ("Fernando Alonso", "Aston Martin", 19, 0),
        ("Pierre Gasly", "Alpine", 20, 0),
    ]),
]
for race_name, race_date, results in all_results:
    race = session.query(Race).filter_by(name=race_name, date=race_date).first()
    for idx, (driver_name, team_name, position, points) in enumerate(results):
        driver = drivers_dict.get(driver_name)
        team = teams_dict.get(team_name)
        status = "DNF" if idx >= len(results) - 2 else "Completed"
        if driver and team and race:
            result = session.query(Result).filter_by(race_id=race.id, driver_id=driver.id).first()
            if result:
                # Update existing result
                result.team_id = team.id
                result.position = position
                result.points = points
                result.laps_completed = race.laps
                result.status = status
            else:
                # Add new result
                session.add(Result(
                    race_id=race.id,
                    driver_id=driver.id,
                    team_id=team.id,
                    position=position,
                    points=points,
                    laps_completed=race.laps,
                    status=status
                ))
session.commit()
session.close()