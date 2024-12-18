import polars as pl

# Increase table display size
pl.Config(tbl_rows=32, tbl_cols=10)

# Read CSV data as a dataframe
games = pl.read_csv("games.csv")
print(games)

# Get the win / loss and scoring results for the home and away teams in each game

homeResults = games.select(
    team = pl.col("home_team"),
    isWin = pl.col("home_score") > pl.col("away_score"),
    scored = pl.col("home_score"),
    allowed = pl.col("away_score"),
)

awayResults = games.select(
    team = pl.col("away_team"),
    isWin = pl.col("away_score") > pl.col("home_score"),
    scored = pl.col("away_score"),
    allowed = pl.col("home_score"),
)

# Combine the home and away win loss results
combined = pl.concat([homeResults, awayResults])
print(combined)

# Group the stats from each team game into a single row
summary = combined.group_by("team").agg(
    numGames = pl.len(),
    wins = pl.sum("isWin"),
    losses = pl.col("isWin").not_().sum(),
    scored = pl.sum("scored"),
    allowed = pl.sum("allowed"),
)

print(summary)

# Calculate the per-game stats for each team
# Sort the team data by win percentage, highest to lowest
finalStats = summary.with_columns(
    winPct = (pl.col("wins") / pl.col("numGames")).round(3),
    scoredPerGame = (pl.col("scored") / pl.col("numGames")).round(1),
    allowedPerGame = (pl.col("allowed") / pl.col("numGames")).round(1),
).sort("winPct", descending = True)

print(finalStats)
