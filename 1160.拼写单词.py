'''
Author: Zhou Hao
Date: 2021-02-24 20:50:16
LastEditors: Zhou Hao
LastEditTime: 2021-02-24 21:16:57
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1160 lang=python3
#
# [1160] 拼写单词
#

# @lc code=start
class Solution:
    # def countCharacters(self, words: List[str], chars: str) -> int:
    #     from collections  import Counter
    #     dict_chars = Counter(chars)

    #     res = 0
    #     for w in words:
    #         if not (Counter(w) - dict_chars):
    #             res += len(w)

    #     # print(res)
    #     return res


    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections  import Counter
        chars_cnt = Counter(chars)
        ans = 0
        for word in words:
            word_cnt = Counter(word)
            for c in word_cnt:
                if chars_cnt[c] < word_cnt[c]:
                    break
            else:
                ans += len(word)
        return ans


# @lc code=end

