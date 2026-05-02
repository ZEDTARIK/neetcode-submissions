class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i+ 1, len(numbers)):
                if numbers[i+j] == target:
                    return numbers[i, j]
        return []
        
        