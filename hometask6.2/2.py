from koningin import check_koningin
import random

if __name__ == "__main__":
    koningin = [(random.randint(1, 8), random.randint(1, 8)) for _ in range(8)]
    print("Случайные пары чисел:", koningin)
    print("True, \"не бьют\"" if check_koningin(koningin) else "False, \"бьют\"")
