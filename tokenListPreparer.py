from mathFunctions import contains, isNumber


class TokenListPreparer:
    def __init__(self, tokenList):
        self.tokenList = tokenList

    def dealWithMinuses(self):
        liste = []
        i = 0
        while i < len(self.tokenList):
            token = self.tokenList[i]
            if token == "-" and i == 0:
                self.tokenList.insert(0, "0")
                i += 1
            elif token == "-" and self.tokenList[i - 1] == "^":

    def prepare(self):
        return []
