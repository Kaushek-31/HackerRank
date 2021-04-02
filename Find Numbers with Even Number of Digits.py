def findNumbers(self, nums: List[int]) -> int:
    total = 0
    for i in nums:
        st = list(str(i))
        count = len(st)
        if count % 2 == 0:
            total += 1
    return total