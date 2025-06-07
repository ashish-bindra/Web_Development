```py
import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('DA.db')  # or 'sf-film-locations.db'
cursor = conn.cursor()

# Read CSV file into a DataFrame
df = pd.read_csv('FilmLocations.csv')

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS FilmLocations (
    Title TEXT,
    Locations TEXT,
    FunFacts INTEGER,
    ProductionCompany,
    Distributor,
    Director,
    Writer,
    Actor1,
    Actor2,
    Actor3
)
''')

# Insert DataFrame into the SQLite table
df.to_sql('FilmLocations', conn, if_exists='append', index=False)

# Commit changes and close the connection
conn.commit()
conn.close()
```

```py
import pandas as pd
import sqlite3

# Read the CSV file into a DataFrame
df = pd.read_csv('FilmLocations.csv')

# Connect to the SQLite database
conn = sqlite3.connect('DA.db')  # Adjust the database file name as needed

# Insert the DataFrame into the SQLite table
df.to_sql('FilmLocations', conn, if_exists='replace', index=False)  # or 'append' if you want to add to an existing table

# Commit changes and close the connection
conn.commit()
conn.close()
```
%%sql
.mode csv

%%sql
.import FilmLocations.csv FilmLocations

%reload_ext sql
%sql sqlite:///DA.db

%%sql
SELECT name FROM sqlite_master WHERE type='table';

<table>
    <thead>
        <tr>
            <th>name</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Medals</td>
        </tr>
        <tr>
            <td>Awards</td>
        </tr>
        <tr>
            <td>FilmLocations</td>
        </tr>
    </tbody>
</table>