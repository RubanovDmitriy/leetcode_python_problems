class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split(' ')
        b = [x for x in a if x != '']
        return len(b[-1])
