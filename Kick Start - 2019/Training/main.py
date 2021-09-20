class Solution:
    def __init__(self, n, p, s):
        self.n = int(n)
        self.p = int(p)
        self.s = sorted(s)
    
    def _hours(self, p):
        total = 0
        for i in range(len(p) - 1):
            total += p[-1] - p[i]
        return total
        
    def trainingHours(self):
        minCoaching = float('inf')
        for i in range(0, len(self.s)-1, self.p):
            minCoaching = min(minCoaching, self._hours(self.s[i:i+self.p]))
        return minCoaching
    
t = int(input())
for i in range(t):
    n, p = input().split()
    s = [int(x) for x in input().split()]
    sol = Solution(n, p, s)
    hours = sol.trainingHours()
    print('Case #{}: {}'.format(i+1, hours))
