class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        # This works but the the .reverse is easy and pythonic way to make the 
        # array upside down
        # start = 0
        # end = rows - 1

        # while start < end:
        #     for i in range(cols):
        #         matrix[start][i], matrix[end][i] = matrix[end][i], matrix[start][i]
        #     start += 1
        #     end -= 1
        matrix.reverse()
        matrix[:] = [list(row) for row in zip(*matrix)]


        
         


        