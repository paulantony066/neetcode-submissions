class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        

        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                temp=matrix[j][i]
                matrix[j][i]=matrix[i][j]
                matrix[i][j]=temp
        for i in range(len(matrix)):
            matrix[i]=matrix[i][::-1]

        

        