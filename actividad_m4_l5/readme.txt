Objetivos

• Comprender qué es una excepción y cómo se captura en Python.
• Aplicar estructuras try, except, else y finally en distintos contextos.
• Crear excepciones personalizadas para validar condiciones específicas.

Instrucciones

Crea una carpeta llamada actividad_m4_l5 y dentro de ella, un archivo llamado manejo_errores.py. En
este archivo, desarrolla lo siguiente:

1. Captura básica de errores
• Escribe un programa que pida al usuario dividir dos números.
Utiliza try/except para capturar una división por cero y mostrar un mensaje de error amigable.

2. Múltiples excepciones
• Agrega validación para que el usuario ingrese solo números.
Usa un bloque try/except con múltiples excepciones (ZeroDivisionError, ValueError).

3. Excepciones personalizadas
• Crea una función validar_edad(edad) que lance una excepción EdadInvalidaError si la edad
es menor que 0.
Define esta excepción como clase hija de Exception.

4. Limpieza de recursos
• Simula la apertura de un archivo (puede ser un print("Abriendo archivo...")) y utiliza
finally para imprimir "Cerrando archivo..." aunque haya ocurrido un error.

Entregables

• Carpeta comprimida (.zip) que contenga:
• El archivo manejo_errores.py
• Un documento README.txt explicando:
• ¿Qué tipo de error crees que es más común en programas reales?

Los errores mas comunes generalmente puede ser el ingreso de un dato no valido
 no reconocido para lo que el sistema está solicitando, por ejemplo, se solicita un numero entero
y el usuario ingresa un decimal o también el sistema puede requerir una palabra y el usuario
por error o desconocimiento ingresa un número.

• ¿Por qué es importante manejar excepciones?

Porque evitaria que un flujo se corte o caiga por datos ingresados no validos.