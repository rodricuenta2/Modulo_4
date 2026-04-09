#1. Definición de una clase con constructor


#• Crea una clase Libro con los atributos titulo, autor y anio_publicacion.
class Libro:
    def __init__(self, titulo, autor, anio_publicacion):

#• Define un método constructor __init__() que inicialice esos atributos.      
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

#• Crea un método mostrar_info() que imprima los datos del libro.
    def mostrar_info(self): # se crea metodo mostrar_info
        print(f"Libro: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.anio_publicacion}")

info_libros = Libro("Romeo y Julieta", "William Shakespeare", 1597)

info_libros.mostrar_info() # se llama a metodo mostrar_info

#2. Métodos accesadores y mutadores

#• Implementa métodos get_titulo() y set_titulo(nuevo_titulo) para acceder y modificar el 
#atributo titulo.

def get_titulo(self):
        return self._titulo

def set_titulo(self, nuevo_titulo):
       
    
#• Repite lo mismo para el atributo anio_publicacion.

    def anio_publicacion(self):
        return self._anio_publicacion

    def set_anio_publicacion(self, nuevo_anio_publicacion):
       
#• Usa estos métodos para modificar el título de un libro desde el programa principal.