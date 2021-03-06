def divisors(num):
    divisors = []
    try:
        if num < 0:
                raise ValueError("Ingrese un número positivo")
        else:
            for i in range(1, num + 1):
                if num % i == 0:
                    divisors.append(i)
            return divisors
    except ValueError as ve:
            print(ve)
            quit()

def run():
    try:
        num = int(input("Ingresa un número: "))
        print(divisors(num))
        print("Termino mi programa")
    except ValueError:
            print("Debes ingresar un número")

if __name__ == '__main__':
    run()