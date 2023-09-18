hasmap = {}
def fib(n):
    if n in hasmap:
        return hasmap[n]
    if n<=2:
        return 1
    hasmap[n]= fib(n-1)+fib(n-2)
    return hasmap[n]
a = fib(50)
print(a)