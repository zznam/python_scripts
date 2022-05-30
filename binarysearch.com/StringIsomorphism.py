class Solution:
    def solve(self, s, t):
        dict1 = {}
        dict2 = {}
        i = 0
        min = len(s)
        if (len(t) < min):
            min = len(t)
        for i in range(0, min):
            if s[i] in dict1:
                if (dict1[s[i]] != t[i]):
                    return False
            else:
                dict1[s[i]] = t[i]
            if t[i] in dict2:
                if (dict2[t[i]] != s[i]):
                    return False
            else:
                dict2[t[i]] = s[i]
        return True