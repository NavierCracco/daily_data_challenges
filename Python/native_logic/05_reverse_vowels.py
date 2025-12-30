'''
Plataforma: LeetCode
Problema: 345. Reverse Vowels of a String
Dificultad: Easy

Descripción:
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        vowels = "aeiouAEIOU"
        i = 0
        j = len(s_list) - 1

        while i < j:
            if s_list[i] not in vowels:
                i += 1
            elif s_list[j] not in vowels:
                j -= 1
            else:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                
                i += 1
                j -= 1
            
            result = "".join(s_list)
            
        return result
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseVowels("hello"))  # Expected output: "holle"
    print(solution.reverseVowels("leetcode"))  # Expected output: "leotcede"