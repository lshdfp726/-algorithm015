# Definition for a binary tree node.
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while(n!= 0):
            res += 1
            n &= (n - 1)
        
        return res

if __name__ == "__main__":
    print(Solution().hammingWeight(0x00000000000000000000000000001011))


