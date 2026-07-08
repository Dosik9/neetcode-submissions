class Solution:
    def isPalindrome(self, s: str) -> bool:
        characters = "!@#$%^&*()_+/*-+'?><~`.,[]{}:; "
        letter =""
        for c in s.lower():
            if c in characters:
                continue
            letter += c

        return letter == letter[::-1]