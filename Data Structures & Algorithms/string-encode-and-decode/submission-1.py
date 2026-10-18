
from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""
        for char in strs:
            st += str(len(char)) + "#" + char
        return st

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            while s[j].isdigit():
                j += 1

            length = int(s[i:j])
            j += 1

            result.append(s[j:j + length])
            i = j + length

        return result
