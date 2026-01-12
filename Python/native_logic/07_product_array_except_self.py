'''
Plataforma: LeetCode
Problema: 238. Product of Array Except Self
Dificultad: Medium

Descripción:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation
'''

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [0] * n

        # 1. Left sweep (prefix)
        # answer[i] will contain the product of all elements to the LEFT of i
        answer[0] = 1
        for i in range(1, n):
            answer[i] = nums[i - 1] * answer[i - 1]

        # 2. Right sweep (suffix)
        # We calculate the product on the right on the fly and update answer
        right_product = 1
        for i in range(n - 1, -1, -1):
            # We multiply what we already had (left) by the new thing (right)
            answer[i] = answer[i] * right_product

            # We update the total on the right for the next step.
            right_product = right_product * nums[i]
        
        return answer
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf([1,2,3,4]))  # Expected output: [24,12,8,6]
    print(solution.productExceptSelf([-1,1,0,-3,3]))  # Expected output: [0,0,9,0,0]