#     print("\n--- TABLA DE VERDAD: AND ---")
#    print("A | B | A AND B")
#    print("0 | 0 |   0")
#    print("0 | 1 |   0")
#    print("1 | 0 |   0")
#    print("1 | 1 |   1")

print("\n--- TABLA DE VERDAD: AND ---")
print("A | B | A AND B")
for i in range (0, 2):
    for b in range (0, 2):
        x = i and b
        print(f"{i} | {b} |   {x}")

#print("\n--- TABLA DE VERDAD: OR ---")
#    print("A | B | A OR B")
#    print("0 | 0 |  0")
#    print("0 | 1 |  1")
#    print("1 | 0 |  1")
#    print("1 | 1 |  1")

print("\n--- TABLA DE VERDAD: OR ---")
print("A | B | A OR B")
for i in range (0, 2):
    for b in range (0, 2):
        x = i or b
        print(f"{i} | {b} |   {x}")


#print("\n--- TABLA DE VERDAD: NOT ---")
#    print("A | NOT A")
#    print("0 |   1")
#    print("1 |   0")

print("\n--- TABLA DE VERDAD: NOT ---")
print("A | NOT A")
for i in range (0, 2):
    x = int(not i)
    print(f"{i} |   {x}")
#print("\n--- TABLA DE VERDAD: XOR ---")
#    print("A | B | A XOR B")
#    print("0 | 0 |   0")
#    print("0 | 1 |   1")
#    print("1 | 0 |   1")
#    print("1 | 1 |   0")

print("\n--- TABLA DE VERDAD: XOR ---")
print("A | B | A XOR B")
for i in range (0, 2):
    for b in range (0, 2):
        x = i ^  b
        print(f"{i} | {b} |   {x}")

#print("\n--- TABLA DE VERDAD: NAND ---")
#    print("A | B | A NAND B")
#    print("0 | 0 |   1")
#    print("0 | 1 |   1")
#    print("1 | 0 |   1")
#    print("1 | 1 |   0")

print("\n--- TABLA DE VERDAD: NAND ---")
print("A | B | A NAND B")
for i in range (0, 2):
    for b in range (0, 2):
        x = int(not (i and b))
        print(f"{i} | {b} |   {x}")