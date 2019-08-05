# assuming rotate 90 degrees clockwise
# perform by layers


def rotateMatrix(matrix):
    print('before rotation')
    printMarix(matrix)
    if len(matrix) != 0 and len(matrix) == len(matrix[0]):
        # only need to go at the half point, do not need to care about the middle point since the central cell does not need to be changed 
        for start in range(len(matrix)//2):
            end = len(matrix)-1-start
            # ends at end -1 since the cell at end has been replaced when i = 1
            for i in range(start, end):
                offset = i - start
                top = matrix[start][i]
                # left to top
                matrix[start][i] = matrix[end-offset][start]
                # bottom to left
                matrix[end-offset][start] = matrix[end][end - offset]
                # right to bottom
                matrix[end][end-offset] = matrix[start + offset][end]
                # top to right
                matrix[start + offset][end] = top
    print('after rotation')
    printMarix(matrix)


def printMarix(matrix):
    result = '\n'.join([' '.join(row) for row in matrix])
    print(result)


if __name__ == '__main__':
    rotateMatrix([[str(i) for i in range(3)], [
                 str(i) for i in range(3, 6)], [str(i) for i in range(6, 9)]])
