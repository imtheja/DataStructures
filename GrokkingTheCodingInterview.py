#Grokking the coding interview
#Chapter 1. Sliding Window
import math
class slidingWindow:
    def maximumSumSubArray(self, nums, k):
        intWindowSum= sum(nums[i] for i in range(k))
        intMaxSum=intWindowSum
        intArrayLength=len(nums)

        for i in range(0, intArrayLength-k):
            intWindowSum = intWindowSum - nums[i] + nums[i+k]
            intMaxSum = max(intWindowSum, intMaxSum)
        return intMaxSum

    def minimumSubArray(self, nums, k):
        intWindowSum=0
        intStartIndex=0
        intMinSubArrayLength= math.inf
        intSubArrayLength=0
        intArrayLength=len(nums)
        for i in range(intArrayLength):
            intWindowSum+=nums[i]
            while intWindowSum >= k:
                intSubArrayLength = i - intStartIndex +1
                intMinSubArrayLength = min(intMinSubArrayLength, intSubArrayLength)
                intWindowSum -= nums[intStartIndex]
                intStartIndex += 1
        if intMinSubArrayLength == math.inf:
            return 0
        else:
            return intMinSubArrayLength














TestInstance=slidingWindow()
print(TestInstance.maximumSumSubArray([2,1,5,1,3,2], 3))
print(TestInstance.minimumSubArray([2, 1, 5, 2, 3, 2], 7))

