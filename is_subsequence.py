class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > 0:
            i = 0
            for j in t:
                if s[i] == j:
                    i += 1
            if i == len(s):
                return True
            return False
        return True
    
x = Solution()

x.isSubsequence('abca','rabsrca')

