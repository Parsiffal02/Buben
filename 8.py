n = int(input("Введите количество строк (n): ")) 
m = int(input("Введите количество столбцов (m): ")) 
A = [[1 if (i+j) % 2 == 0 else 0 for j in range(m)] for i in range(n)] 
for row in A: print(' '.join(map(str, row)))