from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
from PyQt5.QtTest import QTest
import pytemperature as pt
import datetime as dt
import pyqtgraph
from pyqtgraph.graphicsItems.ViewBox.axisCtrlTemplate_pyqt5 import *
from pyqtgraph.graphicsItems.PlotItem.plotConfigTemplate_pyqt5 import *
from pyqtgraph.imageview.ImageViewTemplate_pyqt5 import *
from pyqtgraph.console.template_pyqt5 import *
import json 
import sys
import sqlite3
from src.scripts.general import if_desc
import src.scripts.recursos
from src.scripts.error_log import Error_format_incorrect, Error_load_none
from src.scripts.windows import *
from src.scripts.general import load_style, if_desc
from src.scripts.database import add_op, get_all

###################################
#         Clase Principal         #
###################################
class AppConvert(QMainWindow):
    def __init__(self):
        #Inicializamos la calse
        super().__init__()

        #Diseño de app
        loadUi("src/ui/main_window.ui", self)

        #RUTAS
        self.styles = r"src/styles/"

        #Información de conversiones
        self.dict_convert = {
        "Celsius-Kelvin": lambda t: pt.c2k(t),
        "Celsius-Farenheit": lambda t: pt.c2f(t),
        "Kelvin-Celsius": lambda t: pt.k2c(t),
        "Kelvin-Farenheit": lambda t: pt.k2f(t),
        "Farenheit-Kelvin": lambda t: pt.f2k(t),
        "Farenheit-Celsius": lambda t: pt.f2c(t)
        }

        #Mostramos ventana
        self.show()

        #Menu principal
        self.btn_convert.clicked.connect(lambda: self.pages.setCurrentIndex(0))
        self.btn_graph.clicked.connect(lambda: self.pages.setCurrentIndex(1))
        self.support.clicked.connect(lambda: self.pages.setCurrentIndex(2))

    ###################################
    #           Pagina N°2            #
    ###################################

        ###########################################################################
        #  Caracteristicas Pagina N°1
        ###########################################################################

        ##Removemos la opción Kelvin por defecto
        self.combox_temp_2.removeItem(0)
        self.cache = "Kelvin"

        ##Botones
        self.calculate.clicked.connect(self.convert_temperature)
        ##Señales
        self.combox_temp_1.currentTextChanged.connect(self.remove_option)
        ##Otras opciones
        self.btn_load_text.clicked.connect(self.load_file)
        self.btn_history.clicked.connect(self.show_history)

        ###########################################################################
        #  Caracteristicas Pagina N°1
        ###########################################################################

        ##Botones
        self.load_graph.clicked.connect(self.load_graphic)
        self.action_graph.clicked.connect(self.temp_graphic)

        #Variables de la información guardada
        self.time_graph = None
        self.temp_graph = None

    def temp_graphic(self):
        #Verificamos si las variables contienen la información
        if self.time_graph is None and self.temp_graph is None:
            Error_load_none(self)
            return

        #Verificamos el tipo de curva
        option_graph = self.select_graph.currentText()

        if option_graph == "Calentamiento":
            v_temp = if_desc(self.temp_graph)

            if not v_temp:
                self.temp_graph = self.temp_graph[::-1]

            self.graphicsView.plot(self.time_graph, self.temp_graph)

        elif option_graph == "Enfriamiento":
            v_temp = if_desc(self.temp_graph)

            if v_temp == True:
                self.temp_graph = self.temp_graph[::-1]

            self.graphicsView.plot(self.time_graph, self.temp_graph)

    def load_graphic(self):
        #Abrimos ventana QFileDialog
        file, _ = QFileDialog.getOpenFileName(
            self, "Abrir archivo de grafica", 
            "C:/Users/MIGUEL NIEVES/Documents", 
            "Archivos Json (*.json)")

        #Cargamos el archivo json
        try:
            with open(file, "r") as archivo:
                json_file = json.load(archivo)

                #Información que colocaremos en la grafica lineal
                self.time_graph = json_file["tiempo"]
                self.temp_graph = json_file["temperatura"]

        except FileNotFoundError:
            return

        #Crear Label para el mensaje
        self.label_5.setText("Cargado con exito!")
        self.label_5.setStyleSheet("QLabel {color: rgb(91, 255, 88); font-size: 11pt; }")
        
        #Cambiamos la información una vez pasado 2 segundos
        QTest.qWait(1500)
        self.label_5.setText("Cargar datos")
        self.label_5.setStyleSheet("QLabel {color: white; font-size: 14pt; }")



    ###################################
    #           Pagina N°1            #
    ###################################

    ############################################
    #           Ventanas Emergentes            #
    ############################################
    def load_file(self):
        window = Window_load_file(self)
        window.exec_()

    def show_history(self):
        window = Window_history(self)
        window.exec_()

    ############################################################################################
    def remove_option(self, selection):
        if not self.cache is None:
            self.combox_temp_2.addItem(self.cache)
        
        index = self.combox_temp_2.findText(selection)
        self.combox_temp_2.removeItem(index)
        self.cache = selection
            
    
    def convert_temperature(self):
        #Comprobamos si las entradas estan vacías
        
        if not bool(self.temp_a.text()):
            self.label_result.setStyleSheet("QLabel {color: red; font-size: 25px;}")
            self.label_result.setText("Entrada vacía!")
            return

        #Convertimos la temperatura
        temp_1 = str(self.temp_a.text())

        #Obtenemos info del comboBox
        option_1 = self.combox_temp_1.currentText()
        option_2 = self.combox_temp_2.currentText()

        #Obtenemos el resultado
        result_temp = self.dict_convert[f"{option_1}-{option_2}"](float(temp_1))
        result_temp = round(result_temp, 1)

        #Mostramos el resultado
        self.label_result.setStyleSheet("QLabel {color: white; font-size: 75px;}")
        self.label_result.setText(str(result_temp))

        #Agregamos la operación a la base de datos
        date = dt.datetime.today().strftime('%Y-%m-%d')
        num = float(temp_1)
        unit = option_1
        unit_result = option_2
        result = result_temp

        #Vemos si la operación ya existe en la base de datos
        op_save = (date, num, unit, unit_result, result)
        results_op = get_all()

        if op_save in results_op:
            return

        add_op(date, num, unit, unit_result, result)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(r"src\icons\Comet_icon-icons.com_54192.svg"))
    window = AppConvert()
    sys.exit(app.exec_())