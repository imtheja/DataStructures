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

resultObject=HundredDaysChallenge()
#print(resultObject.maximumSubarraySumOfK([2, 3, 4, 1, 5], 2))
#print(resultObject.smallestSubarrarSumGreaterThank([3, 4, 1, 1, 6], 8))
#print(resultObject.longestSubstringWithKDistinctChars("araaci", 1))
#print(resultObject.longestSubstringAfterReplacingKLetters("abccde", 1))
#print(resultObject.maximumFruitsInBaskets(['A', 'B', 'C', 'B', 'B', 'C']))
