# TABULATION
def gridTravellerTab(x,y):
    table = [[0 for a in range(y+1)] for b in range(x+1)]
    table[1][1]=1
    for x in range(len(table)):
        for y in range(len(table[0])):
            if y+1<len(table[0]):
                table[x][y+1]+=table[x][y]
            if x+1<len(table):
                table[x+1][y]+=table[x][y]
    return table[x][y]


a = gridTravellerTab(18,18)
print(a)
# ==========================================================================
# MEMOIZATION
hasmap = {}
def gridTravellerMemoization(x,y):
    if (x,y) in hasmap:
        return hasmap[(x,y)]
    if (y,x) in hasmap:
        return hasmap[(y,x)]
    if x==1 and y==1:
        return 1
    if x==0 or y==0:
        return 0
    hasmap[(x,y)]= gridTravellerMemoization(x-1,y)+gridTravellerMemoization(x,y-1)
    return hasmap[(x,y)]

b = gridTravellerMemoization(18,18)
print(b)