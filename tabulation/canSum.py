def canSum(target, numbers):
    table=[0 for x in range(target+1)]
    table[0] = 1
    x = 0
    while x<target+1:
        for y in numbers:
            if table[x]==0:
                break
            if x+y<target+1:
                table[x+y] = 1
        x+=1
    return table[target]==1
print(canSum(1, [3,2,5]))

