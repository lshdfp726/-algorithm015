class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        #饼干尺寸map
        g.sort()
        s.sort()
        si,gi = 0,0
        while(gi < len(g) and si < len(s)):
            if  s[si]>= g[gi]:
                gi += 1
                si += 1
            elif s[si] < g[gi]:
                si += 1
        
        return gi

#时间复杂度 排序（n*logn） + loop(O(n)) n=min(len(g),len(s))
#空间复杂度 O(1)