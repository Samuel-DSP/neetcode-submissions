# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         temp = 0
#         can_reach = True
#         for i in range(len(nums)-2,-1,-1):
#             can_reach = False
#             if nums[i] == 0:
#                 temp += 1
#             elif temp != 0:
#                 if nums[i] < temp + 1:
#                     temp += 1
#                 else:
#                     temp = 0
#                     can_reach = True
#             else:
#                 can_reach = True

#         return can_reach

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= target:
                target = i

        return target == 0