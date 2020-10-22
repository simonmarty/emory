/*
THIS CODE WAS OUR OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING ANY
SOURCES OUTSIDE OF THOSE APPROVED BY THE INSTRUCTOR. 
Bhargav Annigeri, Simon Marty
*/

SET search_path TO artistdb;

DROP VIEW IF EXISTS Collabs;
DROP VIEW IF EXISTS NotCollabs;

CREATE VIEW Collabs AS (
    SELECT Artist.artist_id, avg(sales)
    FROM Album JOIN BelongsToAlbum
    ON Album.album_id = BelongsToAlbum.album_id
    JOIN Collaboration
    ON Collaboration.song_id = BelongsToAlbum.song_id
    JOIN Artist
    ON Artist.artist_id = Album.artist_id
    GROUP BY Artist.artist_id
);

CREATE VIEW NotCollabs AS (
    SELECT Album.artist_id, avg(sales)
    FROM Album
    WHERE Album.album_id NOT IN (
        SELECT album_id
        FROM Collaboration 
        JOIN BelongsToAlbum
        ON Collaboration.song_id = BelongsToAlbum.song_id
    )
    GROUP BY Album.artist_id
);

SELECT name , Collabs.avg as avg_collab_sales
FROM Collabs JOIN Artist 
ON Collabs.artist_id = Artist.artist_id
WHERE Collabs.avg > ALL (
    SELECT avg 
    FROM NotCollabs
    WHERE Collabs.artist_id = NotCollabs.artist_id
) AND Collabs.artist_id IN (SELECT artist_id FROM NotCollabs);

DROP VIEW IF EXISTS Collabs;
DROP VIEW IF EXISTS NotCollabs;
