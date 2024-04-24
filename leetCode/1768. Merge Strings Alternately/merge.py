class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        mergedString = ""
        word1Len = len(word1)
        word2Len = len(word2)

        if word1Len == word2Len:

            for i in range(word1Len):
                mergedString += word1[i]
                mergedString += word2[i]

        elif word1Len < word2Len:
            for i in range(word1Len):
                mergedString += word1[i]
                mergedString += word2[i]

            mergedString += word2[word1Len-1:]

        elif word2Len < word1Len:
            for i in range(word2Len):
                mergedString += word1[i]
                mergedString += word2[i]

            mergedString += word1[word2Len-1:]
        return mergedString

