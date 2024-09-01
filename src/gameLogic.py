def init():
    return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def showGame(matrix):
    result = ""

    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 1:
                result += "X"
            elif matrix[i][j] == 2:
                result += "O"
            else:
                result += "*"
        result += "\n"

    print(result)

def makeMove(matrix, crossPlayer, i, j):
    symbol = 1 if crossPlayer else 2
    if matrix[i][j] == 0:
        matrix[i][j] = symbol

    return matrix


def checkGameOver(matrix):
    for i in range(3):
        if (matrix[i][2] and matrix[i][0]) == matrix[i][1] and matrix[i][1] != 0:
            return True

    for j in range(3):
        if (matrix[2][j] and matrix[0][j]) == matrix[1][j] and matrix[1][j] != 0:
            return True

    if (matrix[0][0] and matrix[2][2]) == matrix[1][1] and matrix[1][1] != 0:
        return True
    elif (matrix[2][0] and matrix[0][2]) == matrix[1][1] and matrix[1][1] != 0:
        return True

    return False
