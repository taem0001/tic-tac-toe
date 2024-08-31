import Program as prog

gameMatrix = prog.init()
crossPlayer = True

while True:
    print(prog.showGame(gameMatrix))
    playerTurn = "Cross" if crossPlayer else "Circle"

    print(playerTurn + " player, make your move: ")
    i = int(input())
    j = int(input())

    prog.makeMove(gameMatrix, crossPlayer, i, j)
    crossPlayer = not crossPlayer
