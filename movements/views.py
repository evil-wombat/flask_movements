from movements import app
from flask import render_template
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

@app.route('/creaalta')
def algo ():
  return 'Aquí ira algo'