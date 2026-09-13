import math


def is_prime(number: int) -> bool:
    for divisor in range(2, math.ceil(math.sqrt(number)) + 1):
        if number % divisor == 0:
            return False
    return True

def main() -> None:
    print("Prime numbers from 1 to 100:")
    for number in range(2, 101):
        if is_prime(number):
            print(number)

main()