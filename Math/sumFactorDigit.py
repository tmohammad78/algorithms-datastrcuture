if __name__ == '__main__':
    arr = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

    for i in range(100000):
        total = 0
        stringNum = str(i)
        for j in stringNum:
            total += arr[int(j)]
            if total == i:
                print(total)
