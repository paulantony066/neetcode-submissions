class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref=strs[0]
        for i in range(len(strs[0])):
            for word in strs:
                if i==len(word) or word[i]!=pref[i]:
                    return word[:i]
        return pref
