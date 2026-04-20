
# Escribe un programa que pida al usuario dividir dos números.

# Utiliza try/except para capturar una división por cero y mostrar un mensaje de error amigable.

def dividir_numeros():
    try:
        # Pedimos los datos al usuario
        num1 = float(input("Ingresa el primer número (dividendo): "))
        num2 = float(input("Ingresa el segundo número (divisor): "))
        
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado}")
        
    except ValueError:
        print("Error: ¡Debes ingresar solo números!")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero. Intenta con otro número.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

dividir_numeros()





# Crea una función validar_edad(edad) que lance una excepción EdadInvalidaError si la edad es menor que 0.
# Define esta excepción como clase hija de Exception.
# Definimos la excepción personalizada

class EdadInvalidaError(Exception):
    """Excepción lanzada cuando la edad es menor a cero."""
    pass

def validar_edad(edad):
    if edad < 0:
        raise EdadInvalidaError("La edad no puede ser un número negativo.")
    else:
        print(f"Edad validada correctamente: {edad}")

# Ejemplo de uso:
try:
    mi_edad = int(input("Ingresa tu edad: "))
    validar_edad(mi_edad)
except EdadInvalidaError as error:
    print(f"Error de validación: {error}")
except ValueError:
    print("Error: Ingrese un número entero válido.")



# Simula la apertura de un archivo (puede ser un print("Abriendo archivo...")) y utiliza
# finally para imprimir "Cerrando archivo..." aunque haya ocurrido un error.

def simular_archivo():
    try:
        print("Abriendo archivo...")
        # Simulamos una operación que podría fallar
        dato = int(input("Introduce un número para procesar en el archivo: "))
        resultado = 100 / dato
        print(f"Procesando datos: {resultado}")
        
    except Exception as e:
        print(f"Se produjo un error durante el procesamiento: {e}")
        
    finally:
        # Este bloque siempre se ejecuta
        print("Cerrando archivo...")

simular_archivo()
