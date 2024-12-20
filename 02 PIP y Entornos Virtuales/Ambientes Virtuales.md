# Ambientes Virtuales

## ¿Qué es un ambiente virtual?

Instalar módulos y pquetes a nivel global puede causar problemas al momento de manejar varios ´royectos, por ejemplo, ára algunos proyectos necesitas otro tipo de versión de python, librerías o módulos. Para soluciónar esto se crea un ambiente virtual en cual se encapsula cada proyecto y no lo deja de forma compartida.

El ambiente global de python, se puede ver en la siguiente imagen:

![Python global](./globalPython.png)

Se ven los módulos de forma general, lo que puede cuasr problemas de versiones. La solución es crear un entorno virtual para cada proyecto de forma que se encapsulan los modulos y los atan a cada proyecto.

![Python ven](./venvPython.png)

Cada proyecto tiene sus propias dependencias y sus propias versiones.

Los **entornos virtuales** son una forma de crear un sistema operativo virtual dentro de otro sistema operativo. Esto permite a un usuario tener varios sistemas operativos diferentes en un mismo equipo físico, lo que puede ser muy útil en situaciones en las que es necesario utilizar diferentes aplicaciones o tecnologías que requieren entornos diferentes

## Ventajas de los entornos virtuales

- Permiten utilizar varios sistemas operativos en un mismo equipo físico
- Permiten instalar y utilizar diferentes aplicaciones y tecnologías de manera segura, sin tener que hacer cambios permanentes en el sistema operativo principal
- Pueden ser fácilmente movidos o copiados, lo que significa que pueden ser utilizados en diferentes equipos o compartidos con otros usuarios
- También pueden ser fácilmente respaldados y restaurados en caso de que se produzca un problema, lo que puede ayudar a prevenir la pérdida de datos o el tiempo de inactividad
- Ofrecen una forma conveniente y segura de utilizar diferentes aplicaciones y tecnologías en un mismo equipo

> 📝 **Nota:** En resumen, los entornos virtuales ofrecen una forma conveniente y segura 🔒 de utilizar diferentes aplicaciones y tecnologías en un mismo equipo, lo que puede ser muy útil para muchos usuarios y situaciones diferentes
