class Solution:
    def solve(self, tasks, people):
        n = len(tasks)
        m = len(people)
        tasks.sort()
        people.sort()
        flagP = 0
        ret = 0
        for i in range(0, n):
            while flagP < m and people[flagP] < tasks[i]:
                flagP += 1
            if (flagP < m):
                if (people[flagP] >= tasks[i]):
                    ret += 1
                    flagP += 1
            else:
                break
        return ret