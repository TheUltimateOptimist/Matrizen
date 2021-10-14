def getNumbersLengthList(list):
    lengthList = []
    maxLengths = []
    for i, row in enumerate(list):
        for j, element in enumerate(row):
            if i == 0:
                maxLengths.append(len(str(element)))
            else:
                length = len(str(element))
                if length > maxLengths[j]:
                    maxLengths[j] = length
    for reihe in list:
        newRow = []
        for n, number in enumerate(reihe):
            newRow.append(maxLengths[n] - len(str(number)) + 1)
        lengthList.append(newRow)
    return lengthList
