n, m = map(int, input().split())
A = [ [ i + j * m for i in range(m) ] for j in range (n) ]
for i in range(n):
    for j in range(m):
        print(A[i][j], end = ' ')
    print()