### Problem Statement ###

# A string s is called good if there are no two different characters in s that have the same frequency.

# Given a string s, return the minimum number of characters you need to delete to make s good.

# The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.


class Solution:
    def minDeletions(self, s: str) -> int:
        charLookUp = {}  # dictionary
        resultCount = 0
        for char in s:
            if char in charLookUp:
                charLookUp[char] += 1
            else:
                charLookUp[char] = 1

        while self.checkIfDuplicates(charLookUp.values()):
            for k in charLookUp.keys():
                if charLookUp[k] > 0:
                    occurance_count = list(charLookUp.values()).count(charLookUp[k])
                    if occurance_count > 1:
                        charLookUp[k] -= 1
                        resultCount += 1
        return resultCount

    def checkIfDuplicates(self, listOfElems) -> bool:
        frequencyCountList = [i for i in listOfElems if i != 0]
        setOfElems = set()
        for elem in frequencyCountList:
            if elem in setOfElems:
                return True
            else:
                setOfElems.add(elem)      
        return False

s = Solution()
### print(Solution.minDeletions(s, "baeccdae"))