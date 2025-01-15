# Docker

Es una herramienta que sirve para aislar entornos. Sirve para casos en los que no solo necesites aislar modulos de python, si no también el entorno de ejecución y la verisón de Pyhton. Esto lo hace usando **contenedores**.

También, asegura hacer despliegues de nuestra computadora a la nube. [1]

Docker es una plataforma de código abierto que permite crear, distribuir y ejecutar aplicaciones de forma independiente del sistema operativo subyacente. Proporciona una forma eficiente y rápida de crear entornos aislados llamados contenedores, que encapsulan una aplicación y todas sus dependencias, incluyendo bibliotecas, frameworks y herramientas necesarias para su funcionamiento.

## Características de Docker

- **Contenedores**: Los contenedores son entornos ligeros y portátiles que permiten empaquetar una aplicación y sus dependencias en una unidad autónoma. Cada contenedor se ejecuta de manera aislada, lo que significa que no se ve afectado por el sistema operativo o las aplicaciones que se ejecutan en el host.

- **Imágenes**: Una imagen de Docker es una plantilla o un conjunto de instrucciones que define cómo se debe crear un contenedor. Las imágenes son inmutables y se utilizan como base para crear y ejecutar contenedores.

- **Orquestación**: Docker proporciona herramientas y características para administrar y orquestar contenedores a gran escala. Docker Swarm y Kubernetes son dos ejemplos populares de herramientas de orquestación que permiten administrar múltiples contenedores en múltiples nodos o servidores.

- **Portabilidad**: Docker garantiza la portabilidad de las aplicaciones, lo que significa que un contenedor puede ejecutarse en cualquier entorno compatible con Docker sin problemas. Esto simplifica la implementación y la gestión de aplicaciones en diferentes entornos, ya sea en máquinas locales, servidores en la nube o en entornos de desarrollo y producción.

- **Eficiencia**: Los contenedores de Docker comparten el núcleo del sistema operativo y solo incluyen las dependencias necesarias para ejecutar la aplicación. Esto los hace ligeros y rápidos de implementar, lo que permite un uso eficiente de los recursos del sistema.

En resumen, Docker es una tecnología de virtualización a nivel de sistema operativo que permite empaquetar, distribuir y ejecutar aplicaciones de forma independiente y eficiente en contenedores. Proporciona portabilidad, escalabilidad y aislamiento de aplicaciones, lo que lo convierte en una herramienta popular para la creación y administración de entornos de desarrollo, pruebas y producción.

## Instalación

### Instalación en Windows con WSL (Recomendada) 🐧

Debes descargar el instalador desde la página de Docker for Windows [2].

Cuando ya tienes instalado Docker Desktop dentro de tus programas debes abrirlo y debes asegurarte que la opción “Use the WSL 2 based engine” está habilitada:

<!-- Referencias -->

[1]: <https://collectednotes.com/barckcode/docker-cheat-sheet> "Docker Cheatsheet"
[2]: <https://docs.docker.com/desktop/setup/install/windows-install/> "Docker for Windows"