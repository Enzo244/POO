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
        try:
            legajo = request.form['legajo'].strip()
            dni_4 = request.form['dni_4'].strip()
            dependencia = request.form['dependencia'].strip()

            if not legajo or not dni_4 or not dependencia:
                raise ValueError("Todos los campos son obligatorios.")

            trabajador = Trabajador.query.filter_by(legajo=legajo).first()
            if not trabajador:
                raise LookupError("No se encontró un trabajador con ese legajo.")

            if not trabajador.dni.endswith(dni_4):
                raise ValueError("Los últimos 4 dígitos del DNI no coinciden.")

            hoy = date.today()
            ya_registrado = RegistroHorario.query.filter_by(
                fecha=hoy, idtrabajador=trabajador.id
            ).first()

            if ya_registrado:
                raise RuntimeError("Ya registraste tu entrada hoy.")

            nuevo_registro = RegistroHorario(
                fecha=hoy,
                horaentrada=datetime.now().time(),
                dependencia=dependencia,
                idtrabajador=trabajador.id
            )
            db.session.add(nuevo_registro)
            db.session.commit()
            flash("✅ Entrada registrada correctamente.")

        except ValueError as ve:
            flash(f"⚠ Error de validación: {ve}")
        except LookupError as le:
            flash(f"⚠ Error de búsqueda: {le}")
        except RuntimeError as re:
            flash(f"⚠ Error de registro: {re}")
        except Exception as e:
            flash(f"❌ Error inesperado: {e}")

        return redirect('/entrada')

    return render_template('entrada.html')
@app.route('/salida', methods=['GET', 'POST'])
def registrar_salida():
    if request.method == 'POST':
        try:
            legajo = request.form['legajo'].strip()
            dni_4 = request.form['dni_4'].strip()

            if not legajo or not dni_4:
                raise ValueError("Todos los campos son obligatorios.")

            trabajador = Trabajador.query.filter_by(legajo=legajo).first()
            if not trabajador:
                raise LookupError("No se encontró un trabajador con ese legajo.")

            if not trabajador.dni.endswith(dni_4):
                raise ValueError("Los últimos 4 dígitos del DNI no coinciden.")

            hoy = date.today()
            registro = RegistroHorario.query.filter_by(
                fecha=hoy, idtrabajador=trabajador.id
            ).filter(RegistroHorario.horasalida == None).first()

            if not registro:
                raise RuntimeError("No hay entrada registrada hoy o ya registraste salida.")

            registro.horasalida = datetime.now().time()
            db.session.commit()
            flash(f"✅ Salida registrada correctamente para dependencia {registro.dependencia}.")

        except ValueError as ve:
            flash(f"⚠ Error de validación: {ve}")
        except LookupError as le:
            flash(f"⚠ Error de búsqueda: {le}")
        except RuntimeError as re:
            flash(f"⚠ Error de registro: {re}")
        except Exception as e:
            flash(f"❌ Error inesperado: {e}")

        return redirect('/salida')

    return render_template('salida.html')

@app.route('/consulta', methods=['GET', 'POST'])
def consultar_registros():
    if request.method == 'POST':
        try:
            legajo = request.form['legajo'].strip()
            dni_4 = request.form['dni_4'].strip()
            fecha_inicio = request.form['fecha_inicio'].strip()
            fecha_fin = request.form['fecha_fin'].strip()

            if not legajo or not dni_4 or not fecha_inicio or not fecha_fin:
                raise ValueError("Todos los campos son obligatorios.")

            trabajador = Trabajador.query.filter_by(legajo=legajo).first()
            if not trabajador:
                raise LookupError("No se encontró un trabajador con ese legajo.")

            if not trabajador.dni.endswith(dni_4):
                raise ValueError("Los últimos 4 dígitos del DNI no coinciden.")

            registros = RegistroHorario.query.filter(
                RegistroHorario.idtrabajador == trabajador.id,
                RegistroHorario.fecha >= fecha_inicio,
                RegistroHorario.fecha <= fecha_fin
            ).order_by(RegistroHorario.fecha).all()

            if not registros:
                flash("ℹ No se encontraron registros para el período seleccionado.")
            return render_template('consulta.html', registros=registros)

        except ValueError as ve:
            flash(f"⚠ Error de validación: {ve}")
        except LookupError as le:
            flash(f"⚠ Error de búsqueda: {le}")
        except Exception as e:
            flash(f"❌ Error inesperado: {e}")
        return redirect('/consulta')

    return render_template('consulta.html', registros=None)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug = True)