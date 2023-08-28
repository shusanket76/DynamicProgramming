def howSum(target, nums):
    if target == 0:
        return []
    if target<0:
        return None
    for x in nums:
        a = howSum(target-x, nums)
        if a is not None:
            a.append(x)
            return a
    return None

a = howSum(10, [7,4])
print(a)