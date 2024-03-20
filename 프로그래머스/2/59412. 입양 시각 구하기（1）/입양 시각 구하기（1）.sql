-- 코드를 입력하세요
# with time as (select date_format(datetime, '%H') HOUR, animal_id from animal_outs)

# SELECT HOUR, count(*) COUNT
# from time
# group by HOUR
# having hour > '08'
# order by hour
SELECT HOUR(DATETIME) AS HOUR, COUNT(*) AS COUNT
    FROM ANIMAL_OUTS
    GROUP BY HOUR 
    HAVING HOUR BETWEEN 9 AND 19
    ORDER BY HOUR;

# select hour(datetime) HOUR, count(*) COUNT
# from animal_outs
# group by hour
# having HOUR > 8
# order by HOUR;