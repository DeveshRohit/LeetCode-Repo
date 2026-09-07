class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        minm = right
        while left <= right:
            total = 0
            k = (left+right) // 2
            for pile in piles:
                total += math.ceil(pile/k)
            if total <= h and k < minm:
                minm = k
                right = k - 1
            else:
                left = k + 1
        return minm