'''
Plataforma: LeetCode
Problema: 1071. Greatest Common Divisor of Strings
Dificultad: Easy

Descripción:
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
'''

import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        
        gcd_lenght = math.gcd(len(str1), len(str2))
        return str1[:gcd_lenght]

if __name__ == "__main__":
    solution = Solution()
    print(solution.gcdOfStrings('ABCABC', 'ABC'))  # Expected output: "ABC"
    print(solution.gcdOfStrings('ABABAB', 'ABAB'))  # Expected output: "AB"
    print(solution.gcdOfStrings('LEET', 'CODE'))    # Expected output: ""