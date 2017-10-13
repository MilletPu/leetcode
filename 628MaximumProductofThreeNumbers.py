# coding=utf-8
class Solution(object):
    def maximumProduct1(self, nums):
        res = []
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    res.append(nums[i] * nums[j] * nums[k])
        return max(res)


    def maximumProduct2(self, nums):
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])

if __name__ == '__main__':
    s = Solution()
    print s.maximumProduct2([5, 3, 4, 2, 6, 4, 9])

# leetcode提供的扫描方法，扫描找出(min1,min2), (max1,max2,max3)。
# 然后返回min1*min2*max1和 max1*max2*max3中最大的数。（http://milletpu.com/2017/08/26/leet-628/）