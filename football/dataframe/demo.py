import polars as pl

pl.Config(tbl_rows=32)

df = pl.read_csv("scores.csv")

# print(df)

homeResults = df.select(
    team = pl.col("home_team"),
    is_win = pl.col("home_score") > pl.col("away_score"),
)

# print(homeResults)

awayResults = df.select(
    team = pl.col("away_team"),
    is_win = pl.col("away_score") > pl.col("home_score"),
)

# print(awayResults)

byTeam = pl.concat([homeResults, awayResults])

# print(byTeam)

results = byTeam.group_by("team").agg(
    num_games = pl.len(),
    wins = pl.col("is_win").sum(),
    losses = pl.col("is_win").not_().sum(),
)

print(results)

# stats = results.group_by("team").agg(
#     pl.col("num_games", "wins", "losses").sum(),
# ).with_columns(
#     win_percentage = (pl.col("wins") / pl.col("num_games")).round(3),
# ).sort(
#     pl.col("win_percentage"),
#     descending = True,
# )

# print(stats)
