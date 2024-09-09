numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 35]
primes = []
not_primes = []

def is_prime(num):
    prime = num > 1 and (num % 2 != 0 or num == 2) and (num % 3 != 0 or num == 3)
    i = 5;
    number = 2;

    while prime and i * i <= num:
        prime = num % i != 0
        i += number
        number = 6 - number
    return prime

for i in range(len(numbers)):
    if numbers[i] == 1:
        continue
    else:
        a = is_prime(numbers[i])
        if a == True:
            primes.append(numbers[i])
        else:
            not_primes.append(numbers[i])

print(primes)
print(not_primes)
