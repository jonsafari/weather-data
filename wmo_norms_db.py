#!/usr/bin/env python3
"""
Imports WMO data to an SQLite3 database
WMO data comes from http://webapp1.dlib.indiana.edu/virtual_disk_library/index.cgi/4296047/FID427/
By Jon Dehdari, 2016
Usage: python3 wmo_norms_db.py
Then:  sqlite3 wmo_norms.db
An example website that uses this data is www.climate-charts.com
"""

import sqlite3 as lite
import os, sys, argparse, lzma, codecs


def open_files(args, data):
    # Read climate element codes
    # Table 6 of wmo_norms/data/ALLNORMS.TXT
    # Code, Unit, Description
    with open(args.climate_elem_codes) as clim_elem_codes_file:
        for line in clim_elem_codes_file:
            data['clim_elem_codes'].append(tuple(line.rstrip().split('\t')))

    # Read region codes
    # Table 1 of wmo_norms/data/ALLNORMS.TXT
    # Code, Region
    with open(args.region_codes) as region_codes_file:
        for line in region_codes_file:
            data['region_codes'].append(tuple(line.rstrip().split('\t')))

    # Read statistic codes
    # Table 7 of wmo_norms/data/ALLNORMS.TXT
    # Code, Description
    with open(args.stat_codes) as statistic_codes_file:
        for line in statistic_codes_file:
            data['statistic_codes'].append(tuple(line.rstrip().split('\t')))


    # Main weather data (allnorms)
    # File: wmo_norms/data/allnorms.dat.utf8.xz
    # Docs: wmo_norms/doc/allnorms.txt
    _, allnorms_suffix = os.path.splitext(args.allnorms)
    if allnorms_suffix == '.xz':
        allnorms_file = lzma.open(args.allnorms, mode='rt', encoding='utf-8')
    else:
        allnorms_file = codecs.open(args.allnorms, 'r', 'iso-8859-1') # original file is iso-8859
    for line in allnorms_file:
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
        data['allnorms'].append((region, country, station, clim_elem_code, statistic_code, jan, feb, mar, apr, may, jun, jul, aug, sep, octr, nov, dec, annual_norms_reported, annual_norms_computed))
    allnorms_file.close()


    # Station metadata
    # File: wmo_norms/data/stnmeta.dat.utf.xz
    # Docs: wmo_norms/doc/stnmeta.txt
    _, stnmeta_suffix  = os.path.splitext(args.stnmeta)
    if stnmeta_suffix == '.xz':
        stnmeta_file = lzma.open(args.stnmeta, mode='rt', encoding='utf-8')
    else:
        stnmeta_file = codecs.open(args.stnmeta, 'r', 'iso-8859-1') # original file is iso-8859
    for line in stnmeta_file:
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
        data['station_meta'].append((region, country, station, lat_degs_mem, lat_mins_mem, lat_hem_mem, lon_degs_mem, lon_mins_mem, lon_hem_mem, elev_mem, lat_degs_wmo, lat_mins_wmo, lat_hem_wmo, lon_degs_wmo, lon_mins_wmo, lon_hem_wmo, elev_wmo, name, country_name))
    stnmeta_file.close()




def gen_db(args, data):
    con = lite.connect(args.db)
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
        cur.executemany("INSERT INTO `allnorms` VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", data['allnorms'])

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
        cur.executemany("INSERT INTO `station_meta` VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", data['station_meta'])

        cur.execute("DROP TABLE IF EXISTS `region_codes`")
        cur.execute("""
    CREATE TABLE `region_codes` (
        `code`   TEXT PRIMARY KEY,
        `region` TEXT NOT NULL
    );
    """)
        cur.executemany("INSERT INTO `region_codes` VALUES(?,?)", data['region_codes'])

        cur.execute("DROP TABLE IF EXISTS `clim_elem_codes`")
        cur.execute("""
    CREATE TABLE `clim_elem_codes` (
        `code`   TEXT PRIMARY KEY,
        `units`  TEXT NOT NULL,
        `desc`   TEXT NOT NULL
    );
    """)
        cur.executemany("INSERT INTO `clim_elem_codes` VALUES(?,?,?)", data['clim_elem_codes'])

        cur.execute("DROP TABLE IF EXISTS `statistic_codes`")
        cur.execute("""
    CREATE TABLE `statistic_codes` (
        `code`   TEXT PRIMARY KEY,
        `desc`   TEXT NOT NULL
    );
    """)
        cur.executemany("INSERT INTO `statistic_codes` VALUES(?,?)", data['statistic_codes'])

        cur.execute("VACUUM;")


def main():
    parser = argparse.ArgumentParser(description='Builds weather database')
    parser.add_argument('--db', help='Specify Sqlite3 database output (default: %(default)s)', type=str, default='wmo_norms.db')
    parser.add_argument('--allnorms', help='Specify allnorms.dat input (default: %(default)s)', type=str, default='wmo_norms_1961-1990/data/allnorms.dat.utf8.xz')
    parser.add_argument('--stnmeta', help='Specify stnmeta.dat input (default: %(default)s)', type=str, default='wmo_norms_1961-1990/data/stnmeta.dat.utf8.xz')
    parser.add_argument('--climate_elem_codes', help='Specify climate_elem_code.tsv (default: %(default)s)', type=str, default='wmo_norms_1961-1990/data/climate_elem_code.tsv')
    parser.add_argument('--region_codes', help='Specify region_code.tsv (default: %(default)s)', type=str, default='wmo_norms_1961-1990/data/region_code.tsv')
    parser.add_argument('--stat_codes', help='Specify statistic_code.tsv (default: %(default)s)', type=str, default='wmo_norms_1961-1990/data/statistic_code.tsv')
    args = parser.parse_args()

    data = {'allnorms':[], 'station_meta': [], 'clim_elem_codes':[], 'region_codes':[], 'statistic_codes':[]}

    open_files(args, data)
    gen_db(args, data)


if __name__ == '__main__':
    main()
