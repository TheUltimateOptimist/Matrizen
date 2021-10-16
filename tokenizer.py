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


class Tokenizer:
    """
    tokenizes a string returning list with extracted tokens
    instantioation requires:
    rule: string -> "mathematical" or "language" or "custom"
    tokens: two dimensional list lists of ascii ranges to return from the string e.g. tokens=[[34,45], 22] -> all symbols with a value between 34 and 45 and with the value 22 will be returned
    above-only has an affect if rule is set to custom
    groups: three dimensional list of lists of lists containing ascii ranges that belong together e.g.: groups = [[[34,45], [22]], [[11,12], [34,40]]]
    first group-> all ascii values between 34 and 45 as well as ascii value 22
    second group-> all ascii values between 11 and 12, all ascii values between 34 and 40
    above-only has an affect if rule is set to custom

    """

    def __init__(self, rule, tokens=[], groups=[]):
        match rule:
            case "custom":
                self.tokens = tokens
                self.groups = groups
            case "mathematical":
                self.tokens = [[33], [40, 45], [
                    47, 57], [65, 90], [94], [97, 122]]
                self.groups = [[[48, 57]], [[65, 90], [97, 122]]]
            case _:
                self.tokens = []
                self.groups = []

    def __matches(self, code):
        for range in self.tokens:
            if len(range) == 1 and range[0] == code:
                return True
            elif len(range) == 2 and code >= range[0] and code <= range[1]:
                return True
        return False

    def __getGroup(self, code):
        for i, group in enumerate(self.groups):
            for range in group:
                if len(range) == 1 and code == range[0]:
                    return i
                elif len(range) == 2 and code >= range[0] and code <= range[1]:
                    return i
        return -1

    def tokenize(self, input):
        resultList = []
        previousGroupIndex = -1
        for i in range(len(input)):
            code = ord(input[i])
            if self.__matches(code):
                currentGroupIndex = self.__getGroup(code)
                if currentGroupIndex == previousGroupIndex and currentGroupIndex >= 0:
                    resultList[len(resultList) -
                               1] = resultList[len(resultList) - 1] + input[i]
                else:
                    resultList.append(input[i])
                previousGroupIndex = currentGroupIndex
            else:
                previousGroupIndex = -1
        return resultList

    def tokenizeFromConsole(self):
        textToTokenize = input("text to tokenize: ")
        print(self.tokenize(textToTokenize))
        self.tokenizeFromConsole()


#tokenizer = Tokenizer("mathematical")
# tokenizer.tokenizeFromConsole()


class PunktVorStrichCalculator:
    def __getClosingBraceIndex(self, openingBraceIndex, list):
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

    def calculate(self, tokenizedList):
        i = 0
        while i < len(tokenizedList):
            token = tokenizedList[i]
            if token == "(":
                print(i)
                print(tokenizedList)
                closingBraceIndex = self.__getClosingBraceIndex(
                    i, tokenizedList)
                print("kdddk:")
                print(closingBraceIndex)
                tokenizedList[i] = self.calculate(split_list(
                    i + 1, closingBraceIndex - 1, tokenizedList))
                tokenizedList = delete_range(
                    i + 1, closingBraceIndex, tokenizedList)
            i += 1
        i = 0
        while i < len(tokenizedList):
            token = tokenizedList[i]
            if token == "*":
                tokenizedList[i] = float(
                    tokenizedList[i - 1]) * float(tokenizedList[i + 1])
                del tokenizedList[i + 1]
                del tokenizedList[i - 1]
            elif token == "/":
                tokenizedList[i] = float(
                    tokenizedList[i - 1]) / float(tokenizedList[i + 1])
                del tokenizedList[i + 1]
                del tokenizedList[i - 1]
            else:
                i += 1
        i = 0
        while i < len(tokenizedList):
            token = tokenizedList[i]
            if token == "+":
                print(f"+: {i}")
                tokenizedList[i] = float(
                    tokenizedList[i - 1]) + float(tokenizedList[i + 1])
                del tokenizedList[i + 1]
                del tokenizedList[i - 1]
            elif token == "-":
                print(f"-: {i}")
                tokenizedList[i] = float(
                    tokenizedList[i - 1]) - float(tokenizedList[i + 1])
                del tokenizedList[i + 1]
                del tokenizedList[i - 1]
            else:
                i += 1
        print(tokenizedList)
        return tokenizedList[0]


test = "2+ 2 *(3 + 3* (3 +3))"
tokenizer = Tokenizer("mathematical")
tokenizedList = tokenizer.tokenize(test)
print(tokenizedList)
print(PunktVorStrichCalculator().calculate(
    tokenizedList))
print("right one:")
print(eval(test))
