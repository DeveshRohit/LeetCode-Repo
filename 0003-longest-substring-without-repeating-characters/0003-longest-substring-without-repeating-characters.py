class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        i, j = 0, 0
        hashset = set()
        while j<len(s):
            if hashset == {}:
                return 0
            if s[j] not in hashset:
                hashset.add(s[j])
                max_count = max(max_count, j - i + 1)
                j += 1
            else:
                hashset.remove(s[i])
                i += 1
        return max_count
                

            