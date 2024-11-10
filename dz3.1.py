import random

secret_number = random.randint(1, 10)
attempts = 3

print("Я загадав число від 1 до 10 Вгадай яке!!")

for attempt in range(1, attempts + 1):
    guess = int(input(f"Введи число: "))

    if guess == secret_number:
        print("Вітаю! Ви вгадали число!")
        break
    elif guess < secret_number:
        print("Більше.")
    else:
        print("Менше.")

    if attempt == attempts:
        print(f"На жаль, ви не вгадали. Загадане число було: {secret_number}")
