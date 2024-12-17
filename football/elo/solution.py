import csv

# Read game data
with open("scores.csv") as file:
    games = list(csv.DictReader(file))

# Convert scores from strings to numbers
for game in games:
    game["away_score"] = int(game["away_score"])
    game["home_score"] = int(game["home_score"])

# Store team ratings, keys are team names, values are elo ratings
ratings = {}

# Rating sensitivity
k = 20

# Initialize ratings for all teams
for game in games:
    ratings[game["home_team"]] = 1500
    ratings[game["away_team"]] = 1500

for game in games:
    home = game["home_team"]
    away = game["away_team"]

    sHome = 1 if game["home_score"] > game["away_score"] else 0
    sAway = 1 - sHome

    eHome = 1 / (1 + 10 ** ((ratings[away] - ratings[home]) / 400))
    eAway = 1 / (1 + 10 ** ((ratings[home] - ratings[away]) / 400))

    ratings[home] += k * (sHome - eHome)
    ratings[away] += k * (sAway - eAway)

# Display team names and ratings sorted from highest to lowest
for (team, rating) in sorted(ratings.items(), key = lambda i: i[1], reverse = True):
    print(f"{team:21}", round(rating))

# Calculate the win probabilities for a given matchup

print("\nMatchup predictor:\n")

teamA = "Philadelphia Eagles"
teamB = "Las Vegas Raiders"

ra = ratings[teamA]
rb = ratings[teamB]

ea = 1 / (1 + 10 ** ((rb - ra) / 400))
eb = 1 / (1 + 10 ** ((ra - rb) / 400))

print(teamA, ea)
print(teamB, eb)
