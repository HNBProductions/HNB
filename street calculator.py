from secrets import choice


def add(a, b):
    return a + b 
def subtract(a, b):
    return a - b
def divide(a,b):
    return a / b
def multiply (a, b):
    return a * b
print("gimme da numba homie")
a = int(float(input("da first numba: ")))
b = int(float(input("da second numba: ")))
print("wot do homie")
print("1.Add")
print("2.Subtract")
print("3.Divide")
print("4.Multiply")  
choice = str(input(""))
if choice == "1":
    print(add(a,b))
elif choice == "2":
    print(subtract(a,b))
elif choice == "3":
    print(divide(a,b))
elif choice == "4":
    print(multiply(a,b))    