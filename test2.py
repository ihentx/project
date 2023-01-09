import time


def eratosthenes1(n):
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(2 * i, len(sieve), i):
                sieve[j] = 0
    return list(filter(lambda x: x != 0, sieve))

def eratosthenes2(n):
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    sieve1 = [x for x in sieve if x != 0]
    return sieve1

def eratosthenes3(n2):
    prime = [True for _ in range(n2 + 1)]
    n1 = 2
    while (n1 ** 2 <= n2):
        if prime[n1]:
            for i in range(n1 ** 2, n2 + 1, n1):
                prime[i] = False
        n1 += 1
    prime_numbers = []
    for i in range(2, n2 + 1):
        if prime[i]:
            prime_numbers.append(i)
    return prime_numbers

def eratosthenes4(n2):
    n1 = 2
    whole_numbers = [number for number in range(n1, n2 + 1)]
    temp = whole_numbers[:]
    prime_numbers = []
    while len(temp) > 0:
        for i in range(1, len(whole_numbers)):
            if whole_numbers[i] % whole_numbers[0] == 0:
                temp.remove(whole_numbers[i])
        temp.remove(whole_numbers[0])
        prime_numbers.append(whole_numbers[0])
        whole_numbers = temp[:]
    return prime_numbers

start_time = time.time()
eratosthenes1(10 ** 6)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
eratosthenes2(10 ** 6)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
eratosthenes3(10 ** 6)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
eratosthenes4(100)
print("--- %s seconds ---" % (time.time() - start_time))
