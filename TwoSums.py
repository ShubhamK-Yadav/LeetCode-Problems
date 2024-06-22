class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """ 
        found = False
        i = 0
        j = i + 1
        while(not found or i > len(nums)):
            if (nums[i] + nums[j] == target):
                found = True
                return [i, j]
            else:
                j += 1
            
            if j == len(nums):
                if i + 1 < len(nums) and i + 1 != j:
                    i += 1
                    j = i + 1
    
nums = [1,2,3,4,5,6]
target = 10
solution = Solution()
print("Hello!")
print(solution.twoSum(nums, target))