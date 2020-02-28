# https://leetcode-cn.com/problems/text-justification/
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []  # 最后的答案
        cur_c = 0  # 当前行的字母数
        cur_w = 0  # 当前行的单词数
        wl = []  # 当前行的单词列表
        for i, wd in enumerate(words):
            l = len(wd)
            if cur_c + l + cur_w > maxWidth:  # 加上这个单词是否会超过最大长度
                if cur_w == 1:  # 当前行仅有一个超长的单词，后面全部补空格
                    ans.append(wl[0] + ' ' * (maxWidth - cur_c))
                else:
                    left = maxWidth - cur_c  # 这行一共有几个空格
                    if left % (cur_w - 1) == 0:  # 空格刚好平均分配
                        ans.append((' ' * (left // (cur_w - 1))).join(wl))
                    else:  # 空格不能平均分配
                        x = left % (cur_w - 1)  # 多余的空格
                        b = left // (cur_w - 1)  # 平均每个间隔最少的空格数
                        cans = wl[0]
                        for i in range(x):  # 前 x 个间隔空 b + 1 个
                            cans += ' ' * (b + 1) + wl[i + 1]
                        for i in range(x + 1, len(wl)):  # 后面的都空 b 个
                            cans += ' ' * b + wl[i]
                        ans.append(cans)
                cur_c = l
                cur_w = 1
                wl = [wd]
            else:
                cur_c += l
                cur_w += 1
                wl.append(wd)

        if cur_w > 0:  # 所有单词过完了把余下的词放入最后一行
            cans = ' '.join(wl)
            cans += ' ' * (maxWidth - len(cans))
            ans.append(cans)
        return ans

