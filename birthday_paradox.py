import sys
from time import sleep

from numpy.random import randint


def check_birthdays(students_amount):
    birthdays = []
    for i in range(students_amount):
        a = randint(1, 366)
        if a in birthdays:
            return True
        else:
            birthdays.append(a)
    return False


def birthday_paradox():
    iterations_amount_str = input("Number of iterations (default = 100): ")
    iterations_amount = int(iterations_amount_str) \
        if iterations_amount_str.isdigit() else 100
    students_amount_str = input("Number of students (default = 23): ")
    students_amount = int(students_amount_str) \
        if students_amount_str.isdigit() else 23

    rectangle = u"▮"
    hyphen = "-"

    groups_with_pairs = 0
    for iter_number in range(1, iterations_amount + 1):
        if check_birthdays(students_amount):
            groups_with_pairs += 1
        percentage = (groups_with_pairs / iter_number) * 100
        percentage_int = int(percentage)
        sys.stdout.write(u"\r{progress_bar} {percentage:.2f} %\r".format(
            progress_bar=(rectangle * percentage_int + hyphen * (100 - percentage_int)),
            percentage=percentage))
        sys.stdout.flush()
        sleep(0.01)
    print()


if __name__ == "__main__":
    birthday_paradox()
