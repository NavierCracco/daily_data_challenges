/*
Plataforma: LeetCode
Problema: 197. Rising Temperature
Dificultad: Easy

Descripción:
Table: Weather

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the column with unique values for this table.
There are no different rows with the same recordDate.
This table contains information about the temperature on a certain day.

 

Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).
*/

/* CTE */
WITH table_previous_date AS (
    SELECT
    id,
    recordDate,
    temperature,
    LAG(temperature) OVER (ORDER BY recordDate) AS "prev_temp",
    LAG(recordDate) OVER (ORDER BY recordDate) AS "prev_date"
    FROM Weather
)
SELECT 
    id
FROM table_previous_date
WHERE temperature > prev_temp
AND recordDate = prev_date + 1;


/* SELF-JOIN */
SELECT w1.id
FROM Weather AS w1
JOIN Weather AS w2 ON w1.recordDate = w2.recordDate + 1
WHERE w1.temperature > w2.temperature;