# Python con Git y Github

Creamos un proyecto, y lo unimos a un repositorio remoto para darle seguimiento a lo largo del curso. (Esto se ha hecho previamente)

## Repositorio remoto y enlazado

Desde nuestro perfil de Github, se busca la opción `New repository`, esto nos llevara a una panatalla donde se nos mostrarán distintas opciones para crear el repositorio. Nos limitamos a solo asignarle un nombre, hacelo publico, y crearlo.

Localmente, dentro del directorio que contendrá el repositorio, se inicializa con el comando `git init`.

> 📝 **Nota:** Se crea la carpeta `.git` en donde se hace *tracking* del repositorio

Para enlazar repositorios se usa el comando `git remote add origin <url-repositorio>`, se puede verificar el enlace con `git remote -v`

Luego hace el proceso basico para subir cambios:

```sh
git add *
git commit -m "Primeros cambios"
git push origin master
```
