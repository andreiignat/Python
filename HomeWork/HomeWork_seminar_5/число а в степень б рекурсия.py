
a = int(input('Введите число: '))
b = int(input('Введите степень: '))

def f(a, b):
    if b == 0:
        return 1
    return a * f(a, b - 1)

print(f(a, b))

