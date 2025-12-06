def rec_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return rec_fibonacci(n - 1) + rec_fibonacci(n - 2)

if __name__ == '__main__':
    n = int(input("Введите число: "))
    res = rec_fibonacci(n)
    print("Результат:", res)
