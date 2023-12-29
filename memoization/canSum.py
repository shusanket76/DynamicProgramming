# def canSum(target, numbers):
#     res = []
#     def dfs(target, curr, i):
#         if target ==0:
#             res.append(curr[:])
#             return True
#         if target<0 or i>=len(numbers):
#             return False
#         curr.append(numbers[i])
#         a=dfs(target-numbers[i], curr, i)
#         curr.pop()
#         b=dfs(target, curr, i+1)
#         return (a or b)

    
#     if dfs(target, [], 0) is True:
#         return True
#     return False
    

# a = canSum(7,[5,4])
# print(a)
hasmap = {}
def canSum(target, numbers):
    if target in hasmap:
        return hasmap[target]
    if target<0:
        return 
    if target==0:
        return True
    for x in numbers:
        hasmap[target] = canSum(target-x, numbers)
        if hasmap[target] is True:
            return True
    hasmap[target] = False
    return False


a = canSum(900,[1,2])
print(a)