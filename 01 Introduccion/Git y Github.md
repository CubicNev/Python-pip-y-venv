# Python con Git y Github

Creamos un proyecto, y lo unimos a un repositorio remoto para darle seguimiento a lo largo del curso. (Esto se ha hecho previamente)

## Repositorio remoto y enlazado

Desde nuestro perfil de Github, se busca la opción `New repository`, esto nos llevara a una panatalla donde se nos mostrarán distintas opciones para crear el repositorio. Nos limitamos a solo asignarle un nombre, hacelo publico, y crearlo.

Localmente, dentro del directorio que contendrá el repositorio, se inicializa con el comando `git init`.

> 📝 **Nota:** Se crea la carpeta `.git` en donde se hace *tracking* del repositorio

Para enlazar repositorios se usa el comando `git remote add origin <url-repositorio>`, se puede verificar el enlace con `git remote -v`

Luego hace el proceso basico para subir cambios:

```sh
# alternativa 1
git add *
# alternativa 2 (recomendada):
git add .

git commit -m "Primeros cambios"
git push origin master
```

## Archivo `README.md`

Este archivo es un archivo en **markdown** (god chavito 🛐), en el que se ponen las instrucciones para las personas que quieran empezar a trabajar con el proyecto.

## Archivo `.gitignore` para python

Un repositorio no esta completo sin un archivo `.gitignore` que indique que archivos no tomar en cuenta para el control de versiones. Se usa la pagína `gitignore.io`, esta es un herramitna para generar un gitignore que se adecue a nuestro proyecto.

> 📝 **Nota:** La pagína se puede encontar en el siguiente enlace: gitignore.io[1]

Normalmente una buena configuración es por sistema operativo (Windows, Linux, Mac, etc), es recomendable escoger todos los que se usan en el entorno de desarrollo. Además se escoge la opción Python para trabajar en este proyecto.

> 📝 **Nota:** Puedes ver el resultado de en el archivo `.gitignore` de este repositorio.

La parte por default generada por Github al momento de crear el repositorio fue la siguiente:

```text
### Python ###
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/#use-with-ide
.pdm.toml

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/
```

[1]: <https://www.toptal.com/developers/gitignore> "Gitignore io"
