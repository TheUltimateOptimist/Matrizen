from language import matrixChecks, generateMatrixCommands
from littleFunctions.mathFunctions import isNumber
from variables import Variables


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

    def __init__(self):
        self.tokens = [[33], [40, 45], [
            47, 57], [94], [65, 90], [97, 122]]
        self.words = matrixChecks + generateMatrixCommands + Variables.names

    def __isWord(self, textString):
        for word in self.words:
            if word == textString:
                return True
        return False

    def __isContainedInWord(self, textString):
        for word in self.words:
            if word.__contains__(textString):
                return True
        return False

    def __matches(self, code):
        for range in self.tokens:
            if len(range) == 1 and range[0] == code:
                return True
            elif len(range) == 2 and code >= range[0] and code <= range[1]:
                return True
        return False

    def __nextSymbolNotALetter(self, currentIndex, text):
        if len(text) == currentIndex + 1:
            return True
        code = ord(text[currentIndex + 1])
        if (code < 65 or code > 90) and (code < 97 or code > 122):
            return True
        else:
            return False

    def tokenize(self, input):
        resultList = []
        word = ""
        number = ""
        for i in range(len(input)):
            code = ord(input[i])
            if self.__matches(code):
                if self.__isContainedInWord(word + input[i]):
                    if self.__isWord(word + input[i]) and self.__nextSymbolNotALetter(i, input):
                        resultList.append(word + input[i])
                        word = ""
                    else:
                        word = word + input[i]
                elif self.__nextSymbolNotALetter(i, input) and isNumber(input[i] == False):
                    resultList.append(input[i])
                elif isNumber(input[i]):
                    if isNumber(input[i + 1]) == False:
                        resultList.append(number + input[i])
                        number = ""
                    else:
                        number += input[i]
            else:
                word = ""
                number = ""
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
