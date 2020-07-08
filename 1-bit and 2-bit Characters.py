class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        tam = 0
        while tam < len(bits) - 1:
            if bits[tam]:
                tam+=2
            else :
                tam +=1
            
            
        return tam == len(bits) - 1

# https://leetcode.com/problems/1-bit-and-2-bit-characters/