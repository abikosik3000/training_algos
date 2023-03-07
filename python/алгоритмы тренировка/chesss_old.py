
fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

buf = fin.readline().rstrip().split(" ")
n = int(buf[0])
m = int(buf[1])

board = [ [0]*m for i in range(n) ]

def get_from_board(board , i , j):
    if(i >= n  or j >= m or i < 0 or j <0):
        return 0
    return board[i][j]

def shag(board , i , j):
    if(i >= n  or j >= m or i < 0 or j <0):
        return 0
    board[i][j] += get_from_board(board , i - 2, j + 1)
    board[i][j] += get_from_board(board , i - 2, j - 1)
    board[i][j] += get_from_board(board , i - 1, j - 2)
    board[i][j] += get_from_board(board , i + 1, j - 2)


board[0][0] = 1

for k in range(m + n):
    for h in range(k + 1):
        shag(board , k - h , h)


#for i in range(n):
#    print(board[i])
fout.write( str(board[n-1][m-1]) )

fout.close()
fin.close()
