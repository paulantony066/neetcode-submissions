class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        mat=[]

        for i in range(len(matrix[0])):
            mat.append([0]*len(matrix))

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                mat[j][i]=matrix[i][j]
        return mat