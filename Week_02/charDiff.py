class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        mp = {}
        for index in range(len(s)):
            if s[index] in mp.keys():
                mp[s[index]] += 1
            else:
                mp[s[index]] = 1
                
        for index in range(len(t)):
            if t[index] in mp.keys():
                mp[t[index]] -= 1 
                if mp[t[index]] < 0:#对应的的字母记数一旦小于0说明肯定有不同的
                    return False
        return True


if __name__ == '__main__':
    print(Solution().twoSum([3,2,4],6))