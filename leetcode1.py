class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for num in range(length):
            for num2 in range(num, length):
                if nums[num] + nums[num2] == target and num != num2 :
                    return [num, num2]
        
