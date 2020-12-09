from movements import app
from flask import render_template, request, url_for, redirect
import csv

@app.route('/')
def lista_ingresos ():
   fIngresos = open ('movements/data/database.csv', 'r')
   csvReader= csv.reader(fIngresos, delimiter=',', quotechar= '"')
   ingresos = list (csvReader)
   suma = 0
   for ingreso in ingresos:
      suma += float(ingreso[2])
   
   print (ingresos)

   return render_template ('movement_list.html', datos=ingresos, total = suma)

@app.route('/creaalta', methods= ['GET', 'POST'])
def nuevoIngreso ():
   if request.method == 'POST':
      fIngresos = open ('movements/data/database.csv', 'a', newline='')
      csWriter = csv.writer(fIngresos, delimiter=',', quotechar='"')
      csWriter.writerow([request.form.get('fecha'), request.form.get('concepto'), request.form.get('cantidad')])
      return redirect(url_for('lista_ingresos'))

   
   return render_template ('alta.html')