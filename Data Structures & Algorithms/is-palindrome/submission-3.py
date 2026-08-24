class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        # skip alphanumeric characters from the left 
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[left].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return true 

            


        