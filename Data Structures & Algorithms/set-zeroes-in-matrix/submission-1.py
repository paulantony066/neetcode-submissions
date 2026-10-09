class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        seen1=set()
        seen2=set()


        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    seen1.add(i)
                    seen2.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in seen1 or j in seen2:
                    matrix[i][j]=0