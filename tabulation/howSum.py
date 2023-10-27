def howSum(target, numbers):
    table = [[] for x in range(target+1)]
    table[0] = [[]]
    for ab in range(target+1):
        if len(table[ab])!=0:
            for cd in numbers:
                if ab+cd < len(table):
                    for ef in table[ab]:
                        cop = ef[:]
                        cop.append(cd)
                        table[ab+cd].append(cop)
    return table[target]

                    


a = howSum(7, [5,3,4])
print(a)