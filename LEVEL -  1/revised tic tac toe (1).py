B=["","","","","","","","",""]
def print_board():
    print(" "+B[0]+"  |  "+B[1]+"  |  "+B[2])
    print("-------------")
    print(" "+B[3]+"  |  "+B[4]+"  |  "+B[5])
    print("-------------")
    print(" "+B[6]+"  |  "+B[7]+"  |  "+B[8])

def check_winner():
    if B[0] == 'X' and B[1] == 'X' and B[2] == 'X':
        return "X won"
    if B[3] == 'X' and B[4] == 'X' and B[5] == 'X':
        return "X won"
    if B[6] == 'X' and B[7] == 'X' and B[8] == 'X':
        return "X won"
    if B[0] == 'X' and B[3] == 'X' and B[6] == 'X':
        return "X won"
    if B[1] == 'X' and B[4] == 'X' and B[7] == 'X':
        return "X won"
    if B[2] == 'X' and B[5] == 'X' and B[8] == 'X':
        return "X won"
    if B[0] == 'X' and B[4] == 'X' and B[8] == 'X':
        return "X won"
    if B[2] == 'X' and B[4] == 'X' and B[6] == 'X':
        return "X won"
    if B[0] == 'O' and B[1] == 'O' and B[2] == 'O':
        return "O won"
    if B[3] == 'O' and B[4] == 'O' and B[5] == 'O':
        return "O won"
    if B[6] == 'O' and B[7] == 'O' and B[8] == 'O':
        return "O won"
    if B[0] == 'O' and B[3] == 'O' and B[6] == 'O':
        return "O won"
    if B[1] == 'O' and B[4] == 'O' and B[7] == 'O':
        return "O won"
    if B[2] == 'O' and B[5] == 'O' and B[8] == 'O':
        return "O won"
    if B[0] == 'O' and B[4] == 'O' and B[8] == 'O':
        return "O won"
    if B[2] == 'O' and B[4] == 'O' and B[6] == 'O':
        return "O won"
    return None
for X in range(0,9):
    a=int(input("Enter a position"))
    if X%2==0:
        B[a-1]='X'
    else:
        B[a-1]='O'
    print_board()
    check =check_winner()
    if check=='X won':
        print("X won")
        break