-- THIS WORK WAS MY (OUR) OWN WORK. IT WAS WRITTEN WITHOUT CONSULTING
-- WORK WRITTEN BY OTHER STUDENTS OR COPIED FROM ONLINE RESOURCES. Simon Marty

select vehiclelocationlatitude, vehiclelocationlongitude
from busdata
where publishedlinename LIKE 'M%'
and recordedattime LIKE '2017-06-01 00:%'
;
