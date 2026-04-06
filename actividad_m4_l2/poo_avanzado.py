#1. Definición de una clase con constructor


#• Crea una clase Libro con los atributos titulo, autor y anio_publicacion.
class Libro:
    def __init__(self, titulo, autor, anio_publicacion):

#• Define un método constructor __init__() que inicialice esos atributos.      
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

#• Crea un método mostrar_info() que imprima los datos del libro.
    def mostrar_info(self):
        print(f"Libro: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.anio_publicacion}")

info_libros = Libro("Romeo y Julieta", "William Shakespeare", 1597)

info_libros.mostrar_info()