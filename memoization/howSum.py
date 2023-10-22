hasmap ={}
def howSum(target, numbers):
    if target in hasmap:
        return None
    if target==0:
        return []
    if target<0:
        return None
    for x in numbers:
        a = howSum(target-x, numbers)
        if a is not None:
            a.append(x)
            return a
    hasmap[target] =False
    return None

a = howSum(300,[7,14])
print(a)