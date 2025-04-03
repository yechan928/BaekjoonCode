import sys
row, col = map(int,sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(row)]


count=0

for i in range(row):
    for j in range(col):
        if board[i][j] == "-" :
            if j==0 or  board[i][j-1] != "-":
                count+=1


for i in range(row):
    for j in range(col):
        if board[i][j] == "|" :
            if i==0 or  board[i-1][j] != "|":
                count+=1

print(count)