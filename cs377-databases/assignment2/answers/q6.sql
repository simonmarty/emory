/*
THIS CODE WAS OUR OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING ANY
SOURCES OUTSIDE OF THOSE APPROVED BY THE INSTRUCTOR. 
Bhargav Annigeri, Simon Marty
*/

SET search_path TO artistdb;

DROP VIEW IF EXISTS CanadianArtistsFirstAlbumIndie;

CREATE VIEW CanadianArtistsFirstAlbumIndie AS(
SELECT artist_id
FROM Album
Where 
(artist_id, year) IN ( -- album is his first
    SELECT Album.artist_id, min(year) as year
    FROM Album
    GROUP BY artist_id
)
AND (artist_id) IN ( -- artist is canadian
    SELECT artist_id 
    FROM Artist 
    WHERE nationality = 'Canada'
) 
AND (album_id) NOT IN ( -- Album is indie
    SELECT album_id
    FROM ProducedBy
)
);


SELECT Artist.name as artist_name
FROM Album JOIN Artist ON Album.artist_id = Artist.artist_id
WHERE album_id IN (
    SELECT album_id
    FROM ProducedBy JOIN RecordLabel ON ProducedBy.label_id = RecordLabel.label_id
    WHERE RecordLabel.country = 'America'
)
AND Artist.artist_id IN (
    SELECT artist_id FROM CanadianArtistsFirstAlbumIndie)
ORDER BY artist_name DESC;

DROP VIEW IF EXISTS CanadianArtistsFirstAlbumIndie;
