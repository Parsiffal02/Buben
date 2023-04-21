n = int(input("Введите количество строк (n): "))
m = int(input("Введите количество столбцов (m): "))
A = [[i*n + j for i in range(m)] for j in range(n)]
for row in A:
    print(' '.join(map(str, row)))