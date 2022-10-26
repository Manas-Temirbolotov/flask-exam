from flask import render_template, request, redirect, url_for, flash

from . import app, db
from .models import Employee, Position
from .forms import EmployeeForm, PositionForm


def index():

    employee = Employee.query.all()
    return render_template('index.html', employee=employee)


def position_create():
    title = 'Новая позиция'
    form = PositionForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            position = Position()
            form.populate_obj(position)
            db.session.add(position)
            db.session.commit()
            flash(f'Позиция успешно добавлена {position.name}', 'success')
            return redirect(url_for('position'))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f'Ошибка в  поле {field} текст ошибки{error}', 'danger')
    return render_template('position_form.html', form=form, title=title)


def position_delete(position_id):
    position = Position.query.filter_by(id=position_id).first()
    if request.method == 'GET':
        return render_template('position_delete.html', position=position)
    if request.method == 'POST':
        db.session.delete(position)
        db.session.commit()
        return redirect(url_for('position_delete'))


def position_update(position_id):
    position = Position.query.filter_by(id=position_id).first()
    form = PositionForm(request.form, obj=position)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(position)
            db.session.commit()
            flash(f'Данные о позиции под номером {position.id} успешно обнавлен')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f'Ошибка в  поле {field} текст ошибки{error}', 'danger')
        # return redirect(url_for('position_update', position_id=position.id))
    return render_template('position_form.html', form=form, position=position)


def employee_create():
    title = 'Добавление сотрудника'
    form = EmployeeForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            employee = Employee()
            form.populate_obj(employee)
            db.session.add(employee)
            db.session.commit()
            flash(f'Сотрудник под номером {employee.id}успешно добавлен', 'success')
            return redirect(url_for('new_employee'))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f'Ошибка в  поле {field} текст ошибки{error}', 'danger')
    return render_template('employee_form.html', form=form, title=title)


def employee_detail(employee_id):
    employee = Employee.query.filter_by(id=employee_id).first()
    return render_template('employee_detail.html', employee=employee)


def employee_delete(employee_id):
    employee = Employee.query.filter_by(id=employee_id).first()
    if request.method == 'GET':
        return render_template('employee_delete.html', employee=employee)
    if request.method == 'POST':
        db.session.delete(employee)
        db.session.commit()
        return redirect(url_for('employee_delete'))


def employee_update(employee_id):
    employee = Employee.query.filter_by(id=employee_id).first()
    form = EmployeeForm(request.form, obj=employee)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(employee)
            db.session.commit()
            flash(f'Сотрудник под номером {employee_id} успешно обнавлен')
        return redirect(url_for('employee_update', employee_id=employee.id))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'Ошибка в  поле {field} текст ошибки {error}', 'danger')
    return render_template('employee_form.html', form=form, employee=employee)
