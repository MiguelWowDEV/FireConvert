#######################
#  FUNCIONES GENERAL  #
#######################
from PyQt5.QtWidgets import QMessageBox as qmb
import pytemperature as pt

##########################
# Cargar Estilo CSS
##########################
def load_style(ruta, object):
    with open(ruta, "r") as file:
        content = file.read()
        print(content)
        object.setStyleSheet(content)


#################################
# Comprobar lista descendente
#################################
def if_desc(list):
    value_i = list[0]
    for i in range(1, len(list)):
        if list[i] > value_i:
            value_i = list[i]
            print(value_i)

        else:
            return False

    return True

#########################################
# Interpretar temperaturas archivo .txt
#########################################
def save_temps(ruta, results):
    try:
        with open(ruta, "w") as file:
            for r in results:
                file.write(f"{r[0]} {r[1]} = {r[2]}\n")

    except Exception as error:
        qmb.warning(f"Un Error inesperado ocurrio: {error}")

def inter_temps(ruta):

    try:
        with open(ruta, "r") as file:
            lines_temps = file.readlines()

            #Limpiamos los datos
            lines_temps = list(map(lambda text: text.strip(), lines_temps))

            #Las convertimos en una función para invocar
            results = list()
            for temp in lines_temps:
                info = temp.split(" ")
                result = pt.__dict__[info[1].replace("-", "2")](int(info[0]))
                
                #Colocamos en la lista
                results.append((info[0], info[1], round(float(result), 2)))

            return results

    except:
        return

if __name__ == "__main__":
    pass