###################################
#  FUNCIONES de la base de datos  #
###################################
import sqlite3 as sql

cnn = sql.connect(r"src\scripts\history.db")
cursor = cnn.cursor()

#Crear tabla
#cursor.execute("CREATE TABLE Historial (date text, number real, unit text, unit_result text, result real)")

#Guardar los cambios 
#cnn.commit()
#cnn.close()

#########################
#  FUNCIONES DE MANEJO  #
#########################
def add_op(date, num, unit, unit_result, result):
    with cnn:
        info = (date, num, unit, unit_result, result)
        cursor.execute("INSERT INTO Historial VALUES (?,?,?,?,?)", info)
        cnn.commit()

def search_op(column, value):
    with cnn:
        if type(value) == int:
            cursor.execute(f"SELECT * from Historial WHERE {column}={value}")

        else:
            cursor.execute(f"SELECT * from Historial WHERE {column} like '%{value}%'")
        
        return cursor.fetchall()


def get_all():
    with cnn:
        cursor.execute("SELECT * FROM HISTORIAL")
        
        return cursor.fetchall()

if __name__ == "__main__":
    lista = get_all()
    print(lista)