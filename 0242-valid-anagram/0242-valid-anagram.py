class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dics = {}
        dicst = {}
        for char in s:
            if(char in dics.keys()):
                dics[char] += 1
            else:
                dics[char] = 1
        for char in t:
            if(char in dicst.keys()):
                dicst[char] += 1
            else:
                dicst[char] = 1
        return dics == dicst