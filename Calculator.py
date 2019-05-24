def add(x, y):
    return x + y


def subtrack(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Infinite!"
    else:
        return x / y


print("SELECT OPERATION")
print("1. Add")
print("2. Subtrack")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice(1/2/3/4): ")

X = int(input("Enter X number: "))
Y = int(input("Enter Y number: "))

if choice == '1':
    print(X, "+", Y, "=", add(X, Y))
elif choice == '2':
    print(X, "-", Y, "=", subtrack(X, Y))
elif choice == '3':
    print(X, "*", Y, "=", multiply(X, Y))
elif choice == '4':
    print(X, "/", Y, "=", divide(X, Y))
else:
    print("Invalid input!")