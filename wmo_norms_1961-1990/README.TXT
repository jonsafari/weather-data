From http://webapp1.dlib.indiana.edu/virtual_disk_library/index.cgi/4296047/FID427/



Technical support and ordering information may be found at the end of this
document.

    =====================================================================
                       CONTENTS AND ARRANGEMENT OF THE
                   1961-1990 GLOBAL CLIMATE NORMALS CD-ROM
    =====================================================================

     (NOTE:  The documentation text files on this CD-ROM set are best read
          with a non-scalable font [for example, Courier New] and wide
          margins.)

     This CD-ROM contains a collection of DOS files which describe the 1961-
1990 global standard climate normals for over 4000 stations worldwide
computed by more than 135 countries and territories.  The files include ASCII
data files (file extension .dat), documentation files (file extension .txt),
eye-readable ASCII table files (file extension .txt in subdirectories of the
TABLES directory), graphics files (file extension .pcx), and limited
extraction software (file extension .exe).  

     The data files (file extension .dat) are large files in a fixed length
record format.  They can be read by software written by the user in a high
level computer language (FORTRAN, C, COBOL, and others) according to the
format specifications outlined in the documentation files.  The data files
may also be opened by any ASCII-compatible application that can handle the
data volume.

       The normals data on this CD-ROM were computed by the Member countries
and territories of the World Meteorological Organization (WMO) and submitted
to the USA National Oceanic and Atmospheric Administration's National
Climatic Data Center (World Data Center-A for Meteorology) for collection and
processing.  This CD-ROM contains additional data that were not published by
the WMO in paper copy form.  The global standard normals are prepared
worldwide once every 30 years.

     The files on this CD-ROM are arranged using the following overall
directory structure.

                                  ROOT
                                    |
                                    |
   ----------------------------------------------------------------
   |           |                                     |            |
DOCUMENT    METADATA                               TABLES       DATA
               |                                     |
               |                                     |
   -------------------------------------------       |
   |      |      |      |      |      |      |       |
REG__I REG_II REGIII REG_IV REG__V REG_VI ANTARCTC   |
                                                     |
                                                     |
                                                     |
                                                     |
                       -------------------------------------------
                       |      |      |      |      |      |      |
                    REG__I REG_II REGIII REG_IV REG__V REG_VI ANTARCTC


     The DOCUMENT directory contains documentation files, including (1) text
files that document how the data were analyzed, identify data record formats,
and list translation tables for the various code values, and (2) graphics
files of maps identifying WMO regions and identifying countries which
submitted normals.

     The METADATA directory contains metadata files.  The metadata files
include station metadata (station name, location, and other information) and
narrative metadata (which explain aspects of how the normals were computed). 
The amount of metadata provided by each WMO Member varies considerably, with
some Members not providing narrative metadata.  The metadata files are
arranged by country within WMO Region directories**.

     The DATA directory contains the normals data file, plus limited software
which provides for extraction of all records for a country, or all records
for a station.

     The TABLES directory contains eye-readable table files.  The global
normals table files are arranged by station within country directories, with
the country directories arranged within WMO Region directories**.

** NOTE:  Some countries have stations in more than one region.  The WMO
          global normals were arranged by WMO Region, which means that some
          countries appear in more than one region.  The NCDC assigned
          internal country codes based on country and region.  Consequently,
          countries having stations in more than one region will have more
          than one country code.  A total of 153 country codes were required.

     The following is a summary of the files that are in each subdirectory:

ROOT DIRECTORY
     readme.txt     this file
DOCUMENT
     data_fmt.txt   file format describing how to read the data file
                    (allnorms.dat)
     stn_meta.txt   file format describing how to read the station metadata
                    files (master file stnmeta.dat and the parsed country
                    files CC_stn.dat)
     narrmeta.txt   file format describing how to read the narrative metadata
                    files (master file narrmeta.dat and the parsed country
                    files CC_nar1.dat and CC_nar2.dat)
     ctryinv.txt    limited inventory by country code (includes number of
                    stations, number of records, number of different climatic
                    parameters, and number of stations having specific
                    climatic parameters)
     region.txt     table listing the WMO Regions corresponding to the
                    internal region codes used by NCDC in the project files
     ctrycod1.txt   table listing the countries and their country codes (in
                    ascending order by country name)
     ctrycod2.txt   table listing the countries and their country codes (in
                    ascending order by country code)
     rgctycod.txt   table listing the countries and their country codes (in
                    ascending order by region number, then country name)
     elemcod1.txt   table listing the climatic parameter codes (in ascending
                    order by parameter name)
     elemcod2.txt   table listing the climatic parameter codes (in ascending
                    order by parameter code)
     statist.txt    table listing the statistics codes (in ascending order by
                    code value)
     allcodes.txt   tables listing the country, climatic parameter, and
                    statistic codes and their corresponding descriptions
     foreword.txt   the foreword written by WMO Secretary-General G.O.P.
                    Obasi, as it appeared in the WMO global normals
                    publication, WMO-No. 847: Climatological Normals (CLINO)
                    For The Period 1961-1990
     ncdc9641.txt   documentation file (NCDC format) for the 1961-1990 WMO
                    Global Normals project dataset in NCDC's TD-9641 archive;
                    contains detailed background information on the project
     readmaps.txt   read me file that explains how to interpret the map
                    graphics files (.pcx files)
     wmo_rgn.pcx    map showing the WMO Regions (large, English language
                    version)
     wmo_rgnf.pcx   map showing the WMO Regions (smaller, French language
                    version)
     wmosubm.pcx    map showing which countries submitted normals to the
                    1961-1990 WMO Global Normals project
     mean_slp.pcx   map showing which countries submitted sea level pressure
                    or geopotential height normals (element-statistic codes
                    are also indicated)
     meantave.pcx   map showing which countries submitted mean average
                    temperature normals (element-statistic codes are also
                    indicated)
     meantmax.pcx   map showing which countries submitted mean maximum
                    temperature normals (element-statistic codes are also
                    indicated)
     meantmin.pcx   map showing which countries submitted mean minimum
                    temperature normals (element-statistic codes are also
                    indicated)
     abstmax.pcx    map showing which countries submitted absolute maximum
                    temperature normals (element-statistic codes are also
                    indicated)
     abstmin.pcx    map showing which countries submitted absolute minimum
                    temperature normals (element-statistic codes are also
                    indicated)
     vaporprs.pcx   map showing which countries submitted vapor pressure
                    normals (element-statistic codes are also indicated)
     relhum.pcx     map showing which countries submitted mean maximum,
                    minimum, and/or average relative humidity normals
                    (element-statistic codes are also indicated)
     sunshine.pcx   map showing which countries submitted sunshine duration
                    normals (element-statistic codes are also indicated)
     windspd.pcx    map showing which countries submitted mean wind speed
                    normals (element-statistic codes are also indicated)
     prec_amt.pcx   map showing which countries submitted mean amount of
                    precipitation normals (element-statistic codes are also
                    indicated)
     dayspge1.pcx   map showing which countries submitted normals for mean
                    number of days with precipitation greater than or equal
                    to 1 mm (element-statistic codes are also indicated)
     quintile.pcx   map showing which countries submitted precipitation
                    quintile normals (element-statistic codes are also
                    indicated)
     dewpoint.pcx   map showing which countries submitted dew point
                    temperature normals (element codes are also indicated)
     snowfall.pcx   map showing which countries submitted mean snowfall
                    amount normals (element codes are also indicated)
     winddir.pcx    map showing which countries submitted wind direction
                    normals (element codes are also indicated)
     soiltemp.pcx   map showing which countries submitted soil temperature
                    normals (element codes are also indicated)
     skycover.pcx   map showing which countries submitted sky cover normals
                    (element codes are also indicated)
     evaporat.pcx   map showing which countries submitted evaporation normals
                    (element codes are also indicated)
     solarrad.pcx   map showing which countries submitted solar radiation
                    normals (element codes are also indicated)
     dthunder.pcx   map showing which countries submitted normals for number
                    of days with thunder or lightning (element codes are also
                    indicated)
     dsnowfal.pcx   map showing which countries submitted normals for number
                    of days with snowfall (element codes are also indicated)
     dprecip.pcx    map showing which countries submitted normals for number
                    of days with precipitation or rainfall, with or without a
                    threshold amount indicated (element codes are also
                    indicated)
     dtempera.pcx   map showing which countries submitted normals for number
                    of days with temperatures beyond a specified threshold
                    (element codes are also indicated)
     dfogvsby.pcx   map showing which countries submitted normals for number
                    of days with fog or with visibility below a specified
                    threshold (element codes are also indicated)
METADATA
     readmeta.txt   a read-me file describing aspects of the METADATA branch
                    of the directory tree, including file name structure
     stn_meta.txt   file format describing how to read the station metadata
                    files (master file stnmeta.dat and the parsed country
                    files CC_stn.dat)
     narrmeta.txt   file format describing how to read the narrative metadata
                    files (master file narrmeta.dat and the parsed country
                    files CC_nar1.dat and CC_nar2.dat)
     stnmeta.dat    the station metadata (name, location, and other
                    information) for all of the stations in all of the
                    countries that were submitted
     narrmeta.dat   the narrative metadata (description of aspects of how the
                    normals were computed) from all of the countries that
                    submitted narrative metadata 
METADATA\REG__I
METADATA\REG_II
METADATA\REGIII
METADATA\REG_IV
METADATA\REG__V
METADATA\REG_VI
METADATA\ANTARCTC
          The station metadata and narrative metadata are parsed into country
          files, which are put into their respective WMO Region directories. 
          All countries will have a station metadata file, however not all
          countries will have a narrative metadata file.  A few countries
          submitted more than one narrative (for example, one in English and
          another one containing the same information in the country's native
          language).  The file naming convention is as follows, where CC
          represents the country code:
     CC_stn.dat     the station metadata for that country
     CC_nar1.dat    the narrative metadata submitted by that country
     CC_nar2.dat    additional narrative metadata submitted by that country
DATA
     allnorms.dat   the normals data for all stations in all countries that
                    were submitted
     allnorms.txt   file record format for allnorms.dat
     progdoc.txt    documentation describing how to use the two programs,
                    cntryext.exe and stn_ext.exe
     cntryext.exe   a DOS-executable program that extracts all records for a
                    country from file allnorms.dat and writes them to a file
                    specified by the user
     stn_ext.exe    a DOS-executable program that extracts all records for a
                    station from file allnorms.dat and writes them to a file
                    specified by the user
     stnmeta.dat    the station metadata (name, location, and other
                    information) for all of the stations in all of the
                    countries that were submitted (needed by the two programs
                    to identify country names and station names)
TABLES
     readtabl.txt   a read-me file describing aspects of the TABLES branch of
                    the directory tree
          This directory branch contains eye-readable ASCII text files of
          normals data tables by station.  The station table files are in
          directories identified by country code, and these country
          directories are in the seven WMO Region directories.  Each of the
          region directories has a translation table file which lists the
          countries in the region with their country name and country code,
          and the stations within each country code directory with their
          station name and corresponding file name. 
TABLES\REG__I
     file_id1.txt   translation table for Region I
TABLES\REG_II
     file_id2.txt   translation table for Region II
TABLES\REGIII
     file_id3.txt   translation table for Region III
TABLES\REG_IV
     file_id4.txt   translation table for Region IV
TABLES\REG__V
     file_id5.txt   translation table for Region V
TABLES\REG_VI
     file_id6.txt   translation table for Region VI
TABLES\ANTARCTC
     file_id7.txt   translation table for the Antarctic stations

     While this CD-ROM contains extraction routines that parse data by
country or station, it contains no software that allows the user to import
the data directly into spreadsheets or other applications.  A file, however,
may be easily copied from the CD-ROM onto a hard drive or other device with
the DOS copy command.  The text files (extension .txt) may be easily read by
a text file editor or word processor.

     All data and information files (files with extension .dat) are in a DOS
ASCII format in which a CR-LF indicates the end of record.  The files may be
converted to an appropriate UNIX format by simply transferring them from a
DOS machine to a UNIX machine using the FTP (File Transfer Protocol).  In
addition, some versions of UNIX have a "dos2unix" command that converts the
end of record indicator.  Check your UNIX manuals for further information.

     Technical support questions or comments about the CD-ROM should be
directed to:

          Climate Services Division
          National Climatic Data Center
          151 Patton Avenue, Room 120
          Asheville, NC 28801-5001

          (828) 271-4702

     Questions or comments about the global climate normals project or
methodology should be directed to:

          Climate Perspectives Branch
          National Climatic Data Center
          151 Patton Avenue, Room 120
          Asheville, NC 28801-5001

     If you desire any additional CD-ROM's or data, write, call, or e-mail:

          Climate Services Division
          National Climatic Data Center
          151 Patton Avenue, Room 120
          Asheville, NC 28801-5001

          (828) 271-4800
          orders@ncdc.noaa.gov
          http://www.ncdc.noaa.gov/

