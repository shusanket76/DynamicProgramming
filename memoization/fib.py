hasmap = {}
def fib(n):
    if n in hasmap:
        return hasmap[n]
    if n<=2:
        return 1
    
    hasmap[n]=fib(n-1)+fib(n-2)
    return hasmap[n]

print(fib(8))
# print(fib(50))
