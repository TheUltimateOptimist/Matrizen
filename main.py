from color import printRed
from variables import Variables
from term import Term
from attributes import Attributes


def evaluateExpression(expression, variables):
    if expression.__contains__("="):
        variables.add(expression.split("=")[0].strip(), Term(
            expression.split("=")[1].strip()).calculate())
    elif expression.__contains__("."):
        print(Attributes().check(expression.split(".")[
              0].strip(), variables.getValue(expression.split(".")[1].strip())))
    else:
        Term(expression.strip()).calculate(True)


class TerminalSession:
    variables = Variables()

    def interact(self):
        operation = input(">: ")
        try:
            evaluateExpression(operation, self.variables)
        except:
            printRed("ERROR: UNGÜLTIGE EINGABE")
        self.interact()


if __name__ == '__main__':
    TerminalSession().interact()
