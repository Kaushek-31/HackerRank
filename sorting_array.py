def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
    sorted_array = []
    for i in range(len(nums)):
        sorted_array.insert(index[i], nums[i])
    return sorted_array