'''
Author: Zhou Hao
Date: 2021-02-05 17:25:51
LastEditors: Zhou Hao
LastEditTime: 2021-02-05 17:28:34
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    '''
        1.设置上下界 MAX_INT 和 MIN_INT
    2.先把被除数dividend和除数divisor转化为正数，保留商的正负即 flag 的正负
    3.核心思想：在被除数小于除数的条件下，第一次cur = divisor，
    4.判断divisor的1倍、2倍、4倍....2的n次方倍（这里用cur+cur使得判断的更快）是否小于dividend，是则保存倍数的值multiple，否则dividend-cur为新的dividend，multiple还原为1
    5.判断是否过界


    '''
    def divide(self, dividend: int, divisor: int) -> int:
        MIN_INT, MAX_INT = -2147483648, 2147483647
        flag = 1
        if dividend < 0:
            flag, dividend = -flag, -dividend
        if divisor < 0:
            flag, divisor = -flag, -divisor
        res = 0
        while dividend >= divisor:
            cur = divisor    #第一次是cur = divisor
            multiple = 1
            while cur+cur < dividend:
                cur += cur   # 这里是将cur x 2，即直接比较divisor x 2的次方（加快比较速度）
                multiple += multiple   # 保留divisor的倍数
            dividend -= cur    # dividend 变为 dividend-cur 进行下一轮while
            res += multiple   
        

        res = res if flag >0 else -res  #还原商的正负
    
        if res < MIN_INT:
            return MIN_INT
        elif res > MAX_INT:
            return MAX_INT
        else:
            return res  


# @lc code=end

