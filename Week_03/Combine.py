import copy
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # n + 1 保证dfs上边界能取到n
        self.path = []
        self.res = []
        self.dfs(n + 1, k, 1)
        return self.res

    def dfs(self, n, k, start):
        #终止条件
        if k == 0:
            self.res.append(copy.copy(self.path))
            return 
        for i in range(start, n):
            #process logic
            self.path.append(i)
            #drill down
            self.dfs(n, k - 1, i + 1)
            self.path.pop() #reverse 
        return

#时间复杂度:O(n)
#空间复杂度:res:O(n/k) + path: O(N)= O(N)

