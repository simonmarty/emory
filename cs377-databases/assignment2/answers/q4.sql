/*
THIS CODE WAS OUR OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING ANY
SOURCES OUTSIDE OF THOSE APPROVED BY THE INSTRUCTOR. 
Bhargav Annigeri, Simon Marty
*/

SET search_path to artistdb;

DROP VIEW IF EXISTS A1;
DROP VIEW IF EXISTS A2;
DROP VIEW IF EXISTS VarArtists;
DROP VIEW IF EXISTS VarSongwriters;

CREATE VIEW VarArtists AS (
  SELECT Album.artist_id as a_id, role, count(distinct genre_id) as genres
  FROM Album JOIN
  Role ON Album.artist_id = Role.artist_id
  GROUP BY Album.artist_id, Role 
  HAVING count(distinct genre_id) >= 3
  AND role <> 'Songwriter'
);

CREATE VIEW VarSongwriters AS (
  SELECT songwriter_id as a_id, role, count(distinct genre_id) as genres

  FROM Song JOIN BelongsToAlbum ON Song.song_id = BelongsToAlbum.song_id

  JOIN Album ON BelongsToAlbum.album_id = Album.album_id JOIN
  Role ON Song.songwriter_id = Role.artist_id
  JOIN Artist ON Album.artist_id = Artist.artist_id

  GROUP BY songwriter_id, role HAVING count(DISTINCT genre_id) >=3
  AND role = 'Songwriter'
);

CREATE VIEW a1 AS (
SELECT name as artist, role as capacity, genres, 0 as filter
  FROM VarArtists 
  JOIN Artist ON VarArtists.a_id = Artist.artist_id
  ORDER BY genres DESC, name ASC
);

CREATE VIEW a2 as (
  SELECT name as artist, role as capacity, genres, 1 as filter
  FROM VarSongwriters 
  JOIN Artist ON VarSongwriters.a_id = Artist.artist_id
  ORDER BY genres DESC, name ASC
);

SELECT artist, capacity, genres FROM
  (SELECT * FROM a1 UNION SELECT * FROM a2
  ORDER BY filter ASC) mix;

DROP VIEW IF EXISTS A1;
DROP VIEW IF EXISTS A2;
DROP VIEW IF EXISTS VarArtists;
DROP VIEW IF EXISTS VarSongwriters;
