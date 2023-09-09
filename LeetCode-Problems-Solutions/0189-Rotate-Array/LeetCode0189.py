""" LeetCode Problems: #189. Rotate Array

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1: Input: nums = [1,2,3,4,5,6,7], k = 3
           Output: [5,6,7,1,2,3,4]
Example 2: Input: nums = [-1,-100,3,99], k = 2
           Output: [3,99,-1,-100]
"""

def rotate(nums, k):
    k %= len(nums)
    for i in range(k):
        nums.insert(0,nums.pop(-1))

nums = [1,2,3,4,5,6,7]
k = 3

rotate(nums, k)
print(nums)