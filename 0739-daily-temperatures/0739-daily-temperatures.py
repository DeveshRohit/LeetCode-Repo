class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)-1, -1, -1):
            while stack:
                if temperatures[i] >= temperatures[stack[-1]]:
                    stack.pop()
                else:
                    break
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res