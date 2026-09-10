class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0

        seen=set()

        l=0
        r=0
        curr=0
        while r<len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            longest=max(longest,(r-l+1))
            r+=1
        return longest


