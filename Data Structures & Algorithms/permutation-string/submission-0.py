class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = {}
        for c in s1:
            s1_count[c] = s1_count.get(c, 0) +1
        
        window_count = {}
        for i in range(len(s1)):
            char = s2[i]
            window_count[char] = window_count.get(char, 0) +1

        if s1_count == window_count:
            return True

        l, r = 0, len(s1)

        while r<len(s2):
            new_char = s2[r]
            window_count[new_char] = window_count.get(new_char, 0) +1

            old_char = s2[l]
            window_count[old_char] -= 1
            if window_count[old_char] == 0:
                del window_count[old_char]

            l+=1
            r+=1 

            if s1_count == window_count:
                return True

        return False