def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i, flag = 0, 0
    while i+flag < len(nums):
        if nums[i] == 0:
            nums.append(nums.pop(i))
            flag += 1
        else:
            i += 1