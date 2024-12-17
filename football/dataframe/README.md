Data analysis with a dataframe library: Polars.

https://docs.pola.rs/user-guide/getting-started/

```
shape: (32, 5)
┌───────────────────────┬───────────┬──────┬────────┬────────────────┐
│ team                  ┆ num_games ┆ wins ┆ losses ┆ win_percentage │
│ ---                   ┆ ---       ┆ ---  ┆ ---    ┆ ---            │
│ str                   ┆ u32       ┆ u32  ┆ u32    ┆ f64            │
╞═══════════════════════╪═══════════╪══════╪════════╪════════════════╡
│ Kansas City Chiefs    ┆ 14        ┆ 13   ┆ 1      ┆ 0.929          │
│ Philadelphia Eagles   ┆ 14        ┆ 12   ┆ 2      ┆ 0.857          │
│ Detroit Lions         ┆ 14        ┆ 12   ┆ 2      ┆ 0.857          │
│ Minnesota Vikings     ┆ 13        ┆ 11   ┆ 2      ┆ 0.846          │
│ Buffalo Bills         ┆ 14        ┆ 11   ┆ 3      ┆ 0.786          │
│ Pittsburgh Steelers   ┆ 14        ┆ 10   ┆ 4      ┆ 0.714          │
│ Green Bay Packers     ┆ 14        ┆ 10   ┆ 4      ┆ 0.714          │
│ Washington Commanders ┆ 14        ┆ 9    ┆ 5      ┆ 0.643          │
│ Denver Broncos        ┆ 14        ┆ 9    ┆ 5      ┆ 0.643          │
│ Houston Texans        ┆ 14        ┆ 9    ┆ 5      ┆ 0.643          │
│ Baltimore Ravens      ┆ 14        ┆ 9    ┆ 5      ┆ 0.643          │
│ Los Angeles Chargers  ┆ 14        ┆ 8    ┆ 6      ┆ 0.571          │
│ Tampa Bay Buccaneers  ┆ 14        ┆ 8    ┆ 6      ┆ 0.571          │
│ Seattle Seahawks      ┆ 14        ┆ 8    ┆ 6      ┆ 0.571          │
│ Los Angeles Rams      ┆ 14        ┆ 8    ┆ 6      ┆ 0.571          │
│ Arizona Cardinals     ┆ 14        ┆ 7    ┆ 7      ┆ 0.5            │
│ Atlanta Falcons       ┆ 13        ┆ 6    ┆ 7      ┆ 0.462          │
│ Miami Dolphins        ┆ 14        ┆ 6    ┆ 8      ┆ 0.429          │
│ Dallas Cowboys        ┆ 14        ┆ 6    ┆ 8      ┆ 0.429          │
│ Cincinnati Bengals    ┆ 14        ┆ 6    ┆ 8      ┆ 0.429          │
│ Indianapolis Colts    ┆ 14        ┆ 6    ┆ 8      ┆ 0.429          │
│ San Francisco 49ers   ┆ 14        ┆ 6    ┆ 8      ┆ 0.429          │
│ New Orleans Saints    ┆ 14        ┆ 5    ┆ 9      ┆ 0.357          │
│ Chicago Bears         ┆ 13        ┆ 4    ┆ 9      ┆ 0.308          │
│ New York Jets         ┆ 14        ┆ 4    ┆ 10     ┆ 0.286          │
│ Carolina Panthers     ┆ 14        ┆ 3    ┆ 11     ┆ 0.214          │
│ New England Patriots  ┆ 14        ┆ 3    ┆ 11     ┆ 0.214          │
│ Cleveland Browns      ┆ 14        ┆ 3    ┆ 11     ┆ 0.214          │
│ Tennessee Titans      ┆ 14        ┆ 3    ┆ 11     ┆ 0.214          │
│ Jacksonville Jaguars  ┆ 14        ┆ 3    ┆ 11     ┆ 0.214          │
│ Las Vegas Raiders     ┆ 13        ┆ 2    ┆ 11     ┆ 0.154          │
│ New York Giants       ┆ 14        ┆ 2    ┆ 12     ┆ 0.143          │
└───────────────────────┴───────────┴──────┴────────┴────────────────┘
```