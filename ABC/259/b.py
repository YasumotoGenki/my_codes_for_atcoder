import math

a, b, d = map(int, input().split())

radd = math.radians(d)
new_x = math.cos(radd) * a - math.sin(radd) * b
new_y = math.sin(radd) * a + math.cos(radd) * b

print(new_x, new_y)

# ref: https://mathwords.net/heimenkaiten
# ref: https://note.nkmk.me/python-math-sin-cos-tan/