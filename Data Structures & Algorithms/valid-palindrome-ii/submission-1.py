class Solution:
    def validPalindrome(self, s: str) -> bool:
        chance=1

        left=0
        right=len(s)-1

        while left<right:
            if s[left]!=s[right]:
                l_removed=s[left+1:right+1]
                r_removed=s[left:right]

                if l_removed==l_removed[::-1]:
                    return True
                elif r_removed==r_removed[::-1]:
                    return True
                else:
                    return False
            left+=1
            right-=1
        return True

            
        