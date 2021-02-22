# https://leetcode-cn.com/problems/dota2-senate/
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        if n == 1:
            return 'Radiant' if senate == 'R' else 'Dire'
        senate = list(senate)
        while True:
            for i in range(n):
                if senate[i] == 'R':
                    # found = False
                    for j in range(i + 1, n):
                        if senate[j] == 'D':
                            senate[j] = 'B'
                            # found = True
                            break
                    else:
                        for j in range(i):
                            if senate[j] == 'D':
                                senate[j] = 'B'
                                # found = True
                                break
                        else:
                            return 'Radiant'
                elif senate[i] == 'D':
                    for j in range(i + 1, n):
                        if senate[j] == 'R':
                            senate[j] = 'B'
                            # found = True
                            break
                    else:
                        for j in range(i):
                            if senate[j] == 'R':
                                senate[j] = 'B'
                                # found = True
                                break
                        else:
                            return 'Dire'



# deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = collections.deque()
        dire = collections.deque()

        for i, ch in enumerate(senate):
            if ch == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant[0] + n)
            else:
                dire.append(dire[0] + n)
            radiant.popleft()
            dire.popleft()

        return "Radiant" if radiant else "Dire"
