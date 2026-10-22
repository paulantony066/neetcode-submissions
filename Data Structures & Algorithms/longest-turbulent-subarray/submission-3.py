class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        s=""
        if len(arr)==1:
            return 1
        for i in range(1,len(arr)):
            if arr[i-1]<arr[i]:
                s+='<'
            elif arr[i-1]>arr[i]:
                s+='>'
            else:
                s+='='
    
        if s[0]!='=':
            longest=1
            curr=1
        else:
            longest=0
            curr=0


        l=0

        for i in range(1,len(s)):
            if s[i]=='=':
                curr=0
            elif s[i]!=s[i-1] and s[i]!='=':
                curr+=1
            else:
                curr=1
            longest=max(longest,curr)
        return longest+1


