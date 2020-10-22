/*
THIS CODE WAS OUR OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING ANY
SOURCES OUTSIDE OF THOSE APPROVED BY THE INSTRUCTOR. 
Bhargav Annigeri, Simon Marty
*/

SET search_path TO artistdb;

SELECT DISTINCT name, nationality
FROM artist
WHERE Extract(year FROM Artist.birthdate) = 
(SELECT min(year)
FROM album JOIN artist
ON album.artist_id = Artist.artist_id
WHERE artist.name = 'Steppenwolf')
AND NOT Artist.artist_id IN (
    SELECT Role.artist_id
    FROM Role
    WHERE role = 'Band'
)
ORDER BY name;
