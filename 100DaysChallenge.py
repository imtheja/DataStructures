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


resultObject=HundredDaysChallenge()
#print(resultObject.maximumSubarraySumOfK([2, 3, 4, 1, 5], 2))
#print(resultObject.smallestSubarrarSumGreaterThank([3, 4, 1, 1, 6], 8))
#print(resultObject.longestSubstringWithKDistinctChars("araaci", 1))
print(resultObject.longestSubstringAfterReplacingKLetters("abccde", 1))
