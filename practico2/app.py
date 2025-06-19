from flask import Flask, render_template, request, redirect, flash
from datetime import datetime, date


app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import  db
from models import Trabajador, RegistroHorario

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/entrada', methods=['GET', 'POST'])
def registrar_entrada():
    if request.method == 'POST':
        legajo = request.form['legajo']
        dni_4 = request.form['dni_4']
        dependencia = request.form['dependencia']

        print("LEG:", legajo)
        print("DNI ingresado:", dni_4)
        print("Dependencia:", dependencia)

        trabajador = Trabajador.query.filter(Trabajador.legajo == legajo.strip()).first()

        if trabajador:
            print("Encontrado: ", trabajador.nombre, trabajador.apellido)
            print("DNI real:", trabajador.dni)
        else:
            print("❌ No se encontró trabajador con ese legajo.")

        if not trabajador or not str(trabajador.dni).endswith(dni_4):
            print("❌ Legajo o DNI incorrecto.")
            flash('Datos incorrectos: legajo o DNI.')
            return redirect('/entrada')

        hoy = date.today()
        ya_registrado = RegistroHorario.query.filter_by(fecha=hoy, idtrabajador=trabajador.id).first()
        if ya_registrado:
            print("⚠ Ya hay entrada para hoy.")
            flash('Ya registraste entrada hoy.')
            return redirect('/entrada')

        nuevo_registro = RegistroHorario(
            fecha=hoy,
            horaentrada=datetime.now().time(),
            dependencia=dependencia,
            idtrabajador=trabajador.id
        )
        db.session.add(nuevo_registro)
        db.session.commit()
        print("✅ Entrada registrada.")
        flash('Entrada registrada correctamente.')
        return redirect('/entrada')

    return render_template('entrada.html')

@app.route('/salida', methods=['GET', 'POST'])
def registrar_salida():
    if request.method == 'POST':
        legajo = request.form['legajo']
        dni_4 = request.form['dni_4']

        trabajador = Trabajador.query.filter_by(legajo=legajo).first()
        if not trabajador or not trabajador.dni.endswith(dni_4):
            flash('Datos incorrectos: legajo o DNI.')
            return redirect('/salida')

        hoy = date.today()
        registro = RegistroHorario.query.filter_by(
            fecha=hoy, idtrabajador=trabajador.id
        ).filter(RegistroHorario.horasalida == None).first()

        if not registro:
            flash('No hay entrada registrada o ya registraste salida hoy.')
            return redirect('/salida')

        registro.horasalida = datetime.now().time()
        db.session.commit()
        flash(f'Salida registrada correctamente para dependencia {registro.dependencia}.')
        return redirect('/salida')

    return render_template('salida.html')


@app.route('/consulta', methods=['GET', 'POST'])
def consultar_registros():
    if request.method == 'POST':
        legajo = request.form['legajo']
        dni_4 = request.form['dni_4']
        fecha_inicio = request.form['fecha_inicio']
        fecha_fin = request.form['fecha_fin']

        trabajador = Trabajador.query.filter_by(legajo=legajo).first()
        if not trabajador or not trabajador.dni.endswith(dni_4):
            flash('Datos incorrectos: legajo o DNI.')
            return redirect('/consulta')

        registros = RegistroHorario.query.filter(
            RegistroHorario.idtrabajador == trabajador.id,
            RegistroHorario.fecha >= fecha_inicio,
            RegistroHorario.fecha <= fecha_fin
        ).order_by(RegistroHorario.fecha).all()

        return render_template('consulta.html', registros=registros)

    return render_template('consulta.html', registros=None)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug = True)