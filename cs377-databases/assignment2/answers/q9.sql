/*
THIS CODE WAS OUR OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING ANY
SOURCES OUTSIDE OF THOSE APPROVED BY THE INSTRUCTOR. 
Bhargav Annigeri, Simon Marty
*/

SET search_path to artistdb;

--      What this does
-- update end_year for adam levine in maroon 5
-- update end_year for mick jagger with the rolling stones
-- update start year for mick jagger in maroon 5

UPDATE wasinband
SET end_year = 2014
WHERE artist_id = ANY (
    Select artist_id
    FROM artist
    where name = 'Adam Levine' 
    or name = 'Mick Jagger'
);

INSERT INTO wasinband (artist_id, band_id, start_year, end_year)
VALUES(
    (SELECT artist_id FROM artist where name = 'Mick Jagger'),
    (SELECT artist_id FROM artist where name = 'Maroon 5'),
    2014, 2020 -- 2020 was the default end year for other tuples, assuming it's the same here
);
