#Grokking the coding interview
#Chapter 1. Sliding Window

class slidingWindow:
    def maximumSumSubArray(self, nums, k):
        intWindowSum= sum(nums[i] for i in range(k))
        intMaxSum=intWindowSum
        intArrayLength=len(nums)

        for i in range(0, intArrayLength-k):
            intWindowSum = intWindowSum - nums[i] + nums[i+k]
            intMaxSum = max(intWindowSum, intMaxSum)
        return intMaxSum

TestInstance=slidingWindow()
print(TestInstance.maximumSumSubArray([2,1,5,1,3,2], 3))

