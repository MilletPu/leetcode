# coding=utf-8

# 35. Search Insert Position
#
# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0
#

# 二分查找
# 二分查找算法就是不断将数组进行对半分割，每次拿中间元素和goal进行比较。

class Solution(object):
    def searchInsert(self, nums, target):

        leftIndex = 0  # 左指针
        rightIndex = len(nums) - 1  # 右指针

        while leftIndex <= rightIndex:
            middle = leftIndex + (rightIndex - leftIndex) / 2  # 取中点middle，直接使用(left+right)/2也许会导致溢出
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                rightIndex = middle - 1  # rightIndex移动到先前中点middle的左侧（折半了）
            elif nums[middle] < target:
                leftIndex = middle + 1  # leftInde移动到先前中点middle的右侧（折半了）

        return leftIndex  # 当target不存在的时候，直接return左指针就就可以了！思考一下过程就知道了！


if __name__ == '__main__':
    array = [1, 3, 5, 6, 9]
    so = Solution()
    print so.searchInsert(array, 2)
