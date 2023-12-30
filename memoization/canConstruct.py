hasmap  ={}
def canConstruct(target, wordbank):
    if target in hasmap:
        return hasmap[target]
    if len(target)==0:
        return True
    for x in wordbank:
        if x == target[0:len(x)]:
            if canConstruct(target[len(x):], wordbank) is True:
                return True
    hasmap[target] = False
    return False


# a = canConstruct("abcdef",["ab","abc","cd","def", "abcd"])
a = canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])
print(a)