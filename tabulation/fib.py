def fib(n):
    table = [0 for x in range(n+1)]
    table[1]=1
    x = 1
    while x<len(table)-1:
        table[x+1] = table[x+1]+table[x]
        if x+2<len(table):
            table[x+2] = table[x+2]+table[x]
        x+=1

    return table[n]

print(fib(10000))