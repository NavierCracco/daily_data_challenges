'''
Plataforma: LeetCode
Problema: 2882. Drop Duplicate Rows
Dificultad: Easy

Descripción:
There are some duplicate rows in the DataFrame based on the email column.
Write a solution to remove these duplicate rows and keep only the first occurrence.
'''

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    df_drop_duplicates = customers.drop_duplicates(subset=['email'], keep='first')
    
    return df_drop_duplicates

if __name__ == "__main__":
    data = {
        'customer_id': [1, 2, 3, 4],
        'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'email': ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'charlie@example.com']
    }
    customers_df = pd.DataFrame(data)
    print(dropDuplicateEmails(customers_df))
    # Expected output:
    #    customer_id     name               email
    # 0            1   Alice    alice@example.com
    # 1            2     Bob    bob@example.com
    # 2            3 Charlie    charlie@example.com