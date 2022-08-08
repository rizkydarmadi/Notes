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

```        
        WITH jen AS (SELECT
            ref.id,
            ref.kode,
            ref.nama
        FROM
            referensi ref
            LEFT JOIN (SELECT id, kode FROM referensi) par ON
            (ref.parent_id=par.id)
        WHERE
            par.kode='jenis-laporan'
        ORDER BY
            ref.id ASC
        ),
        lap AS (SELECT
            DISTINCT(laporan.id),
            laporan.jenis_id,
            laporan.tujuan_id
        FROM
            laporan
            LEFT JOIN laporan_tembusan ltem
                ON (laporan.id = ltem.laporan_id)
            LEFT JOIN (
                SELECT id, name FROM auth_group) tem
                ON (ltem.satuankerja_id=tem.id)
        WHERE
            status=1
            
            AND tanggal_laporan >= date_trunc('year', CURRENT_DATE)
            
                AND (laporan.tujuan_id=ANY(ARRAY[3]) OR tem.id=ANY(ARRAY[3]))
            )
        SELECT
            jen.nama,
            COUNT(lap.id)
        FROM
            jen
            LEFT JOIN lap ON (lap.jenis_id=jen.id)
        GROUP BY
            jen.nama
```

```
SELECT 
CONCAT(neraca_penilaian_kepercayaan.nama,neraca_penilaian_kebenaran.nama) AS neraca_penilaian,COUNT(laporan.id) AS jumlah 
FROM laporan
LEFT JOIN neraca_penilaian_kebenaran ON laporan.neraca_kebenaran_id = neraca_penilaian_kebenaran.id
LEFT JOIN neraca_penilaian_kepercayaan ON laporan.neraca_kepercayaan_id = neraca_penilaian_kepercayaan.id
WHERE laporan.neraca_kebenaran_id IS NOT NULL 
AND laporan.neraca_kepercayaan_id IS NOT NULL
AND laporan.jenis_id = 9
AND laporan.status = 1
GROUP BY neraca_penilaian_kebenaran.nama,neraca_penilaian_kepercayaan.nama
ORDER BY jumlah DESC;
```