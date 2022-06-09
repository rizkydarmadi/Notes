# SQL: How to make multiple joins to the same column of a table without overriding results?
[stackoverflow](https://stackoverflow.com/questions/12912537/sql-how-to-make-multiple-joins-to-the-same-column-of-a-table-without-overriding)

```
MATCHES:
ID   |   HOME_TEAM_ID  |  AWAY_TEAM_ID | SCORE_HOME | SCORE_AWAY
----------------------------------------------------------------
1    |       20        |       21      |     80     |    110
2    |       12        |       10      |     96     |     90


TEAMS:
ID   |   NAME
-------------------------
20   |   BULLS
21   |   KNICKS

```


```
SELECT
    Matches.ID,
    Matches.Score_Home,
    Matches.Score_Away,
    HomeTeam.Name Home_Team_Name,
    AwayTeam.Name Away_Team_Name
FROM
    Matches
    INNER JOIN Teams HomeTeam ON Matches.Home_Team_ID = HomeTeam.ID
    INNER JOIN Teams AwayTeam ON Matches.Away_Team_ID = AwayTeam.ID

```

# How to start and stop PostgreSQL server?
[reference](https://tableplus.com/blog/2018/10/how-to-start-stop-restart-postgresql-server.html)
## Start the PostgreSQL server
``` sudo service postgresql start ```
## Stop the PostgreSQL server:
``` sudo service postgresql stop ``` 

# sql to json
``` SELECT json_agg(referensi) FROM referensi; ```
