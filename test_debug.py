import pandas as pd

print("Script iniciado")

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    print("Función llamada")
    selected_student = students.loc[students['student_id'] == 101, ['name', 'age']]
    print("Resultado:", selected_student)
    return selected_student

if __name__ == "__main__":
    print("Entrando al main")
    data = {
        'student_id': [100, 101, 102, 103],
        'name': ['John', 'Jane', 'Doe', 'Smith'],
        'age': [20, 21, 22, 23],
        'grade': ['A', 'B', 'C', 'D']
    }
    students_df = pd.DataFrame(data)
    print("DataFrame creado:", students_df)
    result = selectData(students_df)
    print("Resultado final:", result)