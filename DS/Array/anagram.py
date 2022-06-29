




def anagram(s1:str, s2: str)->bool:
    if len(s1) != len(s2):
        return False
    if len(s1) == 1:
        return s1 == s2
    string1 = {};
    string2 = {};
  
    for i in range(len(s1)):
        if not (s1[i] in string1):
            string1[s1[i]] = 1
        else:
             string1[s1[i]] += 1
            
        if not (s2[i] in string2):
            string2[s2[i]] = 1
        else:
             string2[s2[i]] += 1
    print(string1, string2)
        
    for key in string1:
        if key not in string2:
            return False
        if string1[key] != string2[key]:
            return False
        
    return True

print(anagram('abc', 'cbk'))
print(anagram('abc', 'cbk'))

        


