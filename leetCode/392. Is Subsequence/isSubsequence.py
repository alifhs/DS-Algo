class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        charAt = 0
        lastMatchedChar = ""
        numOfMatchedChars = 0
        for i in range(0, len(t)):
            if(numOfMatchedChars == len(s)):
                return True
            if s[charAt] == t[i]:
                # lastMatchedChar = s[charAt]
                charAt += 1
                numOfMatchedChars += 1
                
        if(numOfMatchedChars == len(s)):
                return True     
        else:
            return False

# assertion

# solution = Solution()
# assert solution.isSubsequence("abc", "ahbgdc") == True
# assert solution.isSubsequence("axc", "ahbgdc") == False
# assert solution.isSubsequence("ace", "aaecce") == True
# assert solution.isSubsequence("a", "aaece") == True
# assert solution.isSubsequence("aaaa", "aaaaece") == True
