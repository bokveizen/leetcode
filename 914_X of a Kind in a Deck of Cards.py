# https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards/
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1:
            return False
        if len(deck) == 2:
            return deck[0] == deck[1]
        card_kind = set(deck)
        kind_num = len(card_kind)
        card_num = []
        for i in card_kind:
            card_num.append(deck.count(i))
        if 1 in card_num:
            return False
        min_num = min(card_num)
        if [i % min_num for i in card_num] == [0] * kind_num:
            return True
        fact = 2
        while fact <= min_num:
            if [i % fact for i in card_num] == [0] * kind_num:
                return True
            fact += 1
        return False


'''
class Solution(object):
    def hasGroupsSizeX(self, deck):
        from math import gcd
        import collections
        from functools import reduce
        vals = collections.Counter(deck).values()
        return reduce(gcd, vals) >= 2
'''
