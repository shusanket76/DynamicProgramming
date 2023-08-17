hasmap = {}
def howSum(target, numbers):
    if target in hasmap:
        return hasmap[target]
    if target == 0:
        return []
    if target<0:
        return 
    for x in numbers:
        a = howSum(target-x, numbers) 
        if a is not None:
            a.append(x)
            return a
    hasmap[target] = None
    return  


a = howSum(300, [7,14])
print(a)