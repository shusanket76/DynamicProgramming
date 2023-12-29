hasmap = {}
def gridtraveller(m,n):
    if (m,n) in hasmap:
        return hasmap[(m,n)]
    if (n,m) in hasmap:
        return hasmap[(n,m)]
    if m==1 and n==1:
        return 1
    if m<=0 or n<=0:
        return 0
    hasmap[(m,n)] = gridtraveller(m-1,n)+gridtraveller(m,n-1)
    return hasmap[(m,n)]

a = gridtraveller(18,18)
print(a)
