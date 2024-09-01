import gameLogic as logic

gameMatrix = logic.init()
crossPlayer = True
gameOver = False
logic.showGame(gameMatrix)

while True:
    playerTurn = "Cross" if crossPlayer else "Circle"

    print(playerTurn + " player, make your move: ")
    i = int(input())
    j = int(input())

    gameMatrix = logic.makeMove(gameMatrix, crossPlayer, i, j)
    crossPlayer = not crossPlayer
    
    logic.showGame(gameMatrix)

    gameOver = logic.checkGameOver(gameMatrix)
    print(gameOver)

    if gameOver:
        break
