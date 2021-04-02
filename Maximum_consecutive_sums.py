def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, m, ma = 0, 0, 0

        for i in range(len(nums)):
            count += nums[i]
            if count == m:
                if count > ma:
                    ma = count
                count = 0
            m = count
            
            if i == len(nums)-1:
                if ma < count:
                    ma = count
                count = 0
        return ma
        