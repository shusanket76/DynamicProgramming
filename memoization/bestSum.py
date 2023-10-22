hasmap  = {}
def bestSum(target, numbers):
    if target in hasmap:
        return hasmap[target][:]
    if target == 0:
        return []
    if target<0:
        return None
    shortcomb = None
    for x in numbers:
        a  = bestSum(target-x, numbers)
        if a is not None:
            a.append(x)
            if shortcomb is None or len(a)<len(shortcomb):
                shortcomb = a[:]
    hasmap[target] = shortcomb[:]
    return shortcomb
                


a = bestSum(100,[1,2,5,25,50])
print(a)