class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        pair = {"IV" : 4, "IX" : 9, "XL" : 40, "XC" : 90, "CD" : 400, "CM" : 900}
        str_len = len(s)
        sum = 0
        i = 0;
        while i < str_len:
            if i+1 < str_len:
                
                sub_str = s[i:i+2]
            if i + 1 < str_len and sub_str in pair:
                sum += pair[sub_str]
                i += 2
            else:
                sum += roman_to_int[s[i]]
                i += 1
        return sum
        
# solution = Solution()
# assert solution.romanToInt("III") == 3
# assert solution.romanToInt("LVIII") == 58
# assert solution.romanToInt("MCMXCIV") ==  1994
# assert solution.romanToInt("MCMXCIV") ==  1994
            
        