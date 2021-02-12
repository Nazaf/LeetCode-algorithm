class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x *= sign
        
#         while x:
#             if x % 10 == 0:
#                 x /= 10
#             else:
#                 break
                
        x = str(x)
        lst = list(x)
        
        lst.reverse()
        x = "".join(lst)
        x = int(x)
        if x > 1<<31:
            return 0
        
        return sign * x
