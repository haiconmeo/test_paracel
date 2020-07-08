class Solution(object):
    def check(self,i):
        i=i.lower()
        hang1 = ['q','w','e','r','t','y','u','i','o','p']
        hang2 = ['a','s','d','f','g','h','j','k','l']
        hang3 = ['z','x','c','v','b','n','m']
        if i[0] in hang1:
            for ch in i:
                if ch not in hang1:
                    return False
        elif i[0] in hang2:
            for ch in i:
                if ch not in hang2:
                    return False
        else:
            for ch in i:
                if ch not in hang3:
                    return False
        return True
            
            
        
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        kq= []
        
        for i in words:
            if self.check(i):
                kq.append(i)
        return kq
            