Objetivos
•	Comprender la importancia del manejo de archivos en la programación.
•	Leer y escribir archivos de texto utilizando diferentes modos de apertura.
•	Aplicar buenas prácticas al trabajar con archivos (apertura, cierre, control de errores).

Instrucciones
Crea una carpeta llamada actividad_m4_l6 y dentro de ella, un archivo Python llamado
manejo_archivos.py. Este script debe resolver los siguientes ejercicios:
1.	Escribir en un archivo
•	Crea un archivo llamado datos.txt desde Python (modo escritura).
•	Escribe al menos 3 líneas de texto en él usando write().
2.	Leer el archivo completo
•	Abre el archivo datos.txt en modo lectura y muestra su contenido en pantalla usando read().
3.	Leer línea por línea
•	Usa readline() para leer e imprimir solo la primera línea del archivo.
•	Luego, usa un ciclo for para leer línea por línea el resto del archivo.
4.	Añadir contenido (modo append)
•	Vuelve a abrir el archivo en modo append y agrega una línea nueva.
•	Luego vuelve a abrirlo en modo lectura para comprobar que se agregó correctamente.
5.	Atributos y cierre
•	Muestra por pantalla el nombre del archivo (.name), si está cerrado (.closed) y el modo de apertura (.mode).
•	Asegúrate de cerrar el archivo correctamente con .close() o usando with.

 


Entregables
•	Carpeta comprimida (.zip) que contenga:
•	El archivo manejo_archivos.py
•	El archivo datos.txt generado por el script
•	Un documento README.txt con una breve explicación:
•	¿Qué diferencia notaste entre write() y append()?
•	¿Qué ventaja tiene usar with open(...) frente a abrir y cerrar manualmente?
