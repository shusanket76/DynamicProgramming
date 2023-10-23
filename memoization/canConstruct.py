hasmap = {}
def canConstruct(target, aplhabets):
    if target in hasmap:
        return False
    if len(target)==0:
        return True
    for x in aplhabets:
        if x==target[0:len(x)]:
            if canConstruct(target[len(x):], aplhabets) is True:
                return True
    hasmap[target] = False
    return False


    
    
# a = canConstruct("abcdeff", ["ab", "abc", "cd", "def", "abcd"])
a = canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e","ee","eee", "eeee", "eeeee", "eeeee", "eeeeee"])
print(a)