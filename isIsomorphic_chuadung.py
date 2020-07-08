
def isIsomorphic(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        L = list(s)
        T = list(t)
        manh1 = dict(zip(L, T))
        print (manh1)
        for i in range(len(T)):
            print(T[i])
            L[i] = manh1[L[i]]
        if T==L :
            return True
        return False
print(isIsomorphic("egg","add"))


