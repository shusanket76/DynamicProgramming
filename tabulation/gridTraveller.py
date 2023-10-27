def gridTraveller(m,n):
    table = [[0 for a in range(n+1)] for b in range(m+1) ]
    table[1][1] = 1
    row = 0
    col = 0
    while (row<len(table)):
        col = 0
        while (col<len(table[0])):
            if col+1<len(table[0]):
                table[row][col+1]+=table[row][col]
            if row+1<len(table):
                table[row+1][col]+=table[row][col]
            col+=1
        row+=1
    print(table)
    return table[m][n]

a = gridTraveller(3,3)
print(a)