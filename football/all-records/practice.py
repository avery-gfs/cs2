import csv

# Read game data
with open("games.csv") as file:
    games = list(csv.DictReader(file))

# Convert scores from strings to numbers
for game in games:
    game["away_score"] = int(game["away_score"])
    game["home_score"] = int(game["home_score"])

# wins and losses are dictionaries for keeping track of
# stats for every team, where keys are team names and
# values are win or loss counts
wins = {}
losses = {}

# Initialize wins and losses to zero for each team
for game in games:
    homeTeam = game["home_team"]
    awayTeam = game["away_team"]

    wins[homeTeam] = 0
    wins[awayTeam] = 0

    losses[homeTeam] = 0
    losses[awayTeam] = 0

# Update stats for home and away teams for each game
for game in games:
    pass # Your code goes here !!

# Print final stats for each team
for team in wins:
    print(team, wins[team], losses[team])
