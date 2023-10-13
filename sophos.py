n = 5
i = 0

while i < n:
    row = ['X' if (i + j) % 2 == 0 else '_' for j in range(n)]
    print(''.join(row))
    i += 1
