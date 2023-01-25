import random

number = input("How many pencils would you like to use:\n")

flag = True

while flag:
    if number.isnumeric():
        if number == '0':
            print("The number of pencils should be positive")
            number = input()
        else:
            flag = False
    else:
        print("The number of pencils should be numeric")
        number = input()

name1 = "John"
name2 = "Jack"

while True:
    name = input(f'Who will be the first ({name1}, {name2}):\n')
    while True:
        if name == name1 or name == name2:
            break
        else:
            print("Choose between " + name1 + " and " + name2)
            name = input()
    break

number = int(number)

print("|" * int(number))

while number > 0:

    pencils_to_be_used = 0
    pencils_to_be_used1 = 0

    if name == name1:
        pencils_to_be_used = input(f"{name1}'s turn!\n")
        who_losses = ""
        while True:
            if pencils_to_be_used == '1' or pencils_to_be_used == '2' or pencils_to_be_used == '3':
                pencils_to_be_used = int(pencils_to_be_used)
                if pencils_to_be_used > number:
                    print("Too many pencils were taken")
                    pencils_to_be_used = input()
                else:
                    number = number - pencils_to_be_used
                    print("|" * number)
                    who_losses += name1
                    break;
            else:
                print("Possible values: '1', '2' or '3'")
                pencils_to_be_used = input()

        if number != 0:
            print(f"{name2}'s turn:")
            who_losses = ""
            if number in [5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89,
                          93, 97, 101]:
                pencils_to_be_used1 = random.randint(1, 3)
                print(pencils_to_be_used1)
                number = number - pencils_to_be_used1
                print("|" * number)
                who_losses = name2
            elif number in [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88,
                            92, 96, 100]:
                pencils_to_be_used1 = 3
                print(pencils_to_be_used1)
                number = number - pencils_to_be_used1
                print("|" * number)
                who_losses = name2
            elif number in [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79, 83,
                            87, 91, 95, 99, 103]:
                pencils_to_be_used1 = 2
                print(pencils_to_be_used1)
                number = number - pencils_to_be_used1
                print("|" * number)
                who_losses = name2
            elif number in [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82,
                            86, 90, 94, 98, 102]:
                pencils_to_be_used1 = 1
                print(pencils_to_be_used1)
                number = number - pencils_to_be_used1
                print("|" * number)
                who_losses = name2
            elif number == 1:
                pencils_to_be_used1 = 1
                print(pencils_to_be_used1)
                number = number - pencils_to_be_used1
                print("|" * number)
                who_losses = name2

    elif name == name2:
        print(f"{name2}'s turn:")
        who_losses = ""
        if number in [5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89,
                      93, 97, 101]:
            pencils_to_be_used = random.randint(1, 3)
            print(pencils_to_be_used)
            number = number - pencils_to_be_used
            print("|" * number)
            who_losses = name2
        elif number in [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88,
                        92, 96, 100]:
            pencils_to_be_used = 3
            print(pencils_to_be_used)
            number = number - pencils_to_be_used
            print("|" * number)
            who_losses = name2
        elif number in [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79, 83,
                            87, 91, 95, 99, 103]:
            pencils_to_be_used = 2
            print(pencils_to_be_used)
            number = number - pencils_to_be_used
            print("|" * number)
            who_losses = name2
        elif number in [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82,
                        86, 90, 94, 98, 102]:
            pencils_to_be_used = 1
            print(pencils_to_be_used)
            number = number - pencils_to_be_used
            print("|" * number)
            who_losses = name2
        elif number == 1:
            pencils_to_be_used = 1
            print(pencils_to_be_used)
            number = number - pencils_to_be_used
            print("|" * number)
            who_losses = name2


        if number != 0:
            pencils_to_be_used1 = input(f"{name1}'s turn:\n")
            who_losses = ""
            while True:
                if pencils_to_be_used1 == '1' or pencils_to_be_used1 == '2' or pencils_to_be_used1 == '3':
                    pencils_to_be_used1 = int(pencils_to_be_used1)
                    if pencils_to_be_used1 > number:
                        print("Too many pencils were taken")
                        pencils_to_be_used1 = input()
                    else:
                        number = number - pencils_to_be_used1
                        print("|" * number)
                        who_losses = name1
                        break;
                else:
                    print("Possible values: '1', '2' or '3'")
                    pencils_to_be_used1 = input()

if who_losses == "John":
    print(f"{name2} won!")
else:
    print(f"{name1} won!")