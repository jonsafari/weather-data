.echo ON

-- Listing of annual sunshine hours in Germany
select allnorms.station, station_meta.name, station_meta.country_name, region_codes.region, annual_norms_computed
from allnorms
join station_meta on station_meta.station = allnorms.station
join region_codes on region_codes.code = allnorms.region
where clim_elem_code = '15' and statistic_code = '44' and station_meta.country_name = 'Germany'
order by `annual_norms_computed` desc;

-- Listing of December sunshine hours in Germany
select allnorms.station, station_meta.name, station_meta.country_name, region_codes.region, allnorms.dec
from allnorms
join station_meta on allnorms.station = station_meta.station
join region_codes on region_codes.code = allnorms.region
where clim_elem_code = '15' and statistic_code = '44' and station_meta.country_name = 'Germany'
order by allnorms.dec desc;

-- Listing of December sunshine hours in US
select allnorms.station, station_meta.name, station_meta.country_name, region_codes.region, allnorms.dec
from allnorms
join station_meta on allnorms.station = station_meta.station
join region_codes on region_codes.code = allnorms.region
where clim_elem_code = '15' and statistic_code = '44' and station_meta.country_name = 'United States Of America'
order by allnorms.dec desc  limit 40;
