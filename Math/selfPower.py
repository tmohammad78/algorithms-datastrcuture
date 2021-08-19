def power(a, b):
    if b == 0:
        return 1

    answer = a
    increment = a

    for i in range(1, b):
        for j in range(1, a):
            answer += increment
        increment = answer
    return increment


if __name__ == "__main__":
    total = 0
    # for i in range(11):
    #     powere = i ** i
    #     print("i \n", i, powere)
        # for j in range(10):
        #     if i+1 == j+1:
        #         total += i+1 ** j+1
        #         print("i,j",i,j,i ** j)

    print(power(10,20))
