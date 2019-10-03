# my-project
Proyecto de la facultad

Probado desde Linux Ubuntu 18.04 corriendo sobre Windows 10 (Windows Subsystem for Linux)

Para correr el ambiente debe estar instalado: 
- Python 2.7
- virtualenv
- virtualenvwrapper
- Tener actualizado pip -> pip install --upgrade pip
- MySQL -> una db creada my_project

$ source /usr/local/bin/virtualenvwrapper.sh
 
$ mkvirtualenv venv
 
$ pip install -r requirements.txt
 
$ pip install pymysql
 
$ export FLASK_ENV=development
 
$ export FLASK_CONFIG=development
 
$ export FLASK_APP=run.py
 
