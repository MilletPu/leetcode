# coding=utf-8

# 119. Pascal's Triangle II
#
# Given an index k, return the kth row of the Pascal's triangle.
#
# For example, given k = 3,
# Return [1,3,3,1].
#
# Note:
# Could you optimize your algorithm to use only O(k) extra space?

# 杨辉三角，打印出第k行的所有数字。（从第0行开始计数）
# 我发现每一行都等于上一行错一位相加自己。
# 例如：
# 第3行的[1 3 3 1]等于第2行的[0 1 2 1] + [1 2 1 0]。
# 第4行的[1 4 6 4 1]等于第3行的[0 1 3 3 1] + [1 3 3 1 0]。
import numpy as np

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row


if __name__ == '__main__':
    s = Solution()
    print s.getRow(4)