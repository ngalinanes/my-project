# my-project
Proyecto de la facultad
 
Para correr el ambiente debe estar instalado: 
- Python 2.7
- virtualenv
- virtualenvwrapper
- Tener actualizado pip -> pip install --upgrade pip

$ source /usr/local/bin/virtualenvwrapper.sh
 
$ mkvirtualenv venv
 
$ pip install -r requirements.txt
 
$ pip install pymysql
 
$ export FLASK_ENV=development
 
$ export FLASK_CONFIG=development
 
$ export FLASK_APP=run.py
 
