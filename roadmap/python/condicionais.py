
x = 30
y = 10
z = 0
l = ["a", "b", "c", 10]

print(x > y)                     # True
print(y < x)                     # True
print(y <= 10)                   # True
print("a" in l)                  # True
             
print(x == 2)                    # False
print(y > z)                     # False
print(y != 10)                   # False
print(z >= 1)                    # False
             
print("z" not in l)              # True
print(10 == z)                   # False
print(y in l)                    # True
print(x == 30 and z != 0)        # False
print(x == 30 or y == "v")       # True