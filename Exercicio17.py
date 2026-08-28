p = int(input("Primeiro número: "))
s = int(input("Segundo número: "))

r = 0
x = 1


multiplicador = abs(s)

while x <= multiplicador:
    r = r + p
    x = x + 1


if s < 0:
    r = -r

print(f"{p} x {s} = {r}")