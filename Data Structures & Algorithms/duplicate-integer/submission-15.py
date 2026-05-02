class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dataSet = set()
        for i in nums:
            if i in dataSet:
                return True
            dataSet.add(i)    
        return False
        # return Set(nums).count < nums.count