'''
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
'''

# Operadores aritméticos
a = 10
b = 3
print(f"Operadores aritméticos: {a} + {b} = {a + b}, {a} - {b} = {a - b}, {a} * {b} = {a * b}, {a} / {b} = {a / b}, {a} % {b} = {a % b}, {a} // {b} = {a // b}, {a} ** {b} = {a ** b}")

# Operadores lógicos
a = True
b = False
print(f"Operadores lógicos: {a} and {b} = {a and b}, {a} or {b} = {a or b}, not {a} = {not a}")

# Operadores de comparación
a = 10
b = 3
print(f"Operadores de comparación: {a} == {b} = {a == b}, {a} != {b} = {a != b}, {a} > {b} = {a > b}, {a} < {b} = {a < b}, {a} >= {b} = {a >= b}, {a} <= {b} = {a <= b}")

# Operadores de asignación
a = 10
b = 3
print(f"Operadores de asignación: a = {a}, b = {b}, a += b -> {a + b}, a -= b -> {a - b}, a *= b -> {a * b}, a /= b -> {a / b}, a %= b -> {a % b}, a //= b -> {a // b}, a **= b -> {a ** b}")

# Operadores de identidad
a = 10
b = 3

print(f"Operadores de identidad: a is b = {a is b}, a is not b = {a is not b}")

# Operadores de pertenencia
a = 10
b = [1, 2, 3, 4, 5]
print(f"Operadores de pertenencia: {a} in {b} = {a in b}, {a} not in {b} = {a not in b}")

# Operadores de bits
a = 10
b = 3
print(f"Operadores de bits: {a} & {b} = {a & b}, {a} | {b} = {a | b}, {a} ^ {b} = {a ^ b}, ~{a} = {~a}, {a} << {b} = {a << b}, {a} >> {b} = {a >> b}")

# Estructuras de control condicionales
a = 10
b = 3
if a > b:
    print(f"Estructuras de control condicionales: {a} > {b}")
elif a < b:
    print(f"Estructuras de control condicionales: {a} < {b}")
else:
    print(f"Estructuras de control condicionales: {a} = {b}")

# Estructuras de control iterativas
a = 10
b = 3
while a > b:
    print(f"Estructuras de control iterativas: {a} > {b}")
    a -= 1

# Estructuras de control de excepciones
try:
    a = 10
    b = 0
    print(f"Estructuras de control de excepciones: {a} / {b} = {a / b}")
except ZeroDivisionError:
    print(f"Estructuras de control de excepciones: Error al dividir por 0")
finally:
    print(f"Estructuras de control de excepciones: Finalizado")


for i in range(10, 56):
    if i != 16 and i % 3 != 0:
        print(i)
