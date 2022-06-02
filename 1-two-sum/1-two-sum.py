class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookfor = dict()
        
        for i in range(len(nums)):
            num = nums[i]
            other = target - num
            
            if num in lookfor:
                return sorted([lookfor[num], i])
            
            lookfor[other] = i
            