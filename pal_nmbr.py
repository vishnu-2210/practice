class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=reversed(str(x))
        rev_str = "".join(s)
        if(rev_str==str(x)):
            return True
        else:
            return False