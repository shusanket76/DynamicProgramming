hasmap = {}
def bestSum(numbers, target):
    if target in hasmap:
        return hasmap[target]
    if target == 0:
        return []
    if target<0:
        return None
    
    short = None
    for x in numbers:
        a = bestSum(numbers, target-x)
        if a is not None:
            a.append(x)
            if short is None or len(short)>len(a):
               short = a[:]
    hasmap[target] = short[:]
    return short
numbers = [1,2,5,25]

target = 100
a = bestSum(numbers, target)
print(hasmap)
print(a)