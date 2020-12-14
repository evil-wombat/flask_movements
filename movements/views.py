from movements import app
from flask import render_template, request, url_for, redirect
import csv
import sqlite3


DBfile = 'movements/data/database.db'

def consulta (query, params=()):
   conn = sqlite3.connect(DBfile)
   c = conn.cursor()

   c.execute (query, params)
   conn.commit()

   filas = c.fetchall()
   print (filas)

   conn.close()

   if len(filas) == 0:
      return filas
   
   columnNames = []
   for columnName in c.description:
      columnNames.append(columnName[0])

   listaDeDiccionarios = []

   for fila in filas:
      d= {}
      for ix, columnName in enumerate(columnNames):
         d[columnName] = fila [ix]
      listaDeDiccionarios.append (d)

   return listaDeDiccionarios


@app.route('/')
def lista_ingresos ():

   ingresos = consulta ('SELECT fecha, concepto, cantidad, id FROM movements;')

   suma = 0
   for ingreso in ingresos:
      print (ingreso)
      suma += float(ingreso['cantidad'])
   
   return render_template ('movement_list.html', datos=ingresos, total = suma)

@app.route('/creaalta', methods= ['GET', 'POST'])
def nuevoIngreso ():
   if request.method == 'POST':

      cantidad = request.form.get('cantidad')
      try:
         cantidad = float(cantidad)
      except ValueError:
         msgError = 'Cantidad debe ser numérica'
         return render_template('alta.html', errores = msgError)

      consulta ('INSERT INTO movements (cantidad, concepto, fecha) VALUES (?, ?, ?);', 
               (
                  float(request.form.get('cantidad')),
                  request.form.get('concepto'),
                  request.form.get('fecha')
               )
            )
      
      return redirect(url_for('lista_ingresos'))
   
   return render_template ('alta.html')

@app.route("/modifica/<id>", methods = ['GET', 'POST'])
def modifica_ingreso(id):

   if request.method == 'GET':

      
      registro = consulta ('SELECT fecha, concepto, cantidad, id FROM movements WHERE id = ?', (id,)) [0]

      return render_template ('modifica.html', registro = registro)

   if request.method == 'POST':

      consulta ('UPDATE movements SET fecha = ?, concepto = ?, cantidad = ? WHERE id= ?', 
               (
                  request.form.get('fecha'),
                  request.form.get('concepto'),
                  float(request.form.get('cantidad')),
                  id
               )
      )
               

      return redirect(url_for('lista_ingresos'))

   


'''  
@app.route('/delete', methods = 'POST')
def eliminar_registro(id):

   conn = sqlite3.connect (DBfile)  
   c = conn.cursor()

   c.execute ('DELETE FROM WHERE id= id', 
                          
   conn.commit()
   conn.close()
   return redirect(url_for('lista_ingresos'))
'''