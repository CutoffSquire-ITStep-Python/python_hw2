# #1
def is_prime_number(n : int) -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_numbers():
    for i in range(2, 1000):
        if is_prime_number(i):
            yield i

def prime_numbers_sum(n : int) -> int:
    numbers_sum = 0
    gen = prime_numbers()
    for _ in range(n):
        numbers_sum += next(gen)
    return numbers_sum

print(prime_numbers_sum(3))

#2
def armstrong_numbers(min_limit : int, max_limit : int):
    for i in range(min_limit, max_limit + 1):
        numbers_sum = 0
        str_num = str(i)
        for j in str_num:
            numbers_sum += int(j) ** 3
        if numbers_sum == i:
            yield i

for num in armstrong_numbers(100, 500):
    print(num)