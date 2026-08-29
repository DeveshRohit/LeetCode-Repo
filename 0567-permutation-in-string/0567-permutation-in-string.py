from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        freq = Counter(s1)
        for right in range(len(s1)-1, len(s2)):
            if(Counter(s2[left:right+1]) == freq):
                return True
            else:
                left+=1
                right+=1
        return False