.echo ON
.headers ON
.mode column
.width 14 25 13 9 9 9 9 9

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
select an_sun.station,
	station_meta.name,
	station_meta.country_name,
	region_codes.region,
	an_sun.dec,
	an_low.dec
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
select an_sun.station,
	station_meta.name,
	station_meta.country_name,
	--region_codes.region,
	an_sun.dec as "sun_dec",
	an_low.jan as "low_jan",
	an_hi.jul  as "hi_july",
	an_hi.jul - an_low.jan as "temp_range",
	an_hum.jul as "hum_july"
from allnorms an_sun
join station_meta on an_sun.station = station_meta.station
--join region_codes on region_codes.code = an_sun.region
join allnorms an_low on an_low.station = an_sun.station
join allnorms an_hi  on an_hi.station = an_sun.station
join allnorms an_hum on an_hum.station = an_sun.station
where station_meta.country_name = 'United States Of America'
	and an_sun.clim_elem_code = '15' -- sunshine
	and an_sun.statistic_code = '44'
	and an_low.clim_elem_code = '03' -- mean low temp (in january)
	and an_low.statistic_code = '01'
	and an_hi.clim_elem_code  = '02' -- mean hi temp (in july)
	and an_hi.statistic_code  = '01'
	and an_hum.clim_elem_code = '11' -- mean humidity (in july)
	and an_hum.statistic_code = '94'
order by an_sun.dec desc  limit 45;
