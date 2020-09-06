class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #左右双指针
        a,b = 0,len(nums) - 1
        #原数组下标和对应的值
        temp = []
        temp.extend(nums)
        nums.sort()
        while(True):
            if a == b:#相对说明没找到target
                break
            if nums[a] + nums[b] > target:
                b -= 1
            elif nums[a] + nums[b] < target:
                a += 1
            else:
                break
        
        #不相等说明找到target
        if a != b:
            fi = 0
            se = 0
            if nums[a] == nums[b]:
                fi = temp.index(nums[a])
                se = temp.index(nums[b],fi+1)
            else:
                fi = temp.index(nums[a])
                se = temp.index(nums[b])
                if fi > se:fi,se = se,fi
            return [fi,se]
        else:
            return []

if __name__ == '__main__':
    print(Solution().twoSum([3,2,4],6))