#Escribe en comentarios (#) respuestas a las siguientes preguntas:

#• ¿Qué es la programación orientada a objetos?

#La programacion orientada a objetos POO es un paradigma de programacion mediante el cual
#se puede llegar a estructutar programas de una manera que las propiedades y comportamientos del mismo se puedan agrupar en obejtos.

#• ¿En qué se diferencia de la programación estructurada?

#La POO se basa en clases, encapsula datos y metodos que esten relacionados entre si, define conjunto de objetos donde se combinan de forma
#modular datos y funciones.
#La Programacion estructurada se orienta a acciones y se basa en funciones, separa los datos de las funciones.

#• Menciona un ejemplo de la vida cotidiana donde se vea reflejado el concepto de objeto.

#Un ejemplo de objeto seria "perro" que tiene "raza","color","peso","edad" que serian los atributos del objeto "perro"

#2. Definición de una clase simple
#• Crea una clase llamada Perro.
#• Agrega atributos como nombre, edad y raza.
#• Define un método ladrar() que imprima "¡Guau!".
#• Crea una instancia de la clase Perro y llama al método ladrar().

class Perro:   # se crea clase llamada perro

    def __init__(self,nombre,edad,raza): # se agregan atributos
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    def ladrar(self):
        print(f"Guau!")
    
pepe = Perro("pepe",5,"pastoraleman") # se crea instanacia

#3. Diferenciar conceptos
#• En comentarios, explica la diferencia entre:

#• Clase, instancia y objeto

# Clase es el plano o diseño (atributos y metodos) que referncia un objeto de la vida real.
# El objeto se crea en base a la clase, es darle vida a la clase mediante datos.
# La instancia es la creacion de un objeto a partir de una clase.


#• Atributo y estado

# El Atributo es la caracteristica que puede tener un objeto.
# El estado es el conjunto de esos atributos en momento especifico.

#• Método y comportamiento

# El Metodo es la accion que puede ejecutar el objeto de una clase.
# El Comportamiento es la deficion de lo que hara ante mensajes enviados por otros objetos.



#4. Principios de POO

#• Modifica la clase Perro para que los atributos estén encapsulados (prefijo _).

class Perro:   # se crea clase llamada perro

    def __init__(self,nombre,edad,raza): # se agregan atributos
        self.__nombre = nombre # atributo queda encapsulado
        self.__edad = edad     # atributo queda encapsulado
        self.__raza = raza     # atributo queda encapsulado


#• Agrega un método mostrar_info() que devuelva el estado del objeto en forma de texto.

def mostrar_info(self):
        
        return f"Perro: {self.nombre} {self.edad} ({self.raza})" # esto devuelve el estado del objeto en forma de texto



#• Comenta brevemente qué significa la abstracción y cómo se relaciona con este ejemplo.

# La Abtraccion es el proceso de identificar las características esenciales de un objeto,
#  ignorando los detalles internos no relevantes para el sistema.