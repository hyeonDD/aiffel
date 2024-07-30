SELECT 
    type as type_name, count(*) as cnt
FROM
    netflix_titles
GROUP BY
    type;