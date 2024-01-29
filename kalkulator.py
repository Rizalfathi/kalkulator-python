def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "gabisa dibagi 0 pintar❗❗"

def calculator():
    print("Kalkulator simpel 😁")
    print("Pilih Operasinya boss:")
    print("1. Pertambahan ➕")
    print("2. Pengurangan ➖")
    print("3. Perkalian ✖")
    print("4. Pembagian ➗")

    choice = input("Pilihan ente (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        print("Bukan itu inputnya cok")
        return

    num1 = float(input("Masukkan Angka Pertama: "))
    num2 = float(input("Masukkan Angka Kedua: "))

    if choice == '1':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")

if __name__ == "__main__":
    calculator()
