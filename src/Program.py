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

    return result


def makeMove(matrix, crossPlayer, i, j):
    symbol = 1 if crossPlayer else 2
    matrix[i][j] = symbol

    return matrix


def checkGameOver(matrix):
    # TODO: implement this method to check if game is over
    pass
