def is_prime(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def prime_numbers(numbers: list) -> dict:
    return {number: is_prime(number) for number in numbers}


numbers = [3, 6, 12, 17]
print(prime_numbers(numbers))