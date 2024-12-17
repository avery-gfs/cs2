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

    # YOUR CODE GOES HERE !!
    # YOUR CODE GOES HERE !!

    ratings[home] += 0 # YOUR CODE GOES HERE !!
    ratings[away] += 0 # YOUR CODE GOES HERE !!

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
