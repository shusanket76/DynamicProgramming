# SOLUTION1
numbers = [1,2,3,7]
target = 7
res1=[numbers]
def bestSum(target, numbers, curr, pointer):
    if target==0:
        if len(res1[0])>=len(curr):
            res1[0]=curr[:]
            return 
    if target<0:
        return 
    for x in range(pointer, len(numbers)):
        curr.append(numbers[x])
        bestSum(target-numbers[x], numbers, curr, x)
        curr.pop()

a = bestSum(7,[1,2,3,7],curr=[], pointer=0)

