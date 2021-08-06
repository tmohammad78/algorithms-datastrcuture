def sumArr(number):
    return int((number * (number + 1)) / 2)


def sumSquare(number):
    return int((number * (number + 1) * (2 * number + 1)) / 6)


def sqrtNum(number):
    return number * number


def difference(firstNum, secondNum):
    return secondNum - firstNum


if __name__ == '__main__':
    maxNumber = 100
    resultSqrt = sqrtNum(sumArr(maxNumber))
    print(difference(sumSquare(maxNumber), resultSqrt))
