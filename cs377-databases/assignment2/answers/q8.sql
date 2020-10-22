/*
THIS CODE WAS OUR OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING ANY
SOURCES OUTSIDE OF THOSE APPROVED BY THE INSTRUCTOR. 
Bhargav Annigeri, Simon Marty
*/

SET search_path to artistdb;

INSERT INTO WasInBand(artist_id,band_id, start_year, end_year)
  (
    SELECT WasInBand.artist_id, band_id, 2018, 2019 FROM WasInBand
    JOIN Artist ON WasInBand.band_id = Artist.artist_id
    WHERE Artist.name = 'AC/DC'
  );
