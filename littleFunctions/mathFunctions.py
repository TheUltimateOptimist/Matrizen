def isNumber(s):
    try:
        float(s)
        return True
    except:
        return False


def contains(text, stringList):
    for element in stringList:
        if text.__contains__(element):
            return True
    return False


def getClosingBraceIndex(openingBraceIndex, list):
    print("data:")
    print(openingBraceIndex)
    print(list)
    state = 0
    i = openingBraceIndex + 1
    while i < len(list):
        element = list[i]
        if element == "(":
            state += 1
        elif element == ")" and state != 0:
            state -= 1
        elif element == ")" and state == 0:
            return i
        i += 1
        print("state: ")
        print(state)
