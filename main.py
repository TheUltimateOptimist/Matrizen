from variables import Variables
from term import Term
from attributes import Attributes


def evaluateExpression(expression, variables):
    if expression.__contains__("="):
        variables.add(expression.split("=")[0].strip(), Term(
            expression.split("=")[1].strip()).calculate())
    elif expression.__contains__("."):
        print(Attributes().check(expression.split(".")[
              0].strip(), expression.split(".")[1].strip()))
    else:
        Term(expression.strip()).calculate()


class TerminalSession:
    variables = Variables()

    def interact(self, variables):
        operation = input(">: ")
        evaluateExpression(operation, self.matrixContainer)
        self.interact()


if __name__ == '__main__':
    TerminalSession().interact()
