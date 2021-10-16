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
