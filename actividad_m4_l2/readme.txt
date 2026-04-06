Objetivos
• Crear clases en Python con atributos, métodos y constructor.
• Aplicar métodos accesadores y mutadores para encapsular información.
• Comprender y utilizar la sobrecarga de métodos.
• Implementar relaciones de colaboración y composición entre objetos.

Instrucciones
Crea una carpeta llamada actividad_m4_l2 y dentro de ella, un archivo Python llamado poo_avanzado.py 
que contenga los siguientes ejercicios:

1. Definición de una clase con constructor
• Crea una clase Libro con los atributos titulo, autor y anio_publicacion.
• Define un método constructor __init__() que inicialice esos atributos.
• Crea un método mostrar_info() que imprima los datos del libro.

2. Métodos accesadores y mutadores
• Implementa métodos get_titulo() y set_titulo(nuevo_titulo) para acceder y modificar el 
atributo titulo.
• Repite lo mismo para el atributo anio_publicacion.
• Usa estos métodos para modificar el título de un libro desde el programa principal.

3. Sobrecarga de métodos
• En la clase Libro, crea un método resumen() que:
• Si no recibe parámetros, imprime "Libro sin resumen disponible".
• Si recibe un texto como parámetro, imprime ese resumen.
• Simula la sobrecarga usando valores por defecto y condicionales en el método.

4. Colaboración entre objetos
• Crea una clase Autor con atributos nombre y pais.
• Modifica la clase Libro para que el atributo autor sea un objeto de tipo Autor.
• En el método mostrar_info(), muestra también el nombre y país del autor.

5. Composición
• Crea una clase Editorial con atributos nombre y ciudad.
• Modifica la clase Libro para que tenga un atributo editorial (objeto de tipo Editorial).
• Asegúrate de que la instancia de Editorial se cree dentro del constructor de Libro.

Entregables
• Carpeta comprimida (.zip) que contenga:
• El archivo poo_avanzado.py
• Un documento README.txt con una breve reflexión:
• ¿Qué relación te pareció más fácil de implementar: colaboración o composición? ¿Por
qué?