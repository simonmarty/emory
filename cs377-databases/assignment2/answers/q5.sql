/*
THIS CODE WAS OUR OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING ANY
SOURCES OUTSIDE OF THOSE APPROVED BY THE INSTRUCTOR. 
Bhargav Annigeri, Simon Marty
*/

SET search_path to artistdb;


SELECT DISTINCT Artist.name as artist_name, Album.title as album_name
FROM Album JOIN Artist on Album.artist_id = Artist.artist_id
WHERE Album.artist_id = ALL 
(
    SELECT songwriter_id 
    FROM Song JOIN BelongsToAlbum ON Song.song_id = BelongsToAlbum.song_id
    WHERE BelongsToAlbum.album_id = Album.album_id
)
ORDER BY artist_name ASC, album_name ASC
;
