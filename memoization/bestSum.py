hasmap={}
def bestSum(target, numbers):
    if target in hasmap:
        return hasmap[target][:]
    if target == 0:
        return []
    if target<0:
        return 
    shortanswer =None
    for x in numbers:
        a = bestSum(target-x, numbers)
        if a is not None:
            a.append(x)
            if shortanswer is None or len(a)<len(shortanswer):
                shortanswer=a
    hasmap[target]=shortanswer[:]
    return shortanswer



a = bestSum(100,[1,2,5,25])
print(a)