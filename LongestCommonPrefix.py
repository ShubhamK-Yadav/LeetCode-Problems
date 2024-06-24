# ["flower","flow","flight"]
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_prefix = {}
        common_index = 0
        i = 0
        j=0
        length = 0
        for index in range(len(strs[i])):
             common_prefix[index] = strs[i][index]
        while(i < len(strs)):
          if strs[i] != strs[i+1]:
            if len(strs[i]) < len(strs[i+1]):
                length = len(strs[i])
            else:
                length = len(strs[i+1])
            if(strs[i][j] == strs[i+1][j]):
                if (j+1 < length):
                  j += 1
        print(common_prefix)

solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))