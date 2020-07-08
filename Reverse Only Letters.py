class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        kitu = [c for c in S if c.isalpha()]
        kq = []
        for c in S:
            if c.isalpha():
                kq.append(kitu.pop())
            else:
                kq.append(c)
        return "".join(kq)