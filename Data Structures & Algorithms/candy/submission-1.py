class Solution:
    def candy(self, ratings: List[int]) -> int:

        arr=[1]*len(ratings)

        for i in range(len(ratings)):
            if i==0:
                continue
            if ratings[i]>ratings[i-1]:
                arr[i]=arr[i-1]+1
        for i in range(len(ratings)-1,-1,-1):
            if i==len(ratings)-1:
                continue
            if ratings[i+1]<ratings[i]:
                arr[i]=max(arr[i],arr[i+1]+1)
        return sum(arr)








        



        


