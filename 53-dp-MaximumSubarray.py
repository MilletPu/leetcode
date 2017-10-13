# coding=utf-8
# 经典的动态规划问题，最大子序列和。
# 之前做121的时候已经提到过了：请参考http://milletpu.com/2017/04/21/leet-dp-121/


class Solution:
    # 只要求给出最后的和。
    def maxSubArray(self, A):
        maxCur = Result = A[0]  # init = A[0]
        for x in A[1:]:
            maxCur = max(x, maxCur + x)
            Result = max(Result, maxCur)
        return Result

    # 这个可以输出具体的子序列。!!!
    def maxSubArray_record_series(self, A):
        maxCur = Result = A[0]  # init = A[0]
        start = end = 0
        for i, x in enumerate(A[1:], 1):  # 最后这个参数1是使enumerate的index从1开始计数
            if x > maxCur + x:
                maxCur, start = x, i
            else:
                maxCur, end = maxCur + x, i
            Result = max(Result, maxCur)

        print [A[i] for i in range(start, end + 1)]
        return Result


if __name__ == '__main__':
    s = Solution()
    print s.maxSubArray([-1, 2, -3, 1, 3, 4, -4, 6])
    print s.maxSubArray_record_series([-1, 2, -3, 1, 3, 4, -4, 6])
