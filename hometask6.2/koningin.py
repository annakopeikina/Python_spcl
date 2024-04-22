import random

def check_koningin(koningin):
    return all(
        x1 != x2 and y1 != y2 and abs(x1 - x2) != abs(y1 - y2)
        for i in range(len(koningin))
        for j in range(i + 1, len(koningin))
        for x1, y1, x2, y2 in [(*koningin[i], *koningin[j])]
    )

if __name__ == "__main__":
    koningin = [(random.randint(1, 8), random.randint(1, 8)) for _ in range(8)]
    print("Случайные пары чисел:", koningin)
    print("True, \"не бьют\"" if check_koningin(koningin) else "False, \"бьют\"")

