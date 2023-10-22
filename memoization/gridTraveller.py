hasmap = {}
def grid_Traveller(x,y):
    if (x,y) in hasmap:
        return hasmap[(x,y)]
    if (y,x) in hasmap:
        return hasmap[y,x]
    if x==1 and y==1:
        return 1
    if x==0 or y==0:
        return 0
    hasmap[(x,y)] =  grid_Traveller(x-1,y)+grid_Traveller(x,y-1)
    return hasmap[(x,y)]
a = grid_Traveller(18,23)
print(a)