class User_interfaces:
    error: str
    one_number: float
    two_number: float
    answer: str
    def start_user_interfaces():
        User_interfaces.answer = input("Ведите первое число: ")
        User_interfaces.one_number = float(User_interfaces.answer)
        User_interfaces.main_user_interfaces()
    def main_user_interfaces():
        User_interfaces.answer = input("Ведите второе число: ")
        User_interfaces.two_number = float(User_interfaces.answer)
        User_interfaces.answer = input("1. Вычитание\n2. Деление\n3. Нахождение остатка при делении\n4. Сложение\n5. Умножение\n:: Выбирете действие (1-5):\n:: ")
        Calculation.calculation()
        print("Результат: " + str(Calculation.result))
        User_interfaces.answer = input("Начать вычесление над результатом? [y/n] ")
        if (User_interfaces.answer == 'y' or User_interfaces.answer == 'Y'):
            User_interfaces.main_user_interfaces()
        if (User_interfaces.answer == 'n' or User_interfaces.answer == 'N'):
            exit
        if (User_interfaces.answer != 'y' and User_interfaces.answer != 'Y' and User_interfaces.answer != 'n' and User_interfaces.answer != 'N'):
            User_interfaces.error = "ответ не понятен (надо было написать y (что означает, что вы согласны) или n (вы не согласны))"
            User_interfaces.answer_error()
    def answer_error():
        print("Ошибка: " + User_interfaces.error + ". Перезагрузка программы...")
        User_interfaces.start_user_interfaces()
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
            User_interfaces.answer_error()
        #Для того что бы можно было выполнить матиматическое действие над результатом
        User_interfaces.one_number = Calculation.result
User_interfaces.start_user_interfaces()