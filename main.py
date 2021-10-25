from littleFunctions.color import printRed
from variables import Variables
from ExpressionSolving.term import Term
from MatricesAndNumbers.attributes import Attributes


def evaluateExpression(expression):
    if expression.__contains__("="):
        Variables.add(expression.split("=")[0].strip(), Term(
            expression.split("=")[1].strip()).calculate())
    elif expression.__contains__("."):
        print(Attributes().check(Variables.getValue(expression.split(".")[
              0].strip()), expression.split(".")[1].strip()))
    else:
        Term(expression.strip()).calculate(shouldPrint = True)


class TerminalSession:

    def interact(self):
        operation = input(">: ")
        #try:
        evaluateExpression(operation)
        #except:
        #printRed("ERROR: UNGÜLTIGE EINGABE")
        self.interact()


if __name__ == '__main__':
    TerminalSession().interact()
