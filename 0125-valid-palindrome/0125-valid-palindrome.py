class Solution:
    def isPalindrome(self, s: str) -> bool:
        flag = True
        i = 0
        j = len(s) - 1
        s = s.lower()

        while i<=j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i] != s[j]:
                    flag = False
                    break
                i += 1
                j -= 1
            elif not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
        
        return flag