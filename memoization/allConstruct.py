hasmap = {}
def allConstruct(target, alphabets):
    # if target in hasmap:
    #     return hasmap[target]
    if len(target)==0:
        return [[]]
    allcombinations = None
    for x in alphabets:
        if x == target[0:len(x)]:
            comb  = allConstruct(target[len(x):], alphabets)
            if comb is not None:
                for y in comb:
                    y.insert(0, x)
                if allcombinations is None:
                    allcombinations = comb
                else:
                    allcombinations+=comb
    hasmap[target] = allcombinations
    return hasmap[target]

a = allConstruct("abcdef", ["ab","abc", "cd","def","abcd", "ef","c"])
# a = allConstruct("aaaaaaaaaaaaaaaaaaaaaz", ["a","aa","aaa","aaaa","aaaaaa"])
print(a)