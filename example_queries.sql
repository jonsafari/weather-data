.echo ON

-- -- Listing of Germany annual sunshine hours
-- select an_sun.station, station_meta.name, station_meta.country_name, region_codes.region, an_sun.annual_norms_computed
-- from allnorms an_sun
-- join station_meta on station_meta.station = an_sun.station
-- join region_codes on region_codes.code = an_sun.region
-- where station_meta.country_name = 'Germany'
--  and an_sun.clim_elem_code = '15' -- sunshine
--	and an_sun.statistic_code = '44'
-- order by an_sun.annual_norms_computed desc;

-- Listing of Germany December sunshine hours and mean lows
select an_sun.station, station_meta.name, station_meta.country_name, region_codes.region, an_sun.dec, an_low.dec
from allnorms an_sun
join station_meta on an_sun.station = station_meta.station
join region_codes on region_codes.code = an_sun.region
join allnorms an_low on an_low.station = an_sun.station
where station_meta.country_name = 'Germany'
 and an_sun.clim_elem_code = '15' -- sunshine
 and an_sun.statistic_code = '44'
 and an_low.clim_elem_code = '03' -- mean low temp in december
 and an_low.statistic_code = '01'
order by an_sun.dec desc;


-- Listing of US December sunshine hours and mean lows
select an_sun.station, station_meta.name, station_meta.country_name, region_codes.region, an_sun.dec, an_low.dec, an_hi.jul
from allnorms an_sun
join station_meta on an_sun.station = station_meta.station
join region_codes on region_codes.code = an_sun.region
join allnorms an_low on an_low.station = an_sun.station
join allnorms an_hi on an_hi.station = an_sun.station
where station_meta.country_name = 'United States Of America'
 and an_sun.clim_elem_code = '15' -- sunshine
 and an_sun.statistic_code = '44'
 and an_low.clim_elem_code = '03' -- mean low temp in december
 and an_low.statistic_code = '01'
 and an_hi.clim_elem_code = '02' -- mean hi temp in july
 and an_hi.statistic_code = '01'
order by an_sun.dec desc  limit 40;
