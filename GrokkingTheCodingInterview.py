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



    def longestSubStringWithKChars(self, str, k):
        intStringLength=len(str)
        intMaxLength=0
        intStartIndex=0
        dictPlaceHolder={}

        for i in range(intStringLength):
            if str[i] not in dictPlaceHolder:
                dictPlaceHolder[str[i]]=1
            else:
                dictPlaceHolder[str[i]]+=1

            while len(dictPlaceHolder) > k:
                if dictPlaceHolder[str[intStartIndex]]==1:
                    del dictPlaceHolder[str[intStartIndex]]
                else:
                    dictPlaceHolder[str[intStartIndex]] -=1
                intStartIndex+=1

            if len(dictPlaceHolder)==k:
                intMaxLength = max(intMaxLength, sum(dictPlaceHolder.values()))

        return intMaxLength

    def fruitsIntoBasket(self, tree):
        intStringLength=len(tree)
        intMaxLength=0
        intStartIndex=0
        dictPlaceHolder={}

        for i in range(intStringLength):
            if tree[i] not in dictPlaceHolder:
                dictPlaceHolder[tree[i]]=1
            else:
                dictPlaceHolder[tree[i]]+=1

            while len(dictPlaceHolder) > 2:
                if dictPlaceHolder[tree[intStartIndex]]==1:
                    del dictPlaceHolder[tree[intStartIndex]]
                else:
                    dictPlaceHolder[tree[intStartIndex]] -=1
                intStartIndex+=1

            intMaxLength = max(intMaxLength, sum(dictPlaceHolder.values()))
        return intMaxLength

TestInstance=slidingWindow()
#print(TestInstance.maximumSumSubArray([2,1,5,1,3,2], 3))
#print(TestInstance.minimumSubArray([2, 1, 5, 2, 3, 2], 7))
#print(TestInstance.longestSubStringWithKChars("araaci", 1))
print(TestInstance.fruitsIntoBasket([0,1,2,2]))

