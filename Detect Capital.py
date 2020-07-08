class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word == word.lower() or word == word.upper() or word == word.capitalize()

# https://leetcode.com/problems/detect-capital/