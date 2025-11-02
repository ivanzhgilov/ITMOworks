while True:
    string = input("Введите целое число в десятичной системе, которое хотите перевести в систему счисления с сонованием (-10): ")
    if string.isdigit() or (string[1:].isdigit() and string[0] == "-"):
        number = int(string)
        break
    else:
        print("Нужно ввести целое число в десятичной системе которое хотите перевести в систему счисления с сонованием (-10)")

start_ns = 10
finish_ns = -10

n = number
result = ""
while n:
    a = n // finish_ns
    b = n % finish_ns
    if b != 0:
        a += 1
        b += 10
    n = a
    result = str(b) + result

print(result)
