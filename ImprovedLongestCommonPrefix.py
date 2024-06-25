# ["flower","flow","flight"]
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Shortened and more line of code efficient version
        # but not as effectively
        shortest_str = min(strs, key=len)
        prefix = shortest_str

        # sort the array alphabetically results in similar strings being grouped together.
        strs = sorted(strs)

        for s in strs:
            # from index 0 to (not including) len(prefix)
            # e.g: len(prefix) is 4 then it would go from index 0 to 3
            while s[:len(prefix)] != prefix:
                # reduce the length of prefix by 1
                prefix = prefix[:-1]
                if not prefix:
                    return ""
            return prefix
                       
solution = Solution()
print(solution.longestCommonPrefix(["","","flight"]))
print(solution.longestCommonPrefix(["flower","flow","flight"]))
print(solution.longestCommonPrefix(["dog","racecar","car"]))
print(solution.longestCommonPrefix(["flower","flow","flows", "flock"]))