from movements import app
from flask import render_template

@app.route('/')
def lista_movimientos ():
   return render_template ('movement_list.html', miTexto='Ya veremos si hay movimientos')
