# Definición de las funciones básicas de la calculadora
def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Error: División por cero"
    return x / y

# Función principal de la calculadora
def calculadora():
    print("Bienvenido a la calculadora")
    while True:
        # Solicitar entradas del usuario
        try:
            num1 = float(input("Ingrese el primer número: "))
            operador = input("Ingrese el operador (+, -, *, /): ")
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Entrada inválida, intente nuevamente.")
            continue

        # Realizar la operación correspondiente
        if operador == "+":
            resultado = sumar(num1, num2)
        elif operador == "-":
            resultado = restar(num1, num2)
        elif operador == "*":
            resultado = multiplicar(num1, num2)
        elif operador == "/":
            resultado = dividir(num1, num2)
        else:
            print("Operador no válido. Intente de nuevo.")
            continue

        # Mostrar el resultado
        print(f"Resultado: {resultado}")

        # Preguntar al usuario si desea realizar otra operación
        continuar = input("¿Desea realizar otra operación? (s/n): ")
        if continuar.lower() != 's':
            break

# Ejecutar la calculadora
if __name__ == "__main__":
    calculadora()