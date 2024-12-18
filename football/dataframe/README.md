Data analysis with a dataframe library: Polars.

https://docs.pola.rs/user-guide/getting-started/

```
shape: (32, 9)
┌───────────────────────┬──────────┬──────┬────────┬────────┬─────────┬────────┬───────────────┬────────────────┐
│ team                  ┆ numGames ┆ wins ┆ losses ┆ scored ┆ allowed ┆ winPct ┆ scoredPerGame ┆ allowedPerGame │
│ ---                   ┆ ---      ┆ ---  ┆ ---    ┆ ---    ┆ ---     ┆ ---    ┆ ---           ┆ ---            │
│ str                   ┆ u32      ┆ u32  ┆ u32    ┆ i64    ┆ i64     ┆ f64    ┆ f64           ┆ f64            │
╞═══════════════════════╪══════════╪══════╪════════╪════════╪═════════╪════════╪═══════════════╪════════════════╡
│ Kansas City Chiefs    ┆ 14       ┆ 13   ┆ 1      ┆ 329    ┆ 259     ┆ 0.929  ┆ 23.5          ┆ 18.5           │
│ Detroit Lions         ┆ 14       ┆ 12   ┆ 2      ┆ 459    ┆ 282     ┆ 0.857  ┆ 32.8          ┆ 20.1           │
│ Philadelphia Eagles   ┆ 14       ┆ 12   ┆ 2      ┆ 369    ┆ 247     ┆ 0.857  ┆ 26.4          ┆ 17.6           │
│ Minnesota Vikings     ┆ 13       ┆ 11   ┆ 2      ┆ 339    ┆ 240     ┆ 0.846  ┆ 26.1          ┆ 18.5           │
│ Buffalo Bills         ┆ 14       ┆ 11   ┆ 3      ┆ 445    ┆ 310     ┆ 0.786  ┆ 31.8          ┆ 22.1           │
│ Pittsburgh Steelers   ┆ 14       ┆ 10   ┆ 4      ┆ 336    ┆ 265     ┆ 0.714  ┆ 24.0          ┆ 18.9           │
│ Green Bay Packers     ┆ 14       ┆ 10   ┆ 4      ┆ 379    ┆ 287     ┆ 0.714  ┆ 27.1          ┆ 20.5           │
│ Washington Commanders ┆ 14       ┆ 9    ┆ 5      ┆ 396    ┆ 315     ┆ 0.643  ┆ 28.3          ┆ 22.5           │
│ Baltimore Ravens      ┆ 14       ┆ 9    ┆ 5      ┆ 418    ┆ 332     ┆ 0.643  ┆ 29.9          ┆ 23.7           │
│ Denver Broncos        ┆ 14       ┆ 9    ┆ 5      ┆ 336    ┆ 247     ┆ 0.643  ┆ 24.0          ┆ 17.6           │
│ Houston Texans        ┆ 14       ┆ 9    ┆ 5      ┆ 328    ┆ 300     ┆ 0.643  ┆ 23.4          ┆ 21.4           │
│ Seattle Seahawks      ┆ 14       ┆ 8    ┆ 6      ┆ 315    ┆ 313     ┆ 0.571  ┆ 22.5          ┆ 22.4           │
│ Los Angeles Chargers  ┆ 14       ┆ 8    ┆ 6      ┆ 294    ┆ 247     ┆ 0.571  ┆ 21.0          ┆ 17.6           │
│ Los Angeles Rams      ┆ 14       ┆ 8    ┆ 6      ┆ 310    ┆ 338     ┆ 0.571  ┆ 22.1          ┆ 24.1           │
│ Tampa Bay Buccaneers  ┆ 14       ┆ 8    ┆ 6      ┆ 403    ┆ 326     ┆ 0.571  ┆ 28.8          ┆ 23.3           │
│ Arizona Cardinals     ┆ 14       ┆ 7    ┆ 7      ┆ 314    ┆ 306     ┆ 0.5    ┆ 22.4          ┆ 21.9           │
│ Atlanta Falcons       ┆ 13       ┆ 6    ┆ 7      ┆ 278    ┆ 333     ┆ 0.462  ┆ 21.4          ┆ 25.6           │
│ Indianapolis Colts    ┆ 14       ┆ 6    ┆ 8      ┆ 280    ┆ 329     ┆ 0.429  ┆ 20.0          ┆ 23.5           │
│ Dallas Cowboys        ┆ 14       ┆ 6    ┆ 8      ┆ 298    ┆ 380     ┆ 0.429  ┆ 21.3          ┆ 27.1           │
│ Cincinnati Bengals    ┆ 14       ┆ 6    ┆ 8      ┆ 399    ┆ 387     ┆ 0.429  ┆ 28.5          ┆ 27.6           │
│ San Francisco 49ers   ┆ 14       ┆ 6    ┆ 8      ┆ 314    ┆ 320     ┆ 0.429  ┆ 22.4          ┆ 22.9           │
│ Miami Dolphins        ┆ 14       ┆ 6    ┆ 8      ┆ 276    ┆ 312     ┆ 0.429  ┆ 19.7          ┆ 22.3           │
│ New Orleans Saints    ┆ 14       ┆ 5    ┆ 9      ┆ 309    ┆ 312     ┆ 0.357  ┆ 22.1          ┆ 22.3           │
│ Chicago Bears         ┆ 13       ┆ 4    ┆ 9      ┆ 254    ┆ 278     ┆ 0.308  ┆ 19.5          ┆ 21.4           │
│ New York Jets         ┆ 14       ┆ 4    ┆ 10     ┆ 283    ┆ 325     ┆ 0.286  ┆ 20.2          ┆ 23.2           │
│ Tennessee Titans      ┆ 14       ┆ 3    ┆ 11     ┆ 254    ┆ 379     ┆ 0.214  ┆ 18.1          ┆ 27.1           │
│ Carolina Panthers     ┆ 14       ┆ 3    ┆ 11     ┆ 247    ┆ 418     ┆ 0.214  ┆ 17.6          ┆ 29.9           │
│ New England Patriots  ┆ 14       ┆ 3    ┆ 11     ┆ 238    ┆ 337     ┆ 0.214  ┆ 17.0          ┆ 24.1           │
│ Cleveland Browns      ┆ 14       ┆ 3    ┆ 11     ┆ 239    ┆ 356     ┆ 0.214  ┆ 17.1          ┆ 25.4           │
│ Jacksonville Jaguars  ┆ 14       ┆ 3    ┆ 11     ┆ 263    ┆ 377     ┆ 0.214  ┆ 18.8          ┆ 26.9           │
│ Las Vegas Raiders     ┆ 13       ┆ 2    ┆ 11     ┆ 236    ┆ 361     ┆ 0.154  ┆ 18.2          ┆ 27.8           │
│ New York Giants       ┆ 14       ┆ 2    ┆ 12     ┆ 208    ┆ 328     ┆ 0.143  ┆ 14.9          ┆ 23.4           │
└───────────────────────┴──────────┴──────┴────────┴────────┴─────────┴────────┴───────────────┴────────────────┘
```