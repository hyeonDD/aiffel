SELECT
    title
FROM
    netflix_titles
WHERE
    release_year = 2019
INTO OUTFILE '/var/lib/mysql-files/new.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';