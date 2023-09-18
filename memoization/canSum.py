hasmap={}
def canSum(numbers, target):
    if target in hasmap:
        return False
    if target==0:
        return True
    if target<0:
        return False
    
    for x in numbers:
        if canSum(numbers, target-x) is True:
            return True
    hasmap[target] =False
    return False



a = canSum([7,10], 300)
print(a)