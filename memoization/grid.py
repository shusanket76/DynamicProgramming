hasmap = {}
def manyPath(x,y):
    if (x,y) in hasmap:
        return hasmap[(x,y)]
    if (y,x) in hasmap:
        return hasmap[(y,x)]
    if x==1 and y==1:
        return 1
    if x==0 or y==0:
        return 0
    hasmap[(x,y)] = manyPath(x-1,y)+manyPath(x,y-1)
    return hasmap[(x,y)]
print(manyPath(2,3))
print(manyPath(3,3))
print(manyPath(18,18))