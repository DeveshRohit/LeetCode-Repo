from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq = Counter(s1)
        window_freq = Counter(s2[:len(s1)]) #pre fill with first window

        if freq == window_freq:
            return True

        for i in range(len(s1), len(s2)):
            window_freq[s2[i]] += 1

            left_char = s2[i - len(s1)]
            window_freq[left_char] -= 1

            # deleting key if it hits 0 so that '==' check works
            if window_freq[left_char] == 0:
                del window_freq[left_char]

            if freq == window_freq:
                return True

        return False