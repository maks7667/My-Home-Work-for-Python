"""CALCULATION"""
def factorial(n):
    """Функция для вычисления факториала числа"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    """Функция для вычисления чисел Фибоначчи"""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def calculator():
    """Главная функция калькулятора"""
    survey = input(
        "Доступные операции: \n1. Сложение (+)\n2. Вычитание (-)\n3. Умножение (*)\n"
        "4. Деление (/) \n5. Возведение в степень (**) \n"
        "6. Число фибоначи (f)\n7. Факториал(!)\nВыберите операцию: ")
    try:
        if survey in {"1","2","3","4","5","6","7","+","-","*","/","**","f","!"}:
            if survey in {"5", "**"}:
                base = float(input("Введите основание: "))
                exponent = float(input("Введите показатель степени: "))
                result = base**exponent
                print("Результат:", result)
            elif survey in {"1", "2", "3", "4", "+", "-", "*", "/"}:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
                if survey in  {"1", "+"}:
                    result = num1 + num2
                elif survey in  {"2", "-"}:
                    result = num1 - num2
                elif survey in {"3", "*"}:
                    result = num1 * num2
                elif survey in {"4", "/"}:
                    result = num1 / num2
                print("Результат:", result)
            else:
                n = float(input("Введите число"))
                if survey in {"6", "f"}:
                    print(fibonacci(n))
                else:
                    print(factorial(n))

        else:
            print("Неверная операция.")

        more_calculations = input("Хотите выполнить еще вычисления? (yes/no): ")
        if more_calculations.lower() == "yes" or more_calculations.lower() == "y":
            calculator()
        else:
            print("До свидания!")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    calculator()
