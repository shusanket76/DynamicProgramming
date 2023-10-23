hasmap  ={}
count = [0]
def countConstruct(target, alphabets):
    if target in hasmap:
        return hasmap[target]
    if len(target) ==0:
        return 1
    totalcount = 0
    for x in alphabets:
        if x == target[0:len(x)]:
            a = countConstruct(target[len(x):], alphabets)
            if a==1:
                totalcount+=1
    hasmap[target] = totalcount
    return totalcount
a = countConstruct("abcdef", ["ab", "abc", "cd","def", "abcd"])             
# a = countConstruct("purple",["purp", "p", "ur", "le", "purpl"])
# a = countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e","ee","eee", "eeee", "eeeee", "eeeee", "eeeeee"])

print(a)