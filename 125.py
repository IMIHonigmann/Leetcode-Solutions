import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        backwardsLetters = ''
        
        for i in range(len(s)-1, -1, -1):
            backwardsLetters += s[i]

        if(backwardsLetters == s):
            return True
        else:
            return False