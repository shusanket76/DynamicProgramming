def fib1(n):
    table = [0 for x in range(n+1)]
    table[1] = 1
    for x in range(len(table)):
        if x+1<len(table):
            table[x+1]+=table[x]
        if x+2<len(table):
            table[x+2]+=table[x]
        
    return table[n]


print(fib1(60))
# +++++++++++++++++++++++++++++++++++++e+++++++++++++++++++++++++++=
# Memoization.
hasmap = {}
def fib(n):
    if n in hasmap:
        return hasmap[n]
    if n==1 or n==2:
        return 1
    hasmap[n]= fib(n-1)+fib(n-2)
    return hasmap[n]
print(fib(60))