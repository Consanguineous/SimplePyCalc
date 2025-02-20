calculater1 = input("Input your number 1").strip()
calculater2 = input("Input your number 2").strip()
calc = input('x, +, -, /').strip().lower()
if calc == "+":
    print(int(calculater1) + int(calculater2))
if calc == "x".lower().strip():
    print(int(calculater1) * int(calculater2))
if calc == "-".strip():
    print(int(calculater1) - int(calculater2))
if calc == "/".strip():
    print(int(calculater1) / int(calculater2))