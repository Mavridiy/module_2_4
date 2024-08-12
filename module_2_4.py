numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for number in range(2,len(numbers)+1):
    is_prime = False
    for n in range(2, number+1):
        if (number % n) == 0:
            is_prime += True
    if is_prime == True:
        primes.append(number)
    else:
        not_primes.append(number)
print('Primes:', primes)
print('Not rimes:', not_primes)