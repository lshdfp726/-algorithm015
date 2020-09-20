# Definition for a binary tree node.
class TreeNode(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        nums = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    nums += 1
                    self.dfs(grid, i, j)
        
        return nums

    def dfs(self, grid, i, j):
        if self.isArea(grid, i, j) == True and grid[i][j] == '1':#理解为剪枝，不是‘1’的不需要关心
            grid[i][j] = '0'
            self.dfs(grid, i - 1, j)
            self.dfs(grid, i + 1, j)
            self.dfs(grid, i, j - 1)
            self.dfs(grid, i, j + 1)
    
    def isArea(self, grid, i, j):
        return 0 <= i < len(grid) and 0<= j < len(grid[i])


