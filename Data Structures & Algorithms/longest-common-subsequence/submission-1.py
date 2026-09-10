
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp={}
        def subseq(i,j):
            if i==len(text1) or j==len(text2):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            elif text1[i]==text2[j]:
                dp[(i,j)]=1+subseq(i+1,j+1)
            else:
                dp[(i,j)]=max(subseq(i,j+1),subseq(i+1,j))
            return dp[(i,j)]
        return subseq(0,0)