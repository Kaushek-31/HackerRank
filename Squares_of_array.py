def sortedSquares(self, nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        nums[i] *= nums[i]
    nums = sorted(nums)
    return nums