class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left,right):
            l=0
            r=0
            res=[]

            while l<len(left) and r<len(right):
                if left[l]<right[r]:
                    res.append(left[l])
                    l+=1
                else:
                    res.append(right[r])
                    r+=1
            if l<len(left):
                res.extend(left[l:])
            else:
                res.extend(right[r:])
            return res
        


        def mergesort(arr):
            if len(arr)<=1:
                return arr
            mid=len(arr)//2
            left=mergesort(arr[:mid])
            right=mergesort(arr[mid:])

            return merge(left,right)

        ans=mergesort(nums)
        return ans

        