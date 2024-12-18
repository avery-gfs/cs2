import csv

# Read game data
with open("games.csv") as file:
    games = list(csv.DictReader(file))

# Convert scores from strings to numbers
for game in games:
    game["away_score"] = int(game["away_score"])
    game["home_score"] = int(game["home_score"])

# Each team gets its own TeamStats object
class TeamStats:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.pointsScored = 0
        self.pointsAllowed = 0
        self.numGames = 0

    # Update wins, losses, pointsScored, pointsAllowed, and numGames
    # based on game info
    def addStats(self, game):
        self.numGames += 1

        isHomeTeam = self.name == game["home_team"]
        isHomeWin = game["home_score"] > game["away_score"]

        if isHomeTeam == isHomeWin:
            self.wins += 1
        else:
            self.losses += 1

        self.pointsScored += game["home_score"]
        self.pointsAllowed += game["away_score"]

    # Calculate the win fraction
    def winPercent(self):
        return self.wins / self.numGames

    # Calculate points scored per game
    def pointsScoredPerGame(self):
        return self.pointsScored / self.numGames

    # Calculate points allowed per game
    def pointsAllowedPerGame(self):
        return self.pointsAllowed / self.numGames

    def __repr__(self):
        result = ""

        result += f"name:               {self.name}\n"
        result += f"wins:               {self.wins}\n"
        result += f"losses:             {self.losses}\n"
        result += f"winPercent:         {self.winPercent():.3f}\n"
        result += f"pointsScored:       {self.pointsScored}\n"
        result += f"pointsAllowed:      {self.pointsAllowed}\n"
        result += f"numGames:           {self.numGames}\n"
        result += f"pointsScored/game:  {self.pointsScoredPerGame():.1f}\n"
        result += f"pointsAllowed/game: {self.pointsAllowedPerGame():.1f}\n"

        return result

# Keys are team names, values are TeamStats objects
stats = {}

# Give each team an empty TeamStats object
for game in games:
    homeTeam = game["home_team"]
    awayTeam = game["away_team"]

    stats.setdefault(homeTeam, TeamStats(homeTeam))
    stats.setdefault(awayTeam, TeamStats(awayTeam))

# Update stats for home and away teams for each game
for game in games:
    homeStats = stats[game["home_team"]]
    awayStats = stats[game["away_team"]]

    homeStats.addStats(game)
    awayStats.addStats(game)

# Print final stats for each team
for team in stats:
    print(stats[team])

resultCSV = "name,wins,losses,win_percent,points_scored,points_allowed,num_games,points_scored_per_game,points_allowed_per_game"

# Generate output CSV file for team stats
for team in stats:
    teamStats = stats[team]

    rowData = [
      teamStats.name,
      teamStats.wins,
      teamStats.losses,
      teamStats.winPercent(),
      teamStats.pointsScored,
      teamStats.pointsAllowed,
      teamStats.numGames,
      teamStats.pointsScoredPerGame(),
      teamStats.pointsAllowedPerGame(),
    ]

    resultCSV += "\n" + ",".join(map(str, rowData))

# Write output CSV
with open("stats.csv", "w") as file:
    file.write(resultCSV)

