from movements import app
from flask import render_template, request, url_for, redirect
import csv
import sqlite3

@app.route('/')
def lista_ingresos ():
   conn = sqlite3.connect ('movements/data/database.db') #Conectamos nuestro programa con SQLite
   c = conn.cursor()

   c.execute ('SELECT fecha, concepto, cantidad, id FROM movements')
  
   '''
   fIngresos = open ('movements/data/database.csv', 'r')
   csvReader= csv.reader(fIngresos, delimiter=',', quotechar= '"')
   ingresos = list (csvReader)
   '''
   ingresos = c.fetchall()


   suma = 0
   for ingreso in ingresos:
      suma += float(ingreso[2])
   
   conn.close()

   return render_template ('movement_list.html', datos=ingresos, total = suma)

@app.route('/creaalta', methods= ['GET', 'POST'])
def nuevoIngreso ():
   if request.method == 'POST':

      conn = sqlite3.connect ('movements/data/database.db')  
      c = conn.cursor()

      c.execute ('INSERT INTO movements (cantidad, concepto, fecha) VALUES (?, ?, ?);', 
               (
                  float(request.form.get('cantidad')),
                  request.form.get('concepto'),
                  request.form.get('fecha')
               )
            )
      
      conn.commit()
      conn.close()
      return redirect(url_for('lista_ingresos'))
      
      '''
      fIngresos = open ('movements/data/database.csv', 'a', newline='')
      csWriter = csv.writer(fIngresos, delimiter=',', quotechar='"')
      csWriter.writerow([request.form.get('fecha'), request.form.get('concepto'), request.form.get('cantidad')])
      '''
   
   return render_template ('alta.html')

@app.route('/modifica/<id>', methods = ['GET', 'POST'])
def modifica_ingreso(id):
   '''
   1. consulta el movimiento por id
   2. render_template (modifica.html, movimiento = resultado de la consulta anterior)
   '''