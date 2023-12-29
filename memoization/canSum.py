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

def canSum(target, numbers):
    if target<0:
        return 
    if target==0:
        return True
    for x in numbers:
        if canSum(target-x, numbers) is True:
            return True
    return False


a = canSum(7,[2,3,7])
print(a)