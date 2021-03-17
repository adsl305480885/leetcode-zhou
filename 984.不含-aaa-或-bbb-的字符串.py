#
# @lc app=leetcode.cn id=984 lang=python3
#
# [984] 不含 AAA 或 BBB 的字符串
#

# @lc code=start
class Solution:

    '''参考 767重构字符串'''
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = ''
        if a==b:
            for i in range(a+b):
                res += 'a' if i%2 ==0 else 'b'
            return res

        if abs(a-b) == 1:
            if a>b:
                for i in range(a+b):
                    res += 'a' if  i%2==0 else 'b'

            else:
                for i in range(a+b):
                    res += 'b' if  i%2==0 else 'a'
            return res


        times = sorted([['a',a],['b',b]],key=lambda x: x[1],reverse=True)
        long = 0
        while long != a+b:
            i = 0

            if times[i][1] >=2 and times[i+1][1] >=1:
                if abs(times[i][1]-times[i+1][1]) == 1:
                    if times[i][1] >times[i+1][1]:
                        for j in range(times[i][1] + times[i+1][1]):
                            res += times[i][0] if  j%2==0 else times[i+1][0]
                    else:
                        for j in range(times[i][1] + times[i+1][1]):
                            res += times[i+1][0] if  j%2==0 else times[i][0]
                    return res


                res += times[i][0]*2   #多的在前面，少的在后面
                res += times[i+1][0]
                long += 3
                times[i][1] -= 2
                times[i+1][1] -= 1

            # elif times[i][1] <2 or times[i+1][1] <1:
            else:
                res += times[i][0] * times[i][1]
                res += times[i+1][0] * times[i+1][1]
                break

        return res
# @lc code=end

