# app/admin/views.py

from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from base64 import b64encode

from . import admin
from .. import db
from ..models import User, Orden
from .forms import EditOrderForm

def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)

@admin.route('/users')
@login_required
def list_users():
    """
    List all users
    """
    check_admin()

    users = User.query.all()
    return render_template('admin/users.html',
                           users=users, title='Users')

@admin.route('/ordenes_all', methods=['GET', 'POST'])
@login_required
def list_ordenes():
    check_admin()

    ordenes = Orden.query.all()
    users = User.query.all()

    return render_template('home/ordenes/ordenes_all.html',
                           ordenes=ordenes, users=users, title="Ordenes")

@admin.route('/ordenes_all/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_orden(id):
    """
    Editar una orden
    """
    check_admin()

    orden = Orden.query.get_or_404(id)
    form = EditOrderForm(obj=orden)
    if form.validate_on_submit():
        orden.estado = form.estado.data
        db.session.commit()
        flash('Has editado la orden de manera satisfactoria.')

        # redirect to the orden page
        return redirect(url_for('admin.list_ordenes'))

    form.estado.data = orden.estado
    form.nombre.data = orden.afiliado
    image = b64encode(orden.data).decode("utf-8")
    return render_template('home/ordenes/orden.html', action="Edit",
                           form=form, image=image,
                           orden=orden, title="Editar Orden")
