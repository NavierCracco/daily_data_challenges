'''
Plataforma: LeetCode
Problema: 2878. Get the Size of a DataFrame
Dificultad: Easy

Descripción:
Write a solution to calculate and display the number of rows and columns of players.
'''

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> list[int]:
    return [players.shape[0], players.shape[1]]

if __name__ == "__main__":
    players = pd.DataFrame({
        'player_id': [1, 2, 3],
        'name': ['Salah', 'Fernández', 'Saka'],
        'age': [33, 24, 24],
        'position': ['Forward', 'Midfielder', 'Forward'],
        'team': ['Liverpool', 'Chelsea', 'Arsenal']
    })
    print(getDataframeSize(players))  # Expected output: [3, 5]