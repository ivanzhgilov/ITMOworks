message = input(
    "Введите сообщение, состоящее из 7-символьной последовательности '0' и '1' без пробелов,\nЗакодированное классическим кодом Хемминга (7;4),\nкоторое хотите расшифровать: ")
array_message = [int(el) for el in list(message)]
while not (len(array_message) == 7 and all([el == 0 or el == 1 for el in array_message])):
    message = input(
        "Неверный ввод попробуйте снова\nВведите сообщение, состоящее из 7-символьной последовательности '0' и '1' без пробелов,\nЗакодированное классическим кодом Хемминга (7;4),\nкоторое хотите расшифровать: ")
    array_message = [int(el) for el in list(message)]

syndrome = []
for i in range(3):
    s = 0
    step = 2 ** i
    start = 2 ** i - 1
    for index in range(start, 7, step * 2):
        s += sum(array_message[index:index + step])

    syndrome.append(s % 2)

if syndrome == [0, 0, 0]:
    print("Ошибки в сообщении не обнаружено")
else:
    index_mistake = -1
    for i in range(3):
        index_mistake += syndrome[i] * 2 ** i
    true_value = (array_message[index_mistake] + 1) % 2
    array_message[index_mistake] = true_value
    print(f"Ошибка в бите номер {index_mistake + 1}, его исходное значение {true_value}")

result_message = str(array_message[2]) + "".join(map(str, array_message[4:]))

print(f"Верное отправленное сообщение: {result_message}")
