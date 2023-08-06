hasmap={}
def canSum(target,nums):
    if target in hasmap:
        return hasmap[target]
    if target<0:
        return False
    if target==0:
        return True
    for x in range(len(nums)):
        if canSum(target-nums[x],nums) is True:
            hasmap[target]=True
            return True
    hasmap[target]=False
    return False
    
a = canSum(300,[1,2])
print(a)