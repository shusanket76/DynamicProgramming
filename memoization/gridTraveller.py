hasmap = {}
def gridTraveller(m,n):
    if (m,n) in hasmap:
        return hasmap[(m,n)]
    if (n,m) in hasmap:
        return hasmap[(n,m)]
    if m==1 and n ==1:
        return 1
    if m==0 or n==0:
        return 0
    hasmap[(m,n)]= gridTraveller(m-1, n)+gridTraveller(m,n-1)
    return hasmap[(m,n)]
a = gridTraveller(20,20)

print(a)