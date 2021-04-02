def twoSum(self, nums: List[int], target: int) -> List[int]:
    flag = 0
    s = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums), 1):
            if nums[i] + nums[j] == target:
                s.append(i)
                s.append(j)
                flag = 1
                break
        if flag == 1:
            break
    return s