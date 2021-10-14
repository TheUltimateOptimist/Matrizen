class MatrixCalculator:
    def add(a, b):
        if (len(a) == len(b)) and (len(a[0]) == len(b[0])):
            newValue = []
            for i, row in enumerate(a):
                newRow = []
                for j, number in enumerate(row):
                    newRow.append(number + b[i][j])
                newValue.append(newRow)
            return newValue
        else:
            print(
                "ERROR: FÜR DIE ADDITION ZWEIER MATRIZEN MÜSSEN DIE DIMENSIONEN ÜBEREINSTIMMEN")
            return None

    def minus(a, b):
        if (len(a) == len(b)) and (len(a[0]) == len(b[0])):
            newValue = []
            for i, row in enumerate(a):
                newRow = []
                for j, number in enumerate(row):
                    newRow.append(number - b[i][j])
                newValue.append(newRow)
            return newValue
        else:
            print(
                "ERROR: FÜR DIE ADDITION ZWEIER MATRIZEN MÜSSEN DIE DIMENSIONEN ÜBEREINSTIMMEN")
            return None

    def transpose(a):
        newValue = []
        for i in range(len(a[0])):
            newRow = []
            for row in a:
                newRow.append(row[i])
            newValue.append(newRow)
        return newValue

    def scalarMultiply(a, b):
        newValue = []
        for row in b:
            newRow = []
            for number in row:
                newRow.append(a*number)
            newValue.append(newRow)
        return newValue

    def matrixMultiply(a, b):
        # todo: implement matrix multiplying
        # following return statement is just for now
        return a

    def invert(a):
        # todo: implement matrix inversing
        # following return statement is just for now
        return 0
