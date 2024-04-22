import random
from koningin import check_koningin

generate_random_koningins = lambda: next(iter(
    [(random.randint(1, 8), random.randint(1, 8)) for _ in range(8)]
    for _ in range(10000)
    if check_koningin([(random.randint(1, 8), random.randint(1, 8)) for _ in range(8)])
), None)

if __name__ == "__main__":
    successful_count = 0
    while successful_count < 4:
        koningins = generate_random_koningins()
        if koningins:
            print("Успешная расстановка ферзей:", koningins)
            successful_count += 1


