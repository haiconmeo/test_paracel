class Solution(object):
    def licenseKeyFormatting(self, S, K):
    
        if (S == None or len(S) == 0) :
            return S
        
        kq=""
        for i in range((len(S)-1),-1,-1):
            if S[i] != '-':            
                if ((len(kq)) % (K + 1) == K ):
                    kq+='-'
                kq += S[i]
        
        return kq[::-1].upper()