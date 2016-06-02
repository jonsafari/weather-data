# Weather-data
Worldwide weather data.  Thirty years of it.

Data and scripts are provided to build an SQL database of 30 years of weather info.

## Building the SQLite Database
To build the SQLite3 database, run the following:
```Bash
python3 wmo_norms_db.py
```
This builds the file `wmo_norms.db` .
You can then use tools like [sqlitebrowser](http://sqlitebrowser.org) or the command-line interface `sqlite3 wmo_norms.db`.

## Example Query
The file [example_queries.sql](example_queries.sql) includes sample queries.  For example, to list the sunniest places in the US, and some additional info:

```sql
select station_meta.name as "Place",
    an_sun.dec as "December_Sun",
    an_low.jan as "January_Low_Avg",
    an_hi.jul  as "July_Hi_Avg",
    an_hi.jul - an_low.jan as "Temp_Range",
    an_hum.jul as "July_Humidity_Avg"
from allnorms an_sun
join station_meta on an_sun.station = station_meta.station
join allnorms an_low on an_low.station = an_sun.station
join allnorms an_hi  on an_hi.station = an_sun.station
join allnorms an_hum on an_hum.station = an_sun.station
where station_meta.country_name = 'United States Of America'
    and an_sun.clim_elem_code = '15' -- sunshine
    and an_sun.statistic_code = '44' 
    and an_low.clim_elem_code = '03' -- mean low temp (in january)
    and an_low.statistic_code = '01' 
    and an_low.jan > -10             -- no cold places
    and an_hi.clim_elem_code  = '02' -- mean hi temp (in july)
    and an_hi.statistic_code  = '01' 
    and an_hum.clim_elem_code = '11' -- mean humidity (in july)
    and an_hum.statistic_code = '94' 
order by an_sun.dec desc  limit 11;
```
The result:

|Place|December_Sun|January_Low_Avg|July_Hi_Avg|Temp_Range|July_Humidity_Avg|
|---|---|---|---|---|---|
|Yuma/Int'l Ap. AZ|252.7|6.8|41.4|34.6|35.2|
|El Paso/Int'l TX|246.3|-1.4|35.6|37.0|43.9|
|Tucson/Int'l AZ|245.8|3.7|37.4|33.7|41.6|
|Phoenix/Int'l AZ|244.8|5.1|41.1|36.0|31.6|
|Las Vegas/McC. NV|236.0|0.9|41.1|40.2|21.1|
|Key West/Int'l FL|234.5|18.3|31.7|13.4|72.2|
|San Diego/Lind. CA|231.3|9.4|24.6|15.2|74.6|
|Albuquerque/Int'l NM|223.3|-5.7|33.6|39.3|41.9|
|Flagstaff/Pulliam AZ|219.8|-9.3|27.7|37.0|51.1|
|San Juan/Int'l PR|217.4|21.6|31.4|9.8|75.9|
|Miami/Int'l FL|216.1|15.1|31.7|16.6|74.8|

## Documentation
Documentation of the weather data is found in the directory [wmo_norms_1961-1990/doc/](wmo_norms_1961-1990/doc/) .
