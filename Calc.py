calculater1 = input("Input your number 1").strip()
calculater2 = input("Input your number 2").strip()
calc = input('x, +, -, /, %').strip().lower()
if calc == "+".strip():
    print(int(calculater1) + int(calculater2))
if calc == "x".lower().strip():
    print(int(calculater1) * int(calculater2))
if calc == "-".strip():
    print(int(calculater1) - int(calculater2))
if calc == "/".strip():
    print(int(calculater1) / int(calculater2))
if calc == "%".strip():
    print(f"{int(calculater1) / int(calculater2) * 100}%")
if calc in ['+'.strip(), '/'.strip(), '-'.strip(), 'x'.lower().strip(), '%'.strip()]:
    print('Credits: Consanguineous\n' '2024\n' 'https://github.com/Consanguineous')