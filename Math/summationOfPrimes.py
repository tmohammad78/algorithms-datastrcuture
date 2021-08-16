from primeNumber import *


def sumArr(arr):
    count = 0
    for i in range(len(arr)):
        count += arr[i]
    return count


if __name__ == '__main__':
    maxNumber = 2000000
    sum = sumArr(primeNumber(maxNumber))
    print(sum)
