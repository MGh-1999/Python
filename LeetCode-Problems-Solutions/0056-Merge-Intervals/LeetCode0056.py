""" LeetCode Problems: #56. Merge Intervals

Given an array of intervals where intervals[i] = [start_i, end_i], merge all 
overlapping intervals, and return an array of the non-overlapping intervals 
that cover all the intervals in the input.

Example 1: Input: intervals = [[1,3],[2,6],[8,10],[15,18]]          Output: [[1,6],[8,10],[15,18]]
Example 2: Input: intervals = [[1,4],[4,5]]                         Output: [[1,5]] """

def merge(intervals):
    for i in range(len(intervals) - 1):
        for j in range(i+1,len(intervals)):
            if (intervals[i][0] > intervals[j][0]):
                intervals[i], intervals[j] = intervals[j], intervals[i]
    merged_intervals = []
    while (len(intervals) > 1):
        overlap = 1 if (intervals[0][1] >= intervals[1][0]) else 0
        if overlap:
            new_interval = [intervals[0][0],max(intervals[0][1],intervals[1][1])]
            del intervals[0:2]
            intervals.insert(0,new_interval)
        else:
            merged_intervals.append(intervals.pop(0))
    merged_intervals.append(intervals[0])
    return merged_intervals

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))