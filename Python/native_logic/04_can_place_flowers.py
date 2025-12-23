'''
Plataforma: LeetCode
Problema: 605. Can Place Flowers
Dificultad: Easy

Descripción:
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
'''

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        
        if n <= 0:
            return True
        
        garden = [0] + flowerbed + [0]

        for i in range(1, len(garden) - 1):
            if garden[i] == 0 and garden[i - 1] == 0 and garden[i + 1] == 0:
                garden[i] = 1
                n -= 1
            
            if n <= 0:
                return True
        
        return n <= 0

if __name__ == "__main__":
    solution = Solution()
    print(solution.canPlaceFlowers([1,0,0,0,1], 1))  # Expected output: True
    print(solution.canPlaceFlowers([1,0,0,0,1], 2))  # Expected output: False
    print(solution.canPlaceFlowers([0,0,1,0,0], 2))  # Expected output: True