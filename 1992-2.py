def f(x, y, s):
    c = 0
    for i in range(y, y+s):
        for j in range(x, x+s):
            c += m[i][j]
    if c == 0:
        return '0'
    elif c == s**2:
        return '1'
    else:
        s //= 2
        return'('+f(x, y, s)+f(x+s, y, s)+f(x, y+s, s)+f(x+s, y+s, s)+')'


n = int(input())
m = [list(map(int, list(input())))for i in range(n)]
print(f(0, 0, n))
