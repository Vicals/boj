import sys

def quad(x1, y1, x2, y2):
    flag = False
    for i in range(y1, y2+1):
        for j in range(x1, x2+1):
            if maps[y1][x1] != maps[i][j]:
                flag = True
                break
        if flag:
            break
    if not flag:
        sys.stdout.write(maps[y1][x1])
    if flag:
        h_x = (x1+x2)//2
        h_y = (y1+y2)//2
        sys.stdout.write('(')
        quad(x1, y1, h_x, h_y)
        quad(h_x+1, y1, x2, h_y)
        quad(x1, h_y+1, x2, y2)
        quad(h_x+1, h_y+1, x2, y2)
        sys.stdout.write(')')


n = int(input())
maps = [list(input()) for i in range(n)]
quad(0, 0, n-1, n-1)
