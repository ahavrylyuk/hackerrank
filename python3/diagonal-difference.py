n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
d1 = sum(matrix[i][i] for i in range(n))
d2 = sum(matrix[n - i - 1][i] for i in range(n))
print(abs(d1 - d2))
