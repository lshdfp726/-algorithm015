class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #dp[i][j] = dp[i + 1]dp[j] + dp[i][j + 1]
        #minSum = max(dp[i+1][j],dp[i][j+1],d[i][j]) + d[i][j]
        l = len(grid)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == j == 0:continue
                elif i == 0:grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:grid[i][j] = grid[i - 1][j] + grid[i][j]
                else: grid[i][j] = min(grid[i - 1][j],grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]