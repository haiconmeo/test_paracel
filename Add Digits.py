class Solution(object):
    def add(self,n):
        tong = 0
        while True:
            if n == 0:
                break
            tong += n % 10
            n = n // 10
        return tong
    def addDigits(self,num):
        """
        :type num: int
        :rtype: int
        """
        kq = self.add(num)
        while True:
    
            chuoi = str(kq)
            if(len(chuoi)==1):
                break
            kq = self.add(kq)
        return kq