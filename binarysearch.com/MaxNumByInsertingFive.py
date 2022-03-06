class Solution:
    def solve(self, n):
        ret = ""
        isAdd = False
        if n == 0:
            return 50
        elif n > 0:
            l = [int(d) for d in str(n)]
            for i in l:
                if (not isAdd and i < 5):
                    ret += str(5)
                    ret += str(i)
                    isAdd = True
                else:
                    ret += str(i)
            return int(ret)
        elif n < 0:
            n = -n
            l = [int(d) for d in str(n)]
            for i in l:
                if (not isAdd and i > 5):
                    ret += str(5)
                    ret += str(i)
                    isAdd = True
                else:
                    ret += str(i)
            if (not isAdd):
                ret += str(5)
            return -int(ret)