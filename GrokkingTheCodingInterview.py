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

    def noRepeatSubString(self,str):
        intStartIndex=0
        dictPlaceHolder={}
        intStrLength=len(str)
        intMaxLength=0

        for i in range(intStrLength):
            if str[i] not in dictPlaceHolder:
                dictPlaceHolder[str[i]]=1
            else:
                dictPlaceHolder[str[i]]+=1

            while dictPlaceHolder[str[i]] > 1:
                if dictPlaceHolder[str[intStartIndex]]>1:
                    dictPlaceHolder[str[intStartIndex]]-=1
                elif dictPlaceHolder[str[intStartIndex]]==1:
                    del dictPlaceHolder[str[intStartIndex]]
                intStartIndex+=1

            intMaxLength=max(intMaxLength, sum(dictPlaceHolder.values()))
        return intMaxLength

    def longestSubstringWithSubstitution(self, str, k):
        intMaxLength, intStartIndex, intCount=0, 0, 0
        intStringLength=len(str)
        dictPlaceHolder={}
        for i in range(intStringLength):
            if str[i] not in dictPlaceHolder:
                dictPlaceHolder[str[i]]=1
            else:
                dictPlaceHolder[str[i]]+=1

            intCount=max(dictPlaceHolder.values())
            while i-intStartIndex+1-intCount > k:
                dictPlaceHolder[str[intStartIndex]]-=1
                intStartIndex+=1

            intMaxLength=max(intMaxLength, i-intStartIndex+1)
        return intMaxLength

TestInstance=slidingWindow()
#print(TestInstance.maximumSumSubArray([2,1,5,1,3,2], 3))
#print(TestInstance.minimumSubArray([2, 1, 5, 2, 3, 2], 7))
#print(TestInstance.longestSubStringWithKChars("araaci", 1))
#print(TestInstance.fruitsIntoBasket([0,1,2,2]))
#print(TestInstance.noRepeatSubString("abccde"))
#print(TestInstance.longestSubstringWithSubstitution("abccde", 1))

class TwoPointers:
    def paitWithTargetSum(self, nums, target):
        intLengthNums=len(nums)
        intLeftPointer=0
        intRightPointer=intLengthNums-1

        while intLeftPointer<=intRightPointer:
            if nums[intLeftPointer]+nums[intRightPointer]==target:
                return [intLeftPointer, intRightPointer]
            elif nums[intLeftPointer]+nums[intRightPointer] < target:
                intLeftPointer+=1
            else:
                intRightPointer-=1
        return [-1,-1]

    def noDuplicatesArrayLength(self, nums):
        intLengthNums=len(nums)
        intNewArrayLength=1
        for i in range (1, intLengthNums):
            if nums[i-1] !=nums[i]:
                intNewArrayLength+=1
        return intNewArrayLength

    def squaringASortedArray(self, nums):
        intLengthNums=len(nums)
        intLeftIndex=0
        intRightIndex=intLengthNums-1
        intSquareIndex=intRightIndex
        listSquares=[0]*intLengthNums

        while intLeftIndex <= intRightIndex:
            if nums[intLeftIndex]**2 <= nums[intRightIndex]**2:
                listSquares[intSquareIndex]=nums[intRightIndex]**2
                intRightIndex-=1
                intSquareIndex-=1
            elif nums[intLeftIndex]**2 > nums[intRightIndex]**2:
                listSquares[intSquareIndex]= nums[intLeftIndex]**2
                intSquareIndex-=1
                intLeftIndex+=1
        return listSquares






TestInstance=TwoPointers()
#print(TestInstance.paitWithTargetSum([2,5,9,11], 11))
#print(TestInstance.noDuplicatesArrayLength([2, 2, 2, 11]))
print(TestInstance.squaringASortedArray([-3, -1, 0, 1, 2]))
