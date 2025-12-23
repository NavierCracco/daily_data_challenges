'''
Plataforma: LeetCode
Problema: 2880. Select Data
Dificultad: Easy

Descripción:
Write a solution to select the name and age of the student with student_id = 101.
'''

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:

    selected_student = students.loc[students['student_id'] == 101, ['name', 'age']]
    
    return selected_student

if __name__ == "__main__":
    data = {
        'student_id': [100, 101, 102, 103],
        'name': ['John', 'Jane', 'Doe', 'Smith'],
        'age': [20, 21, 22, 23],
        'grade': ['A', 'B', 'C', 'D']
    }
    students_df = pd.DataFrame(data)
    print(selectData(students_df))
    # Expected output:
    #    name  age
    # 1  Jane   21