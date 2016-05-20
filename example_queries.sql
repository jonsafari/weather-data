.echo ON

-- Listing of annual sunshine hours in Germany
select allnorms.station, name, annual_norms_computed from allnorms cross join station_meta where clim_elem_code == '15' and statistic_code == '44' and station_meta.country_name == 'Germany' and allnorms.country == station_meta.country and allnorms.station == station_meta.station order by `annual_norms_computed` ASC;

-- Listing of December sunshine hours in Germany
select allnorms.station, name, allnorms.dec from allnorms cross join station_meta where clim_elem_code == '15' and statistic_code == '44' and station_meta.country_name == 'Germany' and allnorms.country == station_meta.country and allnorms.station == station_meta.station order by allnorms.dec ASC;

-- Listing of December sunshine hours in US
select allnorms.station, name, allnorms.dec from allnorms cross join station_meta where clim_elem_code == '15' and statistic_code == '44' and station_meta.country_name == 'United States Of America' and allnorms.country == station_meta.country and allnorms.station == station_meta.station order by allnorms.dec ASC;
