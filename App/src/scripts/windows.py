from posixpath import split
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import src.scripts.recursos
from src.scripts.general import inter_temps, save_temps
from src.scripts.database import search_op, get_all
import src.scripts.error_log as err 
import datetime as dt
import re
import sys

###################################
#    Ventanas emergentes          #
###################################
class Window_history(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        #Cargamos el diseño
        loadUi("src/ui/history.ui", self)

        #Diccionario con palabras de busqueda
        self.dict_search = {
            "fecha": "date", 
            "número": "number", 
            "unidad": "unit", 
            "unidad_resultado":"unit_result", 
            "resultado": "result"
            }

        #Botones
        self.btn_search.clicked.connect(self.buscar)

        #Mostrar las operaciones hechas recientemente
        op_recents = get_all()
        date_actual = dt.datetime.today().strftime('%Y-%m-%d')

        for op_r in op_recents:
            if op_r[0] == date_actual:
                date = op_r[0]
                number = op_r[1]
                unit = op_r[2]
                unit_result = op_r[3]
                result = op_r[4]
                self.list_results.addItem(f"{unit}-{unit_result} {number} = {result} ({date})")

        #Verificamos cuantas operaciones hay con la fecha actual
        if self.list_results.count() > 1:
            self.list_results.takeItem(0)


        #Mostrar ventana
        self.show()

    def buscar(self):
        #Entrada Vacia
        if bool(self.busc.text()) == False:
            err.Error_entry_none(self)
            return

        get_entrada = str(self.busc.text())

        #No es el formato de busqueda
        if not re.search("[A-Za-z]:[A-Za-z]", get_entrada):
            err.Error_invalid_information(self)
            return

        #Limpiamos la QListWidget
        self.list_results.clear()
        
        #Realizar busqueda a la base de datos
        base_info = get_entrada.split(":")
        results = search_op(self.dict_search[base_info[0]], base_info[1])

        if results is None:
            self.list_results.addItem("Sin resultados...")
            return
        
        #Agregamos a el QListWidget
        #Eliminamos el mensaje 'Sin resultados...'
        self.list_results.takeItem(0)
        for r in results:
            date = r[0]
            number = r[1]
            unit = r[2]
            unit_result = r[3]
            result = r[4]
            self.list_results.addItem(f"{unit}-{unit_result} {number} = {result} ({date})")

class Window_load_file(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        #Atributos
        self.vis = True

        #Cargamos el diseño
        loadUi("src/ui/file_temps.ui", self)

        #Cargar temperaturas resueltas
        self.file, _ = QFileDialog.getOpenFileName(
        parent,
        "Abrir archivo de temperaturas",
        "C:/Users/MIGUEL NIEVES/Documents",
        "Archivos de texto (*.txt)"
        )

        self.results = inter_temps(self.file)

        try:
            for r in self.results:
                self.view_temp.addItem(f"{r[0]} {r[1]} = {r[2]}")

        except TypeError:
            self.vis = False

        #########################################-Mostramos la ventana-################
        if not self.vis:
            self.close()
            return

        else:
            self.show()

        #Botones
        self.btn_save.clicked.connect(self.save_update)

    def save_update(self):
        #Guardar el archivo
        save_temps(self.file, self.results)

        #Mostramos mensaje de guardado exitoso
        label_nice = QLabel(self)
        label_nice.setText("Guardado con exito!")
        label_nice.setStyleSheet("QLabel {color: #4eff5a; font-size: 18px;}")
        label_nice.setAlignment(Qt.AlignCenter)

        #Añadimos al frame
        layout = self.frame_result.layout()
        layout.addWidget(label_nice)

        #Cerramos la ventana
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window_history()
    sys.exit(app.exec_())