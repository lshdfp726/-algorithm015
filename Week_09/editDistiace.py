class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        if m * n == 0:
            return m + n

        dp = [[0] * (n + 1)  for _ in range(m + 1)]

        #边界初始化,由于考虑了空字符串在0的位置，所以i从1开始，相对于空字符串的变换步骤就是1...m
        for i in range(1, m + 1):
            dp[i][0] = i

        for j in range(1, n + 1):
            dp[0][j] = j

        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    #i - 1 和 j - 1 相等，意味着 word1 和Word2 当前末尾相同，可以直接替换，而且不需要+1步数
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    #取 三者操作中较小的步骤，并且需要 +1，因为是耗一个操作步骤。
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1 
        
        return dp[m][n]


if __name__ == "__main__":
    print(Solution().minDistance('intention','execution'))