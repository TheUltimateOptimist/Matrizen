import os
mode = "default"
unittestsFile = "\n".join(
    "import unittest-n-if __name__ == '__main__':-n-    unittest.main()-n-".split("-n-"))
generalTestFile = "\n".join(
    "import unittest-n-importstatement-n--n--n-class Testname(unittest.TestCase):-n-    pass-n-".split("-n-"))
generalMethod = "\n".join(
    "    def test_methodName(self):-n-        pass-n-".split("-n-"))


def replaceWords(text, wordsToReplace, replacementWords):
    for i, word in enumerate(wordsToReplace):
        text = replacementWords[i].join(text.split(word))
    return text


def initialize():
    if not os.path.exists('Unittests'):
        os.makedirs('Unittests')
        open("Unittests/modulesAndClasses.txt", mode="w")
        open("Unittests/methods.txt", mode="w")
    else:
        print("ERROR: UNITTESTS FOLDER ALREADY EXISTS!")
    if not os.path.isfile("unittests.py"):
        with open("unittests.py", mode="w") as file:
            file.write(unittestsFile)
    else:
        print("ERROR: FILE UNITTESTS ALREADY EXISTS!")


class Names:
    modulesAndClasses = []
    methods = []

    @classmethod
    def initialize(cls):
        with open("Unittests/modulesAndClasses.txt", mode="r") as file:
            #lines = file.readlines()
            cls.modulesAndClasses = "".join(file.readlines()).split("\n")
        with open("Unittests/methods.txt", mode="r") as file:
            cls.methods = "".join(file.readlines()).split("\n")

    @classmethod
    def isModuleOrClass(cls, name):
        for moduleOrClass in cls.modulesAndClasses:
            if moduleOrClass == name:
                return True
        return False

    @classmethod
    def isMethod(cls, name):
        for method in cls.methods:
            if method == name:
                return True
        return False

    @classmethod
    def addModuleOrClass(cls, name):
        filename = "test_" + name.lower() + ".py"
        if not os.path.isfile(f"Unittests/{filename}"):
            importStatement = input(">import statement: ")
            with open(f"Unittests/{filename}", mode="w") as newFile:
                newFile.write(replaceWords(generalTestFile, ["importstatement", "name"], [
                              importStatement, name.capitalize()]))
            with open("Unittests/modulesAndClasses.txt", mode="a") as file:
                file.write(name.capitalize() + "\n")
            cls.modulesAndClasses.append(name.capitalize())
        else:
            print(f"ERROR: file Unittests/{filename} alreaady exists!")

    @classmethod
    def addMethod(cls, name, classModuleLayer):
        with open("Unittests/" + "test_" + classModuleLayer.lower() + ".py", mode="a") as file:
            file.write(replaceWords(generalMethod, [
                       "methodName"], [name]))
        with open("Unittests/methods.txt", mode="a") as file:
            file.write(name + "\n")
        cls.methods.append(name)

    @staticmethod
    def assertionLine(operation, classModuleLayer, methodLayer):
        if operation == "equal":
            eingabe = input(
                f"{classModuleLayer}->{methodLayer}->equal>eingabe: ")
            ausgabe = input(
                f"{classModuleLayer}->{methodLayer}->equal>ausgabe: ")
            return f"        self.assertEqual({eingabe}, {ausgabe})\n"
        else:
            print(f"ERROR: DIE OPERATION {operation} IST NICHT DEFINIERT!")

    @classmethod
    def addAssertion(cls, classModuleLayer, methodLayer, filepath, operation):
        with open(filepath, mode="r") as file:
            lines = file.readlines()
            methodStart = 0
            for i, line in enumerate(lines):
                if line.__contains__(f"    def test_{methodLayer}"):
                    methodStart = i
                    break
            if methodStart != 0:
                isLast = True
                if lines[methodStart + 1].__contains__("pass"):
                    lines[methodStart + 1] = cls.assertionLine(
                        operation, classModuleLayer, methodLayer)
                else:
                    for j in range(methodStart + 1, len(lines)):
                        if line.__contains__("    def test_"):
                            lines.insert(j, cls.assertionLine(
                                operation, classModuleLayer, methodLayer))
                            isLast = False
                            break
                    if isLast:
                        lines.append(cls.assertionLine(
                            operation, classModuleLayer, methodLayer))
                with open(filepath, mode="w") as newFile:
                    newFile.writelines(lines)


class TerminalSession:
    def __init__(self):
        self.mode = "default"
        self.classModuleLayer = ""
        self.methodLayer = ""
        self.filePath = ""

    def evaluateDefault(self, operation):
        if operation == "init":
            initialize()
        elif Names.isModuleOrClass(operation.capitalize()):
            self.classModuleLayer = operation
            self.mode = "classModule"
            self.filePath = f"Unittests/test_{operation.lower()}.py"
        else:
            Names.addModuleOrClass(operation)
            self.mode = "classModule"
            self.classModuleLayer = operation
            self.filePath = f"Unittests/test_{operation.lower()}.py"

    def evaluateClassModuleLayer(self, operation):
        if operation == "":
            self.mode = "default"
        elif Names.isMethod(operation):
            self.mode = "method"
            self.methodLayer = operation
        else:
            Names.addMethod(operation, self.classModuleLayer)
            self.mode = "method"
            self.methodLayer = operation

    def evaluateMethodLayer(self, operation):
        if operation == "":
            self.mode = "classModule"
        else:
            Names.addAssertion(self.classModuleLayer,
                               self.methodLayer, self.filePath, operation)

    def interact(self):
        if self.mode == "default":
            operation = input(">: ")
            self.evaluateDefault(operation)
        elif self.mode == "classModule":
            operation = input(f"{self.classModuleLayer.capitalize()}>: ")
            self.evaluateClassModuleLayer(operation)
        elif self.mode == "method":
            operation = input(
                f"{self.classModuleLayer.capitalize()}->{self.methodLayer}>: ")
            self.evaluateMethodLayer(operation)
        else:
            print(f"ERROR: MODUS {self.mode} IST NICHT DEFINIERT")
        self.interact()


if __name__ == "__main__":
    print("Welcome!")
    print("Enter 'help' to view all possible options")
    print("Enter 'explain' to get an explanation on how to use this tool")
    try:
        Names.initialize()
    except:
        print("Please initialize!")
    TerminalSession().interact()
