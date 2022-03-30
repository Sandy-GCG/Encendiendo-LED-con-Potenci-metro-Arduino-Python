# Encendiendo-LED-con-Potenci-metro-Arduino-Python
En las siguientes instrucciones de laboratorio se obtuvieron las siguientes:
1. Crear una clase que permita entre 50% o al 100% de resistencia. En caso está menos de ese valor se apague un led de lo contrario encendido (led rojo). Usar función map().
2.  Crear un programa en Python que grafique en un plano cartesiano la cantidad de voltios que pasan en la comunicación serial controlado por el potenciómetro.
3.  Al llegar al máximo del valor de residencia potenciómetro se encienda el led de manera intermitente que permita indicar al usuario que debe bajar la intensidad.
4.  Programar un Dashboard en Python en tiempo real que grafique el valor del potenciómetro.

TENER EN CUENTA:
- La primera y tercera instrccuón se lleva a caso con el archivo codificado en el IDE de Arduino llamado: "Grafica_2D", el cual consiste en extraer el voltaje conforme avance el potenciómetro, por lo tanto entre el 0% y antes del 50% la led Roja se encontrará apagada, mientras que del 50% y antes del 100% se encenderá de forma permanente, de lo contrario, si el voltaje se encuentra al 100% quiere decir que la led se encenderá y apagará de forma intermitente.
- Para la segunda instrucción se obtiene ejecutando el archivo de Python llamado: "Pano Cartesiano", el cuál graficará en 2D el voltaje que recibe el potenciómetro según avance. (OJO: antes de ejecutar el archivo de Python, debe de tener subido el Archivo de Arduino llamado: "Grafica_2D").
- Por último, para obtener la solución de la última instrucción será necesario que usted descargue el archivo completo de Dashboard, en dado caso no sea necesario cambiar el diseño del Dashboard, en caso contrario, será necesario descargar e instalar el IDE de Eric. En caso desee el mismo Dashboardo, necesitará subir el programa que se encuentra  llamado : "Arduino" dentro de la carpeta de Dashboard, para luego compilar el programa en Python, que se encuentra en: "Programa Python" y correr el archivo llamado: "main.py".

VIDEO PARA INSTALAR EL IDE DE ERIC: https://www.youtube.com/watch?v=s81_WnM1oJA
