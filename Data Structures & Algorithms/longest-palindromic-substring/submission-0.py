class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest=""
        for i in range(len(s)):

            l,r=i,i

            while l>=0 and r<len(s) and s[l]==s[r]:
                win_length=r-l+1
                if len(longest)<len(s[l:r+1]):
                    longest=s[l:r+1]
                l-=1
                r+=1

            l=i
            r=i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                win_length=r-l+1
                if len(longest)<len(s[l:r+1]):
                    longest=s[l:r+1]
                l-=1
                r+=1
        return longest

               


                
            
