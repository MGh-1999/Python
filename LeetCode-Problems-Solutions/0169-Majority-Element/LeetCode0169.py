""" LeetCode Problems: #169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1: Input: nums = [3,2,3]                    Output: 3
Example 2: Input: nums = [2,2,1,1,1,2,2]            Output: 2 """

def majorityElement(nums):
    dictionary = {}
    for num in nums:
        if num not in dictionary.keys():
            dictionary[num] = 1
        else:
            dictionary[num] += 1
    for key in dictionary.keys():
        if (dictionary[key] > len(nums) // 2):
            return key

nums = [3,2,3]
print(majorityElement(nums))