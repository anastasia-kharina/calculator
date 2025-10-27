print("Введите данные")
num1, num2, znak = int(input()), int(input()), input()
if znak == '+':
    print(num1+num2)
elif znak == '-':
    print(num1-num2)
elif znak == '*':
    print(num1*num2)
elif znak == '/':
    print(num1/num2)
else:
    print("Неверные данные")
