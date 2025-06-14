# 

%load_ext sql
%sql sqlite:///DA.db

%sql SELECT name FROM sqlite_master WHERE type='table';

```sql
%%sql
CREATE TABLE Awards (
    Awardee TEXT,
    Country TEXT,
    Award TEXT,
    Year INTEGER
);
```

```sql
%%sql
INSERT INTO Awards (Awardee, Country, Award, Year) VALUES
('John', 'Canada', 'Gold', 2023),
('Sam', 'India', 'Gold', 2023),
('Peter', 'Canada', 'Silver', 2022),
('Aby', 'Australia', 'Gold', 2023),
('Richard', 'Canada', 'Bronze', 2023),
('David', 'Canada', 'Gold', 2023),
('Alice', 'India', 'Gold', 2023),
('Tom', 'Australia', 'Silver', 2022),
('Nancy', 'Canada', 'Gold', 2023),
('Paul', 'India', 'Bronze', 2023),
('Eve', 'Australia', 'Gold', 2022),
('Liam', 'Canada', 'Silver', 2023),
('Sophia', 'India', 'Gold', 2022),
('James', 'Australia', 'Bronze', 2023),
('Olivia', 'Canada', 'Gold', 2022),
('Noah', 'India', 'Silver', 2023),
('Emma', 'Australia', 'Gold', 2023),
('Mason', 'Canada', 'Bronze', 2022),
('Ava', 'India', 'Gold', 2022),
('Logan', 'Australia', 'Silver', 2023),
('Isabella', 'Canada', 'Gold', 2023),
('Lucas', 'India', 'Bronze', 2022),
('Mia', 'Australia', 'Gold', 2022),
('Jackson', 'Canada', 'Silver', 2023),
('Amelia', 'India', 'Gold', 2023),
('Ethan', 'Australia', 'Bronze', 2022),
('Harper', 'Canada', 'Gold', 2023),
('Sebastian', 'India', 'Silver', 2023),
('Avery', 'Australia', 'Gold', 2023),
('Matthew', 'Canada', 'Bronze', 2022),
('Ella', 'India', 'Gold', 2023),
('Owen', 'Australia', 'Silver', 2022),
('Zoe', 'Canada', 'Gold', 2023),
('Landon', 'India', 'Bronze', 2023),
('Charlotte', 'Australia', 'Gold', 2022),
('Daniel', 'Canada', 'Silver', 2022),
('Sofia', 'India', 'Gold', 2023),
('Ryan', 'Australia', 'Bronze', 2023),
('Mila', 'Canada', 'Gold', 2023),
('Jameson', 'India', 'Silver', 2022),
('Layla', 'Australia', 'Gold', 2023),
('Gabriel', 'Canada', 'Bronze', 2023),
('Riley', 'India', 'Gold', 2022),
('Hunter', 'Australia', 'Silver', 2023),
('Aiden', 'Canada', 'Gold', 2023);
```

```sql
%%sql
select * from Awards
```
<table>
    <thead>
        <tr>
            <th>Awardee</th>
            <th>Country</th>
            <th>Award</th>
            <th>Year</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>John</td>
            <td>Canada</td>
            <td>Gold</td>
            <td>2023</td>
        </tr>
        <tr>
            <td>Sam</td>
            <td>India</td>
            <td>Gold</td>
            <td>2023</td>
        </tr>
        <tr>
            <td>Peter</td>
            <td>Canada</td>
            <td>Silver</td>
            <td>2022</td>
        </tr>
        <tr>
            <td>Aby</td>
            <td>Australia</td>
            <td>Gold</td>
            <td>2023</td>
        </tr>
        <tr>
            <td>Richard</td>
            <td>Canada</td>
            <td>Bronze</td>
            <td>2023</td>
        </tr>
        <tr>
            <td>David</td>
            <td>Canada</td>
            <td>Gold</td>
            <td>2023</td>
        </tr>
    </tbody>
</table>

```sql
%%sql
ALTER TABLE Awards RENAME TO Medals;

```

## Count

1. Count

- Built-in database fucnction
- retrives the number of rows
- `select COUNT(*) from tablename`

```sql
%%sql
select COUNT(COUNTRY) from MEDALS
```
<table>
    <thead>
        <tr>
            <th>COUNT(COUNTRY)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>6</td>
        </tr>
    </tbody>
</table>

## Distinct
2. Distinct
Removes duplicate values from a resultset.
- Retrieves unique values in a column:
- `select DISTINCT columnname from table`

```sql
%%sql
select DISTINCT COUNTRY from MEDALS where Award= "Gold"
```

<table>
    <thead>
        <tr>
            <th>Country</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Canada</td>
        </tr>
        <tr>
            <td>India</td>
        </tr>
        <tr>
            <td>Australia</td>
        </tr>
    </tbody>
</table>

## Limit

Retrieve just the first 10 rows in a table:
- `select * from tablename LIMIT 10`

```sql
%%sql
select * from medals where year = 2023 LIMIT 3
```

<table>
    <thead>
        <tr>
            <th>Awardee</th>
            <th>Country</th>
            <th>Award</th>
            <th>Year</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>John</td>
            <td>Canada</td>
            <td>Gold</td>
            <td>2023</td>
        </tr>
        <tr>
            <td>Sam</td>
            <td>India</td>
            <td>Gold</td>
            <td>2023</td>
        </tr>
        <tr>
            <td>Aby</td>
            <td>Australia</td>
            <td>Gold</td>
            <td>2023</td>
        </tr>
    </tbody>
</table>

```sql
%%sql
CREATE TABLE IF NOT EXISTS Awards (
    Awardee TEXT,
    Country TEXT,
    Award TEXT,
    Year INTEGER
);

```

%reload_ext sql
%sql sqlite:///sf-film-locations.db

<table>
    <thead>
        <tr>
            <th>name</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Title</td>
        </tr>
        <tr>
            <td>Director</td>
        </tr>
        <tr>
            <td>Writer</td>
        </tr>
        <tr>
            <td>Release Year</td>
        </tr>
        <tr>
            <td>Actors</td>
        </tr>
        <tr>
            <td>Production Company</td>
        </tr>
        <tr>
            <td>Distributor</td>
        </tr>
        <tr>
            <td>Film_Locations_in_San_Francisco</td>
        </tr>
        <tr>
            <td>Film_Locations_in_San_Francisco_fts</td>
        </tr>
        <tr>
            <td>Film_Locations_in_San_Francisco_fts_segments</td>
        </tr>
        <tr>
            <td>Film_Locations_in_San_Francisco_fts_segdir</td>
        </tr>
        <tr>
            <td>Film_Locations_in_San_Francisco_fts_docsize</td>
        </tr>
        <tr>
            <td>Film_Locations_in_San_Francisco_fts_stat</td>
        </tr>
    </tbody>
</table>

%%sql
select * from Film_Locations_in_San_Francisco

<table>
    <thead>
        <tr>
            <th>Title</th>
            <th>Release Year</th>
            <th>Locations</th>
            <th>Fun Facts</th>
            <th>Production Company</th>
            <th>Distributor</th>
            <th>Director</th>
            <th>Writer</th>
            <th>Actor 1</th>
            <th>Actor 2</th>
            <th>Actor 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>1</td>
            <td>Epic Roasthouse (399 Embarcadero)</td>
            <td>None</td>
            <td>1</td>
            <td>None</td>
            <td>1</td>
            <td>1</td>
            <td>237</td>
            <td>1</td>
            <td>439</td>
        </tr>
        <tr>
            <td>1</td>
            <td>1</td>
            <td>Mason &amp; California Streets (Nob Hill)</td>
            <td>None</td>
            <td>1</td>
            <td>None</td>
            <td>1</td>
            <td>1</td>
            <td>237</td>
            <td>1</td>
            <td>439</td>
        </tr>
        <tr>
            <td>1</td>
            <td>1</td>
            <td>Justin Herman Plaza</td>
            <td>None</td>
            <td>1</td>
            <td>None</td>
            <td>1</td>
            <td>1</td>
            <td>237</td>
            <td>1</td>
            <td>439</td>
        </tr>
        <tr>
            <td>1</td>
            <td>1</td>
            <td>200 block Market Street</td>
            <td>None</td>
            <td>1</td>
            <td>None</td>
            <td>1</td>
            <td>1</td>
            <td>237</td>
            <td>1</td>
            <td>439</td>
        </tr>
        <tr>
            <td>1</td>
            <td>1</td>
            <td>City Hall</td>
            <td>None</td>
            <td>1</td>
            <td>None</td>
            <td>1</td>
            <td>1</td>
            <td>237</td>
            <td>1</td>
            <td>439</td>
        </tr>
        <tr>
            <td>1</td>
            <td>1</td>
            <td>Polk &amp; Larkin Streets</td>
            <td>None</td>
            <td>1</td>
            <td>None</td>
            <td>1</td>
            <td>1</td>
            <td>237</td>
            <td>1</td>
            <td>439</td>
        </tr>
        <tr>
            <td>1</td>
            <td>1</td>
            <td>Randall Museum</td>
            <td>None</td>
            <td>1</td>
            <td>None</td>
            <td>1</td>
            <td>1</td>
            <td>237</td>
            <td>1</td>
            <td>439</td>
        </tr>
        <tr>
            <td>1</td>
            <td>1</td>
            <td>555 Market St.</td>
            <td>None</td>
            <td>1</td>
            <td>None</td>
            <td>1</td>
            <td>1</td>
            <td>237</td>
            <td>1</td>
            <td>439</td>
        </tr>
        <tr>
            <td>2</td>
            <td>2</td>
            <td>None</td>
            <td>None</td>
            <td>2</td>
            <td>1</td>
            <td>2</td>
            <td>None</td>
            <td>238</td>
            <td>None</td>
            <td>None</td>
        </tr>
        <tr>
            <td>3</td>
            <td>3</td>
            <td>The Walden House, Buena Vista Park</td>
            <td>Established in 1867, Buena Vista Park is the oldest official park in San Francisco.</td>
            <td>3</td>
            <td>2</td>
            <td>3</td>
            <td>2</td>
            <td>239</td>
            <td>2</td>
            <td>None</td>
        </tr>
        <tr>
            <td>3</td>
            <td>3</td>
            <td>Café Trieste (609 Vallejo)</td>
            <td>Francis Ford Coppola allegedly wrote large portions of &quot;The Godfather&quot; trilogy in Café Trieste.</td>
            <td>3</td>
            <td>2</td>
            <td>3</td>
            <td>2</td>
            <td>239</td>
            <td>2</td>
            <td>None</td>
        </tr>
        <tr>
            <td>4</td>
            <td>4</td>
            <td>None</td>
            <td>None</td>
            <td>4</td>
            <td>3</td>
            <td>4</td>
            <td>3</td>
            <td>19</td>
            <td>3</td>
            <td>440</td>
        </tr>
        <tr>
            <td>5</td>
            <td>5</td>
            <td>Rainforest Café (145 Jefferson Street)</td>
            <td>None</td>
            <td>5</td>
            <td>4</td>
            <td>5</td>
            <td>4</td>
            <td>240</td>
            <td>4</td>
            <td>None</td>
        </tr>
        <tr>
            <td>6</td>
            <td>6</td>
            <td>20th and Folsom Streets</td>
            <td>None</td>
            <td>6</td>
            <td>5</td>
            <td>6</td>
            <td>5</td>
            <td>241</td>
            <td>5</td>
            <td>None</td>
        </tr>
        <tr>
            <td>6</td>
            <td>6</td>
            <td>Golden Gate Park</td>
            <td>During San Francisco&#x27;s Gold Rush era, the Park was part of an area designated as the &quot;Great Sand Waste&quot;. </td>
            <td>6</td>
            <td>5</td>
            <td>6</td>
            <td>5</td>
            <td>241</td>
            <td>5</td>
            <td>None</td>
        </tr>
        <tr>
            <td>7</td>
            <td>7</td>
            <td>Embarcadero Freeway</td>
            <td>Embarcadero Freeway, which was featured in the film was demolished in 1989 because of structural damage from the 1989 Loma Prieta Earthquake)</td>
            <td>7</td>
            <td>6</td>
            <td>7</td>
            <td>6</td>
            <td>242</td>
            <td>6</td>
            <td>None</td>
        </tr>
        <tr>
            <td>7</td>
            <td>7</td>
            <td>Fairmont Hotel (950 Mason Street, Nob Hill)</td>
            <td>In 1945 the Fairmont hosted the United Nations Conference on International Organization as delegates arrived to draft a charter for the organization. The U.S. Secretary of State, Edward Stettinius drafted the charter in the hotel&#x27;s Garden Room.</td>
            <td>7</td>
            <td>6</td>
            <td>7</td>
            <td>6</td>
            <td>242</td>
            <td>6</td>
            <td>None</td>
        </tr>
        <tr>
            <td>7</td>
            <td>7</td>
            <td>San Francisco Chronicle (901 Mission Street at 15th Street)</td>
            <td>The San Francisco Zodiac Killer of the late 1960s sent his notes and letters to the Chronicle&#x27;s offices.</td>
            <td>7</td>
            <td>6</td>
            <td>7</td>
            <td>6</td>
            <td>242</td>
            <td>6</td>
            <td>None</td>
        </tr>
        <tr>
            <td>7</td>
            <td>7</td>
            <td>Broadway (North Beach)</td>
            <td>None</td>
            <td>7</td>
            <td>6</td>
            <td>7</td>
            <td>6</td>
            <td>242</td>
            <td>6</td>
            <td>None</td>
        </tr>
        <tr>
            <td>8</td>
            <td>8</td>
            <td>75 California Street</td>
            <td>None</td>
            <td>4</td>
            <td>3</td>
            <td>8</td>
            <td>7</td>
            <td>243</td>
            <td>7</td>
            <td>None</td>
        </tr>
        <tr>
            <td>9</td>
            <td>8</td>
            <td>Grace Cathedral Episcopal Church (1100 California Street)</td>
            <td>Grace Cathedral Episcopal Church is the West Coast&#x27;s largest Episcopalian cathedral.</td>
            <td>4</td>
            <td>3</td>
            <td>8</td>
            <td>7</td>
            <td>243</td>
            <td>7</td>
            <td>None</td>
        </tr>
        <tr>
            <td>9</td>
            <td>8</td>
            <td>Hills Brothers Plaza (Embarcadero at Harrison Street)</td>
            <td>None</td>
            <td>4</td>
            <td>3</td>
            <td>8</td>
            <td>7</td>
            <td>243</td>
            <td>7</td>
            <td>None</td>
        </tr>
        <tr>
            <td>9</td>
            <td>8</td>
            <td>San Francisco International Airport</td>
            <td>SFO has a museum dedicated to aviation history. </td>
            <td>4</td>
            <td>3</td>
            <td>8</td>
            <td>7</td>
            <td>243</td>
            <td>7</td>
            <td>None</td>
        </tr>
        <tr>
            <td>10</td>
            <td>9</td>
            <td>City Hall</td>
            <td>The dome of SF&#x27;s City Hall is almost a foot taller than that of the US Capitol Building. In 1954, Joe DiMaggio and Marilyn Monroe married at the Beaux Arts-style building.</td>
            <td>8</td>
            <td>7</td>
            <td>9</td>
            <td>8</td>
            <td>244</td>
            <td>8</td>
            <td>441</td>
        </tr>
        <tr>
            <td>10</td>
            <td>9</td>
            <td>Port of San Francisco </td>
            <td>None</td>
            <td>8</td>
            <td>7</td>
            <td>9</td>
            <td>8</td>
            <td>244</td>
            <td>8</td>
            <td>441</td>
        </tr>
        <tr>
            <td>11</td>
            <td>10</td>
            <td>420 Jones St. at Ellis St.</td>
            <td>None</td>
            <td>9</td>
            <td>8</td>
            <td>10</td>
            <td>9</td>
            <td>245</td>
            <td>9</td>
            <td>None</td>
        </tr>
        <tr>
            <td>10</td>
            <td>9</td>
            <td>Lefty O&#x27; Doul Drawbridge/ 3rd Street Bridge (3rd Street, China Basin)</td>
            <td>This is SF&#x27;s only drawbridge, and was named after Francis Joseph &quot;Lefty&quot; O&#x27;Doul, a local baseball hero.</td>
            <td>8</td>
            <td>7</td>
            <td>9</td>
            <td>8</td>
            <td>244</td>
            <td>8</td>
            <td>441</td>
        </tr>
        <tr>
            <td>10</td>
            <td>9</td>
            <td>Golden Gate Bridge</td>
            <td>With 23 miles of ladders and 300,000 rivets in each tower, the Golden Gate Bridge was the world&#x27;s longest span when it opened in 1937.</td>
            <td>8</td>
            <td>7</td>
            <td>9</td>
            <td>8</td>
            <td>244</td>
            <td>8</td>
            <td>441</td>
        </tr>
        <tr>
            <td>10</td>
            <td>9</td>
            <td>Embarcadero Freeway</td>
            <td>Embarcadero Freeway, which was featured in the film, was demolished in 1989 because of structural damage from the 1989 Loma Prieta Earthquake)</td>
            <td>8</td>
            <td>7</td>
            <td>9</td>
            <td>8</td>
            <td>244</td>
            <td>8</td>
            <td>441</td>
        </tr>
        <tr>
            <td>10</td>
            <td>9</td>
            <td>Potrero Hill</td>
            <td>The most crooked street in San Francisco is actually Potrero Hill&#x27;s Vermont Street between 20th St &amp; 22nd St.</td>
            <td>8</td>
            <td>7</td>
            <td>9</td>
            <td>8</td>
            <td>244</td>
            <td>8</td>
            <td>441</td>
        </tr>
        <tr>
            <td>10</td>
            <td>9</td>
            <td>City Hall</td>
            <td>The dome of SF&#x27;s City Hall is almost a foot taller than that of the US Capitol Building. In 1954, Joe DiMaggio and Marilyn Monroe married at the Beaux Arts-style building.</td>
            <td>8</td>
            <td>7</td>
            <td>9</td>
            <td>8</td>
            <td>244</td>
            <td>8</td>
            <td>441</td>
        </tr>
        <tr>
            <td>10</td>
            <td>9</td>
            <td>Chinatown</td>
            <td>First established in the mid-19th Century, SF&#x27;s Chinatown is the oldest and largest Chinatown in the US.</td>
            <td>8</td>
            <td>7</td>
            <td>9</td>
            <td>8</td>
            <td>244</td>
            <td>8</td>
            <td>441</td>
        </tr>
        <tr>
            <td>10</td>
            <td>9</td>
            <td>Burger Island (901 3rd Street, China Basin)</td>
            <td>None</td>
            <td>8</td>
            <td>7</td>
            <td>9</td>
            <td>8</td>
            <td>244</td>
            <td>8</td>
            <td>441</td>
        </tr>
        <tr>
            <td>10</td>
            <td>9</td>
            <td>Van Ness Avenue</td>
            <td>None</td>
            <td>8</td>
            <td>7</td>
            <td>9</td>
            <td>8</td>
            <td>244</td>
            <td>8</td>
            <td>441</td>
        </tr>
        <tr>
            <td>10</td>
            <td>9</td>
            <td>Taylor and Jefferson Streets (Fisherman&#x27;s Wharf)</td>
            <td>None</td>
            <td>8</td>
            <td>7</td>
            <td>9</td>
            <td>8</td>
            <td>244</td>
            <td>8</td>
            <td>441</td>
        </tr>
        <tr>
            <td>12</td>
            <td>11</td>
            <td>Broderick from Fulton to McAlister</td>
            <td>None</td>
            <td>10</td>
            <td>9</td>
            <td>11</td>
            <td>10</td>
            <td>246</td>
            <td>10</td>
            <td>None</td>
        </tr>
        <tr>
            <td>12</td>
            <td>11</td>
            <td>Crissy Field</td>
            <td>None</td>
            <td>10</td>
            <td>9</td>
            <td>11</td>
            <td>10</td>
            <td>246</td>
            <td>10</td>
            <td>None</td>
        </tr>
        <tr>
            <td>12</td>
            <td>11</td>
            <td>Powell from Bush and Sutter</td>
            <td>None</td>
            <td>10</td>
            <td>9</td>
            <td>11</td>
            <td>10</td>
            <td>246</td>
            <td>10</td>
            <td>None</td>
        </tr>
        <tr>
            <td>13</td>
            <td>12</td>
            <td>Coit Tower</td>
            <td>The Tower was funded by a gift bequeathed by Lillie Hitchcock Coit, a socialite who reportedly liked to chase fires. Though the tower resembles a firehose nozzle, it was not designed this way.</td>
            <td>8</td>
            <td>10</td>
            <td>12</td>
            <td>11</td>
            <td>247</td>
            <td>11</td>
            <td>432</td>
        </tr>
        <tr>
            <td>14</td>
            <td>10</td>
            <td>Pier 50- end of the pier</td>
            <td>None</td>
            <td>11</td>
            <td>None</td>
            <td>13</td>
            <td>12</td>
            <td>248</td>
            <td>12</td>
            <td>442</td>
        </tr>
        <tr>
            <td>14</td>
            <td>10</td>
            <td>California @ Montgomery</td>
            <td>None</td>
            <td>11</td>
            <td>None</td>
            <td>13</td>
            <td>12</td>
            <td>248</td>
            <td>12</td>
            <td>442</td>
        </tr>
        <tr>
            <td>14</td>
            <td>10</td>
            <td>Montgomery/Green</td>
            <td>None</td>
            <td>11</td>
            <td>None</td>
            <td>13</td>
            <td>12</td>
            <td>248</td>
            <td>12</td>
            <td>442</td>
        </tr>
        <tr>
            <td>14</td>
            <td>10</td>
            <td>Driving various SF Streets</td>
            <td>None</td>
            <td>11</td>
            <td>None</td>
            <td>13</td>
            <td>12</td>
            <td>248</td>
            <td>12</td>
            <td>442</td>
        </tr>
        <tr>
            <td>14</td>
            <td>10</td>
            <td>Plate Shots SF streets various</td>
            <td>None</td>
            <td>11</td>
            <td>None</td>
            <td>13</td>
            <td>12</td>
            <td>248</td>
            <td>12</td>
            <td>442</td>
        </tr>
        <tr>
            <td>15</td>
            <td>13</td>
            <td>Filbert St. from Jones to Mason</td>
            <td>None</td>
            <td>12</td>
            <td>11</td>
            <td>14</td>
            <td>13</td>
            <td>249</td>
            <td>13</td>
            <td>None</td>
        </tr>
        <tr>
            <td>15</td>
            <td>13</td>
            <td>Leavenworth from Filbert &amp; Francisco St</td>
            <td>None</td>
            <td>12</td>
            <td>11</td>
            <td>14</td>
            <td>13</td>
            <td>249</td>
            <td>13</td>
            <td>None</td>
        </tr>
        <tr>
            <td>15</td>
            <td>13</td>
            <td>Chestnut St. from Larkin to Columbus</td>
            <td>None</td>
            <td>12</td>
            <td>11</td>
            <td>14</td>
            <td>13</td>
            <td>249</td>
            <td>13</td>
            <td>None</td>
        </tr>
        <tr>
            <td>15</td>
            <td>13</td>
            <td>Francisco St from Larkin to Polk</td>
            <td>None</td>
            <td>12</td>
            <td>11</td>
            <td>14</td>
            <td>13</td>
            <td>249</td>
            <td>13</td>
            <td>None</td>
        </tr>
        <tr>
            <td>15</td>
            <td>13</td>
            <td>Broadway from Mason to Taylor</td>
            <td>None</td>
            <td>12</td>
            <td>11</td>
            <td>14</td>
            <td>13</td>
            <td>249</td>
            <td>13</td>
            <td>None</td>
        </tr>
        <tr>
            <td>15</td>
            <td>13</td>
            <td>Taylor St. from Broadway to Filbert</td>
            <td>None</td>
            <td>12</td>
            <td>11</td>
            <td>14</td>
            <td>13</td>
            <td>249</td>
            <td>13</td>
            <td>None</td>
        </tr>
        <tr>
            <td>11</td>
            <td>10</td>
            <td>Broadway between Powell and Davis</td>
            <td>Driving shots</td>
            <td>9</td>
            <td>8</td>
            <td>10</td>
            <td>9</td>
            <td>245</td>
            <td>9</td>
            <td>None</td>
        </tr>
        <tr>
            <td>16</td>
            <td>14</td>
            <td>Cliff House (1090 Point Lobos Avenue)</td>
            <td>In 1887, the Cliff House was severely damaged when the schooner Parallel, abandoned and loaded with dynamite, ran aground on the rocks below.</td>
            <td>13</td>
            <td>12</td>
            <td>15</td>
            <td>14</td>
            <td>250</td>
            <td>14</td>
            <td>443</td>
        </tr>
        <tr>
            <td>16</td>
            <td>14</td>
            <td>San Francisco Bay</td>
            <td>None</td>
            <td>13</td>
            <td>12</td>
            <td>15</td>
            <td>14</td>
            <td>250</td>
            <td>14</td>
            <td>443</td>
        </tr>
        <tr>
            <td>16</td>
            <td>14</td>
            <td>Fairmont Hotel (950 Mason Street, Nob Hill)</td>
            <td>In 1945 the Fairmont hosted the United Nations Conference on International Organization as delegates arrived to draft a charter for the organization. The U.S. Secretary of State, Edward Stettinius drafted the charter in the hotel&#x27;s Garden Room.</td>
            <td>13</td>
            <td>12</td>
            <td>15</td>
            <td>14</td>
            <td>250</td>
            <td>14</td>
            <td>443</td>
        </tr>
        <tr>
            <td>17</td>
            <td>15</td>
            <td>Curran Theater (445 Geary Street)</td>
            <td>Called the Shubert Theatre in the film. </td>
            <td>14</td>
            <td>13</td>
            <td>16</td>
            <td>15</td>
            <td>251</td>
            <td>15</td>
            <td>444</td>
        </tr>
        <tr>
            <td>18</td>
            <td>16</td>
            <td>Mel&#x27;s Drive-In (Corner of Van Ness &amp; Mission Street, Mission District)</td>
            <td>This restaurant location was demolished; however another Mel&#x27;s was reopened in 1986 on 3355 Geary Blvd. </td>
            <td>15</td>
            <td>14</td>
            <td>17</td>
            <td>16</td>
            <td>252</td>
            <td>16</td>
            <td>445</td>
        </tr>
        <tr>
            <td>18</td>
            <td>16</td>
            <td>3355 Geary Blvd.</td>
            <td>None</td>
            <td>15</td>
            <td>14</td>
            <td>17</td>
            <td>16</td>
            <td>252</td>
            <td>16</td>
            <td>445</td>
        </tr>
        <tr>
            <td>19</td>
            <td>5</td>
            <td>None</td>
            <td>None</td>
            <td>16</td>
            <td>None</td>
            <td>18</td>
            <td>17</td>
            <td>253</td>
            <td>17</td>
            <td>None</td>
        </tr>
        <tr>
            <td>20</td>
            <td>10</td>
            <td>St. Francis Episcopal Church (399 San Fernando Way)</td>
            <td>None</td>
            <td>17</td>
            <td>None</td>
            <td>19</td>
            <td>18</td>
            <td>254</td>
            <td>18</td>
            <td>446</td>
        </tr>
        <tr>
            <td>20</td>
            <td>10</td>
            <td>Romolo Place @ Fresno St.</td>
            <td>None</td>
            <td>17</td>
            <td>None</td>
            <td>19</td>
            <td>18</td>
            <td>254</td>
            <td>18</td>
            <td>446</td>
        </tr>
        <tr>
            <td>20</td>
            <td>10</td>
            <td>Palace of Fine Arts</td>
            <td>None</td>
            <td>17</td>
            <td>None</td>
            <td>19</td>
            <td>18</td>
            <td>254</td>
            <td>18</td>
            <td>446</td>
        </tr>
        <tr>
            <td>20</td>
            <td>10</td>
            <td>John Shelley Drive John McLaren Park</td>
            <td>None</td>
            <td>17</td>
            <td>None</td>
            <td>19</td>
            <td>18</td>
            <td>254</td>
            <td>18</td>
            <td>446</td>
        </tr>
        <tr>
            <td>20</td>
            <td>10</td>
            <td>Treasure Island</td>
            <td>None</td>
            <td>17</td>
            <td>None</td>
            <td>19</td>
            <td>18</td>
            <td>254</td>
            <td>18</td>
            <td>446</td>
        </tr>
        <tr>
            <td>20</td>
            <td>10</td>
            <td>The San Francisco School (300 Gavin St.)</td>
            <td>None</td>
            <td>17</td>
            <td>None</td>
            <td>19</td>
            <td>18</td>
            <td>254</td>
            <td>18</td>
            <td>446</td>
        </tr>
        <tr>
            <td>20</td>
            <td>10</td>
            <td>33 Spruce St</td>
            <td>None</td>
            <td>17</td>
            <td>None</td>
            <td>19</td>
            <td>18</td>
            <td>254</td>
            <td>18</td>
            <td>446</td>
        </tr>
        <tr>
            <td>20</td>
            <td>10</td>
            <td>Coi Restaurant (373 Broadway)</td>
            <td>None</td>
            <td>17</td>
            <td>None</td>
            <td>19</td>
            <td>18</td>
            <td>254</td>
            <td>18</td>
            <td>446</td>
        </tr>
        <tr>
            <td>20</td>
            <td>10</td>
            <td>Foreign Cinema (2534 Mission)</td>
            <td>None</td>
            <td>17</td>
            <td>None</td>
            <td>19</td>
            <td>18</td>
            <td>254</td>
            <td>18</td>
            <td>446</td>
        </tr>
        <tr>
            <td>20</td>
            <td>10</td>
            <td>Bernal Heights Park</td>
            <td>None</td>
            <td>17</td>
            <td>None</td>
            <td>19</td>
            <td>18</td>
            <td>254</td>
            <td>18</td>
            <td>446</td>
        </tr>
        <tr>
            <td>20</td>
            <td>10</td>
            <td>Jackson St. at Spruce</td>
            <td>None</td>
            <td>17</td>
            <td>None</td>
            <td>19</td>
            <td>18</td>
            <td>254</td>
            <td>18</td>
            <td>446</td>
        </tr>
        <tr>
            <td>20</td>
            <td>10</td>
            <td>679 Madrid St</td>
            <td>None</td>
            <td>17</td>
            <td>None</td>
            <td>19</td>
            <td>18</td>
            <td>254</td>
            <td>18</td>
            <td>446</td>
        </tr>
        <tr>
            <td>20</td>
            <td>10</td>
            <td>Roxie Theater (3117 16th St.)</td>
            <td>None</td>
            <td>17</td>
            <td>None</td>
            <td>19</td>
            <td>18</td>
            <td>254</td>
            <td>18</td>
            <td>446</td>
        </tr>
        <tr>
            <td>20</td>
            <td>10</td>
            <td>Variety Preview Room (582 Market St.)</td>
            <td>None</td>
            <td>17</td>
            <td>None</td>
            <td>19</td>
            <td>18</td>
            <td>254</td>
            <td>18</td>
            <td>446</td>
        </tr>
        <tr>
            <td>20</td>
            <td>10</td>
            <td>Laguna Honda Hospital; 375 Laguna Honda Blvd.</td>
            <td>None</td>
            <td>17</td>
            <td>None</td>
            <td>19</td>
            <td>18</td>
            <td>254</td>
            <td>18</td>
            <td>446</td>
        </tr>
        <tr>
            <td>20</td>
            <td>10</td>
            <td>3232 Jackson Ave.</td>
            <td>None</td>
            <td>17</td>
            <td>None</td>
            <td>19</td>
            <td>18</td>
            <td>254</td>
            <td>18</td>
            <td>446</td>
        </tr>
        <tr>
            <td>20</td>
            <td>10</td>
            <td>20th St and Illinois/Faxon St. and Kenwood/Glenbrook at Mt. Springs</td>
            <td>None</td>
            <td>17</td>
            <td>None</td>
            <td>19</td>
            <td>18</td>
            <td>254</td>
            <td>18</td>
            <td>446</td>
        </tr>
        <tr>
            <td>21</td>
            <td>17</td>
            <td>None</td>
            <td>None</td>
            <td>18</td>
            <td>3</td>
            <td>4</td>
            <td>3</td>
            <td>3</td>
            <td>19</td>
            <td>None</td>
        </tr>
        <tr>
            <td>11</td>
            <td>10</td>
            <td>Conzelman Rd at McCollough Rd and down Conzelman Rd.</td>
            <td>Aerial shots</td>
            <td>9</td>
            <td>8</td>
            <td>10</td>
            <td>9</td>
            <td>245</td>
            <td>9</td>
            <td>None</td>
        </tr>
        <tr>
            <td>11</td>
            <td>10</td>
            <td>Lombard at Hyde</td>
            <td>None</td>
            <td>9</td>
            <td>8</td>
            <td>10</td>
            <td>9</td>
            <td>245</td>
            <td>9</td>
            <td>None</td>
        </tr>
        <tr>
            <td>11</td>
            <td>10</td>
            <td>601 Buena Vista Ave West at Java St.</td>
            <td>None</td>
            <td>9</td>
            <td>8</td>
            <td>10</td>
            <td>9</td>
            <td>245</td>
            <td>9</td>
            <td>None</td>
        </tr>
        <tr>
            <td>11</td>
            <td>10</td>
            <td>Columbus between Bay and Washington</td>
            <td>Driving shots</td>
            <td>9</td>
            <td>8</td>
            <td>10</td>
            <td>9</td>
            <td>245</td>
            <td>9</td>
            <td>None</td>
        </tr>
        <tr>
            <td>11</td>
            <td>10</td>
            <td>California between Kearney and Davis</td>
            <td>Driving shots</td>
            <td>9</td>
            <td>8</td>
            <td>10</td>
            <td>9</td>
            <td>245</td>
            <td>9</td>
            <td>None</td>
        </tr>
        <tr>
            <td>11</td>
            <td>10</td>
            <td>Pine between Kearney and Davis</td>
            <td>Driving shots</td>
            <td>9</td>
            <td>8</td>
            <td>10</td>
            <td>9</td>
            <td>245</td>
            <td>9</td>
            <td>None</td>
        </tr>
        <tr>
            <td>11</td>
            <td>10</td>
            <td>Market between Stuart and Van Ness</td>
            <td>Driving shots</td>
            <td>9</td>
            <td>8</td>
            <td>10</td>
            <td>9</td>
            <td>245</td>
            <td>9</td>
            <td>None</td>
        </tr>
        <tr>
            <td>11</td>
            <td>10</td>
            <td>Grant between Bush and Broadway</td>
            <td>Driving shots</td>
            <td>9</td>
            <td>8</td>
            <td>10</td>
            <td>9</td>
            <td>245</td>
            <td>9</td>
            <td>None</td>
        </tr>
        <tr>
            <td>11</td>
            <td>10</td>
            <td>Intersection of Broadway at Kearney</td>
            <td>Driving shots</td>
            <td>9</td>
            <td>8</td>
            <td>10</td>
            <td>9</td>
            <td>245</td>
            <td>9</td>
            <td>None</td>
        </tr>
        <tr>
            <td>11</td>
            <td>10</td>
            <td>Intersection of California at Polk</td>
            <td>Driving shots</td>
            <td>9</td>
            <td>8</td>
            <td>10</td>
            <td>9</td>
            <td>245</td>
            <td>9</td>
            <td>None</td>
        </tr>
        <tr>
            <td>11</td>
            <td>10</td>
            <td>Treasure Island, Building #1, Ave of the Palms</td>
            <td>Aerial and exterior shots</td>
            <td>9</td>
            <td>8</td>
            <td>10</td>
            <td>9</td>
            <td>245</td>
            <td>9</td>
            <td>None</td>
        </tr>
        <tr>
            <td>22</td>
            <td>18</td>
            <td>Ocean Beach</td>
            <td>On Jan. 25, 1878, the King Philip ship crashed in Ocean Beach. Occasionally, the ship&#x27;s wreckage may be found on the beach-- most recently it was seen in 2007. </td>
            <td>19</td>
            <td>15</td>
            <td>20</td>
            <td>19</td>
            <td>255</td>
            <td>None</td>
            <td>None</td>
        </tr>
        <tr>
            <td>23</td>
            <td>7</td>
            <td>Hyde Street Cable Car</td>
            <td>SF Cable Cars are the only moving National Historical Landmark.</td>
            <td>20</td>
            <td>16</td>
            <td>21</td>
            <td>20</td>
            <td>256</td>
            <td>None</td>
            <td>None</td>
        </tr>
        <tr>
            <td>24</td>
            <td>19</td>
            <td>None</td>
            <td>None</td>
            <td>21</td>
            <td>17</td>
            <td>22</td>
            <td>21</td>
            <td>257</td>
            <td>20</td>
            <td>None</td>
        </tr>
        <tr>
            <td>25</td>
            <td>20</td>
            <td>Fairmont Hotel (950 Mason Street, Nob Hill)</td>
            <td>None</td>
            <td>22</td>
            <td>18</td>
            <td>23</td>
            <td>22</td>
            <td>258</td>
            <td>21</td>
            <td>447</td>
        </tr>
        <tr>
            <td>25</td>
            <td>20</td>
            <td>Embarcadero around Rincon Park</td>
            <td>None</td>
            <td>22</td>
            <td>18</td>
            <td>23</td>
            <td>22</td>
            <td>258</td>
            <td>21</td>
            <td>447</td>
        </tr>
        <tr>
            <td>25</td>
            <td>20</td>
            <td>San Remo Hotel (2237 Mason)</td>
            <td>None</td>
            <td>22</td>
            <td>18</td>
            <td>23</td>
            <td>22</td>
            <td>258</td>
            <td>21</td>
            <td>447</td>
        </tr>
        <tr>
            <td>25</td>
            <td>20</td>
            <td>Huntington Park (California &amp; Taylor Streets, Nob Hill)</td>
            <td>None</td>
            <td>22</td>
            <td>18</td>
            <td>23</td>
            <td>22</td>
            <td>258</td>
            <td>21</td>
            <td>447</td>
        </tr>
        <tr>
            <td>25</td>
            <td>20</td>
            <td>Driving around Taylor/Pacific/Leavenworth</td>
            <td>None</td>
            <td>22</td>
            <td>18</td>
            <td>23</td>
            <td>22</td>
            <td>258</td>
            <td>21</td>
            <td>447</td>
        </tr>
        <tr>
            <td>25</td>
            <td>20</td>
            <td>California and Jones St.</td>
            <td>None</td>
            <td>22</td>
            <td>18</td>
            <td>23</td>
            <td>22</td>
            <td>258</td>
            <td>21</td>
            <td>447</td>
        </tr>
        <tr>
            <td>25</td>
            <td>20</td>
            <td>Another Café, 1191 Pine St at Leavenworth</td>
            <td>None</td>
            <td>22</td>
            <td>18</td>
            <td>23</td>
            <td>22</td>
            <td>258</td>
            <td>21</td>
            <td>447</td>
        </tr>
        <tr>
            <td>26</td>
            <td>21</td>
            <td>None</td>
            <td>None</td>
            <td>23</td>
            <td>19</td>
            <td>24</td>
            <td>23</td>
            <td>259</td>
            <td>22</td>
            <td>448</td>
        </tr>
        <tr>
            <td>27</td>
            <td>22</td>
            <td>Yerba Buena Center for the Arts</td>
            <td>None</td>
            <td>24</td>
            <td>20</td>
            <td>25</td>
            <td>24</td>
            <td>245</td>
            <td>23</td>
            <td>449</td>
        </tr>
        <tr>
            <td>27</td>
            <td>22</td>
            <td>Transbay Terminal (Mission Street at 1st Street)</td>
            <td>Built in 1939, the Terminal linked San Francisco, the East Bay, and Sacramento by rail for the first time.</td>
            <td>24</td>
            <td>20</td>
            <td>25</td>
            <td>24</td>
            <td>245</td>
            <td>23</td>
            <td>449</td>
        </tr>
        <tr>
            <td>27</td>
            <td>22</td>
            <td>Tosca Café (242 Columbus Avenue)</td>
            <td>None</td>
            <td>24</td>
            <td>20</td>
            <td>25</td>
            <td>24</td>
            <td>245</td>
            <td>23</td>
            <td>449</td>
        </tr>
        <tr>
            <td>27</td>
            <td>22</td>
            <td>Steinhart Aquarium (California Academy of Sciences, Golden Gate Park)</td>
            <td>The Steinhart Aquarium is home to over 38,000 animals, which represent more than 900 species. </td>
            <td>24</td>
            <td>20</td>
            <td>25</td>
            <td>24</td>
            <td>245</td>
            <td>23</td>
            <td>449</td>
        </tr>
        <tr>
            <td>27</td>
            <td>22</td>
            <td>Raw Hide II (280 Seventh Street)</td>
            <td>None</td>
            <td>24</td>
            <td>20</td>
            <td>25</td>
            <td>24</td>
            <td>245</td>
            <td>23</td>
            <td>449</td>
        </tr>
        <tr>
            <td>27</td>
            <td>22</td>
            <td>Pier 7 (The Embarcadero)</td>
            <td>None</td>
            <td>24</td>
            <td>20</td>
            <td>25</td>
            <td>24</td>
            <td>245</td>
            <td>23</td>
            <td>449</td>
        </tr>
        <tr>
            <td>27</td>
            <td>22</td>
            <td>Kearney Street (Telegraph Hill)</td>
            <td>None</td>
            <td>24</td>
            <td>20</td>
            <td>25</td>
            <td>24</td>
            <td>245</td>
            <td>23</td>
            <td>449</td>
        </tr>
        <tr>
            <td>28</td>
            <td>11</td>
            <td>Nobles Alley</td>
            <td>None</td>
            <td>25</td>
            <td>21</td>
            <td>26</td>
            <td>25</td>
            <td>260</td>
            <td>24</td>
            <td>450</td>
        </tr>
        <tr>
            <td>27</td>
            <td>22</td>
            <td>Hall of Justice (850 Bryant Street)</td>
            <td>None</td>
            <td>24</td>
            <td>20</td>
            <td>25</td>
            <td>24</td>
            <td>245</td>
            <td>23</td>
            <td>449</td>
        </tr>
        <tr>
            <td>27</td>
            <td>22</td>
            <td>2930 Vallejo Street</td>
            <td>None</td>
            <td>24</td>
            <td>20</td>
            <td>25</td>
            <td>24</td>
            <td>245</td>
            <td>23</td>
            <td>449</td>
        </tr>
        <tr>
            <td>27</td>
            <td>22</td>
            <td>Chinatown</td>
            <td>First established in the mid-19th Century, SF&#x27;s Chinatown is the oldest and largest Chinatown in the US.</td>
            <td>24</td>
            <td>20</td>
            <td>25</td>
            <td>24</td>
            <td>245</td>
            <td>23</td>
            <td>449</td>
        </tr>
        <tr>
            <td>27</td>
            <td>22</td>
            <td>Gibb Street (Chinatown)</td>
            <td>None</td>
            <td>24</td>
            <td>20</td>
            <td>25</td>
            <td>24</td>
            <td>245</td>
            <td>23</td>
            <td>449</td>
        </tr>
        <tr>
            <td>27</td>
            <td>22</td>
            <td>1158-70 Montgomery Street</td>
            <td>None</td>
            <td>24</td>
            <td>20</td>
            <td>25</td>
            <td>24</td>
            <td>245</td>
            <td>23</td>
            <td>449</td>
        </tr>
        <tr>
            <td>27</td>
            <td>22</td>
            <td>2104 Broadway</td>
            <td>None</td>
            <td>24</td>
            <td>20</td>
            <td>25</td>
            <td>24</td>
            <td>245</td>
            <td>23</td>
            <td>449</td>
        </tr>
        <tr>
            <td>29</td>
            <td>23</td>
            <td>None</td>
            <td>None</td>
            <td>26</td>
            <td>22</td>
            <td>27</td>
            <td>26</td>
            <td>261</td>
            <td>25</td>
            <td>451</td>
        </tr>
        <tr>
            <td>30</td>
            <td>24</td>
            <td>Divisadero between Broadway and Greenwich</td>
            <td>None</td>
            <td>27</td>
            <td>23</td>
            <td>28</td>
            <td>27</td>
            <td>262</td>
            <td>26</td>
            <td>452</td>
        </tr>
        <tr>
            <td>30</td>
            <td>24</td>
            <td>Ohloff Recovery Center (601 Steiner St)</td>
            <td>None</td>
            <td>27</td>
            <td>23</td>
            <td>28</td>
            <td>27</td>
            <td>262</td>
            <td>26</td>
            <td>452</td>
        </tr>
        <tr>
            <td>30</td>
            <td>24</td>
            <td>Haight at Masonic</td>
            <td>None</td>
            <td>27</td>
            <td>23</td>
            <td>28</td>
            <td>27</td>
            <td>262</td>
            <td>26</td>
            <td>452</td>
        </tr>
        <tr>
            <td>30</td>
            <td>24</td>
            <td>Tenderloin Neighborhood</td>
            <td>None</td>
            <td>27</td>
            <td>23</td>
            <td>28</td>
            <td>27</td>
            <td>262</td>
            <td>26</td>
            <td>452</td>
        </tr>
        <tr>
            <td>30</td>
            <td>24</td>
            <td>Olympic Flame Café, 555 Geary St</td>
            <td>None</td>
            <td>27</td>
            <td>23</td>
            <td>28</td>
            <td>27</td>
            <td>262</td>
            <td>26</td>
            <td>452</td>
        </tr>
        <tr>
            <td>30</td>
            <td>24</td>
            <td>18th St at San Bruno Ave.</td>
            <td>None</td>
            <td>27</td>
            <td>23</td>
            <td>28</td>
            <td>27</td>
            <td>262</td>
            <td>26</td>
            <td>452</td>
        </tr>
        <tr>
            <td>30</td>
            <td>24</td>
            <td>Wisconsin between 19th and 20th St</td>
            <td>None</td>
            <td>27</td>
            <td>23</td>
            <td>28</td>
            <td>27</td>
            <td>262</td>
            <td>26</td>
            <td>452</td>
        </tr>
        <tr>
            <td>31</td>
            <td>25</td>
            <td>1155 Filbert Street at Hyde</td>
            <td>None</td>
            <td>14</td>
            <td>13</td>
            <td>29</td>
            <td>28</td>
            <td>263</td>
            <td>27</td>
            <td>None</td>
        </tr>
        <tr>
            <td>31</td>
            <td>25</td>
            <td>Washington Square Park (Filbert, between Stockton and Powell)</td>
            <td>None</td>
            <td>14</td>
            <td>13</td>
            <td>29</td>
            <td>28</td>
            <td>263</td>
            <td>27</td>
            <td>None</td>
        </tr>
        <tr>
            <td>31</td>
            <td>25</td>
            <td>Vaillancourt Fountain (Justin Herman Plaza)</td>
            <td>Installed in 1975, the Vaillancourt Fountain is officially titled, &quot;Québec Libre!&quot;. The night before the sculpture&#x27;s inauguration, artist Armand Vaillancourt inscribed &quot;Québec libre!&quot; in red letters on the sculpture. The next day when he noticed that the note had been erased, Vaillancourt jumped on the statue to re-inscribe his message. </td>
            <td>14</td>
            <td>13</td>
            <td>29</td>
            <td>28</td>
            <td>263</td>
            <td>27</td>
            <td>None</td>
        </tr>
        <tr>
            <td>31</td>
            <td>25</td>
            <td>Montgomery &amp; Market Streets</td>
            <td>None</td>
            <td>14</td>
            <td>13</td>
            <td>29</td>
            <td>28</td>
            <td>263</td>
            <td>27</td>
            <td>None</td>
        </tr>
        <tr>
            <td>31</td>
            <td>25</td>
            <td>City Hall</td>
            <td>The dome of SF&#x27;s City Hall is almost a foot taller than that of the US Capitol Building. In 1954, Joe DiMaggio and Marilyn Monroe married at the Beaux Arts-style building.</td>
            <td>14</td>
            <td>13</td>
            <td>29</td>
            <td>28</td>
            <td>263</td>
            <td>27</td>
            <td>None</td>
        </tr>
        <tr>
            <td>32</td>
            <td>2</td>
            <td>None</td>
            <td>None</td>
            <td>28</td>
            <td>24</td>
            <td>30</td>
            <td>29</td>
            <td>264</td>
            <td>28</td>
            <td>None</td>
        </tr>
        <tr>
            <td>33</td>
            <td>26</td>
            <td>City Hall</td>
            <td>The dome of SF&#x27;s City Hall is almost a foot taller than that of the US Capitol Building. In 1954, Joe DiMaggio and Marilyn Monroe married at the Beaux Arts-style building.</td>
            <td>29</td>
            <td>25</td>
            <td>31</td>
            <td>30</td>
            <td>265</td>
            <td>None</td>
            <td>None</td>
        </tr>
        <tr>
            <td>33</td>
            <td>26</td>
            <td>Golden Gate Bridge</td>
            <td>With 23 miles of ladders and 300,000 rivets in each tower, the Golden Gate Bridge was the world&#x27;s longest span when it opened in 1937.</td>
            <td>29</td>
            <td>25</td>
            <td>31</td>
            <td>30</td>
            <td>265</td>
            <td>None</td>
            <td>None</td>
        </tr>
        <tr>
            <td>33</td>
            <td>26</td>
            <td>Treasure Island</td>
            <td>An artificial island, Treasure Island was created for the 1939 Golden Gate International Exposition, and is named after the novel by Robert Louis Stevenson, a one-time San Francisco resident.</td>
            <td>29</td>
            <td>25</td>
            <td>31</td>
            <td>30</td>
            <td>265</td>
            <td>None</td>
            <td>None</td>
        </tr>
        <tr>
            <td>33</td>
            <td>26</td>
            <td>Postcard Row, Alamo Square, Hayes Valley</td>
            <td>The 6 Victorian homes across from Alamo Square Park are among the few Victorians to survive the Great Fire.</td>
            <td>29</td>
            <td>25</td>
            <td>31</td>
            <td>30</td>
            <td>265</td>
            <td>None</td>
            <td>None</td>
        </tr>
        <tr>
            <td>33</td>
            <td>26</td>
            <td>Grace Cathedral Episcopal Church (1100 California Street)</td>
            <td>Grace Cathedral Episcopal Church is the West Coast&#x27;s largest Episcopalian cathedral.</td>
            <td>29</td>
            <td>25</td>
            <td>31</td>
            <td>30</td>
            <td>265</td>
            <td>None</td>
            <td>None</td>
        </tr>
        <tr>
            <td>28</td>
            <td>11</td>
            <td>Caffe Trieste</td>
            <td>None</td>
            <td>25</td>
            <td>21</td>
            <td>26</td>
            <td>25</td>
            <td>260</td>
            <td>24</td>
            <td>450</td>
        </tr>
        <tr>
            <td>28</td>
            <td>11</td>
            <td>Palace of Fine Arts</td>
            <td>None</td>
            <td>25</td>
            <td>21</td>
            <td>26</td>
            <td>25</td>
            <td>260</td>
            <td>24</td>
            <td>450</td>
        </tr>
        <tr>
            <td>28</td>
            <td>11</td>
            <td>1101 Filbert St. </td>
            <td>None</td>
            <td>25</td>
            <td>21</td>
            <td>26</td>
            <td>25</td>
            <td>260</td>
            <td>24</td>
            <td>450</td>
        </tr>
        <tr>
            <td>28</td>
            <td>11</td>
            <td>Saints Peter &amp; Paul Church</td>
            <td>None</td>
            <td>25</td>
            <td>21</td>
            <td>26</td>
            <td>25</td>
            <td>260</td>
            <td>24</td>
            <td>450</td>
        </tr>
        <tr>
            <td>28</td>
            <td>11</td>
            <td>Green St. &amp; Grant Ave.</td>
            <td>None</td>
            <td>25</td>
            <td>21</td>
            <td>26</td>
            <td>25</td>
            <td>260</td>
            <td>24</td>
            <td>450</td>
        </tr>
        <tr>
            <td>28</td>
            <td>11</td>
            <td>Filbert St. &amp; Leavenworth</td>
            <td>None</td>
            <td>25</td>
            <td>21</td>
            <td>26</td>
            <td>25</td>
            <td>260</td>
            <td>24</td>
            <td>450</td>
        </tr>
        <tr>
            <td>28</td>
            <td>11</td>
            <td>Pine St. &amp; Grant</td>
            <td>None</td>
            <td>25</td>
            <td>21</td>
            <td>26</td>
            <td>25</td>
            <td>260</td>
            <td>24</td>
            <td>450</td>
        </tr>
        <tr>
            <td>28</td>
            <td>11</td>
            <td>Way Faire Inn on Leidesdorff</td>
            <td>None</td>
            <td>25</td>
            <td>21</td>
            <td>26</td>
            <td>25</td>
            <td>260</td>
            <td>24</td>
            <td>450</td>
        </tr>
        <tr>
            <td>28</td>
            <td>11</td>
            <td>Harry&#x27;s Bar on Fillmore</td>
            <td>None</td>
            <td>25</td>
            <td>21</td>
            <td>26</td>
            <td>25</td>
            <td>260</td>
            <td>24</td>
            <td>450</td>
        </tr>
        <tr>
            <td>34</td>
            <td>27</td>
            <td>Tosca Café (242 Columbus Avenue, North Beach)</td>
            <td>None</td>
            <td>30</td>
            <td>None</td>
            <td>32</td>
            <td>31</td>
            <td>266</td>
            <td>29</td>
            <td>453</td>
        </tr>
        <tr>
            <td>35</td>
            <td>28</td>
            <td>None</td>
            <td>None</td>
            <td>13</td>
            <td>12</td>
            <td>33</td>
            <td>32</td>
            <td>267</td>
            <td>30</td>
            <td>454</td>
        </tr>
        <tr>
            <td>36</td>
            <td>29</td>
            <td>Alcatraz Island</td>
            <td>Alcatraz Island was a military fort before it became a prison.</td>
            <td>31</td>
            <td>19</td>
            <td>34</td>
            <td>33</td>
            <td>268</td>
            <td>31</td>
            <td>455</td>
        </tr>
        <tr>
            <td>36</td>
            <td>29</td>
            <td>Pier 43 1/2</td>
            <td>None</td>
            <td>31</td>
            <td>19</td>
            <td>34</td>
            <td>33</td>
            <td>268</td>
            <td>31</td>
            <td>455</td>
        </tr>
        <tr>
            <td>37</td>
            <td>30</td>
            <td>Lands End Trail at Eagles Point/ Lincoln Park Golf Course</td>
            <td>The character of Steve McKee was based on actor Steve McQueen who studied with Bruce Lee in the later 60&#x27;s.</td>
            <td>32</td>
            <td>26</td>
            <td>35</td>
            <td>34</td>
            <td>269</td>
            <td>32</td>
            <td>456</td>
        </tr>
        <tr>
            <td>37</td>
            <td>30</td>
            <td>Pier 45 - Jeremiah O&#x27;Brien Liberty Ship</td>
            <td>The SS Jeremiah O&#x27;Brien is a rare survivor of the invasion at Normandy on D-Day in WWII.</td>
            <td>32</td>
            <td>26</td>
            <td>35</td>
            <td>34</td>
            <td>269</td>
            <td>32</td>
            <td>456</td>
        </tr>
        <tr>
            <td>37</td>
            <td>30</td>
            <td>Leavenworth at Green</td>
            <td>None</td>
            <td>32</td>
            <td>26</td>
            <td>35</td>
            <td>34</td>
            <td>269</td>
            <td>32</td>
            <td>456</td>
        </tr>
        <tr>
            <td>37</td>
            <td>30</td>
            <td>Leavenworth at Union</td>
            <td>None</td>
            <td>32</td>
            <td>26</td>
            <td>35</td>
            <td>34</td>
            <td>269</td>
            <td>32</td>
            <td>456</td>
        </tr>
        <tr>
            <td>37</td>
            <td>30</td>
            <td>Hyde at Union</td>
            <td>None</td>
            <td>32</td>
            <td>26</td>
            <td>35</td>
            <td>34</td>
            <td>269</td>
            <td>32</td>
            <td>456</td>
        </tr>
        <tr>
            <td>37</td>
            <td>30</td>
            <td>California at Grant</td>
            <td>None</td>
            <td>32</td>
            <td>26</td>
            <td>35</td>
            <td>34</td>
            <td>269</td>
            <td>32</td>
            <td>456</td>
        </tr>
        <tr>
            <td>37</td>
            <td>30</td>
            <td>Grant between Bush and Broadway</td>
            <td>None</td>
            <td>32</td>
            <td>26</td>
            <td>35</td>
            <td>34</td>
            <td>269</td>
            <td>32</td>
            <td>456</td>
        </tr>
        <tr>
            <td>37</td>
            <td>30</td>
            <td>California at Mason</td>
            <td>None</td>
            <td>32</td>
            <td>26</td>
            <td>35</td>
            <td>34</td>
            <td>269</td>
            <td>32</td>
            <td>456</td>
        </tr>
        <tr>
            <td>37</td>
            <td>30</td>
            <td>Spofford between Clay and Washington</td>
            <td>None</td>
            <td>32</td>
            <td>26</td>
            <td>35</td>
            <td>34</td>
            <td>269</td>
            <td>32</td>
            <td>456</td>
        </tr>
        <tr>
            <td>37</td>
            <td>30</td>
            <td>Twin Peaks Blvd.</td>
            <td>None</td>
            <td>32</td>
            <td>26</td>
            <td>35</td>
            <td>34</td>
            <td>269</td>
            <td>32</td>
            <td>456</td>
        </tr>
        <tr>
            <td>37</td>
            <td>30</td>
            <td>Waverly Pl between Washington and Sacramento</td>
            <td>None</td>
            <td>32</td>
            <td>26</td>
            <td>35</td>
            <td>34</td>
            <td>269</td>
            <td>32</td>
            <td>456</td>
        </tr>
        <tr>
            <td>38</td>
            <td>27</td>
            <td>Jones &amp; Pacific</td>
            <td>None</td>
            <td>33</td>
            <td>27</td>
            <td>36</td>
            <td>35</td>
            <td>270</td>
            <td>33</td>
            <td>457</td>
        </tr>
        <tr>
            <td>38</td>
            <td>27</td>
            <td>Pacific &amp; Divisadero</td>
            <td>None</td>
            <td>33</td>
            <td>27</td>
            <td>36</td>
            <td>35</td>
            <td>270</td>
            <td>33</td>
            <td>457</td>
        </tr>
        <tr>
            <td>38</td>
            <td>27</td>
            <td>Lombard &amp; Hyde</td>
            <td>None</td>
            <td>33</td>
            <td>27</td>
            <td>36</td>
            <td>35</td>
            <td>270</td>
            <td>33</td>
            <td>457</td>
        </tr>
        <tr>
            <td>38</td>
            <td>27</td>
            <td>5546 Geary Ave</td>
            <td>None</td>
            <td>33</td>
            <td>27</td>
            <td>36</td>
            <td>35</td>
            <td>270</td>
            <td>33</td>
            <td>457</td>
        </tr>
        <tr>
            <td>38</td>
            <td>27</td>
            <td>2898 Broadway</td>
            <td>None</td>
            <td>33</td>
            <td>27</td>
            <td>36</td>
            <td>35</td>
            <td>270</td>
            <td>33</td>
            <td>457</td>
        </tr>
        <tr>
            <td>38</td>
            <td>27</td>
            <td>Motel Capri</td>
            <td>None</td>
            <td>33</td>
            <td>27</td>
            <td>36</td>
            <td>35</td>
            <td>270</td>
            <td>33</td>
            <td>457</td>
        </tr>
        <tr>
            <td>38</td>
            <td>27</td>
            <td>Marina Green</td>
            <td>None</td>
            <td>33</td>
            <td>27</td>
            <td>36</td>
            <td>35</td>
            <td>270</td>
            <td>33</td>
            <td>457</td>
        </tr>
        <tr>
            <td>38</td>
            <td>27</td>
            <td>Ocean Beach at Lincoln</td>
            <td>None</td>
            <td>33</td>
            <td>27</td>
            <td>36</td>
            <td>35</td>
            <td>270</td>
            <td>33</td>
            <td>457</td>
        </tr>
        <tr>
            <td>38</td>
            <td>27</td>
            <td>Heald College</td>
            <td>None</td>
            <td>33</td>
            <td>27</td>
            <td>36</td>
            <td>35</td>
            <td>270</td>
            <td>33</td>
            <td>457</td>
        </tr>
        <tr>
            <td>38</td>
            <td>27</td>
            <td>Marina Blvd from Laguna to Baker</td>
            <td>None</td>
            <td>33</td>
            <td>27</td>
            <td>36</td>
            <td>35</td>
            <td>270</td>
            <td>33</td>
            <td>457</td>
        </tr>
        <tr>
            <td>38</td>
            <td>27</td>
            <td>330 Santa Clara Ave.</td>
            <td>None</td>
            <td>33</td>
            <td>27</td>
            <td>36</td>
            <td>35</td>
            <td>270</td>
            <td>33</td>
            <td>457</td>
        </tr>
        <tr>
            <td>38</td>
            <td>27</td>
            <td>200 Post St. </td>
            <td>None</td>
            <td>33</td>
            <td>27</td>
            <td>36</td>
            <td>35</td>
            <td>270</td>
            <td>33</td>
            <td>457</td>
        </tr>
        <tr>
            <td>38</td>
            <td>27</td>
            <td>2179 48th Ave</td>
            <td>None</td>
            <td>33</td>
            <td>27</td>
            <td>36</td>
            <td>35</td>
            <td>270</td>
            <td>33</td>
            <td>457</td>
        </tr>
        <tr>
            <td>38</td>
            <td>27</td>
            <td>The Ramp Restaurant</td>
            <td>None</td>
            <td>33</td>
            <td>27</td>
            <td>36</td>
            <td>35</td>
            <td>270</td>
            <td>33</td>
            <td>457</td>
        </tr>
        <tr>
            <td>38</td>
            <td>27</td>
            <td>303-305 S. Van Ness</td>
            <td>None</td>
            <td>33</td>
            <td>27</td>
            <td>36</td>
            <td>35</td>
            <td>270</td>
            <td>33</td>
            <td>457</td>
        </tr>
        <tr>
            <td>38</td>
            <td>27</td>
            <td>3563 20th St.</td>
            <td>None</td>
            <td>33</td>
            <td>27</td>
            <td>36</td>
            <td>35</td>
            <td>270</td>
            <td>33</td>
            <td>457</td>
        </tr>
        <tr>
            <td>38</td>
            <td>27</td>
            <td>Taylor &amp; Green St.</td>
            <td>None</td>
            <td>33</td>
            <td>27</td>
            <td>36</td>
            <td>35</td>
            <td>270</td>
            <td>33</td>
            <td>457</td>
        </tr>
        <tr>
            <td>38</td>
            <td>27</td>
            <td>Grant &amp; Washington St.</td>
            <td>None</td>
            <td>33</td>
            <td>27</td>
            <td>36</td>
            <td>35</td>
            <td>270</td>
            <td>33</td>
            <td>457</td>
        </tr>
        <tr>
            <td>38</td>
            <td>27</td>
            <td>2934 24th St.</td>
            <td>None</td>
            <td>33</td>
            <td>27</td>
            <td>36</td>
            <td>35</td>
            <td>270</td>
            <td>33</td>
            <td>457</td>
        </tr>
        <tr>
            <td>38</td>
            <td>27</td>
            <td>1138 Alabama St</td>
            <td>None</td>
            <td>33</td>
            <td>27</td>
            <td>36</td>
            <td>35</td>
            <td>270</td>
            <td>33</td>
            <td>457</td>
        </tr>
        <tr>
            <td>38</td>
            <td>27</td>
            <td>South Park</td>
            <td>None</td>
            <td>33</td>
            <td>27</td>
            <td>36</td>
            <td>35</td>
            <td>270</td>
            <td>33</td>
            <td>457</td>
        </tr>
        <tr>
            <td>38</td>
            <td>27</td>
            <td>2915 16th St.</td>
            <td>None</td>
            <td>33</td>
            <td>27</td>
            <td>36</td>
            <td>35</td>
            <td>270</td>
            <td>33</td>
            <td>457</td>
        </tr>
        <tr>
            <td>38</td>
            <td>27</td>
            <td>Trolley Car from Market and 11th</td>
            <td>None</td>
            <td>33</td>
            <td>27</td>
            <td>36</td>
            <td>35</td>
            <td>270</td>
            <td>33</td>
            <td>457</td>
        </tr>
        <tr>
            <td>38</td>
            <td>27</td>
            <td>Real Guitars</td>
            <td>None</td>
            <td>33</td>
            <td>27</td>
            <td>36</td>
            <td>35</td>
            <td>270</td>
            <td>33</td>
            <td>457</td>
        </tr>
        <tr>
            <td>38</td>
            <td>27</td>
            <td>Aub Zam Zam Bar</td>
            <td>None</td>
            <td>33</td>
            <td>27</td>
            <td>36</td>
            <td>35</td>
            <td>270</td>
            <td>33</td>
            <td>457</td>
        </tr>
        <tr>
            <td>38</td>
            <td>27</td>
            <td>790 Ulloa </td>
            <td>None</td>
            <td>33</td>
            <td>27</td>
            <td>36</td>
            <td>35</td>
            <td>270</td>
            <td>33</td>
            <td>457</td>
        </tr>
        <tr>
            <td>38</td>
            <td>27</td>
            <td>SFO International Airport Terminal 3</td>
            <td>None</td>
            <td>33</td>
            <td>27</td>
            <td>36</td>
            <td>35</td>
            <td>270</td>
            <td>33</td>
            <td>457</td>
        </tr>
        <tr>
            <td>38</td>
            <td>27</td>
            <td>2178 Palou Ave.</td>
            <td>None</td>
            <td>33</td>
            <td>27</td>
            <td>36</td>
            <td>35</td>
            <td>270</td>
            <td>33</td>
            <td>457</td>
        </tr>
        <tr>
            <td>39</td>
            <td>25</td>
            <td>1122 Folsom Street</td>
            <td>None</td>
            <td>34</td>
            <td>28</td>
            <td>37</td>
            <td>36</td>
            <td>271</td>
            <td>34</td>
            <td>None</td>
        </tr>
        <tr>
            <td>39</td>
            <td>25</td>
            <td>St. Peter &amp; Paul&#x27;s Church (666 Filbert Street, Washington Square)</td>
            <td>Though Marilyn Monroe and Joe DiMaggio were not allowed to be married at the Church (DiMaggio had married his first wife at the Church but was divorced), the couple returned to the steps of the Church for photos, following their City Hall nuptials.</td>
            <td>34</td>
            <td>28</td>
            <td>37</td>
            <td>36</td>
            <td>271</td>
            <td>34</td>
            <td>None</td>
        </tr>
        <tr>
            <td>39</td>
            <td>25</td>
            <td>Golden Gate Bridge</td>
            <td>With 23 miles of ladders and 300,000 rivets in each tower, the Golden Gate Bridge was the world&#x27;s longest span when it opened in 1937.</td>
            <td>34</td>
            <td>28</td>
            <td>37</td>
            <td>36</td>
            <td>271</td>
            <td>34</td>
            <td>None</td>
        </tr>
        <tr>
            <td>39</td>
            <td>25</td>
            <td>Fisherman&#x27;s Wharf</td>
            <td>Supposedly, Mikhail S. Gorbachev has said that his favorite part of visiting America was touring Fisherman&#x27;s Wharf.</td>
            <td>34</td>
            <td>28</td>
            <td>37</td>
            <td>36</td>
            <td>271</td>
            <td>34</td>
            <td>None</td>
        </tr>
        <tr>
            <td>39</td>
            <td>25</td>
            <td>Ferry Building</td>
            <td>Every hour and half-hour, the clock bell atop the Ferry Building chimes portions of the Westminster Quarters.</td>
            <td>34</td>
            <td>28</td>
            <td>37</td>
            <td>36</td>
            <td>271</td>
            <td>34</td>
            <td>None</td>
        </tr>
        <tr>
            <td>39</td>
            <td>25</td>
            <td>Coit Tower</td>
            <td>The Tower was funded by a gift bequeathed by Lillie Hitchcock Coit, a socialite who reportedly liked to chase fires. Though the tower resembles a firehose nozzle, it was not designed this way.</td>
            <td>34</td>
            <td>28</td>
            <td>37</td>
            <td>36</td>
            <td>271</td>
            <td>34</td>
            <td>None</td>
        </tr>
        <tr>
            <td>39</td>
            <td>25</td>
            <td>City Hall</td>
            <td>The dome of SF&#x27;s City Hall is almost a foot taller than that of the US Capitol Building. In 1954, Joe DiMaggio and Marilyn Monroe married at the Beaux Arts-style building.</td>
            <td>34</td>
            <td>28</td>
            <td>37</td>
            <td>36</td>
            <td>271</td>
            <td>34</td>
            <td>None</td>
        </tr>
        <tr>
            <td>39</td>
            <td>25</td>
            <td>Lombard Street</td>
            <td>Lombard Street is not actually the most crooked in SF. That honor goes to Potrero Hill&#x27;s Vermont Street between 22nd and 23rd.</td>
            <td>34</td>
            <td>28</td>
            <td>37</td>
            <td>36</td>
            <td>271</td>
            <td>34</td>
            <td>None</td>
        </tr>
        <tr>
            <td>39</td>
            <td>25</td>
            <td>Chinatown</td>
            <td>First established in the mid-19th Century, SF&#x27;s Chinatown is the oldest and largest Chinatown in the US.</td>
            <td>34</td>
            <td>28</td>
            <td>37</td>
            <td>36</td>
            <td>271</td>
            <td>34</td>
            <td>None</td>
        </tr>
        <tr>
            <td>39</td>
            <td>25</td>
            <td>Aquatic Park (Jefferson Street)</td>
            <td>Located at one end of Fisherman&#x27;s Wharf, Aquatic Park was built as part of FDR&#x27;s Works Progress Administration Project.</td>
            <td>34</td>
            <td>28</td>
            <td>37</td>
            <td>36</td>
            <td>271</td>
            <td>34</td>
            <td>None</td>
        </tr>
        <tr>
            <td>39</td>
            <td>25</td>
            <td>Alcatraz Island</td>
            <td>Alcatraz Island was a military fort before it became a prison.</td>
            <td>34</td>
            <td>28</td>
            <td>37</td>
            <td>36</td>
            <td>271</td>
            <td>34</td>
            <td>None</td>
        </tr>
        <tr>
            <td>39</td>
            <td>25</td>
            <td>628 Cole Street</td>
            <td>None</td>
            <td>34</td>
            <td>28</td>
            <td>37</td>
            <td>36</td>
            <td>271</td>
            <td>34</td>
            <td>None</td>
        </tr>
        <tr>
            <td>40</td>
            <td>19</td>
            <td>Ina Coolbrith Park (1700 Taylor Street)</td>
            <td>None</td>
            <td>35</td>
            <td>None</td>
            <td>38</td>
            <td>37</td>
            <td>None</td>
            <td>None</td>
            <td>None</td>
        </tr>
        <tr>
            <td>40</td>
            <td>19</td>
            <td>0-100 block Halleck Street</td>
            <td>None</td>
            <td>35</td>
            <td>None</td>
            <td>38</td>
            <td>37</td>
            <td>None</td>
            <td>None</td>
            <td>None</td>
        </tr>
        <tr>
            <td>41</td>
            <td>20</td>
            <td>3050 24th Street</td>
            <td>None</td>
            <td>36</td>
            <td>29</td>
            <td>39</td>
            <td>38</td>
            <td>272</td>
            <td>35</td>
            <td>458</td>
        </tr>
        <tr>
            <td>41</td>
            <td>20</td>
            <td>3033 24th Street</td>
            <td>None</td>
            <td>36</td>
            <td>29</td>
            <td>39</td>
            <td>38</td>
            <td>272</td>
            <td>35</td>
            <td>458</td>
        </tr>
        <tr>
            <td>41</td>
            <td>20</td>
            <td>2937 24th Street</td>
            <td>None</td>
            <td>36</td>
            <td>29</td>
            <td>39</td>
            <td>38</td>
            <td>272</td>
            <td>35</td>
            <td>458</td>
        </tr>
        <tr>
            <td>41</td>
            <td>20</td>
            <td>1167 Alabama Street</td>
            <td>None</td>
            <td>36</td>
            <td>29</td>
            <td>39</td>
            <td>38</td>
            <td>272</td>
            <td>35</td>
            <td>458</td>
        </tr>
        <tr>
            <td>41</td>
            <td>20</td>
            <td>1641 York Street</td>
            <td>None</td>
            <td>36</td>
            <td>29</td>
            <td>39</td>
            <td>38</td>
            <td>272</td>
            <td>35</td>
            <td>458</td>
        </tr>
        <tr>
            <td>41</td>
            <td>20</td>
            <td>Bernal Heights Boulevard</td>
            <td>None</td>
            <td>36</td>
            <td>29</td>
            <td>39</td>
            <td>38</td>
            <td>272</td>
            <td>35</td>
            <td>458</td>
        </tr>
        <tr>
            <td>41</td>
            <td>20</td>
            <td>40 Prentiss Street</td>
            <td>None</td>
            <td>36</td>
            <td>29</td>
            <td>39</td>
            <td>38</td>
            <td>272</td>
            <td>35</td>
            <td>458</td>
        </tr>
        <tr>
            <td>41</td>
            <td>20</td>
            <td>500 Cortland Avenue</td>
            <td>None</td>
            <td>36</td>
            <td>29</td>
            <td>39</td>
            <td>38</td>
            <td>272</td>
            <td>35</td>
            <td>458</td>
        </tr>
        <tr>
            <td>41</td>
            <td>20</td>
            <td>Lucky Street</td>
            <td>None</td>
            <td>36</td>
            <td>29</td>
            <td>39</td>
            <td>38</td>
            <td>272</td>
            <td>35</td>
            <td>458</td>
        </tr>
        <tr>
            <td>41</td>
            <td>20</td>
            <td>1125 Guerrero Street</td>
            <td>None</td>
            <td>36</td>
            <td>29</td>
            <td>39</td>
            <td>38</td>
            <td>272</td>
            <td>35</td>
            <td>458</td>
        </tr>
        <tr>
            <td>41</td>
            <td>20</td>
            <td>Gough Street &amp; Clay Street</td>
            <td>None</td>
            <td>36</td>
            <td>29</td>
            <td>39</td>
            <td>38</td>
            <td>272</td>
            <td>35</td>
            <td>458</td>
        </tr>
        <tr>
            <td>41</td>
            <td>20</td>
            <td>2007 Franklin Street</td>
            <td>None</td>
            <td>36</td>
            <td>29</td>
            <td>39</td>
            <td>38</td>
            <td>272</td>
            <td>35</td>
            <td>458</td>
        </tr>
        <tr>
            <td>41</td>
            <td>20</td>
            <td>951 Hudson Avenue</td>
            <td>None</td>
            <td>36</td>
            <td>29</td>
            <td>39</td>
            <td>38</td>
            <td>272</td>
            <td>35</td>
            <td>458</td>
        </tr>
        <tr>
            <td>42</td>
            <td>31</td>
            <td>Bayshore Blvd near Cesar Chavez (Bayview)</td>
            <td>None</td>
            <td>37</td>
            <td>30</td>
            <td>40</td>
            <td>39</td>
            <td>273</td>
            <td>36</td>
            <td>459</td>
        </tr>
        <tr>
            <td>42</td>
            <td>31</td>
            <td>Taylor &amp; Vallejo Streets (Russian Hill)</td>
            <td>None</td>
            <td>37</td>
            <td>30</td>
            <td>40</td>
            <td>39</td>
            <td>273</td>
            <td>36</td>
            <td>459</td>
        </tr>
        <tr>
            <td>43</td>
            <td>32</td>
            <td>1627 Haight Street</td>
            <td>None</td>
            <td>38</td>
            <td>6</td>
            <td>41</td>
            <td>40</td>
            <td>274</td>
            <td>37</td>
            <td>None</td>
        </tr>
        <tr>
            <td>42</td>
            <td>31</td>
            <td>SF General Hospital Center (1001 Potrero Avenue, Potrero Hill)</td>
            <td>SF General Hospital is the only Level I Trauma Center serving San Francisco and northern San Mateo County. </td>
            <td>37</td>
            <td>30</td>
            <td>40</td>
            <td>39</td>
            <td>273</td>
            <td>36</td>
            <td>459</td>
        </tr>
        <tr>
            <td>42</td>
            <td>31</td>
            <td>McLaren Park (Visitacion  Valley)</td>
            <td>McLaren Park is the 2nd largest park in San Francisco, after Golden Gate Park.</td>
            <td>37</td>
            <td>30</td>
            <td>40</td>
            <td>39</td>
            <td>273</td>
            <td>36</td>
            <td>459</td>
        </tr>
        <tr>
            <td>42</td>
            <td>31</td>
            <td>Mark Hopkins Hotel (999 California Street)</td>
            <td>The Top of the Mark lounge and restaurant at the top of the hotel was formerly a penthouse suite.</td>
            <td>37</td>
            <td>30</td>
            <td>40</td>
            <td>39</td>
            <td>273</td>
            <td>36</td>
            <td>459</td>
        </tr>
        <tr>
            <td>42</td>
            <td>31</td>
            <td>Marina Green (Marina District)</td>
            <td>Before the 1906 earthquake, the land on which Marina Green sits was a tidal marsh, and rubble from the earthquake was dumped on the site. However, the site was filled in to provide land for the 1915 Panama-Pacific Exhibition. </td>
            <td>37</td>
            <td>30</td>
            <td>40</td>
            <td>39</td>
            <td>273</td>
            <td>36</td>
            <td>459</td>
        </tr>
        <tr>
            <td>42</td>
            <td>31</td>
            <td>Mansell &amp; University Streets (Visitacion  Valley)</td>
            <td>None</td>
            <td>37</td>
            <td>30</td>
            <td>40</td>
            <td>39</td>
            <td>273</td>
            <td>36</td>
            <td>459</td>
        </tr>
        <tr>
            <td>42</td>
            <td>31</td>
            <td>Larkin &amp; Francisco Streets (Russian Hill)</td>
            <td>None</td>
            <td>37</td>
            <td>30</td>
            <td>40</td>
            <td>39</td>
            <td>273</td>
            <td>36</td>
            <td>459</td>
        </tr>
        <tr>
            <td>42</td>
            <td>31</td>
            <td>Larkin &amp; Chestnut Streets (Russian Hill)</td>
            <td>None</td>
            <td>37</td>
            <td>30</td>
            <td>40</td>
            <td>39</td>
            <td>273</td>
            <td>36</td>
            <td>459</td>
        </tr>
        <tr>
            <td>42</td>
            <td>31</td>
            <td>Kennedy Hotel (226 Embarcadero at Howard Street)</td>
            <td>Hotel was destroyed in the 1989 Loma Prieta earthquake. Corporate headquarters for the Gap reside at the location today.</td>
            <td>37</td>
            <td>30</td>
            <td>40</td>
            <td>39</td>
            <td>273</td>
            <td>36</td>
            <td>459</td>
        </tr>
        <tr>
            <td>42</td>
            <td>31</td>
            <td>John Muir Drive (Lake Merced)</td>
            <td>None</td>
            <td>37</td>
            <td>30</td>
            <td>40</td>
            <td>39</td>
            <td>273</td>
            <td>36</td>
            <td>459</td>
        </tr>
        <tr>
            <td>42</td>
            <td>31</td>
            <td>Intersection of York &amp; Peralta (Bernal Heights)</td>
            <td>None</td>
            <td>37</td>
            <td>30</td>
            <td>40</td>
            <td>39</td>
            <td>273</td>
            <td>36</td>
            <td>459</td>
        </tr>
        <tr>
            <td>42</td>
            <td>31</td>
            <td>Filbert &amp; Taylor Streets (Russian Hill)</td>
            <td>None</td>
            <td>37</td>
            <td>30</td>
            <td>40</td>
            <td>39</td>
            <td>273</td>
            <td>36</td>
            <td>459</td>
        </tr>
        <tr>
            <td>42</td>
            <td>31</td>
            <td>Enrico&#x27;s Café (504 Broadway)</td>
            <td>None</td>
            <td>37</td>
            <td>30</td>
            <td>40</td>
            <td>39</td>
            <td>273</td>
            <td>36</td>
            <td>459</td>
        </tr>
        <tr>
            <td>42</td>
            <td>31</td>
            <td>Columbus &amp; Lombard Streets (North Beach)</td>
            <td>None</td>
            <td>37</td>
            <td>30</td>
            <td>40</td>
            <td>39</td>
            <td>273</td>
            <td>36</td>
            <td>459</td>
        </tr>
        <tr>
            <td>42</td>
            <td>31</td>
            <td>Cesar Chavez &amp; Mission Street (Mission)</td>
            <td>None</td>
            <td>37</td>
            <td>30</td>
            <td>40</td>
            <td>39</td>
            <td>273</td>
            <td>36</td>
            <td>459</td>
        </tr>
        <tr>
            <td>42</td>
            <td>31</td>
            <td>Candlestick Park Exit, Highway 101</td>
            <td>None</td>
            <td>37</td>
            <td>30</td>
            <td>40</td>
            <td>39</td>
            <td>273</td>
            <td>36</td>
            <td>459</td>
        </tr>
        <tr>
            <td>42</td>
            <td>31</td>
            <td>Café Cantata (2040 Union Street)</td>
            <td>None</td>
            <td>37</td>
            <td>30</td>
            <td>40</td>
            <td>39</td>
            <td>273</td>
            <td>36</td>
            <td>459</td>
        </tr>
        <tr>
            <td>42</td>
            <td>31</td>
            <td>Brocklebank Apartments (1000 Mason Street)</td>
            <td>None</td>
            <td>37</td>
            <td>30</td>
            <td>40</td>
            <td>39</td>
            <td>273</td>
            <td>36</td>
            <td>459</td>
        </tr>
        <tr>
            <td>42</td>
            <td>31</td>
            <td>Bay Bridge</td>
            <td>Before opening in 1936, the bridge was blessed by Cardinal Secretary of State Eugenio Pacelli, who later became Pope Pius XII. </td>
            <td>37</td>
            <td>30</td>
            <td>40</td>
            <td>39</td>
            <td>273</td>
            <td>36</td>
            <td>459</td>
        </tr>
        <tr>
            <td>42</td>
            <td>31</td>
            <td>2700 Vallejo Street (Pacific Heights)</td>
            <td>None</td>
            <td>37</td>
            <td>30</td>
            <td>40</td>
            <td>39</td>
            <td>273</td>
            <td>36</td>
            <td>459</td>
        </tr>
        <tr>
            <td>42</td>
            <td>31</td>
            <td>20th &amp; Vermont Streets (Potrero Hill)</td>
            <td>The most crooked street in San Francisco is actually Potrero Hill&#x27;s Vermont Street between 20th St &amp; 22nd St.</td>
            <td>37</td>
            <td>30</td>
            <td>40</td>
            <td>39</td>
            <td>273</td>
            <td>36</td>
            <td>459</td>
        </tr>
        <tr>
            <td>42</td>
            <td>31</td>
            <td>1153-57 Taylor Street</td>
            <td>Embarcadero Freeway, which was featured in the film was demolished in 1989 because of structural damage from the 1989 Loma Prieta Earthquake)</td>
            <td>37</td>
            <td>30</td>
            <td>40</td>
            <td>39</td>
            <td>273</td>
            <td>36</td>
            <td>459</td>
        </tr>
        <tr>
            <td>43</td>
            <td>32</td>
            <td>California Academy of Sciences (Golden Gate Park)</td>
            <td>Founded in 1853, 3 years after California joined the United States, the Academy was originally named the California Academy of Natural Sciences and was the first institution of its kind in the United States.</td>
            <td>38</td>
            <td>6</td>
            <td>41</td>
            <td>40</td>
            <td>274</td>
            <td>37</td>
            <td>None</td>
        </tr>
        <tr>
            <td>43</td>
            <td>32</td>
            <td>Green Valley Restaurant (510 Green Street Near Grant)</td>
            <td>None</td>
            <td>38</td>
            <td>6</td>
            <td>41</td>
            <td>40</td>
            <td>274</td>
            <td>37</td>
            <td>None</td>
        </tr>
        <tr>
            <td>43</td>
            <td>32</td>
            <td>1400 18th Street</td>
            <td>None</td>
            <td>38</td>
            <td>6</td>
            <td>41</td>
            <td>40</td>
            <td>274</td>
            <td>37</td>
            <td>None</td>
        </tr>
        <tr>
            <td>44</td>
            <td>33</td>
            <td>The Lexington Club (3464 19th Street at Lexington)</td>
            <td>None</td>
            <td>39</td>
            <td>31</td>
            <td>42</td>
            <td>41</td>
            <td>275</td>
            <td>None</td>
            <td>None</td>
        </tr>
        <tr>
            <td>44</td>
            <td>33</td>
            <td>Royan Hotel (405 Valencia Street, Mission District)</td>
            <td>None</td>
            <td>39</td>
            <td>31</td>
            <td>42</td>
            <td>41</td>
            <td>275</td>
            <td>None</td>
            <td>None</td>
        </tr>
        <tr>
            <td>44</td>
            <td>33</td>
            <td>Department of Public Health (101 Grove Street at Polk, Civic Center)</td>
            <td>None</td>
            <td>39</td>
            <td>31</td>
            <td>42</td>
            <td>41</td>
            <td>275</td>
            <td>None</td>
            <td>None</td>
        </tr>
        <tr>
            <td>45</td>
            <td>34</td>
            <td>101 Henry Adams Place</td>
            <td>None</td>
            <td>40</td>
            <td>32</td>
            <td>43</td>
            <td>42</td>
            <td>276</td>
            <td>38</td>
            <td>460</td>
        </tr>
        <tr>
            <td>46</td>
            <td>10</td>
            <td>3639 Taraval St</td>
            <td>None</td>
            <td>41</td>
            <td>None</td>
            <td>44</td>
            <td>43</td>
            <td>277</td>
            <td>39</td>
            <td>461</td>
        </tr>
        <tr>
            <td>46</td>
            <td>10</td>
            <td>1458 33rd Ave.</td>
            <td>None</td>
            <td>41</td>
            <td>None</td>
            <td>44</td>
            <td>43</td>
            <td>277</td>
            <td>39</td>
            <td>461</td>
        </tr>
        <tr>
            <td>46</td>
            <td>10</td>
            <td>Lyon at Chestnut St.</td>
            <td>None</td>
            <td>41</td>
            <td>None</td>
            <td>44</td>
            <td>43</td>
            <td>277</td>
            <td>39</td>
            <td>461</td>
        </tr>
        <tr>
            <td>46</td>
            <td>10</td>
            <td>1559 Underwood Avenue between Lane and Keith</td>
            <td>None</td>
            <td>41</td>
            <td>None</td>
            <td>44</td>
            <td>43</td>
            <td>277</td>
            <td>39</td>
            <td>461</td>
        </tr>
        <tr>
            <td>46</td>
            <td>10</td>
            <td>1465 Revere Avenue between Keith and Jennings</td>
            <td>None</td>
            <td>41</td>
            <td>None</td>
            <td>44</td>
            <td>43</td>
            <td>277</td>
            <td>39</td>
            <td>461</td>
        </tr>
        <tr>
            <td>46</td>
            <td>10</td>
            <td>1601 Lane St.</td>
            <td>None</td>
            <td>41</td>
            <td>None</td>
            <td>44</td>
            <td>43</td>
            <td>277</td>
            <td>39</td>
            <td>461</td>
        </tr>
        <tr>
            <td>46</td>
            <td>10</td>
            <td>420 Mason St.</td>
            <td>None</td>
            <td>41</td>
            <td>None</td>
            <td>44</td>
            <td>43</td>
            <td>277</td>
            <td>39</td>
            <td>461</td>
        </tr>
        <tr>
            <td>46</td>
            <td>10</td>
            <td>119 Utah</td>
            <td>None</td>
            <td>41</td>
            <td>None</td>
            <td>44</td>
            <td>43</td>
            <td>277</td>
            <td>39</td>
            <td>461</td>
        </tr>
        <tr>
            <td>46</td>
            <td>10</td>
            <td>100 Alemany Blvd.</td>
            <td>None</td>
            <td>41</td>
            <td>None</td>
            <td>44</td>
            <td>43</td>
            <td>277</td>
            <td>39</td>
            <td>461</td>
        </tr>
        <tr>
            <td>46</td>
            <td>10</td>
            <td>812 22nd St. and Tennessee</td>
            <td>None</td>
            <td>41</td>
            <td>None</td>
            <td>44</td>
            <td>43</td>
            <td>277</td>
            <td>39</td>
            <td>461</td>
        </tr>
        <tr>
            <td>47</td>
            <td>35</td>
            <td>Mission Dolores Park (Mission District) via J-Church MUNI Train</td>
            <td>The two land plots that comprise the Park were used as a Jewish cemetery until 1894 when San Francisco prohibited all burials within city limits. The graves were moved to Colma, CA.</td>
            <td>5</td>
            <td>4</td>
            <td>45</td>
            <td>44</td>
            <td>278</td>
            <td>40</td>
            <td>None</td>
        </tr>
        <tr>
            <td>48</td>
            <td>4</td>
            <td>Li Po (916 Grant Avenue at Washington, Chinatown)</td>
            <td>None</td>
            <td>42</td>
            <td>33</td>
            <td>46</td>
            <td>45</td>
            <td>279</td>
            <td>41</td>
            <td>462</td>
        </tr>
        <tr>
            <td>48</td>
            <td>4</td>
            <td>Golden Dragon Restaurant (816 Washington Street at Grant)</td>
            <td>None</td>
            <td>42</td>
            <td>33</td>
            <td>46</td>
            <td>45</td>
            <td>279</td>
            <td>41</td>
            <td>462</td>
        </tr>
        <tr>
            <td>49</td>
            <td>30</td>
            <td>Maiden Lane between Kearny and Grant</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>47</td>
            <td>46</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>49</td>
            <td>30</td>
            <td>The Drew School, 2901 California</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>47</td>
            <td>46</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>49</td>
            <td>30</td>
            <td>State Garage, 818 Leavenworth</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>47</td>
            <td>46</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>49</td>
            <td>30</td>
            <td>60 Leavenworth St.</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>47</td>
            <td>46</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>50</td>
            <td>30</td>
            <td>Harvey Milk Rec Center, 50 Scott St.</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>48</td>
            <td>47</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>50</td>
            <td>30</td>
            <td>66 Potomac</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>48</td>
            <td>47</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>50</td>
            <td>30</td>
            <td>Mario&#x27;s Café, 566 Columbus</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>48</td>
            <td>47</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>50</td>
            <td>30</td>
            <td>Washington Square Park</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>48</td>
            <td>47</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>50</td>
            <td>30</td>
            <td>William Stout Architectural Books, 804 Montgomery St.</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>48</td>
            <td>47</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>50</td>
            <td>30</td>
            <td>1055 Montgomery St.</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>48</td>
            <td>47</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>50</td>
            <td>30</td>
            <td>60 Leavenworth St.</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>48</td>
            <td>47</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>50</td>
            <td>30</td>
            <td>Jefferson Square Park</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>48</td>
            <td>47</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>50</td>
            <td>30</td>
            <td>UN Plaza/ Civic Center Bart steps</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>48</td>
            <td>47</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>50</td>
            <td>30</td>
            <td>940 Powell St.</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>48</td>
            <td>47</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>50</td>
            <td>30</td>
            <td>Ellis and Jones St.</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>48</td>
            <td>47</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>50</td>
            <td>30</td>
            <td>Ellis Food Center, 398 Ellis</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>48</td>
            <td>47</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>50</td>
            <td>30</td>
            <td>Jonell&#x27;s Bar, 401 Ellis</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>48</td>
            <td>47</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>50</td>
            <td>30</td>
            <td>State Garage, 818 Leavenworth</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>48</td>
            <td>47</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>50</td>
            <td>30</td>
            <td>Antonio Alley</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>48</td>
            <td>47</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>50</td>
            <td>30</td>
            <td>253 4th Ave.</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>48</td>
            <td>47</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>50</td>
            <td>30</td>
            <td>Warren&#x27;s Antiques, 375 9th St.</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>48</td>
            <td>47</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>51</td>
            <td>30</td>
            <td>Private alley along 20th St. between Tennessee and Minnesota</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>47</td>
            <td>46</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>52</td>
            <td>30</td>
            <td>Mason and Pacific</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>48</td>
            <td>48</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>52</td>
            <td>30</td>
            <td>John St. between Powell and Mason</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>48</td>
            <td>48</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>52</td>
            <td>30</td>
            <td>Westin St. Francis</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>48</td>
            <td>48</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>52</td>
            <td>30</td>
            <td>Betelnut restaurant, 2030 Union St.</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>48</td>
            <td>48</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>52</td>
            <td>30</td>
            <td>Sutter Stockton Garage, 444 Stockton</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>48</td>
            <td>48</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>52</td>
            <td>30</td>
            <td>YWCA, 940 Powell</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>48</td>
            <td>48</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>52</td>
            <td>30</td>
            <td>Warren&#x27;s Antiques, 375 9th St.</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>48</td>
            <td>48</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>52</td>
            <td>30</td>
            <td>Heron and Berwick Alleys</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>48</td>
            <td>48</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>52</td>
            <td>30</td>
            <td>Duboce St., Duboce Café</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>48</td>
            <td>48</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>52</td>
            <td>30</td>
            <td>Potomac and Waller</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>48</td>
            <td>48</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>52</td>
            <td>30</td>
            <td>State Garage, 818 Leavenworth</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>48</td>
            <td>48</td>
            <td>280</td>
            <td>42</td>
            <td>463</td>
        </tr>
        <tr>
            <td>53</td>
            <td>30</td>
            <td>60 Leavenworth St.</td>
            <td>None</td>
            <td>43</td>
            <td>34</td>
            <td>3</td>
            <td>49</td>
            <td>280</td>
            <td>42</td>
            <td>463</td...(truncated)

%reload_ext sql
%sql sqlite:///sf-film-locations.db

## Qustion related to COUNT
Using COUNT statement
### Q1 we want to count the number of records or rows of the "FilmLocations" table.

%%sql 
select * from FilmLocations
<table>
    <thead>
        <tr>
            <th>title</th>
            <th>release_year</th>
            <th>locations</th>
            <th>fun_facts</th>
            <th>production_company</th>
            <th>distributor</th>
            <th>director</th>
            <th>writer</th>
            <th>actor_1</th>
            <th>actor_2</th>
            <th>actor_3</th>
            <th>state</th>
            <th>city</th>
            <th>point</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Nash Bridges</td>
            <td>2021</td>
            <td>Pier 45, San Francisco</td>
            <td>None</td>
            <td>Village NB Productions, LLC</td>
            <td>USA Nework</td>
            <td>Greg Beeman</td>
            <td>Carlton Cuse, Bill Chais</td>
            <td>Don Johnson</td>
            <td>Cheech Marin</td>
            <td>Joe Dinicol</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.417428501 37.809873676)</td>
        </tr>
        <tr>
            <td>The OA Part II</td>
            <td>2019</td>
            <td>Ada Court at O&#x27;Farrell St</td>
            <td>None</td>
            <td>Lunar Mining LLC</td>
            <td>Netflix</td>
            <td>Zal Batmanglij</td>
            <td>Zal Batmanglij, Brit Marling</td>
            <td>Brit Marling</td>
            <td>Emory Cohen</td>
            <td>Patrick Gibson</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.41568003 37.785469982)</td>
        </tr>
        <tr>
            <td>Looking &quot;Special&quot;</td>
            <td>2016</td>
            <td>1246 Folsom Street</td>
            <td>None</td>
            <td>Mission Street Productions, LLC</td>
            <td>HBO</td>
            <td>Andrew Haigh</td>
            <td>Michael Lannan</td>
            <td>Jonathan Groff</td>
            <td>Frankie Alvarez</td>
            <td>Murray Bartlett</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.411002006 37.774595007)</td>
        </tr>
        <tr>
            <td>The Phone/Jexi</td>
            <td>2019</td>
            <td>Liberty St btwn Castro and Noe St</td>
            <td>None</td>
            <td>CBS Films Inc.</td>
            <td>Lionsgate</td>
            <td>Jon Lucas, Scott Moore</td>
            <td>Jon Lucas, Scott Moore</td>
            <td>Adam Devine</td>
            <td>Alexandra Shipp</td>
            <td>Michael Pena</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.432399999 37.75702)</td>
        </tr>
        <tr>
            <td>Terminator - Genisys</td>
            <td>2015</td>
            <td>California at Larkin</td>
            <td>None</td>
            <td>T5 Productions LLC</td>
            <td>Paramount Pictures</td>
            <td>Alan Taylor</td>
            <td>James Cameron</td>
            <td>Arnold Schwarzenegger</td>
            <td>Jason Clarke</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.419039999 37.790790018)</td>
        </tr>
        <tr>
            <td>Murder in the First, Season 3</td>
            <td>2016</td>
            <td>600 Octavia Street</td>
            <td>None</td>
            <td>Turner North Center Productions</td>
            <td>Turner Network Television (TNT)</td>
            <td>Steven Bochcho</td>
            <td>Eric Lodal</td>
            <td>Taye Diggs</td>
            <td>Kathleen Robertson</td>
            <td>Ian Anthony Dale</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.424684038 37.777814999)</td>
        </tr>
        <tr>
            <td>Ant-Man and the Wasp</td>
            <td>2018</td>
            <td>Bush St at Mason St</td>
            <td>VFX Plate Shots</td>
            <td>PYM Particles Productions II, LLC</td>
            <td>Walt Disney Studios Motion Pictures</td>
            <td>Peyton Reed</td>
            <td>Chris McKenna</td>
            <td>Paul Rudd</td>
            <td>Evangeline Lilly</td>
            <td>Michael Douglas</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.410430025 37.78996)</td>
        </tr>
        <tr>
            <td>Dirty Harry</td>
            <td>1971</td>
            <td>Portsmouth Square (Chinatown)</td>
            <td>In 1847 the first public school in California was erected on what would become Portsmouth Square.</td>
            <td>The Malpaso Company</td>
            <td>Warner Brothers</td>
            <td>Don Siegel</td>
            <td>Harry Julian Fink</td>
            <td>Clint Eastwood</td>
            <td>Harry Guardino</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.40571 37.79479)</td>
        </tr>
        <tr>
            <td>40 Days and 40 Nights</td>
            <td>2002</td>
            <td>Café Trieste (609 Vallejo)</td>
            <td>Francis Ford Coppola allegedly wrote large portions of &quot;The Godfather&quot; trilogy in Café Trieste.</td>
            <td>Miramax Films</td>
            <td>Miramax Films</td>
            <td>Michael Lehmann</td>
            <td>Robert Perez</td>
            <td>Josh Hartnett</td>
            <td>Shaynnyn Sossamon</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.407357973 37.798572992)</td>
        </tr>
        <tr>
            <td>Harold and Maude</td>
            <td>1971</td>
            <td>Sutro Baths (Point Lobos Avenue)</td>
            <td>None</td>
            <td>Mildred Lewis and Colin Higgins Productions</td>
            <td>Paramount Pictures</td>
            <td>Hal Ashby</td>
            <td>Colin Higgins</td>
            <td>Ruth Gordon</td>
            <td>Bud Cort</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.510031794 37.779832009)</td>
        </tr>
        <tr>
            <td>Time After Time</td>
            <td>1979</td>
            <td>Palace of Fine Arts (3301 Lyon Street)</td>
            <td>The original Palace was built for the 1915 Panama-Pacific Exposition, and completely destroyed in 1964. It was rebuilt in 1965.</td>
            <td>Orion Pictures Corp.</td>
            <td>Columbia Broadcasting System (CBS)</td>
            <td>Nicholas Meyer</td>
            <td>Karl Alexander</td>
            <td>Malcolm McDowell</td>
            <td>Mary Steenburgen</td>
            <td>David Warner</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.44899 37.80288)</td>
        </tr>
        <tr>
            <td>Quitters</td>
            <td>2015</td>
            <td>Claire Lilienthal Elementary School</td>
            <td>None</td>
            <td>Frederick &amp; Ashbury, LLC.</td>
            <td>None</td>
            <td>Noah Pritzker</td>
            <td>Noah Pritzker</td>
            <td>Kara Hayward</td>
            <td>Mira Sorvino</td>
            <td>Saffron Burrows</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.45796 37.7871)</td>
        </tr>
        <tr>
            <td>Quitters</td>
            <td>2015</td>
            <td>1536 Noe St.</td>
            <td>None</td>
            <td>Frederick &amp; Ashbury, LLC.</td>
            <td>None</td>
            <td>Noah Pritzker</td>
            <td>Noah Pritzker</td>
            <td>Kara Hayward</td>
            <td>Mira Sorvino</td>
            <td>Saffron Burrows</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.431454017 37.744473004)</td>
        </tr>
        <tr>
            <td>The Dead Pool</td>
            <td>1988</td>
            <td>550 El Camino Del Mar (Seacliff)</td>
            <td>None</td>
            <td>Warner Bros. Pictures</td>
            <td>Warner Bros. Pictures</td>
            <td>Buddy Van Horn</td>
            <td>Harry Julian Fink</td>
            <td>Clint Eastwood</td>
            <td>Liam Neeson</td>
            <td>Patricia Clarkson</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.489937992 37.787534989)</td>
        </tr>
        <tr>
            <td>The Princess Diaries</td>
            <td>2001</td>
            <td>2601 Lyon Street</td>
            <td>None</td>
            <td>Walt Disney Pictures</td>
            <td>Buena Vista Pictures</td>
            <td>Garry Marshall</td>
            <td>Gina Wendkos</td>
            <td>Julie Andrews</td>
            <td>Anne Hathway</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.447010997 37.794680981)</td>
        </tr>
        <tr>
            <td>Murder in the First, Season 1</td>
            <td>2014</td>
            <td>Ida B. Wells High School (1099 Hayes Street)</td>
            <td>Ida B. Wells High School is named after the African-American journalist, suffragist and early leader in the Civil Rights Movement Ida B. Wells</td>
            <td>Turner North Center Productions</td>
            <td>Turner Network Television (TNT)</td>
            <td>Steven Bochcho</td>
            <td>Eric Lodal</td>
            <td>Taye Diggs</td>
            <td>Kathleen Robertson</td>
            <td>Ian Anthony Dale</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.434035978 37.775064017)</td>
        </tr>
        <tr>
            <td>Junior</td>
            <td>1994</td>
            <td>722 Steiner Street</td>
            <td>None</td>
            <td>Northern Lights Entertainment</td>
            <td>Universal Pictures</td>
            <td>Ivan Reitman</td>
            <td>Kevin Wade</td>
            <td>Arnold Schwarzenegger</td>
            <td>Danny DeVito</td>
            <td>Emma Thompson</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.432784979 37.776451012)</td>
        </tr>
        <tr>
            <td>The Woman In Red</td>
            <td>1984</td>
            <td>Postcard Row (Alamo Square, Hayes Valley)</td>
            <td>The 6 Victorian homes across from Alamo Square Park are among the few Victorians to survive the Great Fire.</td>
            <td>Orion Pictures Corp.</td>
            <td>MGM Home Entertainment</td>
            <td>Gene Wilder</td>
            <td>Jean Loup Dabadie &amp; Yves Robert</td>
            <td>Gene Wilder</td>
            <td>Charles Grodin</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.43146 37.77722)</td>
        </tr>
        <tr>
            <td>The Bachelor</td>
            <td>1999</td>
            <td>Pacific Stock Exchange (301 Pine Street at Sansome)</td>
            <td>None</td>
            <td>George Street Pictures</td>
            <td>New Line Cinema</td>
            <td>Gary Sinyor</td>
            <td>Steve Cohen</td>
            <td>Chris O&#x27;Donnell</td>
            <td>Renee Zellweger</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.400920001 37.792099983)</td>
        </tr>
        <tr>
            <td>Final Analysis</td>
            <td>1992</td>
            <td>Bix Restaurant (56 Gold Street)</td>
            <td>None</td>
            <td>Warner Bros. Pictures</td>
            <td>Warner Bros. Pictures</td>
            <td>Phil Joanou</td>
            <td>Robert Berger</td>
            <td>Richard Gere</td>
            <td>Kim Basinger</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.402907 37.796864)</td>
        </tr>
        <tr>
            <td>Women is Losers</td>
            <td>2020</td>
            <td>2712 Bryant St</td>
            <td>None</td>
            <td>Look at the Moon Pictures</td>
            <td>None</td>
            <td>Lissette Feliciano</td>
            <td>Lissette Feliciano</td>
            <td>Lorenza Izzo</td>
            <td>Simu Liu</td>
            <td>Liza Weil</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.409273992 37.750881011)</td>
        </tr>
        <tr>
            <td>Rent</td>
            <td>2005</td>
            <td>Treasure Island</td>
            <td>An artificial island, Treasure Island was created for the 1939 Golden Gate International Exposition, and is named after the novel by Robert Louis Stevenson, a one-time San Francisco resident.</td>
            <td>Rent Productions LLC</td>
            <td>Columbia Pictures</td>
            <td>Chris Columbus</td>
            <td>Stephen Chbosky</td>
            <td>Anthony Rapp</td>
            <td>Rosario Dawson</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.37087 37.82489)</td>
        </tr>
        <tr>
            <td>The Last Black Man in San Francisco</td>
            <td>2019</td>
            <td>Illinois St btwn Marin and Amador</td>
            <td>None</td>
            <td>LBMISF, LLC</td>
            <td>A45</td>
            <td>Joe Talbot</td>
            <td>Joe Talbot, Jimmie Fails, Rob Richert</td>
            <td>Jimmie Fails</td>
            <td>Jonathan Majors</td>
            <td>Danny Glover</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.386040027 37.745770019)</td>
        </tr>
        <tr>
            <td>Smile Again, Jenny Lee</td>
            <td>2015</td>
            <td>Europa Café (4318 California St. and 5th Ave.)</td>
            <td>None</td>
            <td>Carlo Caldana/Marguery Films</td>
            <td>None</td>
            <td>Carlo Caldana</td>
            <td>Linda Demetrick</td>
            <td>Craig Tsuyumine</td>
            <td>Puneet Prasad</td>
            <td>Larry Kitagawa</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.463499961 37.785130012)</td>
        </tr>
        <tr>
            <td>Sense8</td>
            <td>2015</td>
            <td>Market St. overpass</td>
            <td>Bicycle chase scene</td>
            <td>Unpronounceable Productions, LLC</td>
            <td>Netflix</td>
            <td>The Wachowskis</td>
            <td>The Wachowskis</td>
            <td>Jamie Clayton</td>
            <td>None</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.40001657 37.79039257)</td>
        </tr>
        <tr>
            <td>Tucker: The Man and His Dream</td>
            <td>1988</td>
            <td>City Hall</td>
            <td>The dome of SF&#x27;s City Hall is almost a foot taller than that of the US Capitol Building. In 1954, Joe DiMaggio and Marilyn Monroe married at the Beaux Arts-style building.</td>
            <td>Lucasfilm</td>
            <td>Paramount Pictures</td>
            <td>Francis Ford Coppola</td>
            <td>Arnold Schulman</td>
            <td>Jeff Bridges</td>
            <td>Joan Allen</td>
            <td>Marin Landau</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.290284937 38.004649955)</td>
        </tr>
        <tr>
            <td>Dirty Harry</td>
            <td>1971</td>
            <td>Kezar Stadium, Golden Gate Park</td>
            <td>The stadium was demolished and completely rebuilt after sustaining damages in the 1898 Loma Prieta earthquake.</td>
            <td>The Malpaso Company</td>
            <td>Warner Brothers</td>
            <td>Don Siegel</td>
            <td>Harry Julian Fink</td>
            <td>Clint Eastwood</td>
            <td>Harry Guardino</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.45472 37.7664)</td>
        </tr>
        <tr>
            <td>Nash Bridges</td>
            <td>2021</td>
            <td>2800 Pacific Avenue</td>
            <td>None</td>
            <td>Village NB Productions, LLC</td>
            <td>USA Nework</td>
            <td>Greg Beeman</td>
            <td>Carlton Cuse, Bill Chais</td>
            <td>Don Johnson</td>
            <td>Cheech Marin</td>
            <td>Joe Dinicol</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.441781025 37.792684998)</td>
        </tr>
        <tr>
            <td>Terminator - Genisys</td>
            <td>2015</td>
            <td>Pier 14</td>
            <td>None</td>
            <td>T5 Productions LLC</td>
            <td>Paramount Pictures</td>
            <td>Alan Taylor</td>
            <td>James Cameron</td>
            <td>Arnold Schwarzenegger</td>
            <td>Jason Clarke</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.3911 37.79366)</td>
        </tr>
        <tr>
            <td>The Phone/Jexi</td>
            <td>2019</td>
            <td>Tamarind Hall - 1268 Grant Ave</td>
            <td>None</td>
            <td>CBS Films Inc.</td>
            <td>Lionsgate</td>
            <td>Jon Lucas, Scott Moore</td>
            <td>Jon Lucas, Scott Moore</td>
            <td>Adam Devine</td>
            <td>Alexandra Shipp</td>
            <td>Michael Pena</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.407001994 37.79864801)</td>
        </tr>
        <tr>
            <td>Tales of the City</td>
            <td>2019</td>
            <td>Mission District</td>
            <td>None</td>
            <td>Universal Television LLC</td>
            <td>Netflix</td>
            <td>Alan Poul, Silas Howard, Stacie Passon</td>
            <td>Armistead Maupin, Lauren Morelli, Hansol Jung, Marcus Gardley</td>
            <td>Laura Linney</td>
            <td>Ellen Page</td>
            <td>Murray Bartlett</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.41914 37.75993)</td>
        </tr>
        <tr>
            <td>Nine to Five</td>
            <td>1980</td>
            <td>Albert S. Samuels Clock (856 Market Street between Powell and Stockton)</td>
            <td>None</td>
            <td>Twentieth Century Fox Film Corporation</td>
            <td>Twentieth Century Fox Film Corporation</td>
            <td>Colin Higgins</td>
            <td>Colin Higgins</td>
            <td>Jane Fonda</td>
            <td>Lily Tomlin</td>
            <td>Dolly Parton</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.407105007 37.785159013)</td>
        </tr>
        <tr>
            <td>Shit and Champagne</td>
            <td>2020</td>
            <td>Leavenworth at Greenwich St</td>
            <td>None</td>
            <td>Shaboom Boom, LLC</td>
            <td>None</td>
            <td>D&#x27;Arcy Drollinger</td>
            <td>D&#x27;Arcy Drollinger</td>
            <td>D&#x27;Arcy Drollinger</td>
            <td>Matthew Martin</td>
            <td>Steven LeMay</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.417790006 37.801250004)</td>
        </tr>
        <tr>
            <td>Ant-Man</td>
            <td>2015</td>
            <td>Intersection of California at Polk</td>
            <td>Driving shots</td>
            <td>PYM Particles Productions, LLC</td>
            <td>Walt Disney Studios Motion Pictures</td>
            <td>Peyton Reed</td>
            <td>Gabriel Ferrari</td>
            <td>Michael Douglas</td>
            <td>Paul Rudd</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.420680003 37.790569993)</td>
        </tr>
        <tr>
            <td>Pacific Heights</td>
            <td>1990</td>
            <td>Texas &amp; 19th Streets (Potrero Hill)</td>
            <td>None</td>
            <td>Morgan Creek Productions</td>
            <td>Twentieth Century Fox Film Corporation</td>
            <td>John Schlesinger</td>
            <td>Daniel Pyne</td>
            <td>Melanie Griffith</td>
            <td>Matthew Modine</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.395449971 37.761369998)</td>
        </tr>
        <tr>
            <td>Interview With The Vampire</td>
            <td>1994</td>
            <td>Golden Gate Bridge</td>
            <td>With 23 miles of ladders and 300,000 rivets in each tower, the Golden Gate Bridge was the world&#x27;s longest span when it opened in 1937.</td>
            <td>Geffen Pictures</td>
            <td>Geffen Pictures</td>
            <td>Neil Jordan</td>
            <td>Anne Rice</td>
            <td>Brad Pitt</td>
            <td>Christian Slater</td>
            <td>Tom Cruise</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.47847 37.81914)</td>
        </tr>
        <tr>
            <td>Bitter Melon</td>
            <td>2018</td>
            <td>3189 16th St</td>
            <td>None</td>
            <td>Bitter Melon Film LLC/Mammoth Pictures</td>
            <td>ABS-CBN, Gravitas Ventures</td>
            <td>H.P. Mendoza</td>
            <td>H.P. Mendoza</td>
            <td>Jon Norman Schneider</td>
            <td>Patrick Epino</td>
            <td>Brian Rivera</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.423608975 37.764560989)</td>
        </tr>
        <tr>
            <td>Chance Season 2</td>
            <td>2017</td>
            <td>Lombard St between Hyde and Larkin St</td>
            <td>None</td>
            <td>TVM Productions Inc.</td>
            <td>Hulu</td>
            <td>Rozann Dawson</td>
            <td>Alexandra Cunningham</td>
            <td>Hugh Laurie</td>
            <td>Greta Lee</td>
            <td>Ethan Suplee</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.421249972 37.801779992)</td>
        </tr>
        <tr>
            <td>Dawn of the Planet of the Apes</td>
            <td>2014</td>
            <td>Filbert St. from Hyde to Leavenworth</td>
            <td>None</td>
            <td>Fox Louisiana Productions, LLC</td>
            <td>Twentieth Century Fox</td>
            <td>Matt Reeves</td>
            <td>Rick Jaffa</td>
            <td>Gary Oldman</td>
            <td>Keri Russell</td>
            <td>Andy Serkis</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.412683593 37.800975612)</td>
        </tr>
        <tr>
            <td>Hulk</td>
            <td>2003</td>
            <td>Golden Gate Bridge</td>
            <td>With 23 miles of ladders and 300,000 rivets in each tower, the Golden Gate Bridge was the world&#x27;s longest span when it opened in 1937.</td>
            <td>Universal Pictures</td>
            <td>Universal Pictures</td>
            <td>Ang Lee</td>
            <td>Stan Lee</td>
            <td>Eric Bana</td>
            <td>Jennifer Connelly</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.47847 37.81914)</td>
        </tr>
        <tr>
            <td>Venom</td>
            <td>2018</td>
            <td>Grant Ave btwn Washington and Jackson</td>
            <td>None</td>
            <td>L.O.Z. Productions, Inc.</td>
            <td>Columbia Pictures, Sony Pictures Releasing</td>
            <td>Ruben Fleischer</td>
            <td>Jeff Pinkner, Scott Rosenberg</td>
            <td>Tom Hardy</td>
            <td>Michelle Wiliams</td>
            <td>Riz Ahmed</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.406630005 37.796030006)</td>
        </tr>
        <tr>
            <td>Surface</td>
            <td>2022</td>
            <td>Jackson Street between Stockton and Grant</td>
            <td>None</td>
            <td>Apple Studios, LLC</td>
            <td>Apple TV+</td>
            <td>Sam Miller, Kevin Rodney Sullivan, Jennifer Morrison, Tucker Gates</td>
            <td>Veronica West, Erica L. Anderson,Tony Saltzman, Glenise Mullins, Leigh Ann Biety, Dan Lee West, Leigh Ann Biety &amp; Raven Jackson, Martín Zimmerman</td>
            <td>Gugu Mbatha-Raw</td>
            <td>Oliver Jackson-Cohen</td>
            <td>Ari Graynor</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.406630005 37.796030006)</td>
        </tr>
        <tr>
            <td>Sudden Impact</td>
            <td>1983</td>
            <td>The Embarcadero/Ferry Building</td>
            <td>Every hour and half-hour, the clock bell atop the Ferry Building chimes portions of the Westminster Quarters.</td>
            <td>Warner Bros. Pictures</td>
            <td>Warner Bros. Pictures</td>
            <td>Clint Eastwood</td>
            <td>Harry Julian Fink</td>
            <td>Clint Eastwood</td>
            <td>Sondra Locke</td>
            <td>Pat Hingle</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.39343 37.79553)</td>
        </tr>
        <tr>
            <td>Looking Season 2 ep 204</td>
            <td>2015</td>
            <td>970 Geary Street</td>
            <td>None</td>
            <td>Mission Street Productions, LLC</td>
            <td>HBO</td>
            <td>Andrew Haigh</td>
            <td>Michael Lannan</td>
            <td>Jonathan Groff</td>
            <td>Frankie Alvarez</td>
            <td>Murray Bartlett</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.419180983 37.786153987)</td>
        </tr>
        <tr>
            <td>Etruscan Smile</td>
            <td>2017</td>
            <td>3rd Street between Market &amp; Harrison</td>
            <td>None</td>
            <td>Po Valley Productions, LLC</td>
            <td>TBD</td>
            <td>Oded Binnun/ Michel Brezis</td>
            <td>Sarah Bellwood, Michal Lali Kagan, Michael McGowan Amital Stern, Jose Luis Sampedro</td>
            <td>Brian Cox</td>
            <td>Roseanne Arquette</td>
            <td>Thora Birch</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.397389963 37.78255002)</td>
        </tr>
        <tr>
            <td>Summertime</td>
            <td>2015</td>
            <td>Buena Vista East &amp; Duboce; Buena Vista East &amp; Haight</td>
            <td>None</td>
            <td>Creative Monster Productions, Inc.</td>
            <td>5 Distribution</td>
            <td>Gabriele Muccino</td>
            <td>Gabriele Muccino</td>
            <td>Jessica Rothe</td>
            <td>Scott Bakula</td>
            <td>Matilda Anna Ingrid Lutz</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.440319975 37.770850015)</td>
        </tr>
        <tr>
            <td>Always Be My Maybe</td>
            <td>2019</td>
            <td>Pier 7</td>
            <td>None</td>
            <td>Isla Productions, LLC</td>
            <td>Netflix</td>
            <td>Nahnatchka Khan</td>
            <td>Michael Golamco, Randall Park, Ali Wong</td>
            <td>Ali Wong</td>
            <td>Randall Park</td>
            <td>Keanu Reeves</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.397409995 37.799364998)</td>
        </tr>
        <tr>
            <td>San Andreas</td>
            <td>2015</td>
            <td>Hyde St. at Greenwich and Hyde St. at Lombard</td>
            <td>Characters walk to get a vantage point for Coit tower. 250 actors walking &quot;fleeing&quot; the city after earthquake</td>
            <td>Upside Down Productions, Inc.</td>
            <td>Warner Bros.</td>
            <td>Brad Peyton</td>
            <td>Allan Loeb</td>
            <td>Dwayne Johnson</td>
            <td>None</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.419430009 37.801070003)</td>
        </tr>
        <tr>
            <td>Birth of the Dragon</td>
            <td>2016</td>
            <td>Pier 45 - Jeremiah O&#x27;Brien Liberty Ship</td>
            <td>The SS Jeremiah O&#x27;Brien is a rare survivor of the invasion at Normandy on D-Day in WWII.</td>
            <td>BOTD U.S. Productions, Inc.</td>
            <td>Kylin Pictures</td>
            <td>George Nolfi</td>
            <td>Christopher Wilkinson, Stephen J. Rivele</td>
            <td>Philip Ng</td>
            <td>Billy Magnussen</td>
            <td>Yu Xia</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.417428501 37.809873676)</td>
        </tr>
        <tr>
            <td>The Rock</td>
            <td>1996</td>
            <td>Fairmont Hotel (950 Mason Street, Nob Hill)</td>
            <td>In 1945 the Fairmont hosted the United Nations Conference on International Organization as delegates arrived to draft a charter for the organization. The U.S. Secretary of State, Edward Stettinius drafted the charter in the hotel&#x27;s Garden Room.</td>
            <td>Hollywood Pictures</td>
            <td>Buena Vista Pictures</td>
            <td>Michael Bay</td>
            <td>David Weisberg</td>
            <td>Sean Connery</td>
            <td>Nicolas Cage</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.41075 37.79232)</td>
        </tr>
        <tr>
            <td>Sense8</td>
            <td>2015</td>
            <td>18th Street between Guerrero and Valencia Streets</td>
            <td>Re-enactment of &quot;Dyke&#x27;s on Bikes&quot; and &quot;Dyke March&quot;</td>
            <td>Unpronounceable Productions, LLC</td>
            <td>Netflix</td>
            <td>The Wachowskis</td>
            <td>The Wachowskis</td>
            <td>Jamie Clayton</td>
            <td>None</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.453869992 37.492129983)</td>
        </tr>
        <tr>
            <td>So I Married an Axe Murderer</td>
            <td>1993</td>
            <td>Vesuvio Café (255 Columbus Avenue)</td>
            <td>Jack Kerouac was a regular at the café.</td>
            <td>TriStar Pictures</td>
            <td>TriStar Pictures</td>
            <td>Thomas Schlamme</td>
            <td>Robbie Fox</td>
            <td>Mike Myers</td>
            <td>Nancy Travis</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.406458 37.797505)</td>
        </tr>
        <tr>
            <td>Blue Jasmine</td>
            <td>2013</td>
            <td>Taylor &amp; Green St.</td>
            <td>None</td>
            <td>Perdido Productions</td>
            <td>Sony Pictures Classics</td>
            <td>Woody Allen</td>
            <td>Woody Allen</td>
            <td>Cate Blanchett</td>
            <td>Alec Baldwin</td>
            <td>Peter Sarsgaard</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.413929972 37.798900012)</td>
        </tr>
        <tr>
            <td>The Maltese Falcon</td>
            <td>1941</td>
            <td>Burritt Alley (Off Bush Street, between Powell and Stockton Streets)</td>
            <td>None</td>
            <td>Warner Bros. Pictures</td>
            <td>Warner Bros. Pictures</td>
            <td>John Huston</td>
            <td>John Huston</td>
            <td>Humphrey Bogart</td>
            <td>Mary Astor</td>
            <td>Gladys George</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.407150018 37.790380017)</td>
        </tr>
        <tr>
            <td>Surface</td>
            <td>2022</td>
            <td>Merchant Road Trail at Presidio</td>
            <td>None</td>
            <td>Apple Studios, LLC</td>
            <td>Apple TV+</td>
            <td>Sam Miller, Kevin Rodney Sullivan, Jennifer Morrison, Tucker Gates</td>
            <td>Veronica West, Erica L. Anderson,Tony Saltzman, Glenise Mullins, Leigh Ann Biety, Dan Lee West, Leigh Ann Biety &amp; Raven Jackson, Martín Zimmerman</td>
            <td>Gugu Mbatha-Raw</td>
            <td>Oliver Jackson-Cohen</td>
            <td>Ari Graynor</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.474540017 37.806720013)</td>
        </tr>
        <tr>
            <td>Chance- Season 1 ep106</td>
            <td>2016</td>
            <td>2 Rowland</td>
            <td>None</td>
            <td>TVM Productions</td>
            <td>HULU</td>
            <td>Sara Gran</td>
            <td>Dan Attias</td>
            <td>Hugh Laurie</td>
            <td>Gretchen Mol</td>
            <td>Ethan Suplee</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.404530038 37.797715741)</td>
        </tr>
        <tr>
            <td>Chance - Season 1 Pilot</td>
            <td>2016</td>
            <td>UN Plaza/ Civic Center Bart steps</td>
            <td>None</td>
            <td>TVM Productions</td>
            <td>HULU</td>
            <td>Lenny Abrahamson</td>
            <td>Alexandra Cunningham and Kem Nunn</td>
            <td>Hugh Laurie</td>
            <td>Gretchen Mol</td>
            <td>Ethan Suplee</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.41362 37.77964)</td>
        </tr>
        <tr>
            <td>Goliath- Season 4</td>
            <td>2021</td>
            <td>Grant and Commercial</td>
            <td>None</td>
            <td>Picrow, Inc.</td>
            <td>Amazon Studios</td>
            <td>Billy Bob Thornton, Lawrence Trilling, Derek Johansen</td>
            <td>David E. Kelley, Jonathan Shapiro</td>
            <td>Billy Bob Thornton</td>
            <td>Nina Arianda</td>
            <td>Tania Raymonde</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.406179981 37.793839983)</td>
        </tr>
        <tr>
            <td>Groove</td>
            <td>2000</td>
            <td>435 23rd Street at Illinois</td>
            <td>None</td>
            <td>415 Productions</td>
            <td>Sony Pictures Classics</td>
            <td>Greg Harrison</td>
            <td>Greg Harrison</td>
            <td>Chris Ferreira</td>
            <td>Elizabeth Sun</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.387090028 37.755429995)</td>
        </tr>
        <tr>
            <td>Chance Season 2</td>
            <td>2017</td>
            <td>Duboce between Buena Vista East and Alpine St</td>
            <td>None</td>
            <td>TVM Productions Inc.</td>
            <td>Hulu</td>
            <td>Rozann Dawson</td>
            <td>Alexandra Cunningham</td>
            <td>Hugh Laurie</td>
            <td>Greta Lee</td>
            <td>Ethan Suplee</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.437487857 37.768721005)</td>
        </tr>
        <tr>
            <td>The Last Black Man in San Francisco</td>
            <td>2019</td>
            <td>900 Innes Ave</td>
            <td>Boat dock</td>
            <td>LBMISF, LLC</td>
            <td>A26</td>
            <td>Joe Talbot</td>
            <td>Joe Talbot, Jimmie Fails, Rob Richert</td>
            <td>Jimmie Fails</td>
            <td>Jonathan Majors</td>
            <td>Danny Glover</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.375759958 37.732206005)</td>
        </tr>
        <tr>
            <td>Heart Beat</td>
            <td>1980</td>
            <td>Washington Square Bar &amp; Grill (1707 Powell)</td>
            <td>None</td>
            <td>Orion Pictures Corporation</td>
            <td>Orion Pictures Corporation</td>
            <td>John Byrum</td>
            <td>John Byrum</td>
            <td>Nick Nolte</td>
            <td>Sissy Spacek</td>
            <td>John Heard</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.409689986 37.794750006)</td>
        </tr>
        <tr>
            <td>Shit and Champagne</td>
            <td>2020</td>
            <td>La Ferrera Terrace at Kearny St</td>
            <td>None</td>
            <td>Shaboom Boom, LLC</td>
            <td>None</td>
            <td>D&#x27;Arcy Drollinger</td>
            <td>D&#x27;Arcy Drollinger</td>
            <td>D&#x27;Arcy Drollinger</td>
            <td>Matthew Martin</td>
            <td>Steven LeMay</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.406639979 37.803949983)</td>
        </tr>
        <tr>
            <td>DEVS</td>
            <td>2020</td>
            <td>Harrison at 25th St</td>
            <td>None</td>
            <td>Minim Productions</td>
            <td>FX Network</td>
            <td>Alex Garland</td>
            <td>Alex Garland</td>
            <td>Sonoya Mizuno</td>
            <td>Nick Offerman</td>
            <td>Jin Ha</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.411780014 37.75104999)</td>
        </tr>
        <tr>
            <td>Smile Again, Jenny Lee</td>
            <td>2015</td>
            <td>333 Pacheco St at Lopez Ave.</td>
            <td>None</td>
            <td>Carlo Caldana/Marguery Films</td>
            <td>None</td>
            <td>Carlo Caldana</td>
            <td>Linda Demetrick</td>
            <td>Craig Tsuyumine</td>
            <td>Puneet Prasad</td>
            <td>Larry Kitagawa</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.462650036 37.74842)</td>
        </tr>
        <tr>
            <td>Edtv</td>
            <td>1999</td>
            <td>Castro Theatre (429 Castro Street, The Castro)</td>
            <td>The original Castro Theatre was built in 1910, a few doors down from the current theatre. The original theatre was converted into retail space, and the current theatre was built in the 1920s.</td>
            <td>Imagine Entertainment</td>
            <td>MCA / Universal Pictures</td>
            <td>Ron Howard</td>
            <td>Lowell Ganz</td>
            <td>Matthew McConaughey</td>
            <td>Jenna Elfman</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.4346 37.76188)</td>
        </tr>
        <tr>
            <td>Looking Season 2 ep 207</td>
            <td>2015</td>
            <td>770 Haight Street</td>
            <td>None</td>
            <td>Mission Street Productions, LLC</td>
            <td>HBO</td>
            <td>Andrew Haigh</td>
            <td>Michael Lannan</td>
            <td>Jonathan Groff</td>
            <td>Frankie Alvarez</td>
            <td>Murray Bartlett</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.434883976 37.771797002)</td>
        </tr>
        <tr>
            <td>Chance Season 2</td>
            <td>2017</td>
            <td>Scott St between Jackson and Clay St</td>
            <td>None</td>
            <td>TVM Productions Inc.</td>
            <td>Hulu</td>
            <td>Rozann Dawson</td>
            <td>Alexandra Cunningham</td>
            <td>Hugh Laurie</td>
            <td>Greta Lee</td>
            <td>Ethan Suplee</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.439139971 37.790079987)</td>
        </tr>
        <tr>
            <td>Nash Bridges</td>
            <td>2021</td>
            <td>Alameda Street between Vermont and San Bruno</td>
            <td>None</td>
            <td>Village NB Productions, LLC</td>
            <td>USA Nework</td>
            <td>Greg Beeman</td>
            <td>Carlton Cuse, Bill Chais</td>
            <td>Don Johnson</td>
            <td>Cheech Marin</td>
            <td>Joe Dinicol</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.405759963 37.768499981)</td>
        </tr>
        <tr>
            <td>Flubber</td>
            <td>1997</td>
            <td>Treasure Island</td>
            <td>An artificial island, Treasure Island was created for the 1939 Golden Gate International Exposition, and is named after the novel by Robert Louis Stevenson, a one-time San Francisco resident.</td>
            <td>Walt Disney Pictures</td>
            <td>Buena Vista Pictures</td>
            <td>Les Mayfield</td>
            <td>Samuel W. Taylor</td>
            <td>Robin Williams</td>
            <td>Marcia Gay Harden</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.37087 37.82489)</td>
        </tr>
        <tr>
            <td>The Phone/Jexi</td>
            <td>2019</td>
            <td>Texas at 17th St</td>
            <td>None</td>
            <td>CBS Films Inc.</td>
            <td>Lionsgate</td>
            <td>Jon Lucas, Scott Moore</td>
            <td>Jon Lucas, Scott Moore</td>
            <td>Adam Devine</td>
            <td>Alexandra Shipp</td>
            <td>Michael Pena</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.395820032 37.765190009)</td>
        </tr>
        <tr>
            <td>Murder in the First, Season 1</td>
            <td>2014</td>
            <td>AT&amp;T Park</td>
            <td>None</td>
            <td>Turner North Center Productions</td>
            <td>Turner Network Television (TNT)</td>
            <td>Steven Bochcho</td>
            <td>Eric Lodal</td>
            <td>Taye Diggs</td>
            <td>Kathleen Robertson</td>
            <td>Ian Anthony Dale</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.38951 37.77849)</td>
        </tr>
        <tr>
            <td>A Taiwanese Tale of Two Cities</td>
            <td>2018</td>
            <td>Steiner St at Fulton St</td>
            <td>None</td>
            <td>Envision Productions Inc.</td>
            <td>Netflix</td>
            <td>Tien-Lun Yeh</td>
            <td>Ling-Hui Chen, Nancy Chen, Chih-Chi Fan, Chia-Hui Lin</td>
            <td>Tammy Cheng</td>
            <td>Peggy Tseng</td>
            <td>Shen-Hao Wen</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.433210026 37.777489991)</td>
        </tr>
        <tr>
            <td>Nine Months</td>
            <td>1995</td>
            <td>St. Peter &amp; Paul&#x27;s Church (666 Filbert Street, Washington Square)</td>
            <td>Though Marilyn Monroe and Joe DiMaggio were not allowed to be married at the Church (DiMaggio had married his first wife at the Church but was divorced), the couple returned to the steps of the Church for photos, following their City Hall nuptials.</td>
            <td>1492 Pictures</td>
            <td>Twentieth Century Fox Film Corp.</td>
            <td>Chris Columbus</td>
            <td>Chris Columbus</td>
            <td>Hugh Grant</td>
            <td>Julianne Moore</td>
            <td>Robin Williams</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.410437987 37.801430005)</td>
        </tr>
        <tr>
            <td>Sense8</td>
            <td>2015</td>
            <td>Atlas Café, 3049 20th St.</td>
            <td>Dialogue scene inside the café</td>
            <td>Unpronounceable Productions, LLC</td>
            <td>Netflix</td>
            <td>The Wachowskis</td>
            <td>The Wachowskis</td>
            <td>Jamie Clayton</td>
            <td>None</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.411413 37.758937)</td>
        </tr>
        <tr>
            <td>Bullitt</td>
            <td>1968</td>
            <td>2700 Vallejo Street (Pacific Heights)</td>
            <td>None</td>
            <td>Warner Brothers / Seven Arts
<br>Seven Arts</td>
            <td>Warner Brothers</td>
            <td>Peter Yates</td>
            <td>Alan R. Trustman</td>
            <td>Steve McQueen</td>
            <td>Jacqueline Bisset</td>
            <td>Robert Vaughn</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.442026028 37.794603993)</td>
        </tr>
        <tr>
            <td>Summertime</td>
            <td>2015</td>
            <td>Turk St between Lyon and Baker St</td>
            <td>None</td>
            <td>Creative Monster Productions, Inc.</td>
            <td>4 Distribution</td>
            <td>Gabriele Muccino</td>
            <td>Gabriele Muccino</td>
            <td>Jessica Rothe</td>
            <td>Scott Bakula</td>
            <td>Matilda Anna Ingrid Lutz</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.442059974 37.779259997)</td>
        </tr>
        <tr>
            <td>Chance - Season 1 Pilot</td>
            <td>2016</td>
            <td>Washington Square Park</td>
            <td>None</td>
            <td>TVM Productions</td>
            <td>HULU</td>
            <td>Lenny Abrahamson</td>
            <td>Alexandra Cunningham and Kem Nunn</td>
            <td>Hugh Laurie</td>
            <td>Gretchen Mol</td>
            <td>Ethan Suplee</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.41089 37.80051)</td>
        </tr>
        <tr>
            <td>Copycat</td>
            <td>1995</td>
            <td>82 &amp; 67 Rico Way (Marina District)</td>
            <td>None</td>
            <td>Regency Enterprises</td>
            <td>Warner Bros. Pictures</td>
            <td>Jon Amiel</td>
            <td>Ann Biderman</td>
            <td>Sigourney Weaver</td>
            <td>Holly Hunter</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.439788982 37.805006019)</td>
        </tr>
        <tr>
            <td>Clickbait</td>
            <td>2021</td>
            <td>Jackson between Front and Davis</td>
            <td>None</td>
            <td>MasterKey Studios, Inc.</td>
            <td>Netflix</td>
            <td>Brad Anderson, Emma Freeman, Cherie Nowlan, Ben Young</td>
            <td>Tony Ayres, Christian White</td>
            <td>Zoe Kavan</td>
            <td>Betty Gabriel</td>
            <td>Adrian Grenier</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.398329993 37.797080007)</td>
        </tr>
        <tr>
            <td>Sense8 - Season 2</td>
            <td>2016</td>
            <td>67-69 Deming St.</td>
            <td>None</td>
            <td>Unpronounceable Productions, LLC</td>
            <td>Netflix</td>
            <td>Wachowski Siblings</td>
            <td>J. Michael Straczynski, Wachowiski Siblings</td>
            <td>Jamie Clayton</td>
            <td>Daryl Hannah</td>
            <td>Naveen Andrews</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.445766033 37.760332989)</td>
        </tr>
        <tr>
            <td>The Matrix Resurrections</td>
            <td>2021</td>
            <td>Pine between Front and Montgomery</td>
            <td>None</td>
            <td>Adobe Pictures, Inc.</td>
            <td>Warner Brothers</td>
            <td>Lana Wachowski</td>
            <td>Lana Wachowski, David Mitchell, Aleksander Hemon</td>
            <td>Keanu Reeves</td>
            <td>Keanu Reeves</td>
            <td>Neil Patrick Harris</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.40255003 37.791919982)</td>
        </tr>
        <tr>
            <td>Age of Adaline</td>
            <td>2015</td>
            <td>Pier 50- end of the pier</td>
            <td>None</td>
            <td>Lionsgate / Sidney Kimmel Entertainment / Lakeshore Entertainment</td>
            <td>None</td>
            <td>Lee Toland Krieger</td>
            <td>J. Mills Goodloe</td>
            <td>Blake Lively</td>
            <td>Harrison Ford</td>
            <td>Ellen Burstyn</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.383916975 37.773631005)</td>
        </tr>
        <tr>
            <td>Ballers Season 3</td>
            <td>2017</td>
            <td>Huntington Park (California &amp; Taylor Streets, Nob Hill)</td>
            <td>None</td>
            <td>Chori Perros Productions, LLC</td>
            <td>HBO</td>
            <td>Julian Farino</td>
            <td>Stephen Levinson</td>
            <td>Dwayne Johnson</td>
            <td>John David Washington</td>
            <td>Omar Benson Miller</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.412460038 37.791610019)</td>
        </tr>
        <tr>
            <td>God is a Communist?* (show me heart universe)</td>
            <td>2010</td>
            <td>Sacramento &amp; Washington Streets</td>
            <td>None</td>
            <td>Trismegistus Productions</td>
            <td>None</td>
            <td>Jon Poznanter</td>
            <td>Jon Poznanter</td>
            <td>John Wynn</td>
            <td>None</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.422048977 37.793165556)</td>
        </tr>
        <tr>
            <td>Tales of the City</td>
            <td>2019</td>
            <td>Market and Noe St</td>
            <td>None</td>
            <td>Universal Television LLC</td>
            <td>Netflix</td>
            <td>Alan Poul, Silas Howard, Stacie Passon</td>
            <td>Armistead Maupin, Lauren Morelli, Hansol Jung, Marcus Gardley</td>
            <td>Laura Linney</td>
            <td>Ellen Page</td>
            <td>Murray Bartlett</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.433140037 37.764240004)</td>
        </tr>
        <tr>
            <td>Dirty Harry</td>
            <td>1971</td>
            <td>Hall of Justice (850 Bryant Street)</td>
            <td>None</td>
            <td>The Malpaso Company</td>
            <td>Warner Brothers</td>
            <td>Don Siegel</td>
            <td>Harry Julian Fink</td>
            <td>Clint Eastwood</td>
            <td>Harry Guardino</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.404281982 37.775144986)</td>
        </tr>
        <tr>
            <td>Chance- Season 1 ep110</td>
            <td>2016</td>
            <td>18 Urbano</td>
            <td>None</td>
            <td>TVM Productions</td>
            <td>HULU</td>
            <td>Alexandra Cunningham and Kem Nunn</td>
            <td>Michael Lehmann</td>
            <td>Hugh Laurie</td>
            <td>Gretchen Mol</td>
            <td>Ethan Suplee</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.463112968 37.724702986)</td>
        </tr>
        <tr>
            <td>Ballers Season 3</td>
            <td>2017</td>
            <td>Embarcadero around Rincon Park</td>
            <td>None</td>
            <td>Chori Perros Productions, LLC</td>
            <td>HBO</td>
            <td>Julian Farino</td>
            <td>Stephen Levinson</td>
            <td>Dwayne Johnson</td>
            <td>John David Washington</td>
            <td>Omar Benson Miller</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.410722671 37.808306105)</td>
        </tr>
        <tr>
            <td>Bedazzled</td>
            <td>2000</td>
            <td>1155 Filbert Street at Hyde</td>
            <td>None</td>
            <td>Twentieth Century Fox Film Corp.</td>
            <td>Twentieth Century Fox Film Corp.</td>
            <td>Harold Ramis</td>
            <td>Harold Ramis</td>
            <td>Brendan Fraser</td>
            <td>Elizabeth Hurley</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.418469024 37.800035005)</td>
        </tr>
        <tr>
            <td>It Came From Beneath the Sea</td>
            <td>1955</td>
            <td>Golden Gate Bridge</td>
            <td>With 23 miles of ladders and 300,000 rivets in each tower, the Golden Gate Bridge was the world&#x27;s longest span when it opened in 1937.</td>
            <td>Clover Productions</td>
            <td>Columbia Pictures</td>
            <td>Robert Gordon</td>
            <td>George Worthing Yates</td>
            <td>Kenneth Tobey</td>
            <td>Faith Domergue</td>
            <td>Donald Curtis</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.47847 37.81914)</td>
        </tr>
        <tr>
            <td>GirlBoss</td>
            <td>2017</td>
            <td>Mission Thrift, 2330 Mission St.</td>
            <td>None</td>
            <td>Hippolyta Productions, LLC</td>
            <td>Netflix</td>
            <td>Jamie Babbit, Amanda Brotchie, Steven K. Tsuchida, Christian Ditter, John Riggi</td>
            <td>Kay Cannon</td>
            <td>Britt Robertson</td>
            <td>Ellie Reed</td>
            <td>Amanda Rea</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.41957904 37.759416009)</td>
        </tr>
        <tr>
            <td>Dirty Harry</td>
            <td>1971</td>
            <td>St. Peter &amp; Paul&#x27;s Church (666 Filbert Street, Washington Square)</td>
            <td>Though Marilyn Monroe and Joe DiMaggio were not allowed to be married at the Church (DiMaggio had married his first wife at the Church but was divorced), the couple returned to the steps of the Church for photos, following their City Hall nuptials.</td>
            <td>The Malpaso Company</td>
            <td>Warner Brothers</td>
            <td>Don Siegel</td>
            <td>Harry Julian Fink</td>
            <td>Clint Eastwood</td>
            <td>Harry Guardino</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.410437987 37.801430005)</td>
        </tr>
        <tr>
            <td>Cardinal X</td>
            <td>2015</td>
            <td>812 22nd St. and Tennessee</td>
            <td>None</td>
            <td>Fire Horse Film Productions LLC</td>
            <td>None</td>
            <td>Annie Wang</td>
            <td>Annie Wang</td>
            <td>Annie Q</td>
            <td>Francesca Eastwood</td>
            <td>Pierson Fode</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.389249961 37.75789)</td>
        </tr>
        <tr>
            <td>Looking</td>
            <td>2014</td>
            <td>Folsom Street Fair on Folsom St.</td>
            <td>None</td>
            <td>Mission Street Productions, LLC</td>
            <td>Home Box Office (HBO)</td>
            <td>Andrew Haigh</td>
            <td>Michael Lannan</td>
            <td>Jonathan Groff</td>
            <td>Frankie J. Alvarez</td>
            <td>Murray Bartlett</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.393953862 37.787720205)</td>
        </tr>
        <tr>
            <td>Looking Season 2 ep 206</td>
            <td>2015</td>
            <td>770 Haight Street</td>
            <td>None</td>
            <td>Mission Street Productions, LLC</td>
            <td>HBO</td>
            <td>Andrew Haigh</td>
            <td>Michael Lannan</td>
            <td>Jonathan Groff</td>
            <td>Frankie Alvarez</td>
            <td>Murray Bartlett</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.434883976 37.771797002)</td>
        </tr>
        <tr>
            <td>Dim Sum: A Little Bit of Heart</td>
            <td>1985</td>
            <td>San Francisco International Airport</td>
            <td>SFO has a museum dedicated to aviation history.</td>
            <td>CIM</td>
            <td>Orion Classics</td>
            <td>Wayne Wang</td>
            <td>Terrel Seltzer</td>
            <td>Laureen Chew</td>
            <td>Kim Chew</td>
            <td>Victor Wong</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.39169 37.61479)</td>
        </tr>
        <tr>
            <td>Venom</td>
            <td>2018</td>
            <td>Embarcadero at Harrison St</td>
            <td>None</td>
            <td>L.O.Z. Productions, Inc.</td>
            <td>Columbia Pictures, Sony Pictures Releasing</td>
            <td>Ruben Fleischer</td>
            <td>Jeff Pinkner, Scott Rosenberg</td>
            <td>Tom Hardy</td>
            <td>Michelle Wiliams</td>
            <td>Riz Ahmed</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.388610003 37.789500001)</td>
        </tr>
        <tr>
            <td>The Phone/Jexi</td>
            <td>2019</td>
            <td>135 Mississippi St</td>
            <td>None</td>
            <td>CBS Films Inc.</td>
            <td>Lionsgate</td>
            <td>Jon Lucas, Scott Moore</td>
            <td>Jon Lucas, Scott Moore</td>
            <td>Adam Devine</td>
            <td>Alexandra Shipp</td>
            <td>Michael Pena</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.394533997 37.76473198)</td>
        </tr>
        <tr>
            <td>Looking</td>
            <td>2014</td>
            <td>Valencia St. from 16th to 17th</td>
            <td>None</td>
            <td>Mission Street Productions, LLC</td>
            <td>Home Box Office (HBO)</td>
            <td>Andrew Haigh</td>
            <td>Michael Lannan</td>
            <td>Jonathan Groff</td>
            <td>Frankie J. Alvarez</td>
            <td>Murray Bartlett</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.420961108 37.755218654)</td>
        </tr>
        <tr>
            <td>The OA Part II</td>
            <td>2019</td>
            <td>Cameron House - 920 Sacramento St</td>
            <td>None</td>
            <td>Lunar Mining LLC</td>
            <td>Netflix</td>
            <td>Zal Batmanglij</td>
            <td>Zal Batmanglij, Brit Marling</td>
            <td>Brit Marling</td>
            <td>Emory Cohen</td>
            <td>Patrick Gibson</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.408437981 37.793371979)</td>
        </tr>
        <tr>
            <td>Surface</td>
            <td>2022</td>
            <td>Powell Street at Geary</td>
            <td>None</td>
            <td>Apple Studios, LLC</td>
            <td>Apple TV+</td>
            <td>Sam Miller, Kevin Rodney Sullivan, Jennifer Morrison, Tucker Gates</td>
            <td>Veronica West, Erica L. Anderson,Tony Saltzman, Glenise Mullins, Leigh Ann Biety, Dan Lee West, Leigh Ann Biety &amp; Raven Jackson, Martín Zimmerman</td>
            <td>Gugu Mbatha-Raw</td>
            <td>Oliver Jackson-Cohen</td>
            <td>Ari Graynor</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.408209994 37.787360017)</td>
        </tr>
        <tr>
            <td>Time After Time</td>
            <td>1979</td>
            <td>Lombard &amp; Broderick Streets (Marina District)</td>
            <td>None</td>
            <td>Orion Pictures Corp.</td>
            <td>Columbia Broadcasting System (CBS)</td>
            <td>Nicholas Meyer</td>
            <td>Karl Alexander</td>
            <td>Malcolm McDowell</td>
            <td>Mary Steenburgen</td>
            <td>David Warner</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.444329961 37.798800016)</td>
        </tr>
        <tr>
            <td>The Dead Pool</td>
            <td>1988</td>
            <td>San Francisco General Hospital Medical Center (1001 Potrero Avenue, Potrero Hill)</td>
            <td>SF General Hospital is the only Level I Trauma Center serving San Francisco and northern San Mateo County.</td>
            <td>Warner Bros. Pictures</td>
            <td>Warner Bros. Pictures</td>
            <td>Buddy Van Horn</td>
            <td>Harry Julian Fink</td>
            <td>Clint Eastwood</td>
            <td>Liam Neeson</td>
            <td>Patricia Clarkson</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.40523 37.75518)</td>
        </tr>
        <tr>
            <td>Golden Gate</td>
            <td>1994</td>
            <td>University of California Hastings College of the Law</td>
            <td>None</td>
            <td>Metro-Goldwyn-Mayer (MGM)</td>
            <td>Metro-Goldwyn-Mayer (MGM)</td>
            <td>Howard Deutch</td>
            <td>David Henry Hwang</td>
            <td>Matt Dillon</td>
            <td>Joan Chen</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.41554 37.78073)</td>
        </tr>
        <tr>
            <td>Chance- Season 1 ep102</td>
            <td>2016</td>
            <td>Sutter Stockton Garage, 444 Stockton</td>
            <td>None</td>
            <td>TVM Productions</td>
            <td>HULU</td>
            <td>Lenny Abrahamson</td>
            <td>Alexandra Cunningham</td>
            <td>Hugh Laurie</td>
            <td>Gretchen Mol</td>
            <td>Ethan Suplee</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.40648 37.79044)</td>
        </tr>
        <tr>
            <td>Copycat</td>
            <td>1995</td>
            <td>Treasure Island</td>
            <td>An artificial island, Treasure Island was created for the 1939 Golden Gate International Exposition, and is named after the novel by Robert Louis Stevenson, a one-time San Francisco resident.</td>
            <td>Regency Enterprises</td>
            <td>Warner Bros. Pictures</td>
            <td>Jon Amiel</td>
            <td>Ann Biderman</td>
            <td>Sigourney Weaver</td>
            <td>Holly Hunter</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.37087 37.82489)</td>
        </tr>
        <tr>
            <td>Women is Losers</td>
            <td>2020</td>
            <td>26 Edna St</td>
            <td>None</td>
            <td>Look at the Moon Pictures</td>
            <td>None</td>
            <td>Lissette Feliciano</td>
            <td>Lissette Feliciano</td>
            <td>Lorenza Izzo</td>
            <td>Simu Liu</td>
            <td>Liza Weil</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.446353018 37.727060983)</td>
        </tr>
        <tr>
            <td>Steve Jobs</td>
            <td>2015</td>
            <td>California St. from Jones St. to Mason St.</td>
            <td>None</td>
            <td>RDF Productions LLC</td>
            <td>Universal Pictures</td>
            <td>Danny Boyle</td>
            <td>Aaron Sorkin</td>
            <td>Michael Fassbender</td>
            <td>Kate Winslet</td>
            <td>Seth Rogen</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.463695489 37.785102054)</td>
        </tr>
        <tr>
            <td>Nine Months</td>
            <td>1995</td>
            <td>Star&#x27;s Café (55 Golden Gate Avenue at Van Ness)</td>
            <td>None</td>
            <td>1492 Pictures</td>
            <td>Twentieth Century Fox Film Corp.</td>
            <td>Chris Columbus</td>
            <td>Chris Columbus</td>
            <td>Hugh Grant</td>
            <td>Julianne Moore</td>
            <td>Robin Williams</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.420559974 37.781010013)</td>
        </tr>
        <tr>
            <td>Bullitt</td>
            <td>1968</td>
            <td>Kennedy Hotel (226 Embarcadero at Howard Street)</td>
            <td>Hotel was destroyed in the 1989 Loma Prieta earthquake. Corporate headquarters for the Gap reside at the location today.</td>
            <td>Warner Brothers / Seven Arts
<br>Seven Arts</td>
            <td>Warner Brothers</td>
            <td>Peter Yates</td>
            <td>Alan R. Trustman</td>
            <td>Steve McQueen</td>
            <td>Jacqueline Bisset</td>
            <td>Robert Vaughn</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.391200011 37.792329983)</td>
        </tr>
        <tr>
            <td>Final Analysis</td>
            <td>1992</td>
            <td>Westin St. Francis Hotel (335 Powell Street, Union Square)</td>
            <td>The hotel was originally supposed to be named the Crocker Hotel, after Charles Founder the railroad magnate who founded it. However, the hotel took the name the St. Francis after one of the earliest Gold Rush hotels.</td>
            <td>Warner Bros. Pictures</td>
            <td>Warner Bros. Pictures</td>
            <td>Phil Joanou</td>
            <td>Robert Berger</td>
            <td>Richard Gere</td>
            <td>Kim Basinger</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.40833 37.78788)</td>
        </tr>
        <tr>
            <td>I Remember Mama</td>
            <td>1948</td>
            <td>The Ferry Building</td>
            <td>Every hour and half-hour, the clock bell atop the Ferry Building chimes portions of the Westminster Quarters.</td>
            <td>RKO Radio Pictures</td>
            <td>RKO Radio Pictures</td>
            <td>George Stevens</td>
            <td>DeWitt Bodeen</td>
            <td>Irene Dunne</td>
            <td>Barbara Bel Geddes</td>
            <td>Oskar Homolka</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.393945 37.795319996)</td>
        </tr>
        <tr>
            <td>Hemingway &amp; Gelhorn</td>
            <td>2011</td>
            <td>Muni Metro East (501 Cesar Chavez)</td>
            <td>None</td>
            <td>Attaboy Films, For Whom Productions, Home Box Office (HBO)</td>
            <td>Home Box Office (HBO)</td>
            <td>Philip Kaufman</td>
            <td>Jerry Stahl &amp; Barbara Turner</td>
            <td>Nicole Kidman</td>
            <td>Clive Owen</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.382777036 37.750036995)</td>
        </tr>
        <tr>
            <td>Milk</td>
            <td>2008</td>
            <td>Grace Cathedral Episcopal Church (1100 California Street)</td>
            <td>Grace Cathedral Episcopal Church is the West Coast&#x27;s largest Episcopalian cathedral.</td>
            <td>Focus Features</td>
            <td>Focus Features</td>
            <td>Gus Van Sant</td>
            <td>Dustin Lance Black</td>
            <td>Sean Penn</td>
            <td>Emile Hirsch</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.41347 37.79183)</td>
        </tr>
        <tr>
            <td>Sense8</td>
            <td>2015</td>
            <td>Dolores Park, 20th St. between Church &amp; Dolores St.</td>
            <td>group of friends have a heated argument, then flashback of pre-argument</td>
            <td>Unpronounceable Productions, LLC</td>
            <td>Netflix</td>
            <td>The Wachowskis</td>
            <td>The Wachowskis</td>
            <td>Jamie Clayton</td>
            <td>None</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.425296449 37.752457311)</td>
        </tr>
        <tr>
            <td>Looking</td>
            <td>2014</td>
            <td>Jawbone at 99 Rhode Island St.</td>
            <td>None</td>
            <td>Mission Street Productions, LLC</td>
            <td>Home Box Office (HBO)</td>
            <td>Andrew Haigh</td>
            <td>Michael Lannan</td>
            <td>Jonathan Groff</td>
            <td>Frankie J. Alvarez</td>
            <td>Murray Bartlett</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.402485992 37.768911993)</td>
        </tr>
        <tr>
            <td>When We Rise</td>
            <td>2017</td>
            <td>Castro St. between 17th and 18th St.</td>
            <td>None</td>
            <td>Film 49 Productions</td>
            <td>Amercian Broadcasting Company</td>
            <td>Gus Van Sant</td>
            <td>Dustin Lance Black</td>
            <td>Guy Pierce</td>
            <td>Mary-Louise Parker</td>
            <td>Michael Kenneth Williams</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.278570031 37.810609992)</td>
        </tr>
        <tr>
            <td>Goliath- Season 4</td>
            <td>2021</td>
            <td>Mountain Spring Avenue at Glenbrook Avenue</td>
            <td>None</td>
            <td>Picrow, Inc.</td>
            <td>Amazon Studios</td>
            <td>Billy Bob Thornton, Lawrence Trilling, Derek Johansen</td>
            <td>David E. Kelley, Jonathan Shapiro</td>
            <td>Billy Bob Thornton</td>
            <td>Nina Arianda</td>
            <td>Tania Raymonde</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.44953001 37.758189988)</td>
        </tr>
        <tr>
            <td>The Pursuit of Happyness</td>
            <td>2006</td>
            <td>Glide Memorial Church (434 Ellis St)</td>
            <td>None</td>
            <td>Columbia Pictures Corporation</td>
            <td>Columbia Pictures</td>
            <td>Steven Conrad</td>
            <td>Gabriele Muccino</td>
            <td>Will Smith</td>
            <td>Jayden C. Smith</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.41346704 37.785046989)</td>
        </tr>
        <tr>
            <td>Chance- Season 1 ep109</td>
            <td>2016</td>
            <td>850 Bryant- 6th floor County Jail</td>
            <td>The former County Jail on the 6th floor was re-created to resemble a Mexican jail for the scene</td>
            <td>TVM Productions</td>
            <td>HULU</td>
            <td>Sara Gran and Pete Begler</td>
            <td>Dan Attias</td>
            <td>Hugh Laurie</td>
            <td>Gretchen Mol</td>
            <td>Ethan Suplee</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.404281982 37.775144986)</td>
        </tr>
        <tr>
            <td>Super Pumped: The Battle for Uber</td>
            <td>2022</td>
            <td>Alameda St. between Vermont St. &amp; San Bruno Ave.</td>
            <td>None</td>
            <td>Possible Productions</td>
            <td>Showtime</td>
            <td>Allen Coulter, Daniel Gray Longino, John Dahl, Zetna Fuentes</td>
            <td>Brian Koppelman &amp; David Levien, Sarah Acosta, Stephen Schiff, Emily Hornsby, Safie M. Dirie, Beth Schacter</td>
            <td>Joseph Gordon-Levitt</td>
            <td>Kyle Chandler</td>
            <td>Kerry Bishé</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.405759963 37.768499981)</td>
        </tr>
        <tr>
            <td>The Towering Inferno</td>
            <td>1974</td>
            <td>2898 Vallejo Street</td>
            <td>None</td>
            <td>Irwin Allen Productions</td>
            <td>Twentieth Century - Fox</td>
            <td>John Guillermin</td>
            <td>Stirling Silliphant</td>
            <td>Steve McQueen</td>
            <td>Paul Newman</td>
            <td>William Holden</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.444880988 37.79423498)</td>
        </tr>
        <tr>
            <td>Common Threads: Stories From the Quilt</td>
            <td>1989</td>
            <td>The Castro</td>
            <td>From 1910-1920 the Castro was called &quot;Little Scandinavia&quot; because of its high concentration of residents of Scandinavian ancestry.</td>
            <td>Home Box Office (HBO)</td>
            <td>Direct Cinema Limited</td>
            <td>Rob Epstein</td>
            <td>Jeffrey Friedman</td>
            <td>Sara Lewinstein</td>
            <td>David Mandell</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.43486 37.75921)</td>
        </tr>
        <tr>
            <td>Herbie Rides Again</td>
            <td>1974</td>
            <td>Sheraton Palace Hotel (639 Market Street)</td>
            <td>The hotel was destroyed in the 1906 earthquake and fire, had to be rebuilt, and was reopened in 1909.</td>
            <td>Walt Disney Productions</td>
            <td>Buena Vista Distribution</td>
            <td>Robert Stevenson</td>
            <td>Bill Walsh</td>
            <td>Helen Hayes</td>
            <td>Ken Berry</td>
            <td>Stefanie Powers</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.402183833 37.788545667)</td>
        </tr>
        <tr>
            <td>DEVS</td>
            <td>2020</td>
            <td>Corona Heights - 16th at Flint St</td>
            <td>None</td>
            <td>Minim Productions</td>
            <td>FX Network</td>
            <td>Alex Garland</td>
            <td>Alex Garland</td>
            <td>Sonoya Mizuno</td>
            <td>Nick Offerman</td>
            <td>Jin Ha</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.436530014 37.763990014)</td>
        </tr>
        <tr>
            <td>The Net</td>
            <td>1995</td>
            <td>Moscone Convention Center</td>
            <td>None</td>
            <td>Columbia Pictures Corp.</td>
            <td>Columbia Pictures</td>
            <td>Irwin Winkler</td>
            <td>John Brancato</td>
            <td>Sandra Bullock</td>
            <td>Jeremy Northam</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.40053 37.78354)</td>
        </tr>
        <tr>
            <td>Venom: Let There Be Carnage</td>
            <td>2021</td>
            <td>Sutter Stockton Garage</td>
            <td>None</td>
            <td>SM Film Productions</td>
            <td>Sony Pictures</td>
            <td>Andy Serkis</td>
            <td>Kelly Marcel</td>
            <td>Tom Hardy</td>
            <td>Michelle Wiliams</td>
            <td>Woody Harrelson</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.40648 37.79044)</td>
        </tr>
        <tr>
            <td>Terminator - Genisys</td>
            <td>2015</td>
            <td>Embarcadero between Pier 2 and Harrison</td>
            <td>None</td>
            <td>T5 Productions LLC</td>
            <td>Paramount Pictures</td>
            <td>Alan Taylor</td>
            <td>James Cameron</td>
            <td>Arnold Schwarzenegger</td>
            <td>Jason Clarke</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.39517999 37.784330001)</td>
        </tr>
        <tr>
            <td>Ant-Man and the Wasp</td>
            <td>2018</td>
            <td>Saint Louis Alley at Jackson</td>
            <td>None</td>
            <td>PYM Particles Productions II, LLC</td>
            <td>Walt Disney Studios Motion Pictures</td>
            <td>Peyton Reed</td>
            <td>Chris McKenna</td>
            <td>Paul Rudd</td>
            <td>Evangeline Lilly</td>
            <td>Michael Douglas</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.407099978 37.795960017)</td>
        </tr>
        <tr>
            <td>The Presidio</td>
            <td>1988</td>
            <td>Presidio (Golden Gate National Recreation Area)</td>
            <td>In 1776, Spain made the Presidio a fortified area. The area was then given to Mexico, but then given to the US in 1848. The 1994 demilitarization of the area in 1994 marked the end of its 219 years of military use.</td>
            <td>Paramount Pictures</td>
            <td>Paramount Pictures</td>
            <td>Peter Hyams</td>
            <td>Larry Ferguson</td>
            <td>Sean Connery</td>
            <td>Mark Harmon</td>
            <td>Meg Ryan</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.4283 37.80576)</td>
        </tr>
        <tr>
            <td>Ant-Man</td>
            <td>2015</td>
            <td>Intersection of Broadway at Kearney</td>
            <td>Driving shots</td>
            <td>PYM Particles Productions, LLC</td>
            <td>Walt Disney Studios Motion Pictures</td>
            <td>Peyton Reed</td>
            <td>Gabriel Ferrari</td>
            <td>Michael Douglas</td>
            <td>Paul Rudd</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.405489982 37.798019996)</td>
        </tr>
        <tr>
            <td>Murder in the First, Season 3</td>
            <td>2016</td>
            <td>Howard Street at Steuart Street</td>
            <td>None</td>
            <td>Turner North Center Productions</td>
            <td>Turner Network Television (TNT)</td>
            <td>Steven Bochcho</td>
            <td>Eric Lodal</td>
            <td>Taye Diggs</td>
            <td>Kathleen Robertson</td>
            <td>Ian Anthony Dale</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.391639977 37.79202002)</td>
        </tr>
        <tr>
            <td>Surface</td>
            <td>2022</td>
            <td>Jackson Street between Ross and Wentworh</td>
            <td>None</td>
            <td>Apple Studios, LLC</td>
            <td>Apple TV+</td>
            <td>Sam Miller, Kevin Rodney Sullivan, Jennifer Morrison, Tucker Gates</td>
            <td>Veronica West, Erica L. Anderson,Tony Saltzman, Glenise Mullins, Leigh Ann Biety, Dan Lee West, Leigh Ann Biety &amp; Raven Jackson, Martín Zimmerman</td>
            <td>Gugu Mbatha-Raw</td>
            <td>Oliver Jackson-Cohen</td>
            <td>Ari Graynor</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.406219962 37.796069988)</td>
        </tr>
        <tr>
            <td>Cardinal X</td>
            <td>2015</td>
            <td>3639 Taraval St</td>
            <td>None</td>
            <td>Fire Horse Film Productions LLC</td>
            <td>None</td>
            <td>Annie Wang</td>
            <td>Annie Wang</td>
            <td>Annie Q</td>
            <td>Francesca Eastwood</td>
            <td>Pierson Fode</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.505325993 37.741575003)</td>
        </tr>
        <tr>
            <td>Murder in the First, Season 2</td>
            <td>2015</td>
            <td>Columbus Avenue between Washington and Bay Streets</td>
            <td>None</td>
            <td>Turner North Center Productions</td>
            <td>Turner Network Television (TNT)</td>
            <td>Steven Bochcho</td>
            <td>Eric Lodal</td>
            <td>Taye Diggs</td>
            <td>Kathleen Robertson</td>
            <td>Ian Anthony Dale</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-121.959150034 37.532909996)</td>
        </tr>
        <tr>
            <td>The Matrix Resurrections</td>
            <td>2021</td>
            <td>California at Grant Ave</td>
            <td>None</td>
            <td>Adobe Pictures, Inc.</td>
            <td>Warner Brothers</td>
            <td>Lana Wachowski</td>
            <td>Lana Wachowski, David Mitchell, Aleksander Hemon</td>
            <td>Keanu Reeves</td>
            <td>Keanu Reeves</td>
            <td>Neil Patrick Harris</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.405889967 37.792459986)</td>
        </tr>
        <tr>
            <td>The Right Stuff</td>
            <td>1983</td>
            <td>Cow Palace</td>
            <td>Supposedly, the Cow Palace&#x27;s name derives from a newspaper editorial in which the writer wonders whether the soon-to-be-built structure for livestock was a &quot;palace for cows&quot;.</td>
            <td>The Ladd Company</td>
            <td>The Ladd Company</td>
            <td>Philip Kaufman</td>
            <td>Philip Kaufman</td>
            <td>Sam Shepard</td>
            <td>Scott Glenn</td>
            <td>Ed Harris</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.41967 37.70716)</td>
        </tr>
        <tr>
            <td>So I Married an Axe Murderer</td>
            <td>1993</td>
            <td>305 Hugo Street</td>
            <td>None</td>
            <td>TriStar Pictures</td>
            <td>TriStar Pictures</td>
            <td>Thomas Schlamme</td>
            <td>Robbie Fox</td>
            <td>Mike Myers</td>
            <td>Nancy Travis</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.46114589 37.765128612)</td>
        </tr>
        <tr>
            <td>Red Widow</td>
            <td>2013</td>
            <td>California &amp; Davis St</td>
            <td>None</td>
            <td>Beyond Pix</td>
            <td>American Broadcasting Company (ABC)</td>
            <td>Alon Aranya</td>
            <td>Melissa Rosenberg</td>
            <td>Radha Mitchell</td>
            <td>Sterling Beaumon</td>
            <td>Clifton Collins Jr.</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.39763002 37.793500013)</td>
        </tr>
        <tr>
            <td>Venom</td>
            <td>2018</td>
            <td>Larkin St btwn Post and Geary</td>
            <td>None</td>
            <td>L.O.Z. Productions, Inc.</td>
            <td>Columbia Pictures, Sony Pictures Releasing</td>
            <td>Ruben Fleischer</td>
            <td>Jeff Pinkner, Scott Rosenberg</td>
            <td>Tom Hardy</td>
            <td>Michelle Wiliams</td>
            <td>Riz Ahmed</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.418110027 37.786109982)</td>
        </tr>
        <tr>
            <td>Sister Act 2: Back in the Habit</td>
            <td>1993</td>
            <td>St. Peter &amp; Paul&#x27;s Church (666 Filbert Street, Washington Square)</td>
            <td>Though Marilyn Monroe and Joe DiMaggio were not allowed to be married at the Church (DiMaggio had married his first wife at the Church but was divorced), the couple returned to the steps of the Church for photos, following their City Hall nuptials.</td>
            <td>Touchstone Pictures</td>
            <td>Buena Vista Pictures</td>
            <td>Bill Duke</td>
            <td>Joseph Howard</td>
            <td>Whoopi Goldberg</td>
            <td>Maggie Smith</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.410437987 37.801430005)</td>
        </tr>
        <tr>
            <td>Etruscan Smile</td>
            <td>2017</td>
            <td>Treasure Island</td>
            <td>None</td>
            <td>Po Valley Productions, LLC</td>
            <td>TBD</td>
            <td>Oded Binnun/ Michel Brezis</td>
            <td>Sarah Bellwood, Michal Lali Kagan, Michael McGowan Amital Stern, Jose Luis Sampedro</td>
            <td>Brian Cox</td>
            <td>Roseanne Arquette</td>
            <td>Thora Birch</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.37087 37.82489)</td>
        </tr>
        <tr>
            <td>Vertigo</td>
            <td>1958</td>
            <td>San Francisco Drydock (20th and Illinois Streets)</td>
            <td>None</td>
            <td>Alfred J. Hitchcock Productions</td>
            <td>Paramount Pictures</td>
            <td>Alfred Hitchcock</td>
            <td>Alec Coppel</td>
            <td>James Stewart</td>
            <td>Kim Novak</td>
            <td>Barbara Bel Geddes</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.387580035 37.760560013)</td>
        </tr>
        <tr>
            <td>Shang-Chi and the Legend of the Ten Rings</td>
            <td>2021</td>
            <td>Post between Van Ness and Kearny</td>
            <td>None</td>
            <td>Freelance Restorations LLC</td>
            <td>Disney/Marvel</td>
            <td>Destin Daniel Cretton</td>
            <td>Dave Callaham, Destin Daniel Cretton, Andrew Lanham</td>
            <td>Simu Liu</td>
            <td>Tony Chiu-Wai Leung</td>
            <td>Awkwafina</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.403659961 37.788899982)</td>
        </tr>
        <tr>
            <td>The Doors</td>
            <td>1991</td>
            <td>None</td>
            <td>None</td>
            <td>Bill Graham Films</td>
            <td>TriStar Pictures</td>
            <td>Oliver Stone</td>
            <td>J. Randal Johnson</td>
            <td>Val Kilmer</td>
            <td>Meg Ryan</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.41965999999996 37.777120000000025)</td>
        </tr>
        <tr>
            <td>Magnum Force</td>
            <td>1973</td>
            <td>San Francisco International Airport</td>
            <td>SFO has a museum dedicated to aviation history.</td>
            <td>The Malpaso Company</td>
            <td>Warner Bros. Pictures</td>
            <td>Ted Post</td>
            <td>John Milius</td>
            <td>Clint Eastwood</td>
            <td>Hal Holbrook</td>
            <td>Mitchell Ryan</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.39169 37.61479)</td>
        </tr>
        <tr>
            <td>The Game</td>
            <td>1997</td>
            <td>Harrison Street (The Embarcadero)</td>
            <td>None</td>
            <td>Polygram Filmed Entertainment</td>
            <td>Polygram Filmed Entertainment</td>
            <td>David Fincher</td>
            <td>John Brancato</td>
            <td>Michael Douglas</td>
            <td>Sean Penn</td>
            <td>Deborah Kara Unger</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.38837 37.7896)</td>
        </tr>
        <tr>
            <td>The Phone/Jexi</td>
            <td>2019</td>
            <td>3419 16th St</td>
            <td>None</td>
            <td>CBS Films Inc.</td>
            <td>Lionsgate</td>
            <td>Jon Lucas, Scott Moore</td>
            <td>Jon Lucas, Scott Moore</td>
            <td>Adam Devine</td>
            <td>Alexandra Shipp</td>
            <td>Michael Pena</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.429533974 37.764234011)</td>
        </tr>
        <tr>
            <td>Looking Season 2 ep 209</td>
            <td>2015</td>
            <td>Muddy Waters, 521 Valencia Street</td>
            <td>None</td>
            <td>Mission Street Productions, LLC</td>
            <td>HBO</td>
            <td>Andrew Haigh</td>
            <td>Michael Lannan</td>
            <td>Jonathan Groff</td>
            <td>Frankie Alvarez</td>
            <td>Murray Bartlett</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.421581979 37.764504998)</td>
        </tr>
        <tr>
            <td>The Last Thing He Told Me</td>
            <td>2023</td>
            <td>2698 Pacific Avenue</td>
            <td>None</td>
            <td>20th Television</td>
            <td>Apple TV+</td>
            <td>Olivia Newman, Deniz Gamze Ergüven, Daisy Von Scherler Mayer,
<br>Lila Neugebauer</td>
            <td>Laura Dave</td>
            <td>Jennifer Garner</td>
            <td>Angourie Rice</td>
            <td>Aisha Tyler</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.439501985 37.79299999)</td>
        </tr>
        <tr>
            <td>The Diary of a Teenage Girl</td>
            <td>2015</td>
            <td>Ocean Beach at Point Lobos</td>
            <td>None</td>
            <td>Diary the Movie, LLC</td>
            <td>Sony Pictures Classics</td>
            <td>Marielle Heller</td>
            <td>Marielle Heller</td>
            <td>Alexander Skarsgard</td>
            <td>Kristen Wiig</td>
            <td>Christopher Meloni</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.492864995 37.502360012)</td>
        </tr>
        <tr>
            <td>The Phone/Jexi</td>
            <td>2019</td>
            <td>Elixir - 3200 16th St</td>
            <td>None</td>
            <td>CBS Films Inc.</td>
            <td>Lionsgate</td>
            <td>Jon Lucas, Scott Moore</td>
            <td>Jon Lucas, Scott Moore</td>
            <td>Adam Devine</td>
            <td>Alexandra Shipp</td>
            <td>Michael Pena</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.42433 37.764993)</td>
        </tr>
        <tr>
            <td>Venom: Let There Be Carnage</td>
            <td>2021</td>
            <td>238 Columbus</td>
            <td>None</td>
            <td>SM Film Productions</td>
            <td>Sony Pictures</td>
            <td>Andy Serkis</td>
            <td>Kelly Marcel</td>
            <td>Tom Hardy</td>
            <td>Michelle Wiliams</td>
            <td>Woody Harrelson</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.40588278 37.7974432)</td>
        </tr>
        <tr>
            <td>Looking</td>
            <td>2014</td>
            <td>Tiburon Hiking Trail, Tiburon, CA</td>
            <td>None</td>
            <td>Mission Street Productions, LLC</td>
            <td>Home Box Office (HBO)</td>
            <td>Andrew Haigh</td>
            <td>Michael Lannan</td>
            <td>Jonathan Groff</td>
            <td>Frankie J. Alvarez</td>
            <td>Murray Bartlett</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.301192503 37.509261066)</td>
        </tr>
        <tr>
            <td>DEVS</td>
            <td>2020</td>
            <td>Alamo Square Park</td>
            <td>None</td>
            <td>Minim Productions</td>
            <td>FX Network</td>
            <td>Alex Garland</td>
            <td>Alex Garland</td>
            <td>Sonoya Mizuno</td>
            <td>Nick Offerman</td>
            <td>Jin Ha</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.43146 37.77722)</td>
        </tr>
        <tr>
            <td>Patch Adams</td>
            <td>1998</td>
            <td>Treasure Island</td>
            <td>An artificial island, Treasure Island was created for the 1939 Golden Gate International Exposition, and is named after the novel by Robert Louis Stevenson, a one-time San Francisco resident.</td>
            <td>Bungalow 78 Productions</td>
            <td>Universal Pictures</td>
            <td>Tom Shadyac</td>
            <td>Steve Oedekerk</td>
            <td>Robin Williams</td>
            <td>Philip Seymour Hoffman</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.37087 37.82489)</td>
        </tr>
        <tr>
            <td>Blue Jasmine</td>
            <td>2013</td>
            <td>2179 48th Ave</td>
            <td>None</td>
            <td>Perdido Productions</td>
            <td>Sony Pictures Classics</td>
            <td>Woody Allen</td>
            <td>Woody Allen</td>
            <td>Cate Blanchett</td>
            <td>Alec Baldwin</td>
            <td>Peter Sarsgaard</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.507259027 37.745555987)</td>
        </tr>
        <tr>
            <td>Heart and Souls</td>
            <td>1993</td>
            <td>2810 Pacific Avenue</td>
            <td>None</td>
            <td>Universal Pictures</td>
            <td>Electric Parc</td>
            <td>Tomas Gislason</td>
            <td>Tomas Gislason</td>
            <td>Jorgen Leth</td>
            <td>None</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.442088976 37.792703019)</td>
        </tr>
        <tr>
            <td>Junior</td>
            <td>1994</td>
            <td>Postcard Row (Alamo Square, Hayes Valley)</td>
            <td>The 6 Victorian homes across from Alamo Square Park are among the few Victorians to survive the Great Fire.</td>
            <td>Northern Lights Entertainment</td>
            <td>Universal Pictures</td>
            <td>Ivan Reitman</td>
            <td>Kevin Wade</td>
            <td>Arnold Schwarzenegger</td>
            <td>Danny DeVito</td>
            <td>Emma Thompson</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.43146 37.77722)</td>
        </tr>
        <tr>
            <td>Basic Instinct</td>
            <td>1992</td>
            <td>1158-70 Montgomery Street</td>
            <td>None</td>
            <td>Carolco Pictures</td>
            <td>TriStar Pictures</td>
            <td>Paul Verhoeven</td>
            <td>Joe Eszterhas</td>
            <td>Michael Douglas</td>
            <td>Sharon Stone</td>
            <td>George Dzundza</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.40397202 37.799987019)</td>
        </tr>
        <tr>
            <td>Bitter Melon</td>
            <td>2018</td>
            <td>66 Danton St</td>
            <td>None</td>
            <td>Bitter Melon Film LLC/Mammoth Pictures</td>
            <td>ABS-CBN, Gravitas Ventures</td>
            <td>H.P. Mendoza</td>
            <td>H.P. Mendoza</td>
            <td>Jon Norman Schneider</td>
            <td>Patrick Epino</td>
            <td>Brian Rivera</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.432654976 37.731292)</td>
        </tr>
        <tr>
            <td>Chance- Season 1 ep107</td>
            <td>2016</td>
            <td>145 Barlett St.</td>
            <td>None</td>
            <td>TVM Productions</td>
            <td>HULU</td>
            <td>Alexandra Cunningham and Kem Nunn</td>
            <td>Michael Lehmann</td>
            <td>Hugh Laurie</td>
            <td>Gretchen Mol</td>
            <td>Ethan Suplee</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.419537968 37.754663009)</td>
        </tr>
        <tr>
            <td>Budding Prospects, Pilot</td>
            <td>2017</td>
            <td>500 Cortland Avenue</td>
            <td>None</td>
            <td>Picrow Streaming Inc.</td>
            <td>Amazon</td>
            <td>Terry Zwigoff</td>
            <td>Melissa Axelrod, T. C. Boyle (based on the book by)</td>
            <td>Adam Rose</td>
            <td>Will Sasso</td>
            <td>Joel David Moore</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.416142962 37.738855997)</td>
        </tr>
        <tr>
            <td>Dr. Dolittle 2</td>
            <td>2001</td>
            <td>Sacramento St., Between Pierce &amp; Broderick Streets</td>
            <td>None</td>
            <td>Twentieth Century Fox Film Corp.</td>
            <td>Twentieth Century Fox Film Corp.</td>
            <td>Steve Carr</td>
            <td>Larry Levin</td>
            <td>Eddie Murphy</td>
            <td>Kristen Wilson</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.442289974 37.788790012)</td>
        </tr>
        <tr>
            <td>The Last Black Man in San Francisco</td>
            <td>2019</td>
            <td>Shotwell St btwn 20th and 21st St</td>
            <td>None</td>
            <td>LBMISF, LLC</td>
            <td>A41</td>
            <td>Joe Talbot</td>
            <td>Joe Talbot, Jimmie Fails, Rob Richert</td>
            <td>Jimmie Fails</td>
            <td>Jonathan Majors</td>
            <td>Danny Glover</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.383780015 37.759840008)</td>
        </tr>
        <tr>
            <td>San Andreas</td>
            <td>2015</td>
            <td>Water work in SF Bay</td>
            <td>Characters drive in a high speed picture boat to see different views of the city.</td>
            <td>Upside Down Productions, Inc.</td>
            <td>Warner Bros.</td>
            <td>Brad Peyton</td>
            <td>Allan Loeb</td>
            <td>Dwayne Johnson</td>
            <td>None</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.402654 37.767865)</td>
        </tr>
        <tr>
            <td>Blue Jasmine</td>
            <td>2013</td>
            <td>Jones &amp; Pacific</td>
            <td>None</td>
            <td>Perdido Productions</td>
            <td>Sony Pictures Classics</td>
            <td>Woody Allen</td>
            <td>Woody Allen</td>
            <td>Cate Blanchett</td>
            <td>Alec Baldwin</td>
            <td>Peter Sarsgaard</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.415000006 37.795889987)</td>
        </tr>
        <tr>
            <td>Freebie and the Bean</td>
            <td>1974</td>
            <td>Twin Peaks</td>
            <td>The 2nd highest point in SF after Mt. Davidson, Twin Peaks sit at the geographic center of SF. The native Ohlone people called the area &quot;called the area “Los Pechos de la Chola” or &quot;Breasts of the Indian Maiden,&quot; but in the 19th Century when America took over the area, it was renamed &quot;Twin Peaks&quot;.</td>
            <td>Warner Bros. Pictures</td>
            <td>American Broadcasting Company (ABC)</td>
            <td>Richard Rush</td>
            <td>Robert Kaufman</td>
            <td>Alan Arkin</td>
            <td>James Caan</td>
            <td>Loretta Swit</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.44224 37.75669)</td>
        </tr>
        <tr>
            <td>Looking Season 2 ep 204</td>
            <td>2015</td>
            <td>Urban Flowers, 4029 18th Street</td>
            <td>None</td>
            <td>Mission Street Productions, LLC</td>
            <td>HBO</td>
            <td>Andrew Haigh</td>
            <td>Michael Lannan</td>
            <td>Jonathan Groff</td>
            <td>Frankie Alvarez</td>
            <td>Murray Bartlett</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.433364 37.760813)</td>
        </tr>
        <tr>
            <td>Looking &quot...(truncated)


### We want to count the number of locations of the films. But we also want to restrict the output result set so that we only retrieve the number of locations of the films written by a certain writer

```sql
%%sql
SELECT COUNT(Locations) FROM FilmLocations WHERE Writer="James Cameron";
```
<table>
    <thead>
        <tr>
            <th>COUNT(Locations)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>24</td>
        </tr>
    </tbody>
</table>

## Using DISTINCT statement

### Assume that we want to retrieve the titles of all films in the table so that duplicates will be discarded in the output result set

```sql
%%sql
SELECT DISTINCT Title FROM FilmLocations;
```

<table>
    <thead>
        <tr>
            <th>title</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Nash Bridges</td>
        </tr>
        <tr>
            <td>The OA Part II</td>
        </tr>
        <tr>
            <td>Looking &quot;Special&quot;</td>
        </tr>
        <tr>
            <td>The Phone/Jexi</td>
        </tr>
        <tr>
            <td>Terminator - Genisys</td>
        </tr>
        <tr>
            <td>Murder in the First, Season 3</td>
        </tr>
        <tr>
            <td>Ant-Man and the Wasp</td>
        </tr>
        <tr>
            <td>Dirty Harry</td>
        </tr>
        <tr>
            <td>40 Days and 40 Nights</td>
        </tr>
        <tr>
            <td>Harold and Maude</td>
        </tr>
        <tr>
            <td>Time After Time</td>
        </tr>
        <tr>
            <td>Quitters</td>
        </tr>
        <tr>
            <td>The Dead Pool</td>
        </tr>
        <tr>
            <td>The Princess Diaries</td>
        </tr>
        <tr>
            <td>Murder in the First, Season 1</td>
        </tr>
        <tr>
            <td>Junior</td>
        </tr>
        <tr>
            <td>The Woman In Red</td>
        </tr>
        <tr>
            <td>The Bachelor</td>
        </tr>
        <tr>
            <td>Final Analysis</td>
        </tr>
        <tr>
            <td>Women is Losers</td>
        </tr>
        <tr>
            <td>Rent</td>
        </tr>
        <tr>
            <td>The Last Black Man in San Francisco</td>
        </tr>
        <tr>
            <td>Smile Again, Jenny Lee</td>
        </tr>
        <tr>
            <td>Sense8</td>
        </tr>
        <tr>
            <td>Tucker: The Man and His Dream</td>
        </tr>
        <tr>
            <td>Tales of the City</td>
        </tr>
        <tr>
            <td>Nine to Five</td>
        </tr>
        <tr>
            <td>Shit and Champagne</td>
        </tr>
        <tr>
            <td>Ant-Man</td>
        </tr>
        <tr>
            <td>Pacific Heights</td>
        </tr>
        <tr>
            <td>Interview With The Vampire</td>
        </tr>
        <tr>
            <td>Bitter Melon</td>
        </tr>
        <tr>
            <td>Chance Season 2</td>
        </tr>
        <tr>
            <td>Dawn of the Planet of the Apes</td>
        </tr>
        <tr>
            <td>Hulk</td>
        </tr>
        <tr>
            <td>Venom</td>
        </tr>
        <tr>
            <td>Surface</td>
        </tr>
        <tr>
            <td>Sudden Impact</td>
        </tr>
        <tr>
            <td>Looking Season 2 ep 204</td>
        </tr>
        <tr>
            <td>Etruscan Smile</td>
        </tr>
        <tr>
            <td>Summertime</td>
        </tr>
        <tr>
            <td>Always Be My Maybe</td>
        </tr>
        <tr>
            <td>San Andreas</td>
        </tr>
        <tr>
            <td>Birth of the Dragon</td>
        </tr>
        <tr>
            <td>The Rock</td>
        </tr>
        <tr>
            <td>So I Married an Axe Murderer</td>
        </tr>
        <tr>
            <td>Blue Jasmine</td>
        </tr>
        <tr>
            <td>The Maltese Falcon</td>
        </tr>
        <tr>
            <td>Chance- Season 1 ep106</td>
        </tr>
        <tr>
            <td>Chance - Season 1 Pilot</td>
        </tr>
        <tr>
            <td>Goliath- Season 4</td>
        </tr>
        <tr>
            <td>Groove</td>
        </tr>
        <tr>
            <td>Heart Beat</td>
        </tr>
        <tr>
            <td>DEVS</td>
        </tr>
        <tr>
            <td>Edtv</td>
        </tr>
        <tr>
            <td>Looking Season 2 ep 207</td>
        </tr>
        <tr>
            <td>Flubber</td>
        </tr>
        <tr>
            <td>A Taiwanese Tale of Two Cities</td>
        </tr>
        <tr>
            <td>Nine Months</td>
        </tr>
        <tr>
            <td>Bullitt</td>
        </tr>
        <tr>
            <td>Copycat</td>
        </tr>
        <tr>
            <td>Clickbait</td>
        </tr>
        <tr>
            <td>Sense8 - Season 2</td>
        </tr>
        <tr>
            <td>The Matrix Resurrections</td>
        </tr>
        <tr>
            <td>Age of Adaline</td>
        </tr>
        <tr>
            <td>Ballers Season 3</td>
        </tr>
        <tr>
            <td>God is a Communist?* (show me heart universe)</td>
        </tr>
        <tr>
            <td>Chance- Season 1 ep110</td>
        </tr>
        <tr>
            <td>Bedazzled</td>
        </tr>
        <tr>
            <td>It Came From Beneath the Sea</td>
        </tr>
        <tr>
            <td>GirlBoss</td>
        </tr>
        <tr>
            <td>Cardinal X</td>
        </tr>
        <tr>
            <td>Looking</td>
        </tr>
        <tr>
            <td>Looking Season 2 ep 206</td>
        </tr>
        <tr>
            <td>Dim Sum: A Little Bit of Heart</td>
        </tr>
        <tr>
            <td>Golden Gate</td>
        </tr>
        <tr>
            <td>Chance- Season 1 ep102</td>
        </tr>
        <tr>
            <td>Steve Jobs</td>
        </tr>
        <tr>
            <td>I Remember Mama</td>
        </tr>
        <tr>
            <td>Hemingway &amp; Gelhorn</td>
        </tr>
        <tr>
            <td>Milk</td>
        </tr>
        <tr>
            <td>When We Rise</td>
        </tr>
        <tr>
            <td>The Pursuit of Happyness</td>
        </tr>
        <tr>
            <td>Chance- Season 1 ep109</td>
        </tr>
        <tr>
            <td>Super Pumped: The Battle for Uber</td>
        </tr>
        <tr>
            <td>The Towering Inferno</td>
        </tr>
        <tr>
            <td>Common Threads: Stories From the Quilt</td>
        </tr>
        <tr>
            <td>Herbie Rides Again</td>
        </tr>
        <tr>
            <td>The Net</td>
        </tr>
        <tr>
            <td>Venom: Let There Be Carnage</td>
        </tr>
        <tr>
            <td>The Presidio</td>
        </tr>
        <tr>
            <td>Murder in the First, Season 2</td>
        </tr>
        <tr>
            <td>The Right Stuff</td>
        </tr>
        <tr>
            <td>Red Widow</td>
        </tr>
        <tr>
            <td>Sister Act 2: Back in the Habit</td>
        </tr>
        <tr>
            <td>Vertigo</td>
        </tr>
        <tr>
            <td>Shang-Chi and the Legend of the Ten Rings</td>
        </tr>
        <tr>
            <td>The Doors</td>
        </tr>
        <tr>
            <td>Magnum Force</td>
        </tr>
        <tr>
            <td>The Game</td>
        </tr>
        <tr>
            <td>Looking Season 2 ep 209</td>
        </tr>
        <tr>
            <td>The Last Thing He Told Me</td>
        </tr>
        <tr>
            <td>The Diary of a Teenage Girl</td>
        </tr>
        <tr>
            <td>Patch Adams</td>
        </tr>
        <tr>
            <td>Heart and Souls</td>
        </tr>
        <tr>
            <td>Basic Instinct</td>
        </tr>
        <tr>
            <td>Chance- Season 1 ep107</td>
        </tr>
        <tr>
            <td>Budding Prospects, Pilot</td>
        </tr>
        <tr>
            <td>Dr. Dolittle 2</td>
        </tr>
        <tr>
            <td>Freebie and the Bean</td>
        </tr>
        <tr>
            <td>Flower Drum Song</td>
        </tr>
        <tr>
            <td>Chance- Season 1 ep104</td>
        </tr>
        <tr>
            <td>Hard to Hold</td>
        </tr>
        <tr>
            <td>The Bridge</td>
        </tr>
        <tr>
            <td>Sonic the Hedgehog</td>
        </tr>
        <tr>
            <td>I’m A Virgo</td>
        </tr>
        <tr>
            <td>Sweet November</td>
        </tr>
        <tr>
            <td>Looking Season 2 ep 202</td>
        </tr>
        <tr>
            <td>When a Man Loves a Woman</td>
        </tr>
        <tr>
            <td>Godzilla</td>
        </tr>
        <tr>
            <td>Swing</td>
        </tr>
        <tr>
            <td>Chance- Season 1 ep103</td>
        </tr>
        <tr>
            <td>Fearless</td>
        </tr>
        <tr>
            <td>Pushing Dead</td>
        </tr>
        <tr>
            <td>Live Nude Girls Unite</td>
        </tr>
        <tr>
            <td>The Lady from Shanghai</td>
        </tr>
        <tr>
            <td>Invasion of the Body Snatchers</td>
        </tr>
        <tr>
            <td>Americana</td>
        </tr>
        <tr>
            <td>Alexander&#x27;s Ragtime Band</td>
        </tr>
        <tr>
            <td>Big Eyes</td>
        </tr>
        <tr>
            <td>I Am Michael</td>
        </tr>
        <tr>
            <td>The Enforcer</td>
        </tr>
        <tr>
            <td>Petulia</td>
        </tr>
        <tr>
            <td>A Smile Like Yours</td>
        </tr>
        <tr>
            <td>Jagged Edge</td>
        </tr>
        <tr>
            <td>Play it Again, Sam</td>
        </tr>
        <tr>
            <td>Woman on the Run</td>
        </tr>
        <tr>
            <td>Experiment in Terror</td>
        </tr>
        <tr>
            <td>Happy Gilmore</td>
        </tr>
        <tr>
            <td>Star Trek IV: The Voyage Home</td>
        </tr>
        <tr>
            <td>They Call Me MISTER Tibbs</td>
        </tr>
        <tr>
            <td>Patty Hearst</td>
        </tr>
        <tr>
            <td>The Wedding Planner</td>
        </tr>
        <tr>
            <td>San Francisco</td>
        </tr>
        <tr>
            <td>My Big Fat Chinese Christmas</td>
        </tr>
        <tr>
            <td>Pal Joey</td>
        </tr>
        <tr>
            <td>Getting Even with Dad</td>
        </tr>
        <tr>
            <td>Foul Play</td>
        </tr>
        <tr>
            <td>A View to a Kill</td>
        </tr>
        <tr>
            <td>The Conversation</td>
        </tr>
        <tr>
            <td>Vegas in Space</td>
        </tr>
        <tr>
            <td>Ant-Man and the Wasp: Quantumania</td>
        </tr>
        <tr>
            <td>Dying Young</td>
        </tr>
        <tr>
            <td>Haiku Tunnel</td>
        </tr>
        <tr>
            <td>Twisted</td>
        </tr>
        <tr>
            <td>Doctor Dolittle</td>
        </tr>
        <tr>
            <td>48 Hours</td>
        </tr>
        <tr>
            <td>Mrs. Doubtfire</td>
        </tr>
        <tr>
            <td>The Lineup</td>
        </tr>
        <tr>
            <td>Need For Speed</td>
        </tr>
        <tr>
            <td>Looking Season 2 ep 210</td>
        </tr>
        <tr>
            <td>Rollerball</td>
        </tr>
        <tr>
            <td>Looking Season 2 ep 203</td>
        </tr>
        <tr>
            <td>Alive</td>
        </tr>
        <tr>
            <td>Looking Season 2 ep 205</td>
        </tr>
        <tr>
            <td>Chance - Season 1 ep105</td>
        </tr>
        <tr>
            <td>The Last of the Gladiators</td>
        </tr>
        <tr>
            <td>Burglar</td>
        </tr>
        <tr>
            <td>Dark Passage</td>
        </tr>
        <tr>
            <td>Take the Money and Run</td>
        </tr>
        <tr>
            <td>What the Bleep Do We Know</td>
        </tr>
        <tr>
            <td>High Anxiety</td>
        </tr>
        <tr>
            <td>D.O.A</td>
        </tr>
        <tr>
            <td>Beautiful Boy</td>
        </tr>
        <tr>
            <td>50 First Dates</td>
        </tr>
        <tr>
            <td>Alcatraz</td>
        </tr>
        <tr>
            <td>Looking Season 2 ep 208</td>
        </tr>
        <tr>
            <td>Hereafter</td>
        </tr>
        <tr>
            <td>Jade</td>
        </tr>
        <tr>
            <td>Boys and Girls</td>
        </tr>
        <tr>
            <td>Pleasure of His Company</td>
        </tr>
        <tr>
            <td>All About Eve</td>
        </tr>
        <tr>
            <td>Guess Who&#x27;s Coming to Dinner</td>
        </tr>
        <tr>
            <td>The Sweetest Thing</td>
        </tr>
        <tr>
            <td>The Competition</td>
        </tr>
        <tr>
            <td>Sneakers</td>
        </tr>
        <tr>
            <td>A Night Full of Rain</td>
        </tr>
        <tr>
            <td>What&#x27;s Up Doc?</td>
        </tr>
        <tr>
            <td>Pretty Woman</td>
        </tr>
        <tr>
            <td>Serendipity</td>
        </tr>
        <tr>
            <td>James and the Giant Peach</td>
        </tr>
        <tr>
            <td>Bicentennial Man</td>
        </tr>
        <tr>
            <td>Chef Dynasty: House of Fang</td>
        </tr>
        <tr>
            <td>High Crimes</td>
        </tr>
        <tr>
            <td>On the Road</td>
        </tr>
        <tr>
            <td>Innerspace</td>
        </tr>
        <tr>
            <td>This Is Us</td>
        </tr>
        <tr>
            <td>Kamikaze Hearts</td>
        </tr>
        <tr>
            <td>Night of Henna</td>
        </tr>
        <tr>
            <td>Casualties of War</td>
        </tr>
        <tr>
            <td>Joy Luck Club</td>
        </tr>
        <tr>
            <td>The Matrix</td>
        </tr>
        <tr>
            <td>The Assassination of Richard Nixon</td>
        </tr>
        <tr>
            <td>Point Blank</td>
        </tr>
        <tr>
            <td>American Graffiti</td>
        </tr>
        <tr>
            <td>The Caine Mutiny</td>
        </tr>
        <tr>
            <td>The House on Telegraph Hill</td>
        </tr>
        <tr>
            <td>Sphere</td>
        </tr>
        <tr>
            <td>180</td>
        </tr>
        <tr>
            <td>The Times of Harvey Milk</td>
        </tr>
        <tr>
            <td>Birdman of Alcatraz</td>
        </tr>
        <tr>
            <td>Family Plot</td>
        </tr>
        <tr>
            <td>Dopamine</td>
        </tr>
        <tr>
            <td>The Birds</td>
        </tr>
        <tr>
            <td>Another 48 Hours</td>
        </tr>
        <tr>
            <td>Chance - Season 1ep105</td>
        </tr>
        <tr>
            <td>The Internship</td>
        </tr>
        <tr>
            <td>Superman</td>
        </tr>
        <tr>
            <td>George of the Jungle</td>
        </tr>
        <tr>
            <td>Chance- Season 1 ep108</td>
        </tr>
        <tr>
            <td>The Fan</td>
        </tr>
        <tr>
            <td>By Hook or By Crook</td>
        </tr>
        <tr>
            <td>Seven Girlfriends</td>
        </tr>
        <tr>
            <td>Love &amp; Taxes</td>
        </tr>
        <tr>
            <td>Swingin&#x27; Along</td>
        </tr>
        <tr>
            <td>CSI: NY- episode 903</td>
        </tr>
        <tr>
            <td>Marnie</td>
        </tr>
        <tr>
            <td>Serial</td>
        </tr>
        <tr>
            <td>Sausalito</td>
        </tr>
        <tr>
            <td>Class Action</td>
        </tr>
        <tr>
            <td>Mother</td>
        </tr>
        <tr>
            <td>Desperate Measures</td>
        </tr>
        <tr>
            <td>Bee Season</td>
        </tr>
        <tr>
            <td>Maxie</td>
        </tr>
        <tr>
            <td>Dream with the Fishes</td>
        </tr>
        <tr>
            <td>Parks and Recreation</td>
        </tr>
        <tr>
            <td>Memoirs of an Invisible Man</td>
        </tr>
        <tr>
            <td>Chu Chu and the Philly Flash</td>
        </tr>
        <tr>
            <td>Cherish</td>
        </tr>
        <tr>
            <td>A Jitney Elopement</td>
        </tr>
        <tr>
            <td>About a Boy</td>
        </tr>
        <tr>
            <td>Homeward Bound II: Lost in San Francisco</td>
        </tr>
        <tr>
            <td>House of Sand and Fog</td>
        </tr>
        <tr>
            <td>Knife Fight</td>
        </tr>
        <tr>
            <td>Mission (aka City of Bars)</td>
        </tr>
        <tr>
            <td>Blindspotting (Season 2)</td>
        </tr>
        <tr>
            <td>The Nightmare Before Christmas</td>
        </tr>
        <tr>
            <td>Nina Takes a Lover</td>
        </tr>
        <tr>
            <td>Metro</td>
        </tr>
        <tr>
            <td>Romeo Must Die</td>
        </tr>
        <tr>
            <td>The Love Bug</td>
        </tr>
        <tr>
            <td>Gentleman Jim</td>
        </tr>
        <tr>
            <td>To the Ends of the Earth</td>
        </tr>
        <tr>
            <td>Sudden Fear</td>
        </tr>
        <tr>
            <td>American Yearbook</td>
        </tr>
        <tr>
            <td>The Candidate</td>
        </tr>
        <tr>
            <td>After the Thin Man</td>
        </tr>
        <tr>
            <td>Tweek City</td>
        </tr>
        <tr>
            <td>Fat Man and Little Boy</td>
        </tr>
        <tr>
            <td>Star Trek II : The Wrath of Khan</td>
        </tr>
        <tr>
            <td>Silicon Valley Season 4</td>
        </tr>
        <tr>
            <td>Broken-A Modern Love Story</td>
        </tr>
        <tr>
            <td>Big Sur</td>
        </tr>
        <tr>
            <td>Julie and Jack</td>
        </tr>
        <tr>
            <td>Dream for an Insomniac</td>
        </tr>
        <tr>
            <td>Street Music</td>
        </tr>
        <tr>
            <td>Crackers</td>
        </tr>
        <tr>
            <td>The Fog of War</td>
        </tr>
        <tr>
            <td>Midnight Lace</td>
        </tr>
        <tr>
            <td>The Other Sister</td>
        </tr>
        <tr>
            <td>Until the End of the World</td>
        </tr>
        <tr>
            <td>Zodiac</td>
        </tr>
        <tr>
            <td>Panther</td>
        </tr>
        <tr>
            <td>Susan Slade</td>
        </tr>
        <tr>
            <td>Big Trouble in Little China</td>
        </tr>
        <tr>
            <td>Sister Act</td>
        </tr>
        <tr>
            <td>Yours, Mine and Ours</td>
        </tr>
        <tr>
            <td>Thief of Hearts</td>
        </tr>
        <tr>
            <td>Tin Cup</td>
        </tr>
        <tr>
            <td>Days of Wine and Roses</td>
        </tr>
        <tr>
            <td>Mona Lisa Smile</td>
        </tr>
        <tr>
            <td>Playing Mona Lisa</td>
        </tr>
        <tr>
            <td>Good NeighborSam</td>
        </tr>
        <tr>
            <td>Woman on Top</td>
        </tr>
        <tr>
            <td>24 Hours on Craigslist</td>
        </tr>
        <tr>
            <td>Greed</td>
        </tr>
        <tr>
            <td>Escape From Alcatraz</td>
        </tr>
        <tr>
            <td>Down Periscope</td>
        </tr>
        <tr>
            <td>Shattered</td>
        </tr>
        <tr>
            <td>Chan is Missing</td>
        </tr>
        <tr>
            <td>True Believer</td>
        </tr>
        <tr>
            <td>The Doctor</td>
        </tr>
        <tr>
            <td>Fathers&#x27; Day</td>
        </tr>
        <tr>
            <td>Attack of the Killer Tomatoes</td>
        </tr>
        <tr>
            <td>Around the Fire</td>
        </tr>
        <tr>
            <td>Babies</td>
        </tr>
        <tr>
            <td>Just One Night</td>
        </tr>
        <tr>
            <td>Stigmata</td>
        </tr>
        <tr>
            <td>The Californians</td>
        </tr>
        <tr>
            <td>Nora Prentiss</td>
        </tr>
        <tr>
            <td>The Organization</td>
        </tr>
        <tr>
            <td>Raising Cain</td>
        </tr>
        <tr>
            <td>Just Like Heaven</td>
        </tr>
        <tr>
            <td>Confessions of a Burning Man</td>
        </tr>
        <tr>
            <td>Under the Tuscan Sun</td>
        </tr>
        <tr>
            <td>Forrest Gump</td>
        </tr>
        <tr>
            <td>Phenomenon</td>
        </tr>
        <tr>
            <td>The Jazz Singer</td>
        </tr>
        <tr>
            <td>Beaches</td>
        </tr>
        <tr>
            <td>The Laughing Policeman</td>
        </tr>
        <tr>
            <td>Psych-Out</td>
        </tr>
        <tr>
            <td>Red Diaper Baby</td>
        </tr>
        <tr>
            <td>Star Trek VI: The Undiscovered Country</td>
        </tr>
        <tr>
            <td>Never Die Twice</td>
        </tr>
        <tr>
            <td>How Stella Got Her Groove Back</td>
        </tr>
        <tr>
            <td>Jack</td>
        </tr>
        <tr>
            <td>I&#x27;s</td>
        </tr>
        <tr>
            <td>The Parent Trap</td>
        </tr>
        <tr>
            <td>The Graduate</td>
        </tr>
        <tr>
            <td>Quicksilver</td>
        </tr>
        <tr>
            <td>The Ten Commandments</td>
        </tr>
        <tr>
            <td>Can&#x27;t Stop the Music</td>
        </tr>
        <tr>
            <td>City of Angels</td>
        </tr>
        <tr>
            <td>Faces of Death</td>
        </tr>
        <tr>
            <td>On the Beach</td>
        </tr>
        <tr>
            <td>Earth Mama</td>
        </tr>
        <tr>
            <td>Shoot the Moon</td>
        </tr>
        <tr>
            <td>Shadow of the Thin Man</td>
        </tr>
        <tr>
            <td>Fandom</td>
        </tr>
        <tr>
            <td>What Dreams May Come</td>
        </tr>
        <tr>
            <td>Barbary Coast</td>
        </tr>
        <tr>
            <td>The Core</td>
        </tr>
        <tr>
            <td>Hello Frisco, Hello</td>
        </tr>
        <tr>
            <td>Indiana Jones and the Last Crusade</td>
        </tr>
        <tr>
            <td>The Master</td>
        </tr>
        <tr>
            <td>The Zodiac</td>
        </tr>
    </tbody>
</table>

## Using LIMIT statement
### Retrieve only the first 25 rows from the table so that rows other than those are not in the output result set.

```sql
%%sql 
SELECT * FROM FilmLocations LIMIT 25;
```

<table>
    <thead>
        <tr>
            <th>title</th>
            <th>release_year</th>
            <th>locations</th>
            <th>fun_facts</th>
            <th>production_company</th>
            <th>distributor</th>
            <th>director</th>
            <th>writer</th>
            <th>actor_1</th>
            <th>actor_2</th>
            <th>actor_3</th>
            <th>state</th>
            <th>city</th>
            <th>point</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Nash Bridges</td>
            <td>2021</td>
            <td>Pier 45, San Francisco</td>
            <td>None</td>
            <td>Village NB Productions, LLC</td>
            <td>USA Nework</td>
            <td>Greg Beeman</td>
            <td>Carlton Cuse, Bill Chais</td>
            <td>Don Johnson</td>
            <td>Cheech Marin</td>
            <td>Joe Dinicol</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.417428501 37.809873676)</td>
        </tr>
        <tr>
            <td>The OA Part II</td>
            <td>2019</td>
            <td>Ada Court at O&#x27;Farrell St</td>
            <td>None</td>
            <td>Lunar Mining LLC</td>
            <td>Netflix</td>
            <td>Zal Batmanglij</td>
            <td>Zal Batmanglij, Brit Marling</td>
            <td>Brit Marling</td>
            <td>Emory Cohen</td>
            <td>Patrick Gibson</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.41568003 37.785469982)</td>
        </tr>
        <tr>
            <td>Looking &quot;Special&quot;</td>
            <td>2016</td>
            <td>1246 Folsom Street</td>
            <td>None</td>
            <td>Mission Street Productions, LLC</td>
            <td>HBO</td>
            <td>Andrew Haigh</td>
            <td>Michael Lannan</td>
            <td>Jonathan Groff</td>
            <td>Frankie Alvarez</td>
            <td>Murray Bartlett</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.411002006 37.774595007)</td>
        </tr>
        <tr>
            <td>The Phone/Jexi</td>
            <td>2019</td>
            <td>Liberty St btwn Castro and Noe St</td>
            <td>None</td>
            <td>CBS Films Inc.</td>
            <td>Lionsgate</td>
            <td>Jon Lucas, Scott Moore</td>
            <td>Jon Lucas, Scott Moore</td>
            <td>Adam Devine</td>
            <td>Alexandra Shipp</td>
            <td>Michael Pena</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.432399999 37.75702)</td>
        </tr>
        <tr>
            <td>Terminator - Genisys</td>
            <td>2015</td>
            <td>California at Larkin</td>
            <td>None</td>
            <td>T5 Productions LLC</td>
            <td>Paramount Pictures</td>
            <td>Alan Taylor</td>
            <td>James Cameron</td>
            <td>Arnold Schwarzenegger</td>
            <td>Jason Clarke</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.419039999 37.790790018)</td>
        </tr>
        <tr>
            <td>Murder in the First, Season 3</td>
            <td>2016</td>
            <td>600 Octavia Street</td>
            <td>None</td>
            <td>Turner North Center Productions</td>
            <td>Turner Network Television (TNT)</td>
            <td>Steven Bochcho</td>
            <td>Eric Lodal</td>
            <td>Taye Diggs</td>
            <td>Kathleen Robertson</td>
            <td>Ian Anthony Dale</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.424684038 37.777814999)</td>
        </tr>
        <tr>
            <td>Ant-Man and the Wasp</td>
            <td>2018</td>
            <td>Bush St at Mason St</td>
            <td>VFX Plate Shots</td>
            <td>PYM Particles Productions II, LLC</td>
            <td>Walt Disney Studios Motion Pictures</td>
            <td>Peyton Reed</td>
            <td>Chris McKenna</td>
            <td>Paul Rudd</td>
            <td>Evangeline Lilly</td>
            <td>Michael Douglas</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.410430025 37.78996)</td>
        </tr>
        <tr>
            <td>Dirty Harry</td>
            <td>1971</td>
            <td>Portsmouth Square (Chinatown)</td>
            <td>In 1847 the first public school in California was erected on what would become Portsmouth Square.</td>
            <td>The Malpaso Company</td>
            <td>Warner Brothers</td>
            <td>Don Siegel</td>
            <td>Harry Julian Fink</td>
            <td>Clint Eastwood</td>
            <td>Harry Guardino</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.40571 37.79479)</td>
        </tr>
        <tr>
            <td>40 Days and 40 Nights</td>
            <td>2002</td>
            <td>Café Trieste (609 Vallejo)</td>
            <td>Francis Ford Coppola allegedly wrote large portions of &quot;The Godfather&quot; trilogy in Café Trieste.</td>
            <td>Miramax Films</td>
            <td>Miramax Films</td>
            <td>Michael Lehmann</td>
            <td>Robert Perez</td>
            <td>Josh Hartnett</td>
            <td>Shaynnyn Sossamon</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.407357973 37.798572992)</td>
        </tr>
        <tr>
            <td>Harold and Maude</td>
            <td>1971</td>
            <td>Sutro Baths (Point Lobos Avenue)</td>
            <td>None</td>
            <td>Mildred Lewis and Colin Higgins Productions</td>
            <td>Paramount Pictures</td>
            <td>Hal Ashby</td>
            <td>Colin Higgins</td>
            <td>Ruth Gordon</td>
            <td>Bud Cort</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.510031794 37.779832009)</td>
        </tr>
        <tr>
            <td>Time After Time</td>
            <td>1979</td>
            <td>Palace of Fine Arts (3301 Lyon Street)</td>
            <td>The original Palace was built for the 1915 Panama-Pacific Exposition, and completely destroyed in 1964. It was rebuilt in 1965.</td>
            <td>Orion Pictures Corp.</td>
            <td>Columbia Broadcasting System (CBS)</td>
            <td>Nicholas Meyer</td>
            <td>Karl Alexander</td>
            <td>Malcolm McDowell</td>
            <td>Mary Steenburgen</td>
            <td>David Warner</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.44899 37.80288)</td>
        </tr>
        <tr>
            <td>Quitters</td>
            <td>2015</td>
            <td>Claire Lilienthal Elementary School</td>
            <td>None</td>
            <td>Frederick &amp; Ashbury, LLC.</td>
            <td>None</td>
            <td>Noah Pritzker</td>
            <td>Noah Pritzker</td>
            <td>Kara Hayward</td>
            <td>Mira Sorvino</td>
            <td>Saffron Burrows</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.45796 37.7871)</td>
        </tr>
        <tr>
            <td>Quitters</td>
            <td>2015</td>
            <td>1536 Noe St.</td>
            <td>None</td>
            <td>Frederick &amp; Ashbury, LLC.</td>
            <td>None</td>
            <td>Noah Pritzker</td>
            <td>Noah Pritzker</td>
            <td>Kara Hayward</td>
            <td>Mira Sorvino</td>
            <td>Saffron Burrows</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.431454017 37.744473004)</td>
        </tr>
        <tr>
            <td>The Dead Pool</td>
            <td>1988</td>
            <td>550 El Camino Del Mar (Seacliff)</td>
            <td>None</td>
            <td>Warner Bros. Pictures</td>
            <td>Warner Bros. Pictures</td>
            <td>Buddy Van Horn</td>
            <td>Harry Julian Fink</td>
            <td>Clint Eastwood</td>
            <td>Liam Neeson</td>
            <td>Patricia Clarkson</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.489937992 37.787534989)</td>
        </tr>
        <tr>
            <td>The Princess Diaries</td>
            <td>2001</td>
            <td>2601 Lyon Street</td>
            <td>None</td>
            <td>Walt Disney Pictures</td>
            <td>Buena Vista Pictures</td>
            <td>Garry Marshall</td>
            <td>Gina Wendkos</td>
            <td>Julie Andrews</td>
            <td>Anne Hathway</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.447010997 37.794680981)</td>
        </tr>
        <tr>
            <td>Murder in the First, Season 1</td>
            <td>2014</td>
            <td>Ida B. Wells High School (1099 Hayes Street)</td>
            <td>Ida B. Wells High School is named after the African-American journalist, suffragist and early leader in the Civil Rights Movement Ida B. Wells</td>
            <td>Turner North Center Productions</td>
            <td>Turner Network Television (TNT)</td>
            <td>Steven Bochcho</td>
            <td>Eric Lodal</td>
            <td>Taye Diggs</td>
            <td>Kathleen Robertson</td>
            <td>Ian Anthony Dale</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.434035978 37.775064017)</td>
        </tr>
        <tr>
            <td>Junior</td>
            <td>1994</td>
            <td>722 Steiner Street</td>
            <td>None</td>
            <td>Northern Lights Entertainment</td>
            <td>Universal Pictures</td>
            <td>Ivan Reitman</td>
            <td>Kevin Wade</td>
            <td>Arnold Schwarzenegger</td>
            <td>Danny DeVito</td>
            <td>Emma Thompson</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.432784979 37.776451012)</td>
        </tr>
        <tr>
            <td>The Woman In Red</td>
            <td>1984</td>
            <td>Postcard Row (Alamo Square, Hayes Valley)</td>
            <td>The 6 Victorian homes across from Alamo Square Park are among the few Victorians to survive the Great Fire.</td>
            <td>Orion Pictures Corp.</td>
            <td>MGM Home Entertainment</td>
            <td>Gene Wilder</td>
            <td>Jean Loup Dabadie &amp; Yves Robert</td>
            <td>Gene Wilder</td>
            <td>Charles Grodin</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.43146 37.77722)</td>
        </tr>
        <tr>
            <td>The Bachelor</td>
            <td>1999</td>
            <td>Pacific Stock Exchange (301 Pine Street at Sansome)</td>
            <td>None</td>
            <td>George Street Pictures</td>
            <td>New Line Cinema</td>
            <td>Gary Sinyor</td>
            <td>Steve Cohen</td>
            <td>Chris O&#x27;Donnell</td>
            <td>Renee Zellweger</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.400920001 37.792099983)</td>
        </tr>
        <tr>
            <td>Final Analysis</td>
            <td>1992</td>
            <td>Bix Restaurant (56 Gold Street)</td>
            <td>None</td>
            <td>Warner Bros. Pictures</td>
            <td>Warner Bros. Pictures</td>
            <td>Phil Joanou</td>
            <td>Robert Berger</td>
            <td>Richard Gere</td>
            <td>Kim Basinger</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.402907 37.796864)</td>
        </tr>
        <tr>
            <td>Women is Losers</td>
            <td>2020</td>
            <td>2712 Bryant St</td>
            <td>None</td>
            <td>Look at the Moon Pictures</td>
            <td>None</td>
            <td>Lissette Feliciano</td>
            <td>Lissette Feliciano</td>
            <td>Lorenza Izzo</td>
            <td>Simu Liu</td>
            <td>Liza Weil</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.409273992 37.750881011)</td>
        </tr>
        <tr>
            <td>Rent</td>
            <td>2005</td>
            <td>Treasure Island</td>
            <td>An artificial island, Treasure Island was created for the 1939 Golden Gate International Exposition, and is named after the novel by Robert Louis Stevenson, a one-time San Francisco resident.</td>
            <td>Rent Productions LLC</td>
            <td>Columbia Pictures</td>
            <td>Chris Columbus</td>
            <td>Stephen Chbosky</td>
            <td>Anthony Rapp</td>
            <td>Rosario Dawson</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.37087 37.82489)</td>
        </tr>
        <tr>
            <td>The Last Black Man in San Francisco</td>
            <td>2019</td>
            <td>Illinois St btwn Marin and Amador</td>
            <td>None</td>
            <td>LBMISF, LLC</td>
            <td>A45</td>
            <td>Joe Talbot</td>
            <td>Joe Talbot, Jimmie Fails, Rob Richert</td>
            <td>Jimmie Fails</td>
            <td>Jonathan Majors</td>
            <td>Danny Glover</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.386040027 37.745770019)</td>
        </tr>
        <tr>
            <td>Smile Again, Jenny Lee</td>
            <td>2015</td>
            <td>Europa Café (4318 California St. and 5th Ave.)</td>
            <td>None</td>
            <td>Carlo Caldana/Marguery Films</td>
            <td>None</td>
            <td>Carlo Caldana</td>
            <td>Linda Demetrick</td>
            <td>Craig Tsuyumine</td>
            <td>Puneet Prasad</td>
            <td>Larry Kitagawa</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.463499961 37.785130012)</td>
        </tr>
        <tr>
            <td>Sense8</td>
            <td>2015</td>
            <td>Market St. overpass</td>
            <td>Bicycle chase scene</td>
            <td>Unpronounceable Productions, LLC</td>
            <td>Netflix</td>
            <td>The Wachowskis</td>
            <td>The Wachowskis</td>
            <td>Jamie Clayton</td>
            <td>None</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.40001657 37.79039257)</td>
        </tr>
    </tbody>
</table>

### Now, we want to retrieve 15 rows from the table starting from row 11.

```sql
%%sql
SELECT * FROM FilmLocations LIMIT 15 OFFSET 10;
```

<table>
    <thead>
        <tr>
            <th>title</th>
            <th>release_year</th>
            <th>locations</th>
            <th>fun_facts</th>
            <th>production_company</th>
            <th>distributor</th>
            <th>director</th>
            <th>writer</th>
            <th>actor_1</th>
            <th>actor_2</th>
            <th>actor_3</th>
            <th>state</th>
            <th>city</th>
            <th>point</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Time After Time</td>
            <td>1979</td>
            <td>Palace of Fine Arts (3301 Lyon Street)</td>
            <td>The original Palace was built for the 1915 Panama-Pacific Exposition, and completely destroyed in 1964. It was rebuilt in 1965.</td>
            <td>Orion Pictures Corp.</td>
            <td>Columbia Broadcasting System (CBS)</td>
            <td>Nicholas Meyer</td>
            <td>Karl Alexander</td>
            <td>Malcolm McDowell</td>
            <td>Mary Steenburgen</td>
            <td>David Warner</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.44899 37.80288)</td>
        </tr>
        <tr>
            <td>Quitters</td>
            <td>2015</td>
            <td>Claire Lilienthal Elementary School</td>
            <td>None</td>
            <td>Frederick &amp; Ashbury, LLC.</td>
            <td>None</td>
            <td>Noah Pritzker</td>
            <td>Noah Pritzker</td>
            <td>Kara Hayward</td>
            <td>Mira Sorvino</td>
            <td>Saffron Burrows</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.45796 37.7871)</td>
        </tr>
        <tr>
            <td>Quitters</td>
            <td>2015</td>
            <td>1536 Noe St.</td>
            <td>None</td>
            <td>Frederick &amp; Ashbury, LLC.</td>
            <td>None</td>
            <td>Noah Pritzker</td>
            <td>Noah Pritzker</td>
            <td>Kara Hayward</td>
            <td>Mira Sorvino</td>
            <td>Saffron Burrows</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.431454017 37.744473004)</td>
        </tr>
        <tr>
            <td>The Dead Pool</td>
            <td>1988</td>
            <td>550 El Camino Del Mar (Seacliff)</td>
            <td>None</td>
            <td>Warner Bros. Pictures</td>
            <td>Warner Bros. Pictures</td>
            <td>Buddy Van Horn</td>
            <td>Harry Julian Fink</td>
            <td>Clint Eastwood</td>
            <td>Liam Neeson</td>
            <td>Patricia Clarkson</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.489937992 37.787534989)</td>
        </tr>
        <tr>
            <td>The Princess Diaries</td>
            <td>2001</td>
            <td>2601 Lyon Street</td>
            <td>None</td>
            <td>Walt Disney Pictures</td>
            <td>Buena Vista Pictures</td>
            <td>Garry Marshall</td>
            <td>Gina Wendkos</td>
            <td>Julie Andrews</td>
            <td>Anne Hathway</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.447010997 37.794680981)</td>
        </tr>
        <tr>
            <td>Murder in the First, Season 1</td>
            <td>2014</td>
            <td>Ida B. Wells High School (1099 Hayes Street)</td>
            <td>Ida B. Wells High School is named after the African-American journalist, suffragist and early leader in the Civil Rights Movement Ida B. Wells</td>
            <td>Turner North Center Productions</td>
            <td>Turner Network Television (TNT)</td>
            <td>Steven Bochcho</td>
            <td>Eric Lodal</td>
            <td>Taye Diggs</td>
            <td>Kathleen Robertson</td>
            <td>Ian Anthony Dale</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.434035978 37.775064017)</td>
        </tr>
        <tr>
            <td>Junior</td>
            <td>1994</td>
            <td>722 Steiner Street</td>
            <td>None</td>
            <td>Northern Lights Entertainment</td>
            <td>Universal Pictures</td>
            <td>Ivan Reitman</td>
            <td>Kevin Wade</td>
            <td>Arnold Schwarzenegger</td>
            <td>Danny DeVito</td>
            <td>Emma Thompson</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.432784979 37.776451012)</td>
        </tr>
        <tr>
            <td>The Woman In Red</td>
            <td>1984</td>
            <td>Postcard Row (Alamo Square, Hayes Valley)</td>
            <td>The 6 Victorian homes across from Alamo Square Park are among the few Victorians to survive the Great Fire.</td>
            <td>Orion Pictures Corp.</td>
            <td>MGM Home Entertainment</td>
            <td>Gene Wilder</td>
            <td>Jean Loup Dabadie &amp; Yves Robert</td>
            <td>Gene Wilder</td>
            <td>Charles Grodin</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.43146 37.77722)</td>
        </tr>
        <tr>
            <td>The Bachelor</td>
            <td>1999</td>
            <td>Pacific Stock Exchange (301 Pine Street at Sansome)</td>
            <td>None</td>
            <td>George Street Pictures</td>
            <td>New Line Cinema</td>
            <td>Gary Sinyor</td>
            <td>Steve Cohen</td>
            <td>Chris O&#x27;Donnell</td>
            <td>Renee Zellweger</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.400920001 37.792099983)</td>
        </tr>
        <tr>
            <td>Final Analysis</td>
            <td>1992</td>
            <td>Bix Restaurant (56 Gold Street)</td>
            <td>None</td>
            <td>Warner Bros. Pictures</td>
            <td>Warner Bros. Pictures</td>
            <td>Phil Joanou</td>
            <td>Robert Berger</td>
            <td>Richard Gere</td>
            <td>Kim Basinger</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.402907 37.796864)</td>
        </tr>
        <tr>
            <td>Women is Losers</td>
            <td>2020</td>
            <td>2712 Bryant St</td>
            <td>None</td>
            <td>Look at the Moon Pictures</td>
            <td>None</td>
            <td>Lissette Feliciano</td>
            <td>Lissette Feliciano</td>
            <td>Lorenza Izzo</td>
            <td>Simu Liu</td>
            <td>Liza Weil</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.409273992 37.750881011)</td>
        </tr>
        <tr>
            <td>Rent</td>
            <td>2005</td>
            <td>Treasure Island</td>
            <td>An artificial island, Treasure Island was created for the 1939 Golden Gate International Exposition, and is named after the novel by Robert Louis Stevenson, a one-time San Francisco resident.</td>
            <td>Rent Productions LLC</td>
            <td>Columbia Pictures</td>
            <td>Chris Columbus</td>
            <td>Stephen Chbosky</td>
            <td>Anthony Rapp</td>
            <td>Rosario Dawson</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.37087 37.82489)</td>
        </tr>
        <tr>
            <td>The Last Black Man in San Francisco</td>
            <td>2019</td>
            <td>Illinois St btwn Marin and Amador</td>
            <td>None</td>
            <td>LBMISF, LLC</td>
            <td>A45</td>
            <td>Joe Talbot</td>
            <td>Joe Talbot, Jimmie Fails, Rob Richert</td>
            <td>Jimmie Fails</td>
            <td>Jonathan Majors</td>
            <td>Danny Glover</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.386040027 37.745770019)</td>
        </tr>
        <tr>
            <td>Smile Again, Jenny Lee</td>
            <td>2015</td>
            <td>Europa Café (4318 California St. and 5th Ave.)</td>
            <td>None</td>
            <td>Carlo Caldana/Marguery Films</td>
            <td>None</td>
            <td>Carlo Caldana</td>
            <td>Linda Demetrick</td>
            <td>Craig Tsuyumine</td>
            <td>Puneet Prasad</td>
            <td>Larry Kitagawa</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.463499961 37.785130012)</td>
        </tr>
        <tr>
            <td>Sense8</td>
            <td>2015</td>
            <td>Market St. overpass</td>
            <td>Bicycle chase scene</td>
            <td>Unpronounceable Productions, LLC</td>
            <td>Netflix</td>
            <td>The Wachowskis</td>
            <td>The Wachowskis</td>
            <td>Jamie Clayton</td>
            <td>None</td>
            <td>None</td>
            <td>CA</td>
            <td>San Francisco</td>
            <td>POINT (-122.40001657 37.79039257)</td>
        </tr>
    </tbody>
</table>

## Practice exercises
COUNT

### Retrieve the number of locations of the films which are directed by Woody Allen.

```sql
%%sql
SELECT COUNT(Locations) FROM FilmLocations WHERE Director="Woody Allen";
```

<table>
    <thead>
        <tr>
            <th>COUNT(Locations)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>31</td>
        </tr>
    </tbody>
</table>

### Retrieve the number of films shot at Russian Hill.

```sql
%%sql
SELECT Count(Title) FROM FilmLocations WHERE Locations="Russian Hill";
```
<table>
    <thead>
        <tr>
            <th>Count(Title)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
        </tr>
    </tbody>
</table>

### Retrieve the number of rows having a release year older than 1950 from the "FilmLocations" table.

```sql
%%sql
SELECT Count(*) FROM FilmLocations WHERE Release_Year<1950;
```

<table>
    <thead>
        <tr>
            <th>Count(*)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>31</td>
        </tr>
    </tbody>
</table>

### DISTINCT
#### Retrieve the names of all unique films released in the 21st century and onwards, along with their release years.

```sql
%%sql
SELECT DISTINCT Title, Release_Year FROM FilmLocations WHERE Release_Year>=2001;
```

<table>
    <thead>
        <tr>
            <th>title</th>
            <th>release_year</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Nash Bridges</td>
            <td>2021</td>
        </tr>
        <tr>
            <td>The OA Part II</td>
            <td>2019</td>
        </tr>
        <tr>
            <td>Looking &quot;Special&quot;</td>
            <td>2016</td>
        </tr>
        <tr>
            <td>The Phone/Jexi</td>
            <td>2019</td>
        </tr>
        <tr>
            <td>Terminator - Genisys</td>
            <td>2015</td>
        </tr>
        <tr>
            <td>Murder in the First, Season 3</td>
            <td>2016</td>
        </tr>
        <tr>
            <td>Ant-Man and the Wasp</td>
            <td>2018</td>
        </tr>
        <tr>
            <td>40 Days and 40 Nights</td>
            <td>2002</td>
        </tr>
        <tr>
            <td>Quitters</td>
            <td>2015</td>
        </tr>
        <tr>
            <td>The Princess Diaries</td>
            <td>2001</td>
        </tr>
        <tr>
            <td>Murder in the First, Season 1</td>
            <td>2014</td>
        </tr>
        <tr>
            <td>Women is Losers</td>
            <td>2020</td>
        </tr>
        <tr>
            <td>Rent</td>
            <td>2005</td>
        </tr>
        <tr>
            <td>The Last Black Man in San Francisco</td>
            <td>2019</td>
        </tr>
        <tr>
            <td>Smile Again, Jenny Lee</td>
            <td>2015</td>
        </tr>
        <tr>
            <td>Sense8</td>
            <td>2015</td>
        </tr>
        <tr>
            <td>Tales of the City</td>
            <td>2019</td>
        </tr>
        <tr>
            <td>Shit and Champagne</td>
            <td>2020</td>
        </tr>
        <tr>
            <td>Ant-Man</td>
            <td>2015</td>
        </tr>
        <tr>
            <td>Bitter Melon</td>
            <td>2018</td>
        </tr>
        <tr>
            <td>Chance Season 2</td>
            <td>2017</td>
        </tr>
        <tr>
            <td>Dawn of the Planet of the Apes</td>
            <td>2014</td>
        </tr>
        <tr>
            <td>Hulk</td>
            <td>2003</td>
        </tr>
        <tr>
            <td>Venom</td>
            <td>2018</td>
        </tr>
        <tr>
            <td>Surface</td>
            <td>2022</td>
        </tr>
        <tr>
            <td>Looking Season 2 ep 204</td>
            <td>2015</td>
        </tr>
        <tr>
            <td>Etruscan Smile</td>
            <td>2017</td>
        </tr>
        <tr>
            <td>Summertime</td>
            <td>2015</td>
        </tr>
        <tr>
            <td>Always Be My Maybe</td>
            <td>2019</td>
        </tr>
        <tr>
            <td>San Andreas</td>
            <td>2015</td>
        </tr>
        <tr>
            <td>Birth of the Dragon</td>
            <td>2016</td>
        </tr>
        <tr>
            <td>Blue Jasmine</td>
            <td>2013</td>
        </tr>
        <tr>
            <td>Chance- Season 1 ep106</td>
            <td>2016</td>
        </tr>
        <tr>
            <td>Chance - Season 1 Pilot</td>
            <td>2016</td>
        </tr>
        <tr>
            <td>Goliath- Season 4</td>
            <td>2021</td>
        </tr>
        <tr>
            <td>DEVS</td>
            <td>2020</td>
        </tr>
        <tr>
            <td>Looking Season 2 ep 207</td>
            <td>2015</td>
        </tr>
        <tr>
            <td>A Taiwanese Tale of Two Cities</td>
            <td>2018</td>
        </tr>
        <tr>
            <td>Clickbait</td>
            <td>2021</td>
        </tr>
        <tr>
            <td>Sense8 - Season 2</td>
            <td>2016</td>
        </tr>
        <tr>
            <td>The Matrix Resurrections</td>
            <td>2021</td>
        </tr>
        <tr>
            <td>Age of Adaline</td>
            <td>2015</td>
        </tr>
        <tr>
            <td>Ballers Season 3</td>
            <td>2017</td>
        </tr>
        <tr>
            <td>God is a Communist?* (show me heart universe)</td>
            <td>2010</td>
        </tr>
        <tr>
            <td>Chance- Season 1 ep110</td>
            <td>2016</td>
        </tr>
        <tr>
            <td>GirlBoss</td>
            <td>2017</td>
        </tr>
        <tr>
            <td>Cardinal X</td>
            <td>2015</td>
        </tr>
        <tr>
            <td>Looking</td>
            <td>2014</td>
        </tr>
        <tr>
            <td>Looking Season 2 ep 206</td>
            <td>2015</td>
        </tr>
        <tr>
            <td>Chance- Season 1 ep102</td>
            <td>2016</td>
        </tr>
        <tr>
            <td>Steve Jobs</td>
            <td>2015</td>
        </tr>
        <tr>
            <td>Hemingway &amp; Gelhorn</td>
            <td>2011</td>
        </tr>
        <tr>
            <td>Milk</td>
            <td>2008</td>
        </tr>
        <tr>
            <td>When We Rise</td>
            <td>2017</td>
        </tr>
        <tr>
            <td>The Pursuit of Happyness</td>
            <td>2006</td>
        </tr>
        <tr>
            <td>Chance- Season 1 ep109</td>
            <td>2016</td>
        </tr>
        <tr>
            <td>Super Pumped: The Battle for Uber</td>
            <td>2022</td>
        </tr>
        <tr>
            <td>Venom: Let There Be Carnage</td>
            <td>2021</td>
        </tr>
        <tr>
            <td>Murder in the First, Season 2</td>
            <td>2015</td>
        </tr>
        <tr>
            <td>Red Widow</td>
            <td>2013</td>
        </tr>
        <tr>
            <td>Shang-Chi and the Legend of the Ten Rings</td>
            <td>2021</td>
        </tr>
        <tr>
            <td>Looking Season 2 ep 209</td>
            <td>2015</td>
        </tr>
        <tr>
            <td>The Last Thing He Told Me</td>
            <td>2023</td>
        </tr>
        <tr>
            <td>The Diary of a Teenage Girl</td>
            <td>2015</td>
        </tr>
        <tr>
            <td>Chance- Season 1 ep107</td>
            <td>2016</td>
        </tr>
        <tr>
            <td>Budding Prospects, Pilot</td>
            <td>2017</td>
        </tr>
        <tr>
            <td>Dr. Dolittle 2</td>
            <td>2001</td>
        </tr>
        <tr>
            <td>Chance- Season 1 ep104</td>
            <td>2016</td>
        </tr>
        <tr>
            <td>The Bridge</td>
            <td>2006</td>
        </tr>
        <tr>
            <td>Sonic the Hedgehog</td>
            <td>2020</td>
        </tr>
        <tr>
            <td>I’m A Virgo</td>
            <td>2023</td>
        </tr>
        <tr>
            <td>Sweet November</td>
            <td>2001</td>
        </tr>
        <tr>
            <td>Looking Season 2 ep 202</td>
            <td>2015</td>
        </tr>
        <tr>
            <td>Godzilla</td>
            <td>2014</td>
        </tr>
        <tr>
            <td>Swing</td>
            <td>2003</td>
        </tr>
        <tr>
            <td>Chance- Season 1 ep103</td>
            <td>2016</td>
        </tr>
        <tr>
            <td>Pushing Dead</td>
            <td>2016</td>
        </tr>
        <tr>
            <td>Americana</td>
            <td>2015</td>
        </tr>
        <tr>
            <td>Big Eyes</td>
            <td>2014</td>
        </tr>
        <tr>
            <td>I Am Michael</td>
            <td>2015</td>
        </tr>
        <tr>
            <td>The Wedding Planner</td>
            <td>2001</td>
        </tr>
        <tr>
            <td>My Big Fat Chinese Christmas</td>
            <td>2022</td>
        </tr>
        <tr>
            <td>Ant-Man and the Wasp: Quantumania</td>
            <td>2023</td>
        </tr>
        <tr>
            <td>Haiku Tunnel</td>
            <td>2001</td>
        </tr>
        <tr>
            <td>Twisted</td>
            <td>2004</td>
        </tr>
        <tr>
            <td>Need For Speed</td>
            <td>2014</td>
        </tr>
        <tr>
            <td>Looking Season 2 ep 210</td>
            <td>2015</td>
        </tr>
        <tr>
            <td>Rollerball</td>
            <td>2002</td>
        </tr>
        <tr>
            <td>Looking Season 2 ep 203</td>
            <td>2015</td>
        </tr>
        <tr>
            <td>Alive</td>
            <td>2020</td>
        </tr>
        <tr>
            <td>Looking Season 2 ep 205</td>
            <td>2015</td>
        </tr>
        <tr>
            <td>Chance - Season 1 ep105</td>
            <td>2016</td>
        </tr>
        <tr>
            <td>What the Bleep Do We Know</td>
            <td>2004</td>
        </tr>
        <tr>
            <td>Beautiful Boy</td>
            <td>2018</td>
        </tr>
        <tr>
            <td>50 First Dates</td>
            <td>2004</td>
        </tr>
        <tr>
            <td>Alcatraz</td>
            <td>2012</td>
        </tr>
        <tr>
            <td>Looking Season 2 ep 208</td>
            <td>2015</td>
        </tr>
        <tr>
            <td>Hereafter</td>
            <td>2010</td>
        </tr>
        <tr>
            <td>The Sweetest Thing</td>
            <td>2002</td>
        </tr>
        <tr>
            <td>Serendipity</td>
            <td>2001</td>
        </tr>
        <tr>
            <td>Chef Dynasty: House of Fang</td>
            <td>2022</td>
        </tr>
        <tr>
            <td>High Crimes</td>
            <td>2002</td>
        </tr>
        <tr>
            <td>On the Road</td>
            <td>2012</td>
        </tr>
        <tr>
            <td>This Is Us</td>
            <td>2022</td>
        </tr>
        <tr>
            <td>Night of Henna</td>
            <td>2005</td>
        </tr>
        <tr>
            <td>The Assassination of Richard Nixon</td>
            <td>2004</td>
        </tr>
        <tr>
            <td>180</td>
            <td>2011</td>
        </tr>
        <tr>
            <td>Dopamine</td>
            <td>2003</td>
        </tr>
        <tr>
            <td>Chance - Season 1ep105</td>
            <td>2016</td>
        </tr>
        <tr>
            <td>The Internship</td>
            <td>2013</td>
        </tr>
        <tr>
            <td>Chance- Season 1 ep108</td>
            <td>2016</td>
        </tr>
        <tr>
            <td>By Hook or By Crook</td>
            <td>2001</td>
        </tr>
        <tr>
            <td>Love &amp; Taxes</td>
            <td>2014</td>
        </tr>
        <tr>
            <td>CSI: NY- episode 903</td>
            <td>2012</td>
        </tr>
        <tr>
            <td>Bee Season</td>
            <td>2005</td>
        </tr>
        <tr>
            <td>Parks and Recreation</td>
            <td>2014</td>
        </tr>
        <tr>
            <td>Cherish</td>
            <td>2002</td>
        </tr>
        <tr>
            <td>About a Boy</td>
            <td>2014</td>
        </tr>
        <tr>
            <td>House of Sand and Fog</td>
            <td>2003</td>
        </tr>
        <tr>
            <td>Knife Fight</td>
            <td>2013</td>
        </tr>
        <tr>
            <td>Mission (aka City of Bars)</td>
            <td>2001</td>
        </tr>
        <tr>
            <td>Blindspotting (Season 2)</td>
            <td>2023</td>
        </tr>
        <tr>
            <td>American Yearbook</td>
            <td>2004</td>
        </tr>
        <tr>
            <td>Tweek City</td>
            <td>2005</td>
        </tr>
        <tr>
            <td>Silicon Valley Season 4</td>
            <td>2017</td>
        </tr>
        <tr>
            <td>Broken-A Modern Love Story</td>
            <td>2010</td>
        </tr>
        <tr>
            <td>Nash Bridges</td>
            <td>2022</td>
        </tr>
        <tr>
            <td>Big Sur</td>
            <td>2013</td>
        </tr>
        <tr>
            <td>Julie and Jack</td>
            <td>2003</td>
        </tr>
        <tr>
            <td>The Fog of War</td>
            <td>2003</td>
        </tr>
        <tr>
            <td>Zodiac</td>
            <td>2007</td>
        </tr>
        <tr>
            <td>Mona Lisa Smile</td>
            <td>2003</td>
        </tr>
        <tr>
            <td>24 Hours on Craigslist</td>
            <td>2005</td>
        </tr>
        <tr>
            <td>Babies</td>
            <td>2010</td>
        </tr>
        <tr>
            <td>The Californians</td>
            <td>2005</td>
        </tr>
        <tr>
            <td>Just Like Heaven</td>
            <td>2005</td>
        </tr>
        <tr>
            <td>Confessions of a Burning Man</td>
            <td>2003</td>
        </tr>
        <tr>
            <td>Under the Tuscan Sun</td>
            <td>2003</td>
        </tr>
        <tr>
            <td>Red Diaper Baby</td>
            <td>2004</td>
        </tr>
        <tr>
            <td>Never Die Twice</td>
            <td>2001</td>
        </tr>
        <tr>
            <td>I&#x27;s</td>
            <td>2011</td>
        </tr>
        <tr>
            <td>Earth Mama</td>
            <td>2023</td>
        </tr>
        <tr>
            <td>Fandom</td>
            <td>2004</td>
        </tr>
        <tr>
            <td>The Core</td>
            <td>2003</td>
        </tr>
        <tr>
            <td>The Master</td>
            <td>2012</td>
        </tr>
        <tr>
            <td>The Zodiac</td>
            <td>2005</td>
        </tr>
    </tbody>
</table>

#### Retrieve the directors' names and their distinct films shot at City Hall.

```sql
%%sql
SELECT DISTINCT Title, Director FROM FilmLocations WHERE Locations="City Hall";
```

<table>
    <thead>
        <tr>
            <th>title</th>
            <th>director</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Tucker: The Man and His Dream</td>
            <td>Francis Ford Coppola</td>
        </tr>
        <tr>
            <td>Jagged Edge</td>
            <td>Richard Marquand</td>
        </tr>
        <tr>
            <td>Bedazzled</td>
            <td>Harold Ramis</td>
        </tr>
        <tr>
            <td>Foul Play</td>
            <td>Colin Higgins</td>
        </tr>
        <tr>
            <td>Milk</td>
            <td>Gus Van Sant</td>
        </tr>
        <tr>
            <td>Final Analysis</td>
            <td>Phil Joanou</td>
        </tr>
        <tr>
            <td>The Right Stuff</td>
            <td>Philip Kaufman</td>
        </tr>
        <tr>
            <td>The Enforcer</td>
            <td>James Fargo</td>
        </tr>
        <tr>
            <td>Class Action</td>
            <td>Michael Apted</td>
        </tr>
        <tr>
            <td>Boys and Girls</td>
            <td>Robert Iscove</td>
        </tr>
        <tr>
            <td>Knife Fight</td>
            <td>Bill Guttentag</td>
        </tr>
        <tr>
            <td>Dawn of the Planet of the Apes</td>
            <td>Matt Reeves</td>
        </tr>
        <tr>
            <td>A View to a Kill</td>
            <td>John Glen</td>
        </tr>
        <tr>
            <td>Bicentennial Man</td>
            <td>Chris Columbus</td>
        </tr>
        <tr>
            <td>180</td>
            <td>Jayendra</td>
        </tr>
        <tr>
            <td>San Francisco</td>
            <td>W.S. Van Dyke</td>
        </tr>
        <tr>
            <td>Smile Again, Jenny Lee</td>
            <td>Carlo Caldana</td>
        </tr>
        <tr>
            <td>The Wedding Planner</td>
            <td>Adam Shankman</td>
        </tr>
        <tr>
            <td>Magnum Force</td>
            <td>Ted Post</td>
        </tr>
        <tr>
            <td>The Rock</td>
            <td>Michael Bay</td>
        </tr>
        <tr>
            <td>When We Rise</td>
            <td>Gus Van Sant</td>
        </tr>
        <tr>
            <td>Invasion of the Body Snatchers</td>
            <td>Philip Kaufman</td>
        </tr>
    </tbody>
</table>


#### Retrieve the number of distributors who distributed films with the 1st actor, Clint Eastwood.

```sql
%%sql
SELECT COUNT(DISTINCT Distributor) FROM FilmLocations WHERE Actor_1="Clint Eastwood"; 
```

<table>
    <thead>
        <tr>
            <th>COUNT(DISTINCT Distributor)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>3</td>
        </tr>
    </tbody>
</table>

### LIMIT

#### Retrieve the names of the first 50 films.

```sql
%%sql
SELECT DISTINCT Title FROM FilmLocations LIMIT 50
```

<table>
    <thead>
        <tr>
            <th>title</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Nash Bridges</td>
        </tr>
        <tr>
            <td>The OA Part II</td>
        </tr>
        <tr>
            <td>Looking &quot;Special&quot;</td>
        </tr>
        <tr>
            <td>The Phone/Jexi</td>
        </tr>
        <tr>
            <td>Terminator - Genisys</td>
        </tr>
        <tr>
            <td>Murder in the First, Season 3</td>
        </tr>
        <tr>
            <td>Ant-Man and the Wasp</td>
        </tr>
        <tr>
            <td>Dirty Harry</td>
        </tr>
        <tr>
            <td>40 Days and 40 Nights</td>
        </tr>
        <tr>
            <td>Harold and Maude</td>
        </tr>
        <tr>
            <td>Time After Time</td>
        </tr>
        <tr>
            <td>Quitters</td>
        </tr>
        <tr>
            <td>The Dead Pool</td>
        </tr>
        <tr>
            <td>The Princess Diaries</td>
        </tr>
        <tr>
            <td>Murder in the First, Season 1</td>
        </tr>
        <tr>
            <td>Junior</td>
        </tr>
        <tr>
            <td>The Woman In Red</td>
        </tr>
        <tr>
            <td>The Bachelor</td>
        </tr>
        <tr>
            <td>Final Analysis</td>
        </tr>
        <tr>
            <td>Women is Losers</td>
        </tr>
        <tr>
            <td>Rent</td>
        </tr>
        <tr>
            <td>The Last Black Man in San Francisco</td>
        </tr>
        <tr>
            <td>Smile Again, Jenny Lee</td>
        </tr>
        <tr>
            <td>Sense8</td>
        </tr>
        <tr>
            <td>Tucker: The Man and His Dream</td>
        </tr>
        <tr>
            <td>Tales of the City</td>
        </tr>
        <tr>
            <td>Nine to Five</td>
        </tr>
        <tr>
            <td>Shit and Champagne</td>
        </tr>
        <tr>
            <td>Ant-Man</td>
        </tr>
        <tr>
            <td>Pacific Heights</td>
        </tr>
        <tr>
            <td>Interview With The Vampire</td>
        </tr>
        <tr>
            <td>Bitter Melon</td>
        </tr>
        <tr>
            <td>Chance Season 2</td>
        </tr>
        <tr>
            <td>Dawn of the Planet of the Apes</td>
        </tr>
        <tr>
            <td>Hulk</td>
        </tr>
        <tr>
            <td>Venom</td>
        </tr>
        <tr>
            <td>Surface</td>
        </tr>
        <tr>
            <td>Sudden Impact</td>
        </tr>
        <tr>
            <td>Looking Season 2 ep 204</td>
        </tr>
        <tr>
            <td>Etruscan Smile</td>
        </tr>
        <tr>
            <td>Summertime</td>
        </tr>
        <tr>
            <td>Always Be My Maybe</td>
        </tr>
        <tr>
            <td>San Andreas</td>
        </tr>
        <tr>
            <td>Birth of the Dragon</td>
        </tr>
        <tr>
            <td>The Rock</td>
        </tr>
        <tr>
            <td>So I Married an Axe Murderer</td>
        </tr>
        <tr>
            <td>Blue Jasmine</td>
        </tr>
        <tr>
            <td>The Maltese Falcon</td>
        </tr>
        <tr>
            <td>Chance- Season 1 ep106</td>
        </tr>
        <tr>
            <td>Chance - Season 1 Pilot</td>
        </tr>
    </tbody>
</table>

#### Retrieve the first 10 film names released in 2015.

```sql
%%sql
SELECT DISTINCT Title FROM FilmLocations WHERE Release_Year=2015 LIMIT 10;
```

<table>
    <thead>
        <tr>
            <th>title</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Terminator - Genisys</td>
        </tr>
        <tr>
            <td>Quitters</td>
        </tr>
        <tr>
            <td>Smile Again, Jenny Lee</td>
        </tr>
        <tr>
            <td>Sense8</td>
        </tr>
        <tr>
            <td>Ant-Man</td>
        </tr>
        <tr>
            <td>Looking Season 2 ep 204</td>
        </tr>
        <tr>
            <td>Summertime</td>
        </tr>
        <tr>
            <td>San Andreas</td>
        </tr>
        <tr>
            <td>Looking Season 2 ep 207</td>
        </tr>
        <tr>
            <td>Age of Adaline</td>
        </tr>
    </tbody>
</table>

#### Retrieve the next 3 film names that follow after the first 5 films released in 2015.


```sql
%%sql
SELECT DISTINCT Title FROM FilmLocations WHERE Release_Year=2015 LIMIT 3 OFFSET 5;

```

<table>
    <thead>
        <tr>
            <th>title</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Looking Season 2 ep 204</td>
        </tr>
        <tr>
            <td>Summertime</td>
        </tr>
        <tr>
            <td>San Andreas</td>
        </tr>
    </tbody>
</table>