from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        combinedword = ''
        for s in strs:
            combinedword += s + ';:'
        return combinedword

    def decode(self, s: str) -> List[str]:
        resultList = []
        pointer1 = 0
        pointer2 = -1

        for i in range(len(s)-1):
          if s[i] == ';' and s[i+1] == ':':
            pointer2 = i
            resultList.append(s[pointer1:pointer2])
            pointer1 = i+2
            i+=1
        return resultList