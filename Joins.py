import pandas as pd
import sqlite3

database = 'database.sqlite'
conn = sqlite3.connect(database)

tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
print(tables)

joined_city = pd.read_sql_query("""
        SELECT c.Country_Id, c.Country_Name, ci.City_Name
        FROM Country c
        INNER JOIN City ci
        ON c.Country_Id = ci.Country_Id
""", conn)

print(joined_city)

joined_left = pd.read_sql("""
        SELECT *
        FROM player
        LEFT JOIN season
        ON player.Player_Id = season.Man_of_the_Series
        """, conn)

print(joined_left)

joined_cross = pd.read_sql("""
        SELECT c.Country_Id, c.Country_Name, ci.City_Name
        FROM Country c
        CROSS JOIN City ci
        """, conn)

print(joined_cross)

union = pd.read_sql("""
        SELECT Player_Name
        FROM player
        UNION
        SELECT Team_Name
        FROM team
        """, conn)

print(union)
