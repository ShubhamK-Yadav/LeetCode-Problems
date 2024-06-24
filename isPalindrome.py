class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = str(x)
        new_num = ""
        i = len(num) - 1
        while (not (i < 0)):
            new_num += num[i]
            i -= 1

        if(new_num == num):
            return True
        else:
            return False

solution = Solution()
print(solution.isPalindrome(121))
print(solution.isPalindrome(122))
print(solution.isPalindrome(-122))
print(solution.isPalindrome(10))
print(solution.isPalindrome(1))