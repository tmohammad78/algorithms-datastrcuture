def primeNumber(n):
    arr =[]
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:

        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    for p in range(2, n + 1):
        if prime[p]:
            arr.append(p)
            # print(p),
    return arr

# Driver code
if __name__ == '__main__':
    n = 100000001
    print("Following are the prime numbers smaller")
    arr = primeNumber(n)
    print(arr[10000])
