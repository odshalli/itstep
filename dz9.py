result = []

def divider(a, b):
    if a < b:
        raise ValueError("Число a менше числа b")
    if b > 100:
        raise IndexError("Значення b більше 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
    try:
        res = divider(int(key), data[key])
        result.append(res)
    except (ValueError, IndexError, ZeroDivisionError, TypeError) as e:
        print(f"Виникла помилка з ключем {key}: {e}")

print("Результат:", result)
