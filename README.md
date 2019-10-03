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
 
------------------------------------------------------------------

La configuracion de la base de datos que use fue:
- Cree un usuario en MySQL y le di acceso a todo
$ mysql -u root

mysql> CREATE USER 'admin'@'localhost' IDENTIFIED BY 'password';

mysql> CREATE DATABASE my_project;

mysql> GRANT ALL PRIVILEGES ON my_project . * TO 'admin'@'localhost';

- Cree una carpeta instance en la raiz del repo, y dentro un archivo config.py:
# instance/config.py

SECRET_KEY = 'p9Bv<3Eid9%$i01'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:password@localhost/my_project'

