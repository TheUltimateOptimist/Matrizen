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

    # not needed!
    def tokenizeFromConsole(self):
        """
        function is not need!
        added it only for testing
        but i am not strong enough to delete it
        """
        textToTokenize = input("text to tokenize: ")
        print(self.tokenize(textToTokenize))
        self.tokenizeFromConsole()
