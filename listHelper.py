# index 1 and index 2 identify the part of the list that will be split of of the main list and returned
def split_list(index1, index2, list):
    finalList = []
    for i in range(index1, index2 + 1):
        finalList.append(list[i])
    return finalList


def delete_range(index1, index2, list):
    n = index2 - index1 + 1
    for _ in range(n):
        list.pop(index1)
    return list


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
