import math
def calculator():
    calc1 = input("Input your first number: ").strip()
    calc2 = input("Input your second number: ").strip()
    calc = input('Choose an operator (+, -, x, /, %): ').strip().lower()

    if not calc1.isdigit() or not calc2.isdigit():
        print("Invalid input, numbers only!")
        return calculator()

    # Valid operators check
    if calc not in ['+', '-', 'x', '/', '%']:
        print("Invalid operator!")
        return calculator()
    #Defining the calc(s) as integers to make sure they get calculated correctly. How did I forget this
    calc1 = int(calc1)
    calc2 = int(calc2)

    if calc == "+":
        print(calc1 + calc2)
    elif calc == "x":
        print(calc1 * calc2)
    elif calc == "-":
        print(calc1 - calc2)
    elif calc == "/":
        if calc2 == 0:
            print("Error! Division by zero.")
        else:
            print(calc1 / calc2)
    elif calc == "%":
        if calc2 == 0:
            print("Error! Division by zero.")
        else:
            print(f"{(calc1 / calc2) * 100}%")

    print('Credits: Consanguineous\n2024\nhttps://github.com/Consanguineous')
    return calculator()


calculator()
