class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s.len() != t.len():
            return False
        return sorted(s) == sorted(t)
            