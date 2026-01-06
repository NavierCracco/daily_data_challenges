'''
Plataforma: LeetCode
Problema: 151. Reverse Words in a String
Dificultad: Medium

Descripción:
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        list_words = s.split()
        revers_string = " ".join(list_words[::-1])

        return revers_string

if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseWords("the sky is blue"))  # Expected output: "blue is sky the"
    print(solution.reverseWords("  hello world  "))  # Expected output: "world hello"
    print(solution.reverseWords("a good   example"))  # Expected output: "example good a"