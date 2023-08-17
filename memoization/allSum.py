res =[]
def allSum(target, numbers, curr, pointer):
    if target==0:
        res.append(curr[:])
        return 
    if target<0:
        return 
    for x in range(pointer,len(numbers)):
        curr.append(numbers[x])
        allSum(target-numbers[x], numbers, curr, x)
        curr.pop()
    
allSum(300, [2,3], [], 0)
print(res)