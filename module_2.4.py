numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    for j in range(1, i, 1):
        is_prime = i % 1 == 0 and i % j == 0
        if i <= 1:
            continue
        elif is_prime == True:
            primes.append(i)

        else:
            not_primes.append(i)

print('primes: ', primes)
print('not_primes: ', not_primes)


