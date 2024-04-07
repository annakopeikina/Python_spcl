# str.#isalpha
      #isdecimal
      #isdigit
      #isnumeric
      #isascii
#etc
def check_txt(text):
    try:
        # Пытаемся преобразовать текст в целое num
        num = int(text)

        # Если успешно, выводим двоичное, восьмеричное и шестнадцатеричное представление
        print(f"Двоичное представление: {bin(num)}")
        print(f"Восьмеричное представление: {oct(num)}")
        print(f"Шестнадцатеричное представление: {hex(num)}")
    except ValueError:
        # Если текст нельзя преобразовать в целое num, проверяем, написан ли текст на ASCII
        is_ascii = all(ord(char) < 128 for char in text)
        if is_ascii:
            print("Текст написан в кодировке ASCII.")
        else:
            print("Текст не написан в кодировке ASCII.")

# Запрашиваем у пользователя текст
ввод_пользователя = input("Введите текст: ")
check_txt(ввод_пользователя)
