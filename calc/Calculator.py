from time import sleep


class Calculator:

    def iniciarCalc():
        print("Welcome to Calculator")
        print("Choose any of the options below:")
        escolha = int(input("Menu:\n1- Addition\n2- Subtraction\n3- Multiplication\n4- Division\n5- Exit\n----> "))

        if escolha == 1:
            Calculator.addition()
        elif escolha == 2:
            Calculator.subtraction()
        elif escolha == 3:
            Calculator.multiplication()
        elif escolha == 4:
            Calculator.share()
        elif escolha == 5:
            print("Saindo...")
            sleep(1)
            exit()

    def addition():
        print("You choose to addition")
        sleep(1)
        n1 = int(input("Choose the first number: "))
        n2 = int(input("Choose the second number: "))
        result = n1 + n2
        print(f'{n1} + {n2} = {result}')
        Calculator.recomecar()

    def multiplication():
        print("You choose to multiplication")
        sleep(1)
        n1 = int(input("Choose the first number: "))
        n2 = int(input("Choose the second number: "))
        result = n1 * n2
        print(f'{n1} * {n2} = {result}')
        Calculator.recomecar()
    
    def subtraction():
        sleep(1)
        print("You choose to subtraction")
        n1 = int(input("Choose the first number: "))
        n2 = int(input("Choose the second number: "))
        result = n1 - n2
        print(f'{n1} - {n2} = {result}')
        Calculator.recomecar()
    
    def share():
        sleep(1)
        print("You choose to share")
        n1 = int(input("Choose the first number: "))
        n2 = int(input("Choose the second number: "))
        result = n1 / n2
        print(f'{n1} / {n2} = {result}')
        Calculator.recomecar()

    def recomecar():
        print("Wish to reload??\n1- Yes\n2- No")
        escolha = int(input("----> "))
        if escolha == 1:
            Calculator.iniciarCalc()
        elif escolha == 2:
            print("Exiting...")
            sleep(1)
            exit()


Calculator.iniciarCalc()







    

    