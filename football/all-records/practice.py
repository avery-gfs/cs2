import csv

# Read game data
with open("scores.csv") as file:
    games = list(csv.DictReader(file))

# Convert scores from strings to numbers
for game in games:
    game["away_score"] = int(game["away_score"])
    game["home_score"] = int(game["home_score"])

wins = {}
losses = {}

# Initialize wins and losses to zero for each time
for game in games:
    homeTeam = game["home_team"]
    awayTeam = game["away_team"]

    wins.setdefault(homeTeam, 0)
    wins.setdefault(awayTeam, 0)

    losses.setdefault(homeTeam, 0)
    losses.setdefault(awayTeam, 0)

# Update stats for home and away teams for each game
for game in games:
    pass # Your code goes here !!

# Print final stats for each team
for team in wins:
    print(team, wins[team], losses[team])
