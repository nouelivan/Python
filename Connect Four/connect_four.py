# This program is a two player Connect Four game.

# Board creation.
board = [['  1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 '], ['+---+---+---+---+---+---+---+']]

for i in range(6):
    board.append(['|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'])
    board.append(['|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'])
    board.append(['|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'])
    board.append(['+---+---+---+---+---+---+---+'])


# Function to create a visually appealing board.
def print_board(field):
    for row in field:
        print(" ".join(row))


print_board(board)
print("Let's play!")


# Function responsible for the dropping of pieces.
def drop_piece():
    # User selects a piece.
    piece = input("\nChoose an X or an O piece: ").lower()

    while piece != "x" and piece != "o":
        print("\nPlease enter either an x or an 0.")
        piece = input("Choose an X or an O piece: ").lower()
        print(piece)

    # User selects a column.
    col = -1

    while col < 0 or col > 7:
        try:
            col = int(input("Please select a column between 1 and 7: \n"))
        except ValueError:
            print("Please enter a number.")
            continue

    new_col = col + (col - 1)

    for row in range(23, 0, -4):
        if board[row][new_col] == ' ':
            board[row][new_col] = piece
            result = game_over()
            if result:
                return
            break
        else:
            continue

    print_board(board)
    print("Change players!")

    drop_piece()


# Function checks for a winner or tie.
def game_over():
    # Check for a win vertically.
    for col in range(1, 14, 2):
        x_player = []
        o_player = []
        for row in range(3, 24, 4):
            if board[row][col] == "x":
                x_player.append("x")
                o_player = []
            elif board[row][col] == "o":
                o_player.append("o")
                x_player = []

            if len(x_player) == 4:
                print_board(board)
                print("X wins!")
                return True
            elif len(o_player) == 4:
                print_board(board)
                print("O wins!")
                return True

    # Check for a win horizontally.
    for row in range(3, 24, 4):
        x_player = []
        o_player = []
        for col in range(1, 14, 2):
            if board[row][col] == "x":
                x_player.append("x")
                o_player = []
            elif board[row][col] == "o":
                o_player.append("o")
                x_player = []

            if len(x_player) == 4:
                print_board(board)
                print("X wins!")
                return True
            elif len(o_player) == 4:
                print_board(board)
                print("O wins!")
                return True

    # Check for a win diagonally from top to bottom.
    for row in range(3, 12, 4):
        column_num = -1
        checks = 1
        x_player = []
        o_player = []
        while checks < 5:
            column_num += 2
            row_num = row
            x_player = []
            o_player = []
            for col in range(column_num, 14, 2):
                if row_num == 27:
                    break

                if board[row_num][col] == "x":
                    x_player.append("x")
                    o_player = []
                elif board[row_num][col] == "o":
                    o_player.append("o")
                    x_player = []

                if len(x_player) == 4:
                    print_board(board)
                    print("X wins!")
                    return True
                elif len(o_player) == 4:
                    print_board(board)
                    print("O wins!")
                    return True

                row_num += 4
            checks += 1

    # Check for a win diagonally from bottom to top.
    for row in range(23, 16, -4):
        column_num = -1
        checks = 1
        x_player = []
        o_player = []
        while checks < 5:
            column_num += 2
            row_num = row
            x_player = []
            o_player = []
            for col in range(column_num, 14, 2):
                if row_num == -1:
                    break

                if board[row_num][col] == "x":
                    x_player.append("x")
                    o_player = []
                elif board[row_num][col] == "o":
                    o_player.append("o")
                    x_player = []

                if len(x_player) == 4:
                    print_board(board)
                    print("X wins!")
                    return True
                elif len(o_player) == 4:
                    print_board(board)
                    print("O wins!")
                    return True

                row_num -= 4
            checks += 1

    # Check if board is full.
    row_val = []
    for col in range(1, 14, 2):
        if board[3][col] == "x" or board[3][col] == "o":
            row_val.append(board[3][col])
        if len(row_val) == 7:
            print_board(board)
            print("\nThe board is full! Tie!")
            return True

    return


# Function starts the game.
def connect_four():
    drop_piece()


# The game starts.
connect_four()
