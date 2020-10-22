/*
THIS CODE WAS OUR OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING ANY
SOURCES OUTSIDE OF THOSE APPROVED BY THE INSTRUCTOR. 
Bhargav Annigeri, Simon Marty
*/

SET search_path TO artistdb;

SELECT label_name AS record_label, year, sum(Album.sales) total_sales
FROM Album JOIN Producedby ON Album.album_id = Producedby.album_id
JOIN RecordLabel ON RecordLabel.label_id = Producedby.label_id
GROUP BY record_label, year
ORDER BY record_label, year;
