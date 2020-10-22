/*
THIS CODE WAS OUR OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING ANY
SOURCES OUTSIDE OF THOSE APPROVED BY THE INSTRUCTOR. 
Bhargav Annigeri, Simon Marty
*/

set search_path to artistdb;

DROP TABLE IF EXISTS SongsInThriller;

CREATE TABLE SongsInThriller AS (
    SELECT *
    FROM BelongsToAlbum
    WHERE album_id = (SELECT album_id FROM Album WHERE title = 'Thriller')
);

DELETE FROM Collaboration
WHERE song_id = ANY (SELECT song_id FROM SongsInThriller);

DELETE FROM ProducedBy
WHERE album_id = (SELECT album_id FROM Album WHERE title = 'Thriller');

DELETE FROM BelongsToAlbum
WHERE song_id = ANY (SELECT song_id FROM SongsInThriller) OR album_id = (SELECT album_id FROM Album WHERE title = 'Thriller');

DELETE FROM Song
WHERE song_id = ANY (SELECT song_id FROM SongsInThriller);

DELETE FROM Album
WHERE title = 'Thriller'; 

DROP TABLE IF EXISTS SongsInThriller; 
