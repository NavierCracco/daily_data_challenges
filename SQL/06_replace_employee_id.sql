/*
Plataforma: LeetCode
Problema: 1378. Replace Employee ID With The Unique Identifier
Dificultad: Easy

Descripción:
Write a solution to show the unique ID of each user, If a user does not have a unique ID replace just show null.

Return the result table in any order.
*/

SELECT
    e.name,
    u.unique_id
FROM Employees AS e
LEFT JOIN EmployeeUNI AS u ON e.id = u.id;