'''
Plataforma: LeetCode
Problema: 2879. Display the First Three Rows
Dificultad: Easy

Descripción:
Write a solution to display the first 3 rows of this DataFrame.
'''

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

if __name__ == "__main__":
    data = {
        'employee_id': [1, 2, 3, 4, 5],
        'employee_name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'department': ['HR', 'Engineering', 'Marketing', 'Finance', 'Sales']
    }
    employees_df = pd.DataFrame(data)
    print(selectFirstRows(employees_df))
    # Expected output:
    #    employee_id employee_name   department
    # 0            1         Alice           HR
    # 1            2           Bob  Engineering
    # 2            3       Charlie     Marketing