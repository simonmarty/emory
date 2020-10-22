-- THIS WORK WAS MY (OUR) OWN WORK. IT WAS WRITTEN WITHOUT CONSULTING
-- WORK WRITTEN BY OTHER STUDENTS OR COPIED FROM ONLINE RESOURCES. Simon Marty

select vehiclelocationlatitude, vehiclelocationlongitude
from busdata
where publishedlinename = 'M86-SBS'
and destinationname LIKE '%WEST%'
;
