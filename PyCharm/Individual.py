#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def help_info():
    print("Список команд:")
    print("add - добавить студента")
    print("list - вывести список студентов")
    print("filter list - список студентов со средним баллом больше 4")
    print("exit - завершить работу с программой")


def add_student():
    name = input("Фамилия и инициалы студента: ")
    group = int(input("Номер группы: "))
    marks = list(map(int, input("Пять оценок студента: ").split()))

    if len(marks) != 5:
        print("Неверное количество оценок", file=sys.stderr)
        return

    student = {
        'name': name,
        'group': group,
        'marks': marks,
    }

    students.append(student)


def out_students():
    line = '+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 14,
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^14} |'.format(
            "№",
            "Ф.И.О.",
            "Номер группы",
        )
    )
    print(line)

    for idx, student in enumerate(students, 1):
        print(
            '| {:>4} | {:<30} | {:<14} |'.format(
                idx,
                student.get('name', ''),
                student.get('group', ''),
            )
        )
    print(line)


def out_students_filter():
    if len(students) > 0:
        line = '+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 14,
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^14} |'.format(
                "№",
                "Ф.И.О.",
                "Номер группы",
            )
        )
        print(line)

        for idx, student in enumerate(students, 1):
            if sum(student.get('marks')) / 5 > 4:
                print(
                    '| {:>4} | {:<30} | {:<14} |'.format(
                        idx,
                        student.get('name', ''),
                        student.get('group', ''),
                    )
                )
                print(line)

    else:
        print("Список студентов пустой.")


def main():
    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'help':
            help_info()

        elif command == 'add':
            add_student()

            if len(students) > 1:
                students.sort(key=lambda item: item.get('group', ''))

        elif command == 'list':
            if len(students) > 0:
                out_students()
            else:
                print("Список студентов пустой.")

        elif command == "filter list":
            if len(students) > 0:
                out_students_filter()
            else:
                print("Список студентов пустой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    students = []

    main()
