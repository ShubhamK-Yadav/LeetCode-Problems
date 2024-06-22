class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        int_value = 0
        i = len(s) - 1
        roman = {
            "I": 1,
            "V" : 5,
            "X" : 10,
            "L" : 50, 
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        while (i >= 0):
          if s[i] == 'X' and i > 0 and s[i-1] == 'I':
            int_value += 9
            i -= 2
          elif s[i] == 'V' and i > 0 and s[i-1] == 'I':
            int_value += 4
            i -= 2
          elif s[i] == 'L' and i > 0 and s[i-1] == 'X':
            int_value += 40
            i -= 2
          elif s[i] == 'C' and i > 0 and s[i-1] == 'X':
            int_value += 90
            i -= 2
          elif s[i] == 'D' and i > 0 and s[i-1] == 'C':
            int_value += 400
            i -= 2
          elif s[i] == 'M' and i > 0 and s[i-1] == 'C':
            int_value += 900
            i -= 2  
          else:
             int_value += roman.get(s[i])
             i -= 1
        return int_value

solution = Solution()
print(solution.romanToInt("IV"))
print(solution.romanToInt("IX"))
print(solution.romanToInt("MMCDIV"))