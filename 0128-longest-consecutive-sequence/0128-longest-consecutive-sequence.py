class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        hset = set(nums)
        for num in hset:
            if num-1 not in hset:
                cur_num = num
                cur_streak = 1
                while cur_num+1 in hset:
                    cur_streak += 1
                    cur_num += 1
                if cur_streak > longest_streak:
                    longest_streak = cur_streak
                    
        return longest_streak