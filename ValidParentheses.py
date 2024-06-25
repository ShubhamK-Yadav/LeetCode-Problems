# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Using a stack to find valid parentheses in string.
        # if c is any c in '({[', add to stack
        # else, if the stack is empty or
        # if the top of the stack is not the corresponding closing brace to c, return false, else pop stack.

        # if we have an empty stack after iterating through all c in the string and return True
        # otherwise false, since a closing brace for the corresponding open brace could not be found.
        stack = []
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if len(stack) == 0 or \
                    (c == ')' and stack[-1] != '(') or \
                    (c == '}' and stack[-1] != '{') or \
                    (c == ']' and stack[-1] != '['):
                    return False
                stack.pop()
        # if empty, returns true, if not empty, return false
        return not stack

solution = Solution()
print(solution.isValid("([{()}])"))
print(solution.isValid("([{(}])"))
print(solution.isValid("({}"))
print(solution.isValid("([()}])"))
print(solution.isValid("()["))
print(solution.isValid("([])()[]"))