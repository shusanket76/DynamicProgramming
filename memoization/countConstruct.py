res=[0]

def countConstruct(target, wordArr):

    if len(target)==0:
        res[0]+=1
        return 

    for x in wordArr:
        if x == target[:len(x)]:
            countConstruct(target[len(x):], wordArr)
    
    
b = countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e","ee","eee","eeee","eeeee"])
print(b)