class Solution:
    def climbStairs(self, n):

        if n <= 2: 
            return n

        ways = [0 for _ in range(n)]
        ways[0] = 1
        ways[1] = 2

        for i in range(2, n):
            ways[i] += ways[i - 1] + ways[i - 2]

        return ways[-1]
