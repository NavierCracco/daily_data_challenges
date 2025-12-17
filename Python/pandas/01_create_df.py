'''
Plataforma: LeetCode
Problema: 2877. Create a DataFrame from List
Dificultad: Easy

Descripción:
Write a solution to create a DataFrame from a 2D list called student_data. This 2D list contains the IDs and ages of some students.
The DataFrame should have two columns, student_id and age, and be in the same order as the original 2D list.
'''

import pandas as pd

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    column_names = ["student_id", "age"]

    result_df = pd.DataFrame(student_data, columns = column_names)
    return result_df

if __name__ == "__main__":
    print(createDataframe([[1, 20], [2, 21], [3, 19], [4, 18]]))
    # Expected output:
    #    student_id  age
    # 0           1   20
    # 1           2   21
    # 2           3   19
    # 3           4   18
    
