class User_interfaces:
    error: str
    one_number: float
    two_number: float
    result: float
    answer: str
    def start():
        User_interfaces.answer = input("Ведите первое число: ")
        User_interfaces.one_number = float(User_interfaces.answer)
        User_interfaces.Main_interfaces()
    def Main_interfaces():
        User_interfaces.answer = input("Ведите второе число: ")
        User_interfaces.two_number = float(User_interfaces.answer)
        User_interfaces.answer = input("1. Вычитание\n2. Деление\n3. Нахождение остатка при делении\n4. Сложение\n5. Умножение\n:: Выбирете действие (1-5):\n:: ")
        Calculation.calculation()
        print("Результат: " + str(Calculation.result))
        answer = input("Начать вычесление над результатом? [y/n] ")
        if (answer == 'y' or answer == 'Y'):
            print(True)
    def Answer_error():
        print("Ошибка: " + User_interfaces.error)
        exit
class Calculation:
    result: float
    def calculation():
        int_answer: int = int(User_interfaces.answer)
        one_number = User_interfaces.one_number
        two_number = User_interfaces.two_number
        if (int_answer == 1):
            Calculation.result = one_number - two_number
        if (int_answer == 2):
            Calculation.result = one_number / two_number
        if (int_answer == 3):
            Calculation.result = one_number % two_number
        if (int_answer == 4):
            Calculation.result = one_number + two_number
        if (int_answer == 5):
            Calculation.result = one_number * two_number
        if (int_answer < 1 or int_answer > 5):
            User_interfaces.error = "данная операция не найдена"
            User_interfaces.Answer_error()
User_interfaces.start()