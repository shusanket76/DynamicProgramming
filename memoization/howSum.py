hasmap = {}

def howSum(numbers, target):
    if target in hasmap:
        return None
    if target==0:
        return []
    if target<0:
        return None
    for x in numbers:
        a = howSum(numbers, target-x)
        if a is not None:
            a.append(x)
            return a
    hasmap[target] = False
    return None
    

print(howSum([7, 10], 300))