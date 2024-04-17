#Возьмите задачу о банкомате из семинара 2:
#Напишите программу банкомат.
#Начальная сумма равна нулю, Допустимые действия: пополнить, снять, выйти
#Сумма пополнения и снятия кратны 50 GEL
#Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 GEL
#После каждой третей операции пополнения или снятия начисляются проценты - 3%
#Нельзя снять больше, чем на счёте
#При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
#Любое действие выводит сумму денег.
#Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.


TAX_RATE = 0.1
COMMISSION_RATE = 0.015
COMMISSION_MIN = 30
COMMISSION_MAX = 600
COMMISSION_FREQ = 3

balance = 0
transactions = []

def deposit(amount: int) -> None:
    """
    Пополнение счета на указанную сумму.
    """
    global balance
    balance += amount
    transactions.append(('deposit', amount))
    print(f"Поступило {amount} GEL")

def withdraw(amount: int) -> None:
    """
    Снятие указанной суммы со счета.
    """
    global balance
    if balance - amount >= 0:
        commission = max(amount * COMMISSION_RATE, COMMISSION_MIN)
        commission = min(commission, COMMISSION_MAX)
        balance -= (amount + commission)
        transactions.append(('withdraw', amount + commission))
        print(f"Снято {amount} GEL Комиссия составила: {commission} GEL")
    else:
        print("Недостаточно средств на счете.")

def tax() -> None:
    """
    Налог на богатство 10% от суммы счета.
    """
    global balance
    global transactions
    balance *= (1 - TAX_RATE)
    transactions = [(operation, amount * (1 - TAX_RATE)) for operation, amount in transactions]

def atm() -> None:
    """
    Главная функция банкомата.
    """
    global balance
    global transactions
    while True:
        print("Баланс: ", balance, "GEL")
        print("Выберите действие:")
        print("1. Пополнить")
        print("2. Снять")
        print("3. Выйти")
        choice = input("Ваш выбор: ")

        if choice == '1':
            amount = int(input("Введите сумму для пополнения (кратно 50): "))
            if amount % 50 == 0:
                deposit(amount)
            else:
                print("Сумма должна быть кратна 50.")
        elif choice == '2':
            amount = int(input("Введите сумму для снятия (кратно 50): "))
            if amount % 50 == 0:
                withdraw(amount)
            else:
                print("Сумма должна быть кратна 50.")
        elif choice == '3':
            break
        else:
            print("Неверный ввод.")

        if len(transactions) % COMMISSION_FREQ == 0:
            tax()

if __name__ == "__main__":
    atm()
