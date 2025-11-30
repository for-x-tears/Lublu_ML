a: Ellipsis = ...
b: complex = complex(real=3, imag=2)
c: list = [a, b, 3, 4]
d: tuple = (1, 2, 3, 4)
e: set = {1, 2, 3, 4}
f: dict = {1: '11', 2: '22'}


print(
    c[2], c[0], c[-1]
)
#слайсинг ---
print(
    c[1-2]
)
print(
    c[::2] #[start:stop:step]
)
# Чем  кортеж d отличается от цикла? 
print(
    d[::2]
)



