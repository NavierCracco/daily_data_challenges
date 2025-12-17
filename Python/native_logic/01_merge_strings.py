'''
Plataforma: LeetCode
Problema: 1768. Merge Strings Alternately
Dificultad: Easy

Descripción:
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
'''
import itertools

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        for a, b in itertools.zip_longest(word1, word2, fillvalue=''):
            result.append(a)
            result.append(b)

        return ''.join(result)

if __name__ == "__main__":
    solution = Solution()
    print(solution.mergeAlternately('abc', 'pqr'))  # Expected output: "apbqcr"
    print(solution.mergeAlternately('ab', 'pqrs'))  # Expected output: "apbqrs"
    print(solution.mergeAlternately('abcd', 'pq'))  # Expected output: "apbqcd"