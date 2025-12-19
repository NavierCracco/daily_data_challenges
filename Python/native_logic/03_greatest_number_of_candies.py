'''
Plataforma: LeetCode
Problema: 1431. Kids With the Greatest Number of Candies
Dificultad: Easy

Descripción:
Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
'''

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:

        max_candies = max(candies)

        result = []
        for i in range(len(candies)):
            result.append(candies[i] + extraCandies >= max_candies)
        return result
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.kidsWithCandies([2,3,5,1,3], 3))  # Expected output: [True, True, True, False, True]
    print(solution.kidsWithCandies([4,2,1,1,2], 1))  # Expected output: [True, False, False, False, False]
    print(solution.kidsWithCandies([12,1,12], 10))   # Expected output: [True, False, True]