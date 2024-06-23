import math
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start_num = 0
        if x == 0 or x == 1: return x
        
        if x > 0:
          length = int(math.log10(x)+1)
          if(length < 5):
            for i in range(2, (x//2)+2):
              square = i * i
              if x // i == i:
                  return i
              elif square > x:
                  return i - 1
          else:
            if (length % 2 == 0):
              start_num =  int(length / 2)
            else:
              start_num = int((length / 2)) + 1

            num = int(str(1) + '0'*(start_num))
            new_num = int(str(num)[:start_num])      
            for i in range (new_num, num):
              square = i * i
              # print("i is {}, square is {}".format(i, square))
              if x // i == i:
                  return i
              elif square > x:
                  return i - 1
              
solution = Solution()
print(solution.mySqrt(2))
print(solution.mySqrt(183692038))
print(solution.mySqrt(2147395599))
print(solution.mySqrt(8))
print(solution.mySqrt(16))