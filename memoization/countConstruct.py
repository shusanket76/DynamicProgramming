def countConstruct(target, wordbank, hasmap = {}):
    if target in hasmap:
        return hasmap[target]
    if len(target)==0:        
        return 1
    totalways=0
    for x in wordbank:
        if x == target[0:len(x)]:
            numways = countConstruct(target[len(x):], wordbank)
            totalways+=numways
    hasmap[target] = totalways
    return totalways

# a = countConstruct("abcdef",["ab","abc","cd","def", "abcd"])
a = countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeer", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])
print(a)