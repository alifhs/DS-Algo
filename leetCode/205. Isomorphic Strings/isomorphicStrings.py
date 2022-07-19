class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if(len(s) == 1):
            return True
        mapper = {}
        mapper_t = {}
        for i in range(0, len(s)):
            if s[i] not in mapper:
                if(t[i] not in mapper_t):
                    mapper[s[i]] = t[i]
                    mapper_t[t[i]] = s[i]

                elif t[i] in mapper_t and (mapper_t[t[i]] != s[i]): #checks -> if contains two keys for one value
                    return False
                
            elif mapper[s[i]] != t[i]:
                return False
            
        return True

#assertion

# solution = Solution()
# assert solution.isIsomorphic("egg", "add") == True
# assert solution.isIsomorphic("foo", "bar") == False
# assert solution.isIsomorphic("paper", "title") == True
# assert solution.isIsomorphic("ab", "aa") == False
# assert solution.isIsomorphic("egge", "adad") == False
            


     
        