# TABULATION

def canSumTabulation(numbers, target):
    table = [False for b in range(target+1)]
    table[0] = True
    for x in range(len(table)):
        if table[x]!=False:
            for y in numbers:
                if x+y<len(table):
                    table[x+y] = True
           
    return table[target]

            
        

# a = canSumTabulation([7,14],300)
# print(a)

# =======================ds=======================================================================
# MEMOIZATION
hasmap = {}
def canSumMemoization(numbers, target):
    if target in hasmap:
        return False
    if target == 0:
        return True
    if target<0:
        return False
    for x in numbers:
        if canSumMemoization(numbers, target-x) is True:
            return True
    hasmap[target] = False
    return False

b = canSumMemoization([7,14], 300)
print(b)