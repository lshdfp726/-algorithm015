class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(low, high):
            i, j = low, high
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        l = 0
        r = len(s) - 1
        while(l < r):
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return checkPalindrome(l+1,r) or checkPalindrome(l,r - 1)
        return True
    



if __name__ == "__main__":
    print(Solution().validPalindrome('"aba"'))