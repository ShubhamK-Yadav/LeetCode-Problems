# ["flower","flow","flight"]
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # The concept, find min length in the strings, use the length to get substring of two strings and compare them.
        # if the substrings do not match, lower the min_length by 1, if some substring matches proceed to the string and do the same
        # else if nothing matches return ""

        i = 0
        min_length = 12222
        for s in strs:
            if len(s) < min_length:
                min_length = len(s)       
        
        if min_length <= 0:
            return ""
        
        while (min_length > 0):
            frst_str = strs[i]
            if i+1 < len(strs): 
                snd_str = strs[i+1]
                if(frst_str[0:min_length] == snd_str[0:min_length]):
                    if(i+1 < len(strs)):
                        i += 1
                    else:
                        if(min_length <= 0):
                            return ""
                        else:
                            return frst_str[0:min_length]
                else:
                    min_length -= 1
                    if(min_length <= 0):
                            return ""
            else:
                if(min_length <= 0):
                    return ""
                else:
                    return frst_str[0:min_length]
                
solution = Solution()
print(solution.longestCommonPrefix(["","","flight"]))
print(solution.longestCommonPrefix(["flower","flow","flight"]))
print(solution.longestCommonPrefix(["dog","racecar","car"]))
print(solution.longestCommonPrefix(["flower","flow","flows", "flock"]))