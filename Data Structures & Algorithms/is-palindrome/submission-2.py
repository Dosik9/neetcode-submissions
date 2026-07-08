class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        chars = "abcdefghijklmnopqrstuvwxyz0123456789"
        
        while left < right:
            if s[left].lower() not in chars:
                 left += 1
                 continue
            
            if s[right].lower() not in chars:
                right -= 1
                continue
            
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
        
        return True
