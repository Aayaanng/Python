# =============================================
# Python Operators Demo 
# =============================================

print("=== Arithmetic Operators ===\n")

a = 10
b = 3

print(a, "+", b, "=", a + b, "   # Addition")
print(a, "-", b, "=", a - b, "   # Subtraction")
print(a, "*", b, "=", a * b, "   # Multiplication")
print(a, "/", b, "=", a / b, "   # Division")
print(a, "//", b, "=", a // b, "  # Floor Division")#quotient rounded of
print(a, "%", b, "=", a % b, "    # Modulus")#remainder of division
print(a, "**", b, "=", a ** b, "  # Exponents")
print("-" * 40)

print("\n=== Assignment Operators ===\n")

x = 10
print("x =", x)

x += 5
print("x += 5  → x =", x)

x -= 3
print("x -= 3  → x =", x)

x *= 2
print("x *= 2  → x =", x)

x /= 4
print("x /= 4  → x =", x)

x //= 2
print("x //= 2 → x =", x)

x %= 3
print("x %= 3  → x =", x)

x **= 2
print("x **= 2 → x =", x)
print("-" * 40)

print("\n=== Comparison Operators ===\n")

p = 5
q = 3

print(p, "==", q, "→", p == q)
print(p, "!=", q, "→", p != q)
print(p, ">", q, " →", p > q)
print(p, "<", q, " →", p < q)
print(p, ">=", q, "→", p >= q)
print(p, "<=", q, "→", p <= q)
print("-" * 40)

print("\n=== Logical Operators ===\n")

print("(5 > 3) and (3 > 1)  →", (5 > 3) and (3 > 1))
print("(5 > 3) or (3 < 1)   →", (5 > 3) or (3 < 1))
print("not (5 > 3)          →", not (5 > 3))
print("-" * 40)

print("\n=== Identity Operators ===\n")

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 is list2     →", list1 is list2)
print("list1 is list3     →", list1 is list3)
print("list1 is not list2 →", list1 is not list2)
print("-" * 40)

print("\n=== Membership Operators ===\n")

fruits = ['apple', 'banana', 'cherry']

print("'apple' in fruits     →", 'apple' in fruits)
print("'mango' in fruits     →", 'mango' in fruits)
print("'mango' not in fruits →", 'mango' not in fruits)
print("-" * 40)

print("\n=== Bitwise Operators ===\n")

m = 6   # Binary: 110
n = 3   # Binary: 011

print(m, "&", n, " =", m & n, "  # Bitwise AND")
print(m, "|", n, " =", m | n, "  # Bitwise OR")
print(m, "^", n, " =", m ^ n, "  # Bitwise XOR")
print("~", m, "      =", ~m, "   # Bitwise NOT")
print(m, "<< 1   =", m << 1, " # Left Shift")
print(m, ">> 1   =", m >> 1, "  # Right Shift")