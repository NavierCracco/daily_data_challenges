'''
Plataforma: LeetCode
Problema: 2881. Create a New Column
Dificultad: Easy

Descripción:
Write a solution to create a new column name bonus that contains the doubled values of the salary column.
'''

import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees


if __name__ == "__main__":
    data = {
        'employee_id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie'],
        'salary': [50000, 60000, 70000]
    }
    employees_df = pd.DataFrame(data)
    print(createBonusColumn(employees_df))
    # Expected output:
    #    employee_id     name  salary   bonus
    # 0            1   Alice   50000  100000
    # 1            2     Bob   60000  120000
    # 2            3  Charlie   70000  140000   
