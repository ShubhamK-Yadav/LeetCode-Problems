import math

# Uses binary Search
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start_num = 0
        start = 1
        end = (x // 2) + 2
        mid = -1
        if x == 0 or x == 1: return x
        
        if x > 0:
          length = int(math.log10(x)+1)
          if(length < 5):
            # binary search
            
            while (start <= end):
                mid = start + (end - start) / 2
                if (mid * mid > x):
                  end = mid - 1
                elif (mid * mid == x):
                  return mid
                else:
                   start = mid + 1

            return math.floor(end)
          else:
            if (length % 2 == 0):
              start_num =  int(length / 2)
            else:
              start_num = int((length / 2)) + 1
            print(start_num)
            num = int(str(1) + '0'*(start_num))
            new_num = int(str(num)[:start_num])

            start = new_num
            end = num
            while (start <= end):
                mid = start + (end - start) / 2
                if (mid * mid > x):
                  end = mid - 1
                elif (mid * mid == x):
                  return mid
                else:
                   start = mid + 1

            return math.floor(end)

solution = Solution()
print(solution.mySqrt(2))
print(solution.mySqrt(183692038))
print(solution.mySqrt(2147395599))
print(solution.mySqrt(8))
print(solution.mySqrt(16))