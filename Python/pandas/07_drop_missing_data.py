'''
Plataforma: LeetCode
Problema: 2883. Drop Missing Data
Dificultad: Easy

Descripción:
There are some rows having missing values in the name column.

Write a solution to remove the rows with missing values.
'''

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    removed_missing_names = students.dropna(subset='name')
    return removed_missing_names

if __name__ == "__main__":
    data = {
        'student_id': [1, 2, 3, 4],
        'name': ['Alice', None, 'Charlie', 'David'],
        'age': [20, 21, 19, 22]
    }
    students_df = pd.DataFrame(data)
    print(dropMissingData(students_df))
    # Expected output:
    #    student_id     name  age
    # 0           1   Alice   20
    # 2           3 Charlie   19
    # 3           4   David   22