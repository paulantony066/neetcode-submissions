class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        ss=""
        for i in s:
            if i.isalnum():
                ss+=i
        left=0
        right=len(ss)-1
        flag=0
        while left<=right:
            if ss[left]!=ss[right]:
                return False
            left+=1
            right-=1
        return True
            

