from flask import Flask, render_template
import pyodbc

app = Flask(__name__)
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\ALAIN\Desktop\ayuda\TallerDB.accdb;')

def obtener_datos():
    cursor = conn.cursor()

    query = 'SELECT * FROM Estudiante'

    cursor.execute(query)
    data = cursor.fetchall()
    print(data)
        
    return data


def obtener_datos2():
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\ALAIN\Desktop\ayuda\TallerDB.accdb;')
    cursor = conn.cursor()

    query = 'SELECT * FROM Cursos'

    cursor.execute(query)
    data2 = cursor.fetchall()
    print(data2)
        
    return data2

@app.route('/')
def index():
    data = obtener_datos() 
    data2= obtener_datos2()
    return render_template('index.html', data=data, data2=data2)

if __name__ == '__main__':
    app.run(debug=True)