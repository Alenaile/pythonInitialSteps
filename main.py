from typing import Final

SECOND_INTERVAL_ETALON = 10
THIRD_INTERVAL_ETALON = 20


def first_category_interval(first_digit, second_digit):
    return first_digit < second_digit


def second_category_interval(one, another):
    return (one >= another) & (one - another < SECOND_INTERVAL_ETALON)


def third_category_interval(one, another):
    return (one > another) & (one - another >= SECOND_INTERVAL_ETALON) & (one - another < THIRD_INTERVAL_ETALON)


def define_category(a):
    B: Final = 100
    try:
        user_input = round(float(input(a)))

        if first_category_interval(user_input, B):
            print("Первая категория")
        elif second_category_interval(user_input, B):
            print("Вторая категория")
        elif third_category_interval(user_input, B):
            print("Третья категория")
        else:
            print("Четвертая категория")
    except ValueError:
        print("Пожалуйста, введите цифру")


define_category("Enter your digit ")
