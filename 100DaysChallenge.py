import math

class HundredDaysChallenge:
    '''Given an array of positive numbers and a positive number ‘k’,
    find the maximum sum of any contiguous subarray of size ‘k’.
    '''

    def maximumSubarraySumOfK(self, nums, k):
        intWindowSum=intMaximumSum=sum(nums[:k])
        for i in range(len(nums)-k):
            intWindowSum=intWindowSum-nums[i]+nums[i+k]
            intMaximumSum=max(intWindowSum, intMaximumSum)
        return intMaximumSum

    '''
    Given an array of positive numbers and a positive number ‘S’, find the length 
    of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. 
    Return 0, if no such subarray exists. #read about self again and how to use 3.5 python
    '''
    def smallestSubarrarSumGreaterThank(self, nums, k):
        intStartIndex=0
        intSmallestSubArrayLength=math.inf
        intSubarraySum=0

        for intEndIndex in range(len(nums)):
            intSubarraySum+=nums[intEndIndex]
            while intSubarraySum >= k:
                intSmallestSubArrayLength=min(intSmallestSubArrayLength, intEndIndex-intStartIndex+1)
                intSubarraySum-=nums[intStartIndex]
                intStartIndex+=1

        if intSmallestSubArrayLength==math.inf:
            return 0
        else:
            return intSmallestSubArrayLength

    '''
    Given a string, find the length of the longest substring in it with no more than K distinct characters.
    '''
    def longestSubstringWithKDistinctChars(self, string, k):
        intLongestSubstring=0
        intStartIndex=0
        dictStaging={}
        for intEndIndex in range(len(string)):
            if string[intEndIndex] in dictStaging:
                dictStaging[string[intEndIndex]]+=1
            else:
                dictStaging[string[intEndIndex]]=1

            while len(dictStaging)>k:
                if dictStaging[string[intStartIndex]]==1:
                    del dictStaging[string[intStartIndex]]
                else:
                    dictStaging[string[intStartIndex]]-=1
                intStartIndex+=1

            if len(dictStaging)==k:
                #intLongestSubstring = max(intLongestSubstring, intEndIndex-intStartIndex+1)
                intLongestSubstring = max(intLongestSubstring, sum(dictStaging.values()))

        return intLongestSubstring

    '''
    Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters 
    with any letter, find the length of the longest substring having the same letters after replacement.
    '''
    def longestSubstringAfterReplacingKLetters(self, string, k):
        intLongestSubstring=0
        intSameCharacterCount=0
        intStartIndex=0
        dictStaging={}

        for intEndIndex in range(len(string)):
            if string[intEndIndex] in dictStaging:
                dictStaging[string[intEndIndex]]+=1
            else:
                dictStaging[string[intEndIndex]]=1

            intSameCharacterCount=max(dictStaging.values())

            while sum(dictStaging.values()) - intSameCharacterCount > k :
                if dictStaging[string[intStartIndex]]==1:
                    del dictStaging[string[intStartIndex]]
                else:
                    dictStaging[string[intStartIndex]]-=1
                intStartIndex+=1

            intLongestSubstring =max(intLongestSubstring, sum(dictStaging.values()))
        return intLongestSubstring

    '''
    Given an array of characters where each character represents a fruit tree, 
    you are given two baskets and your goal is to put maximum number of fruits in each basket. 
    The only restriction is that each basket can have only one type of fruit.
    You can start with any tree, but once you have started you can’t skip a tree. 
    You will pick one fruit from each tree until you cannot, i.e., you will stop when 
    you have to pick from a third fruit type.
    Write a function to return the maximum number of fruits in both the baskets.
    '''

    def maximumFruitsInBaskets(self, trees):
        dictStaging={}
        intStartIndex=0
        intMaxFruits=0
        for intEndIndex in range(len(trees)):
            if trees[intEndIndex] in dictStaging:
                dictStaging[trees[intEndIndex]]+=1
            else:
                dictStaging[trees[intEndIndex]]=1

            while len(dictStaging) > 2:
                if dictStaging[trees[intStartIndex]]==1:
                    del dictStaging[trees[intStartIndex]]
                else:
                    dictStaging[trees[intStartIndex]]-=1
                intStartIndex+=1
            intMaxFruits = max(intMaxFruits, sum(dictStaging.values()))
        return intMaxFruits
    '''
    Given a string, find the length of the longest substring which has no repeating characters.
    '''
    def longestSubstringWithNoRepeats(self, string):
        intStartIndex=intLongestSubString=0
        dictStaging={}
        for intEndString in range(len(string)):
            if string[intEndString] in dictStaging:
                dictStaging[string[intEndString]]+=1
            else:
                dictStaging[string[intEndString]]=1

            while len(dictStaging) < sum(dictStaging.values()):
                if dictStaging[string[intStartIndex]] == 1:
                    del dictStaging[string[intStartIndex]]
                else:
                    dictStaging[string[intStartIndex]]-=1
                intStartIndex+=1
            intLongestSubString = max(intLongestSubString, sum(dictStaging.values()))
        return intLongestSubString

    '''
    Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, 
    find the length of the longest contiguous subarray having all 1s.
    '''

    def lengthOfLongestSubstringWithOnes(self, nums, k):
        intStartIndex = intMaxLength = intOnesCount=0
        for intEndIndex in range(len(nums)):
            if nums[intEndIndex]==1:
                intOnesCount+=1
            while intEndIndex-intStartIndex+1 - intOnesCount > k:
                if nums[intStartIndex]==1:
                    intOnesCount-=1
                intStartIndex+=1
            intMaxLength=max(intMaxLength, intEndIndex-intStartIndex+1)
        return intMaxLength

    '''
    Given a string and a pattern, find out if the string contains any permutation of the pattern.
    '''
    def determinePermutationPattern(self, string, pattern):
        dictString = dictPattern = {}
        for patternChar in pattern:
            if patternChar not in dictPattern:
                dictPattern[patternChar]=1
            else:
                dictPattern[patternChar]+=1

        for stringIndex in range(len(string)):
            if stringIndex < len(pattern):
                if string[stringIndex] not in dictString:
                    dictString[string[stringIndex]]=1
                else:
                    dictString[string[stringIndex]]+=1
            else:
                if dictString[string[stringIndex-len(pattern)]]==1:
                    del dictString[string[stringIndex-len(pattern)]]
                else:
                    dictString[string[stringIndex-len(pattern)]]-=1

            if string[stringIndex] not in dictString:
                dictString[string[stringIndex]]=1
            else:
                dictString[string[stringIndex]]+=1

            if dictString == dictPattern:
                return True
        return False

    '''
    Given a string and a pattern, find out if the string contains any permutation of the pattern.
    Above problem, but in pure sliding window approach  "aaacb", "abc"
    '''
    def findPermutation(self, string, pattern):
        dictPattern={}
        intStartIndex=0
        intPatternMatched=0
        for char in pattern:
            if char not in dictPattern:
                dictPattern[char]=1
            else:
                dictPattern[char]+=1

        for intEndIndex in range(len(string)):
            if string[intEndIndex] in dictPattern:
                dictPattern[string[intEndIndex]] -= 1
                if dictPattern[string[intEndIndex]]==0:
                    intPatternMatched+=1

            if intPatternMatched == len(dictPattern):
                return True

            if intEndIndex > len(pattern)-1:
                if string[intStartIndex] in dictPattern:
                    if dictPattern[string[intStartIndex]]==0:
                        intPatternMatched-=1
                    dictPattern[string[intStartIndex]]+=1
                intStartIndex+=1
        return False


resultObject=HundredDaysChallenge()
#print(resultObject.maximumSubarraySumOfK([2, 3, 4, 1, 5], 2))
#print(resultObject.smallestSubarrarSumGreaterThank([3, 4, 1, 1, 6], 8))
#print(resultObject.longestSubstringWithKDistinctChars("araaci", 1))
#print(resultObject.longestSubstringAfterReplacingKLetters("abccde", 1))
#print(resultObject.maximumFruitsInBaskets(['A', 'B', 'C', 'B', 'B', 'C']))
#print(resultObject.longestSubstringWithNoRepeats("abccde"))
#print(resultObject.lengthOfLongestSubstringWithOnes([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
#print(resultObject.determinePermutationPattern("aaacb", "abc"))
print(resultObject.findPermutation("bcdxabcdy ", "bcdyabcdx"))
