hasmap = {}
def canSum(target, numbers):
    if target in hasmap:
        return False
    if target==0:
        return True
    if target<0:
        return False
    for x in numbers:
        if canSum(target-x, numbers) is True:
            return True
    hasmap[target] = False
    return False

a  = canSum(300,[7,14])
print(a)