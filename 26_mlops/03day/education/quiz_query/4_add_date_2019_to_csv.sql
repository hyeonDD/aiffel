SELECT
    title, date_added
FROM
    netflix_titles
WHERE
	date_added between '2019-11-01' and '2019-11-30';
INTO OUTFILE '/var/lib/mysql-files/add_date_2019.csv'
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n';