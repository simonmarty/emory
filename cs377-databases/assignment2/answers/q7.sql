/*
THIS CODE WAS OUR OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING ANY
SOURCES OUTSIDE OF THOSE APPROVED BY THE INSTRUCTOR. 
Bhargav Annigeri, Simon Marty
*/

set search_path to artistdb;

DROP VIEW IF EXISTS Covers;

CREATE VIEW Covers AS (

  SELECT DISTINCT b1.song_id, b1.album_id
  FROM belongsToAlbum b1, belongsToAlbum b2
  WHERE b1.song_id = b2.song_id
  AND b1.album_id <> b2.album_id

);

SELECT Song.title as song_name, Album.year, Artist.name as artist_name
FROM Covers
JOIN Album ON Covers.album_id = Album.album_id
JOIN Artist ON Album.artist_id = Artist.artist_id
JOIN Song ON Covers.song_id = Song.song_id
ORDER BY song_name, year, artist_name;

DROP VIEW IF EXISTS Covers;
