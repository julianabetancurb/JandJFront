from flask import Flask, render_template
import pyodbc

app = Flask(__name__)

# Cambia estos datos por los de tu servidor SQL Server
conn_str = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=JULIANA\\SQLEXPRESS;"
    "Database=JandJ;"
    "Trusted_Connection=yes;"
)

def get_usuarios():
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("SELECT id_usuario, nombres, apellidos, email FROM dbo.Usuario")
        usuarios = cursor.fetchall()
        conn.close()
        return usuarios
    except Exception as e:
        print("Error al conectar o consultar:", e)
        return []

@app.route('/')
def index():
    usuarios = get_usuarios()
    print(usuarios) 
    return render_template('index.html', usuarios=usuarios)

if __name__ == '__main__':
    app.run(debug=True)
