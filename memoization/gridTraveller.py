hasmap={}
def gridTraveller(m,n):
    if (m,n) in hasmap:
        return hasmap[(m,n)]
    if (n,m) in hasmap:
        return hasmap[(n,m)]
    if m==0 or n==0:
        return 0
    if m==1 and n==1:
        return 1
    hasmap[(m,n)] = gridTraveller(m-1,n)+gridTraveller(m,n-1)
    return hasmap[(m,n)]

a = gridTraveller(18,18)
print(a)