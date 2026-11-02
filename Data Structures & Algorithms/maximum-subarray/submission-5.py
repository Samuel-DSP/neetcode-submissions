class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]
        
        for num in nums[1:]:
            if current_sum + num > num:
                current_sum = current_sum + num
            else:
                current_sum = num
            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum
            
