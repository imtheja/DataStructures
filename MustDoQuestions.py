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


    def productExceptSelf(self, nums):
        output = [1]
        print ("output:", output)
        for n in nums[:len(nums)-1]:
            print ("output[-1] * n: ", output[-1] * n)
            output.append(output[-1] * n)
            print ("output.append: ", output)
        running_m = 1
        for i in range(len(nums)-2, -1, -1):
            print ("running_m: ", running_m)
            running_m *= nums[i+1]
            print ("running_m*: ", running_m)
            output[i] *= running_m
        print(output)

        return output

    def productExceptSelf(self,nums):
        listResult=[1]
        for i in range(1, len(nums)):
            listResult.append(nums[i-1]*listResult[i-1])
        print(listResult)
        intRunningProduct=1
        for i in range(len(nums)-1, -1, -1):
            listResult[i] *= intRunningProduct
            intRunningProduct *= nums[i]
        print(listResult)

    def findDuplicates(self, nums):
        output = []
        for i in range(len(nums)):
            print("i:", i)
            index = abs(nums[i]) - 1
            print("index:", index)
            if nums[index] < 0:
                output.append(index + 1)
                print("output:", output)

            nums[index] = - nums[index]
            print("nums[index]:", nums[index])
        print("final output:", output)
        return output

    def findDuplicatesInGivenRange(self, nums):
        listResult=[]
        for i in range(len(nums)):
            intGenerateIndex = abs(nums[i])-1
            if nums[intGenerateIndex] < 0 :
                listResult.append(intGenerateIndex+1)
            else:
                nums[intGenerateIndex] = -nums[intGenerateIndex]
        print (listResult)
        return listResult

    def setMatrixZero(self, matrix):
        intRowsLength=len(matrix)
        intColumnsLength=len(matrix[0])

        def setIndexToZero(rows, cols):
            for column in range(intColumnsLength):
                if matrix[rows][column] !=0:
                    matrix[rows][column]='0'
            for row in range(intRowsLength):
                if matrix[row][cols]!=0:
                    matrix[row][cols]='0'

        for i in range(intRowsLength):
            for j in range(intColumnsLength):
                if matrix[i][j]==0:
                    print(i,j)
                    setIndexToZero(i, j)
        print (matrix)
        return matrix

    def spiralOrder(self, matrix):
        m, n = len(matrix), len(matrix[0])
        i, first_row, first_col = 0, 0, 0
        last_row, last_col = m - 1, n - 1
        spiral_order = []
        # until a boundary overlaps
        while first_row <= last_row and first_col <= last_col:
            #left
            for i in range(first_row, last_col + 1):
                spiral_order.append(matrix[first_row][i])
            first_row += 1
            #down
            for i in range(first_row, last_row + 1):
                spiral_order.append(matrix[i][last_col])
            last_col -= 1
            # right
            if first_row <= last_row:
                i = last_col
                while i >= first_col:
                    spiral_order.append(matrix[last_row][i])
                    i -= 1
                last_row -= 1
             # up
            if first_col <= last_col:
                i = last_row
                while i >= first_row:
                    spiral_order.append(matrix[i][first_col])
                    i -= 1
                first_col += 1
        print(spiral_order)
        return spiral_order

    def spiral(self, matrix):
        intCounter=intfirstrow=intfirstcol=0
        intlastrow=len(matrix)-1
        intlastcol=len(matrix[0])-1
        listSpiral=[]

        while intfirstrow <=intlastrow and intfirstcol <=intlastcol:
            for i in range(intfirstrow, intlastcol+1):
                listSpiral.append(matrix[intfirstrow][i])
            intfirstrow+=1

            for i in range(intfirstrow, intlastrow+1):
                listSpiral.append(matrix[i][intlastcol])
            intlastcol-=1

            if intfirstrow <= intlastrow:
                i=intlastcol
                while i>=intfirstcol:
                    listSpiral.append(matrix[intlastrow][i])
                    i-=1
                intlastrow-=1
            if intfirstcol <=intlastcol:
                i=intlastrow
                while i>=intfirstrow:
                    listSpiral.append(matrix[i][intfirstcol])
                    i-=1
                intfirstcol+=1
        print(listSpiral)
        return listSpiral

    def rotateMatrix(self, matrix):
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[j][i], matrix[i][j]=matrix[i][j], matrix[j][i]
        print(matrix)
        return matrix

    def firstMissing(self, nums):
        if not nums:
            print("1")
            return 1
        listReference=[False]*(len(nums)+1)

        for i in nums:
            if 0 < i <= len(nums):
                listReference[i]=True

        for i in range(1, len(listReference)):
            if not listReference[i]:
                print(i)
                return i
        if not listReference:
            print("1")
            return 1
        return print(len(listReference))

    def longestConsequtive(self, nums):
        if not nums: return 0
        numsSet=set(nums)
        length=0
        maxlength=0
        for i in nums:
            if i-1 not in numsSet:
                length=0
                while i+length in numsSet:
                    length+=1
                maxlength=max(length, maxlength)
        return print(maxlength)



    #Binary Search

    def searchL(self, nums, target):
        intLength=len(nums)
        intLeftIndex=0
        intRightIndex=intLength-1

        while intLeftIndex <=intRightIndex:
            intMidvalue=(intLeftIndex+intRightIndex)//2
            if nums[intMidvalue]<=target:
                return print(intMidvalue)
            elif nums[intMidvalue] > target:
                intRightIndex=intMidvalue-1
            else:
                intLeftIndex=intMidvalue+1

        return -1

    def NextGreatLetter(self, nums, target):
        intLength=len(nums)
        intLeftIndex=0
        intRightIndex=intLength-1

        while intLeftIndex <=intRightIndex:
            intMidvalue=(intLeftIndex+intRightIndex)//2
            if nums[intMidvalue]<=target:
                intLeftIndex=intLeftIndex+1
            elif nums[intMidvalue] > target:
                intRightIndex=intMidvalue-1

        return print(nums[intLeftIndex])

    def findMountainI(self, nums):
        intLeftIndex=0
        intRightIndex=len(nums)-1
        while intLeftIndex<=intRightIndex:
            intMid=(intLeftIndex+intRightIndex)//2
            if nums[intMid-1] < nums[intMid] and nums[intMid] > nums[intMid+1]:
                return print(intMid)
            elif nums[intMid]<nums[intMid+1]:
                intLeftIndex=intMid+1
            elif nums[intMid] < nums[intMid-1]:
                intRightIndex =intMid-1
        return print("-1")


TestInstance=Questions()
#TestInstance.MoveZeros2([1,0,2,0,3,0,4,0,5,0,0,0,7,8,9])
#TestInstance.NumRescueBoats([1,2], 3)
#TestInstance.ValidMountainArray([0,3,2,1])
#TestInstance.ContainerWithMostWater([4,3,2,1,4])
#TestInstance.ContainerWithMostWater([1,1])
#TestInstance.ContainerWithMostWater([1,2,1])
#TestInstance.LongestSubstring("abcabcbb")
#TestInstance.TwoSum([7,2,11,15], 9 )
#TestInstance.productExceptSelf([1,2,3,4,5,6,7,8,9])
#TestInstance.findDuplicatesInGivenRange([4,3,2,7,8,2,3,1])
#TestInstance.spiralOrder([[1,1,1],[1,0,1],[1,1,1]])
#TestInstance.spiral([[1,1,1],[1,0,1],[1,1,1]])
#TestInstance.rotate([[1,2,3],[4,5,6],[7,8,9]])
#TestInstance.rotateMatrix([[1,2,3],[4,5,6],[7,8,9]])
#TestInstance.firstMissing([3,4,-1,1])
#TestInstance.longestConsequtive([100,4,200,1,3,2])
#TestInstance.searchL([-1,0,3,5,9,12], 9)
#TestInstance.NextGreatLetter(["c", "f", "j"], "k")
TestInstance.findMountainI([0,1,0])

