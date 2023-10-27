def bestSum(target, numbers):
    table = [[] for x in range(target+1)]
    table[0] = [[]]
    for ab in range(len(table)):
        if len(table[ab])!=0:
            for cd in numbers:
                if ab+cd<len(table):
                    for ef in table[ab]:
                        cop = ef[:]
                        cop.append(cd)
                        if len(table[ab+cd])==0:
                            table[ab+cd].append(cop)
                        elif len(table[ab+cd][0])>len(cop):
                            table[ab+cd][0]=cop

    return(table[target])



a = bestSum(200, [10,2,5,25,75,90])
print(a[0])