class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_array = []
        t_array = []
        for i in range(len(s)):
            s_array.append(s[i])
            t_array.append(t[i])
        s_array.sort()
        t_array.sort()
        for i in range(len(s_array)):
            if s_array[i] == t_array[i]:
                continue
            else:
                return False
        return True
            