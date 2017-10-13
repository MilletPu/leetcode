# coding=utf-8
# Given a binary array, find the maximum number of consecutive 1s in this array.
#
# Example 1:
#
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
# Note:
#
# · The input array will only contain 0 and 1.
# · The length of input array is a positive integer and will not exceed 10,000
#
# 给出一个0、1为元素的数组，找出最长的连续的1的子序列。例如[1,1,0,1,1,1]就是最后连续三个1是最长的的序列。
#
# 初始化max记录当前最长长度，count记录每个连续1子数组的长度。
#
# 开始从头遍历，用count来记录1的个数，遇到0时count归零，并将count与max比较，max用于记录当前最长连续1的个数。

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, max = 0, 0
        for num in nums:
            if num == 1:
                count += 1
                max = max if max > count else count
            else:
                count = 0
        return max


if __name__ == '__main__':
    s = Solution()
    print s.findMaxConsecutiveOnes([0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1])
