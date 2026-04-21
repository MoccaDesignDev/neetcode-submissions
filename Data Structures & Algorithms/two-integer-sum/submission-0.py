class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            keyval = {val:i for i, val in enumerate(nums)}
            for i, val in enumerate(nums):
                 complement = target - val
                 if complement in keyval and keyval[complement] != i:
                    return sorted([i, keyval[complement]])