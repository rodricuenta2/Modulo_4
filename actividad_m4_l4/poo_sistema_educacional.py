class Persona:
    def __init__(self, nombre, id_identificacion):
        self.nombre = nombre
        self.__id_identificacion = id_identificacion

    def presentarse(self):
        """Método base para demostrar polimorfismo"""
        return f"Hola, soy {self.nombre}."

class Profesor(Persona):
    def __init__(self, nombre, id_identificacion, especialidad):
        super().__init__(nombre, id_identificacion)
        self.especialidad = especialidad

    # Polimorfismo: Sobrescribimos el método de la clase padre
    def presentarse(self):
        return f"Buen día, soy el Prof. {self.nombre}, especialista en {self.especialidad}."

class Alumno(Persona):
    def __init__(self, nombre, id_identificacion, matricula):
        super().__init__(nombre, id_identificacion)
        self.matricula = matricula
        self.__notas = []

    # Polimorfismo: Sobrescribimos el método de la clase padre
    def presentarse(self):
        return f"Hola, soy el alumno {self.nombre}. Mi matrícula es {self.matricula}."

    def agregar_nota(self, nota):
        self.__notas.append(nota)

    def obtener_promedio(self):
        return sum(self.__notas) / len(self.__notas) if self.__notas else 0

class Asignatura:
    def __init__(self, nombre_curso, profesor):
        self.nombre_curso = nombre_curso
        self.profesor = profesor
        self.estudiantes = []

    def inscribir_alumno(self, alumno):
        self.estudiantes.append(alumno)

    # Implementación de "Sobrecarga" de métodos (Simulada en Python)
    def generar_reporte(self, detalle=False):
        """
        Si 'detalle' es False, solo imprime nombres.
        Si 'detalle' es True, imprime nombres y promedios.
        """
        print(f"\n--- Reporte de {self.nombre_curso} ---")
        for est in self.estudiantes:
            if detalle:
                print(f"Estudiante: {est.nombre} | Promedio: {est.obtener_promedio()}")
            else:
                print(f"Estudiante: {est.nombre}")

# --- Interacción entre Objetos (Main) ---

# 1. Instanciar objetos
profe_quimica = Profesor("Dr. Walter", "5544-2", "Química")
alumno1 = Alumno("Jesse", "9988-1", "A-12")
alumno2 = Alumno("Skyler", "7766-3", "A-13")

# 2. Interacción y Polimorfismo
# Creamos una lista de personas (profesores y alumnos mezclados)
comunidad_educativa = [profe_quimica, alumno1, alumno2]

print("--- Demostración de Polimorfismo ---")
for individuo in comunidad_educativa:
    # Cada objeto responde al mismo método de forma distinta según su clase
    print(individuo.presentarse())

# 3. Acceder a propiedades y métodos
curso_quimica = Asignatura("Química Orgánica", profe_quimica)
curso_quimica.inscribir_alumno(alumno1)
curso_quimica.inscribir_alumno(alumno2)

# Agregamos notas mediante el método del objeto alumno
alumno1.agregar_nota(4.5)
alumno2.agregar_nota(7.0)

# 4. Demostración de Sobrecarga (usando el mismo método con distintos argumentos)
print("\n--- Demostración de 'Sobrecarga' (Argumentos opcionales) ---")
curso_quimica.generar_reporte()           # Versión simple
curso_quimica.generar_reporte(detalle=True) # Versión detallada