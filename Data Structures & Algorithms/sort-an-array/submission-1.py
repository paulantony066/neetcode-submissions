class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left,right):
            lp,rp,k=0,0,0

            b=[]
            while lp<len(left) and rp<len(right):
                if left[lp]<right[rp]:
                    b.append(left[lp])
                    lp+=1
                else:
                    b.append(right[rp])
                    rp+=1
            b.extend(left[lp:])
            b.extend(right[rp:])
            return b
            l
            



        def mergesort(arr):
            if len(arr)<=1:
                return arr
            m=len(arr)//2
            left=mergesort(arr[:m])
            right=mergesort(arr[m:])

            return merge(left,right)


        ans=mergesort(nums)
        return ans