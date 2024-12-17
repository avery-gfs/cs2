import polars as pl

# Configure polars to output 32 rows so we can see all teams
pl.Config(tbl_rows=32)

# Read CSV data as a dataframe
df = pl.read_csv("scores.csv")

print(df)

# Get the win / loss result for the home team in each game
homeResults = df.select(
    team = pl.col("home_team"),
    is_win = pl.col("home_score") > pl.col("away_score"),
)

print(homeResults)

# Get the win / loss result for the away team in each game
awayResults = df.select(
    team = pl.col("away_team"),
    is_win = pl.col("away_score") > pl.col("home_score"),
)

print(awayResults)

# Combine the home and away win loss results
byTeam = pl.concat([homeResults, awayResults])

print(byTeam)

# Group the wins and losses for each team together, and add
# them together to get total win and loss counts
results = byTeam.group_by("team").agg(
    num_games = pl.len(),
    wins = pl.col("is_win").sum(),
    losses = pl.col("is_win").not_().sum(),
)

print(results)

# Calculate the win percentage for each team from its wins and losses
winPercent = results.with_columns(
    win_percentage = (pl.col("wins") / pl.col("num_games")).round(3),
)

print(winPercent)

# Sort the team data by win percentage, highest to lowest
finalStats = winPercent.sort(
    "win_percentage",
    descending = True,
)

print(finalStats)
