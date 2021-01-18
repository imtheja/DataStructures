#Leet Code Questions
#Arrays: Move Zeros. nums=[1,2,0,3]--> [1,2,3,0]
class Questions:
    def MoveZeros(self, nums):
        #Brute Force
        intCounter=0
        while intCounter < len(nums):
            for i in range(len(nums)-1):
                if nums[i] != nums[i+1] and nums[i]==0:
                    nums[i], nums[i+1]= nums[i+1], nums[i]
            intCounter+=1
        return print(nums)

    def MoveZeros2(self, nums):
        #Questions
        #Break it down to smallest pieces of work
        #Approach
        #0(n)
        #Space Complexity
        #Edge Cases
        #Where to improve
        intCounter=0
        for indx in range(len(nums)):
            if nums[indx]!=0:
                nums[intCounter]=nums[indx]
                intCounter+=1
        for paddingIndx in range(intCounter,len(nums)):
            nums[paddingIndx]=0
        print(nums)
        return nums

    def TwoSum(self, nums, target):
        dictStaging={}
        for indx, number in enumerate(nums):
            if target-number in dictStaging.keys():
                print([indx, dictStaging[target-number]])
                return [indx, dictStaging[target-number]]
            else:
                dictStaging[number] = indx
        return False

    def NumRescueBoats(self, weights, limit):
        #Questions: Weights are not going to be <=0
        weights.sort()
        print(weights)
        intBoatsRequired=0
        intLowerIndex=0
        intUpperIndex=len(weights)-1
        while intLowerIndex<=intUpperIndex:
            if intLowerIndex==intUpperIndex:
                intBoatsRequired+=1
                break
            if weights[intLowerIndex]+weights[intUpperIndex] <=limit:
                intBoatsRequired+=1
                intLowerIndex+=1
                intUpperIndex-=1
            else:
                intBoatsRequired+=1
                intUpperIndex-=1

        print(intBoatsRequired)
        return intBoatsRequired
    def ValidMountainArray(self, arr):
        #Questions
        #Break it down to smallest pieces of work
        #Approach: Two Forloops with a counter and validating counter
        #0(n)
        #Space Complexity
        #Edge Cases
        #Where to improve: where to start the counter number and what will it be in the end.
        if len(arr)<3:
            return False
        intCounter=1
        while intCounter < len(arr) and arr[intCounter]> arr[intCounter-1]:
            intCounter+=1
        if intCounter==1 or intCounter==len(arr)-1:
            return False
        while intCounter < len(arr) and arr[intCounter]< arr[intCounter-1]:
            intCounter+=1
        return print(intCounter==len(arr))

    def ContainerWithMostWater(self, nums):
        #Approach: 2 Pointers Approach
        #edgecase: when n is 0 (i misesed it)
        if len(nums)==0:
            return 0

        intLowerIndex=0
        intUpperIndex=len(nums)-1
        intMaxWater=0
        intArea=0
        while intLowerIndex < intUpperIndex:
            intArea=(intUpperIndex-intLowerIndex)*min(nums[intLowerIndex], nums[intUpperIndex])
            intMaxWater = max(intMaxWater, intArea)
            if nums[intLowerIndex]<=nums[intUpperIndex]:
                intLowerIndex+=1
            else:
                intUpperIndex-=1
        return print(intMaxWater)

    def LongestSubstring(self, strr):
        #Apprach as we have to get the length through indexes, lets have dict object for reference
        if len(strr)==0:
            return 0

        intMaxLength=0
        intStartIndex=0
        intRepeatingCharIndex=0
        dictCharReference={}
        for indx in range(len(strr)):
            if strr[indx] in dictCharReference:
                intRepeatingCharIndex=dictCharReference[strr[indx]]
                dictCharReference[strr[indx]]=indx
                if intRepeatingCharIndex >= intStartIndex:
                    intStartIndex=intRepeatingCharIndex+1
                intMaxLength=max(intMaxLength, (indx-intStartIndex)+1)
            else:
                dictCharReference[strr[indx]]=indx
                intMaxLength=max(intMaxLength, (indx-intStartIndex)+1)
        return print(intMaxLength)

    def FirstBadVersion(self, n, firstBadValue):
        intLeftIndex=1
        intRightIndex=n
        while intLeftIndex < intRightIndex:
            intMidValue=(intLeftIndex+intRightIndex)//2
            if intMidValue==firstBadValue:
                intRightIndex=intMidValue
            else:
                intLeftIndex=intMidValue+1
        print(intLeftIndex)
        return intLeftIndex

    def searchLeftRange(self, nums, target):
        intLeftIndex=0
        intRightIndex=len(nums)-1
        while intLeftIndex <= intRightIndex:
            intMidValue=(intLeftIndex+intRightIndex)//2
            if nums[intMidValue]==target and nums[intMidValue-1]!=target:
                print(intMidValue)
                return intMidValue
            elif nums[intMidValue]==target and nums[intMidValue-1]==target:
                intRightIndex = intMidValue-1
            elif nums[intMidValue]< target:
                intLeftIndex=intMidValue+1
            elif nums[intMidValue]>target:
                intRightIndex=intMidValue-1
        print("-1")
        return -1

    def searchRightRange(self, nums, target):
        intLeftIndex=0
        intRightIndex=len(nums)-1
        while intLeftIndex <= intRightIndex:
            intMidValue=(intLeftIndex+intRightIndex)//2
            if nums[intMidValue]==target and nums[intMidValue+1]!=target:
                print(intMidValue)
                return intMidValue
            elif nums[intMidValue]==target and nums[intMidValue+1]==target:
                intLeftIndex = intMidValue+1
            elif nums[intMidValue]< target:
                intLeftIndex=intMidValue+1
            elif nums[intMidValue]>target:
                intRightIndex=intMidValue-1
        print("-1")
        return -1

    def searchRange(self, nums, target):
        return [Questions.searchLeftRange(self, nums, target), Questions.searchRightRange(self, nums, target)]




TestInstance=Questions()
#TestInstance.MoveZeros2([1,0,2,0,3,0,4,0,5,0,0,0,7,8,9])
#TestInstance.NumRescueBoats([1,2], 3)
#TestInstance.ValidMountainArray([0,3,2,1])
#TestInstance.ContainerWithMostWater([4,3,2,1,4])
#TestInstance.ContainerWithMostWater([1,1])
#TestInstance.ContainerWithMostWater([1,2,1])
#TestInstance.LongestSubstring("abcabcbb")
#TestInstance.TwoSum([7,2,11,15], 9 )

