from flask import Flask, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*", "methods": "GET,POST,PUT,DELETE"}})

@app.route('/datos')
def datos():

  tabla = request.args.get('tabla')
  # print(f"Tabla recibida: {tabla}")

  db = mysql.connector.connect(host="localhost", user="root", passwd="1234", db="practicum")
  cursor = db.cursor()

  if tabla == 'awayteams':
    cursor.execute("SELECT * FROM awayteams")
  elif tabla == 'goals':
    cursor.execute("SELECT * FROM goals")
  elif tabla == 'hometeams':
    cursor.execute("SELECT * FROM hometeams")
  elif tabla == 'matches':
    cursor.execute("SELECT * FROM matches")
  elif tabla == 'players':
    cursor.execute("SELECT * FROM players")
  elif tabla == 'squads':
    cursor.execute("SELECT * FROM squads")
  elif tabla == 'stadiums':
    cursor.execute("SELECT * FROM stadiums")
  elif tabla == 'tournaments':
    cursor.execute("SELECT * FROM tournaments")

  resultados = cursor.fetchall()

  # print(f"Total resultados: {len(resultados)}")
  # print(resultados)

  html = ""

  columnas = [column[0] for column in cursor.description]

  html += "<table><tr>"

  for columna in columnas:
    html += f"<th>{columna}</th>"

  html += "</tr>"

  for fila in resultados:
    html += "<tr>"
    for col in fila:
      html += f"<td>{col}</td>"
    html += "</tr>"

  html += "</table>"

  return html

if __name__ == '__main__':
  app.run()