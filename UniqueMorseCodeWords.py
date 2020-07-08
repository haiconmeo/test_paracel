class Solution(object):
    def uniqueMorseRepresentations(self, words):
 
        dic = {
            "a":".-",
            "b":"-...",
            "c":"-.-.",
            "d":"-..",
            'e':".",
            'f':"..-.",
            'g':"--.",
            'h':"....",
            'i':"..",
            'j':".---",
            'k':"-.-",
            'l':".-..",
            'm':"--",
            'n':"-.",
            'o':"---",
            'p':".--.",
            'q':"--.-",
            'r':".-.",
            's':"...",
            't':"-",
            'u':"..-",
            'v':"...-",
            'w':".--",
            'x':"-..-",
            'y':"-.--",
            'z':"--.."
        }


        # words = ["gin", "zen", "gig", "msg"]
        kq=[]
        for i in words:
            tam=""
            for ch in i:
                tam+=dic[ch]
            if tam in kq:
                continue
            kq.append(tam)

        return(len(kq))


kq = Solution()
print(kq.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
        
