N, r, c = map(int, input().split())
print(int(bin(c)[2:], 4)+2*int(bin(r)[2:], 4))
