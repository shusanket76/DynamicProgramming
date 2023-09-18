hashmap = {}
def canConstruct(words, target):
    if target in hashmap:
        return False
    if len(target) == 0:
        return True
    for x in words:
        if x == target[0:len(x)]:
            if canConstruct(words, target[len(x):]):
            
                return True
    hashmap[target] = False
    return False


a = canConstruct(["e", "ee", "eee","eeee", "eeeee", "eeeeeef"], "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef")
print(a)