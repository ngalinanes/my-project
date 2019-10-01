# app/home/views.py

from flask import render_template, request, redirect, Flask, flash, url_for
from flask_login import login_required
from flask import abort, render_template
from flask_login import current_user, login_required
from . import home
from forms import OrderForm
from ..models import Orden
from .. import db
import os

app = Flask(__name__)

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")


@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")

@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)

    return render_template('home/admin_dashboard.html', title="Dashboard")

#app.config["IMAGE_UPLOADS"] = "/home/ngalinanes/my-project/app/static/img/uploads"

@home.route('/ordenes', methods=["GET", "POST"])
@login_required
def ordenes():
    """
    Render the order template on the /ordenes route
    """
    username = current_user.username
    form = OrderForm()
    if request.method == "POST":
       if request.files:
          file = request.files['image']
          #image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename)) 

          newFile = Orden(name=file.filename, data=file.read(), tipo=form.tipo_tramite.data, observaciones=form.observaciones.data, afiliado=username)
          db.session.add(newFile)
          db.session.commit()

          flash('Su pedido de autorizacion fue cargado con exito')
          return redirect(url_for('home.ordenes'))
    return render_template('home/ordenes/ordenes.html', form=form, title="Ordenes")

@home.route('/mis_ordenes/', methods=['GET', 'POST'])
@login_required
def list_mis_ordenes():

    username = current_user.username
    ordenes = Orden.query.filter_by(afiliado=username).all()

    return render_template('home/ordenes/mis_ordenes.html',
                           ordenes=ordenes, title="Mis Ordenes")
