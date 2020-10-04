class Solution(object):
    # @lru_cache(None)
    def __init__(self):
        self.count = 0

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(s) == 1 and s[0] != '0':
            return 1
        if len(s) >= 2 and '10' < s[0:2] < '26':
            self.count = self.numDecodings(s[0:1]) + self.numDecodings(s[1:])
        else:
            self.count = self.numDecodings(s[1:]) 

        return self.count