class Solution:
    def getRow(self, rowIndex):
       
        dp = [[1],[1,1]]
        temp =[1]
        count = 0
        while count < rowIndex-1:
            temp = [1]
            for i in range(len(dp[-1])-1):
                temp.append(dp[-1][i]+ dp[-1][i+1])
            temp.append(1)
            dp.append(temp)
            count += 1
        return dp[rowIndex]
