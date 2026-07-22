class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        # Count frequency
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Sort by frequency (descending)
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        ans = []

        for i in range(k):
            ans.append(sorted_items[i][0])

        return ans