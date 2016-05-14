#!/usr/bin/env python3
## Imports WMO data to an SQLite3 database
## WMO data comes from http://webapp1.dlib.indiana.edu/virtual_disk_library/index.cgi/4296047/FID427/DATA/ALLNORMS.DAT
## By Jon Dehdari, 2016
## Usage: python3 wmo_norms_db.py ALLNORMS.DAT STN_META.TXT
## An example website that uses this data is www.climate-charts.com

import sqlite3 as lite
import sys, codecs

# Weather data
# File: wmo_norms/data/ALLNORMS.DAT
# Docs: wmo_norms/data/ALLNORMS.TXT
input_file = codecs.open(sys.argv[1], 'r', 'iso-8859-1')
data = []
for line in input_file:
    region         = line[0]
    country        = line[1:3].strip()
    station        = line[3:16].strip()
    clim_elem_code = line[26:28].strip()
    statistic_code = line[28:30].strip()
    jan  = line[37:44].strip()
    feb  = line[45:52].strip()
    mar  = line[53:60].strip()
    apr  = line[61:68].strip()
    may  = line[69:76].strip()
    jun  = line[77:84].strip()
    jul  = line[85:92].strip()
    aug  = line[93:100].strip()
    sep  = line[101:108].strip()
    octr = line[109:116].strip()
    nov  = line[117:124].strip()
    dec  = line[125:132].strip()
    annual_norms_reported = line[133:141].strip()
    annual_norms_computed = line[142:150].strip()
    data.append((region, country, station, clim_elem_code, statistic_code, jan, feb, mar, apr, may, jun, jul, aug, sep, octr, nov, dec, annual_norms_reported, annual_norms_computed))
input_file.close()


# Station metadata
# File: wmo_norms/data/STNMETA.DAT
# Docs: wmo_norms/document/STN_META.TXT
input_file = codecs.open(sys.argv[2], 'r', 'iso-8859-1')
station_meta = []
for line in input_file:
    region       = line[0]
    country      = line[1:3].strip()
    station      = line[3:16].strip()
    lat_degs_mem = line[18:20].strip()
    lat_mins_mem = line[20:22].strip()
    lat_hem_mem  = line[22:23].strip()
    lon_degs_mem = line[23:26].strip()
    lon_mins_mem = line[26:28].strip()
    lon_hem_mem  = line[28:29].strip()
    elev_mem     = line[29:35].strip()
    lat_degs_wmo = line[35:37].strip()
    lat_mins_wmo = line[37:39].strip()
    lat_hem_wmo  = line[39:40].strip()
    lon_degs_wmo = line[40:43].strip()
    lon_mins_wmo = line[43:45].strip()
    lon_hem_wmo  = line[45:46].strip()
    elev_wmo     = line[46:50].strip()
    name         = line[136:158].strip()
    country_name = line[158:208].title().strip()
    station_meta.append((region, country, station, lat_degs_mem, lat_mins_mem, lat_hem_mem, lon_degs_mem, lon_mins_mem, lon_hem_mem, elev_mem, lat_degs_wmo, lat_mins_wmo, lat_hem_wmo, lon_degs_wmo, lon_mins_wmo, lon_hem_wmo, elev_wmo, name, country_name))
input_file.close()


# Table 6 of wmo_norms/data/ALLNORMS.TXT
# Code, Unit, Description
clim_elem_code = [
('01', 'deg C',    'Dry Bulb Temperature'),
('02', 'deg C',    'Maximum Dry Bulb Temperature'),
('03', 'deg C',    'Minimum Dry Bulb Temperature'),
('04', 'deg C',    'Wet Bulb Temperature'),
('05', 'deg C',    'Dew Point Temperature'),
('06', 'mm',       'Precipitation'),
('08', 'mm',       'Maximum 24-Hour Precipitation'),
('09', 'cm',       'Snowfall'),
('10', 'cm',       'Snow Depth'),
('11', '%',        'Relative Humidity'),
('12', 'hPa',      'Sea Level Pressure'),
('13', 'hPa',      'Station Pressure'),
('14', 'hPa',      'Vapor Pressure'),
('15', '*',        'Sunshine'),
('16', 'm/sec',    'Wind Speed'),
('17', 'degrees',  'Wind Direction'),
('18', 'unitless', 'Wind Steadiness'),
('19', 'deg C',    'Soil Temperature'),
('20', 'okta',     'Sky Cover (Cloud Cover)'),
('21', 'mm',       'Pan Evaporation'),
('28', 'm',        'Height of 1000 hPa Geopotential Level'),
('29', 'm',        'Height of 850 hPa Geopotential Level'),
('30', 'm',        'Height of 700 hPa Geopotential level'),
('32', 'MJ/m2',    'Net Solar Radiation'),
('33', 'MJ/m2',    'Global Solar Radiation'),
('34', 'MJ/m2',    'Diffuse Solar Radiation'),
('35', 'MJ/m2',    'Reflected Solar Radiation'),
('36', 'MJ/m2',    'Atmospheric Solar Radiation'),
('37', 'MJ/m2',    'Terrestrial Solar Radiation'),
('38', 'mm',       'Piche Evaporation'),
('39', 'mm',       'Rainfall'),
('40', '*',        'Bright Sunshine'),
('48', '*',        'Calm Winds'),
('49', 'count',    'Number Days with Sandstorm/Thick Dust/Haze'),
('50', 'count',    'Number Days with Measurable Bright Sunshine'),
('51', 'count',    'Number Days with Thunder'),
('52', 'count',    'Number Days with Lightning'),
('53', 'count',    'Number Days with Hail'),
('54', 'count',    'Number Days with Rainfall GE Threshold'),
('55', 'count',    'Number Days with Rain Showers'),
('56', 'count',    'Number Days with Snowfall'),
('57', 'count',    'Number Days with Snow on Ground'),
('58', 'count',    'Number Days with Fog/Ice Fog'),
('59', 'count',    'Number Days with Fog - Sky Obscured'),
('60', 'count',    'Number Days with Fog - Sky Unobscured'),
('61', 'count',    'Number Days with Haze/Smoke'),
('62', 'count',    'Number Days with Dust'),
('63', 'count',    'Number Days with Blowing Dust/Sand'),
('65', 'count',    'Number Days with Visibility LE Threshold'),
('73', 'count',    'Number Days with no Sunshine'),
('74', 'count',    'Number Days with Dew'),
('75', 'count',    'Number Days with Rime/Glaze Ice'),
('76', 'count',    'Number Days with Air Frost'),
('77', 'count',    'Number Days with Grass Frost'),
('82', 'count',    'Number Days with Gale Force Winds'),
('83', 'count',    'Number Days Maximum Temperature GE Threshold'),
('84', 'count',    'Number Days Maximum Temperature LE Threshold'),
('85', 'count',    'Number Days Minimum Temperature LE Threshold'),
('86', 'count',    'Number Days Minimum Temperature GE Threshold'),
('87', 'count',    'Number Days Mean Temperature GE Threshold'),
('89', 'count',    'Number Days with Dust/Haze/Mist'),
('90', 'count',    'Number Days Maximum Temperature GT Threshold'),
('91', 'count',    'Number Days Maximum Temperature LT Threshold'),
('92', 'count',    'Number Days Minimum Temperature GT Threshold'),
('93', 'count',    'Number Days Minimum Temperature LT Threshold'),
('94', 'count',    'Number Days with Snowfall GE Threshold'),
('95', 'count',    'Number Days with Precipitation GE Threshold'),
('96', 'count',    'Number Days with Snow Cover GE Threshold'),
('97', 'count',    'Number Days with Freezing Rain/Drizzle'),
('98', 'count',    'Number Days with Blowing Snow'),
('AA', 'count',    'Number Days with Rain/Drizzle'),
('AB', 'count',    'Number Days with Snow/Hail'),
('AC', 'count',    'Number Days with Fog/Mist'),
('AD', 'count',    'Number Days with Weather Phenomena'),
('AE', 'count',    'Number Days with Ice Storm'),
('AF', 'count',    'Number Days with Thick Haze'),
('AG', 'count',    'Number Days with Rising Sand'),
('AH', 'count',    'Number Days with Mist'),
('AI', 'count',    'Number Days with Squalls'),
('AJ', 'count',    'Number Days with Duststorm/Sandstorm'),
('AK', 'count',    'Number Days with Sleet/Snow'),
('BH', 'count',    'Number Days Mean Temperature LT Threshold'),
('BJ', 'count',    'Number Days with Fog'),
('BM', 'count',    'Number Days with Daily Maximum Wind Speed GE Threshold'),
('BT', 'count',    'Number Days with Occurrence of Rain'),
('BW', 'count',    'Number Days with Daily Maximum Snow Cover GE Threshold')
]

# Table 7 of wmo_norms/data/ALLNORMS.TXT
# Code, Description
statistic_code = [
('01', 'Mean Value'),
('02', 'Median Value'),
('03', 'Standard Deviation of Mean Value'),
('04', 'Maximum Value'),
('05', 'Minimum Value'),
('06', 'Mean Daily Value'),
('08', 'Standard Deviation of Mean Daily Value'),
('09', 'Mean Daily Maximum Value'),
('10', 'Mean Daily Minimum Value'),
('11', 'Maximum Daily Value'),
('12', 'Date (Year/Day) of Occurrence of Maximum Daily Value'),
('13', 'Minimum Daily Value'),
('14', 'Date (Year/Day) of Occurrence of Minimum Daily Value'),
('15', 'Mean Monthly Value'),
('16', 'Standard Deviation of Mean Monthly Value'),
('18', 'Mean Monthly Maximum Value'),
('19', 'Mean Monthly Minimum Value'),
('20', 'Minimum Monthly Value'),
('21', 'Year of Occurrence of Minimum Monthly Value'),
('22', 'First Quintile'),
('23', 'Second Quintile'),
('24', 'Third Quintile'),
('25', 'Fourth Quintile'),
('26', 'Maximum Monthly Value'),
('27', 'Year of Occurrence of Maximum Monthly Value'),
('30', 'Maximum Gust '),
('37', 'Percent of Possible'),
('38', 'Frequency'),
('41', 'Prevailing'),
('42', 'Vector'),
('44', 'Mean Number of Hours'),
('45', 'Mean - Sunrise to Sunset'),
('51', 'Mean on Last Day of Month'),
('53', 'Percent of Daylight Hours'),
('55', 'Year of Occurrence of Maximum Value'),
('56', 'Year of Occurrence of Minimum Value'),
('57', 'Mean Percent'),
('58', 'First Quartile'),
('59', 'Third Quartile'),
('60', 'Standard Deviation of 3-Hourly Values'),
('64', 'Total Count for Period of Record'),
('69', 'Mean of Hourly Observations'),
('70', 'Mean of Observations at 0000 LST'),
('71', 'Mean of Observations at 0100 LST'),
('72', 'Mean of Observations at 0200 LST'),
('73', 'Mean of Observations at 0300 LST'),
('74', 'Mean of Observations at 0400 LST'),
('75', 'Mean of Observations at 0500 LST'),
('76', 'Mean of Observations at 0600 LST'),
('77', 'Mean of Observations at 0700 LST'),
('78', 'Mean of Observations at 0800 LST'),
('79', 'Mean of Observations at 0900 LST'),
('80', 'Mean of Observations at 1000 LST'),
('81', 'Mean of Observations at 1100 LST'),
('82', 'Mean of Observations at 1200 LST'),
('83', 'Mean of Observations at 1300 LST'),
('84', 'Mean of Observations at 1400 LST'),
('85', 'Mean of Observations at 1500 LST'),
('86', 'Mean of Observations at 1600 LST'),
('87', 'Mean of Observations at 1700 LST'),
('88', 'Mean of Observations at 1800 LST'),
('89', 'Mean of Observations at 1900 LST'),
('90', 'Mean of Observations at 2000 LST'),
('91', 'Mean of Observations at 2100 LST'),
('92', 'Mean of Observations at 2200 LST'),
('93', 'Mean of Observations at 2300 LST'),
('94', 'Mean of 3-Hourly Observations'),
('97', 'Mean of Synoptic Observations'),
('98', 'Number of Years used to Calculate Normal'),
('AF', 'Afternoon Average'),
('AM', 'Daytime Average'),
('MO', 'Morning Average'),
('PM', 'Nighttime Average')
]




con = lite.connect('wmo_norms.db')

with con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS `allnorms`")
    cur.execute("""
CREATE TABLE `allnorms` (
    `region`         INTEGER NOT NULL,
    `country`        TEXT NOT NULL,
    `station`        TEXT NOT NULL,
    `clim_elem_code` TEXT NOT NULL,
    `statistic_code` TEXT,
    `jan`            REAL,
    `feb`            REAL,
    `mar`            REAL,
    `apr`            REAL,
    `may`            REAL,
    `jun`            REAL,
    `jul`            REAL,
    `aug`            REAL,
    `sep`            REAL,
    `oct`            REAL,
    `nov`            REAL,
    `dec`            REAL,
    `annual_norms_reported`     REAL,
    `annual_norms_computed`     REAL NOT NULL
);
""")
    cur.executemany("INSERT INTO `allnorms` VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", data)


    cur.execute("DROP TABLE IF EXISTS `station_meta`")
    cur.execute("""
CREATE TABLE `station_meta` (
    `region`       INTEGER NOT NULL,
    `country`      TEXT NOT NULL,
    `station`      TEXT NOT NULL,
    `lat_degs_mem` INTEGER,
    `lat_mins_mem` INTEGER,
    `lat_hem_mem`  TEXT,
    `lon_degs_mem` INTEGER,
    `lon_mins_mem` INTEGER,
    `lon_hem_mem`  TEXT,
    `elev_mem`     INTEGER,
    `lat_degs_wmo` INTEGER,
    `lat_mins_wmo` INTEGER,
    `lat_hem_wmo`  TEXT,
    `lon_degs_wmo` INTEGER,
    `lon_mins_wmo` INTEGER,
    `lon_hem_wmo`  TEXT,
    `elev_wmo`     INTEGER,
    `name`         TEXT NOT NULL,
    `country_name` TEXT NOT NULL
);
""")
    cur.executemany("INSERT INTO `station_meta` VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", station_meta)


    cur.execute("DROP TABLE IF EXISTS `clim_elem_code`")
    cur.execute("""
CREATE TABLE `clim_elem_code` (
    `code`   TEXT PRIMARY KEY,
    `units`  TEXT NOT NULL,
    `desc`   TEXT NOT NULL
);
""")
    cur.executemany("INSERT INTO `clim_elem_code` VALUES(?,?,?)", clim_elem_code)


    cur.execute("DROP TABLE IF EXISTS `statistic_code`")
    cur.execute("""
CREATE TABLE `statistic_code` (
    `code`   TEXT PRIMARY KEY,
    `desc`   TEXT NOT NULL
);
""")
    cur.executemany("INSERT INTO `statistic_code` VALUES(?,?)", statistic_code)
