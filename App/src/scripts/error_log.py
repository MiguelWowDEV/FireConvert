from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import * 
import sys

##########################
#      Ventana ERROR     #
##########################
class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        #Mostramos la ventana
        self.show()

        #Mostramos el error
        Error_warning("LogicError", "Ha ocurrido un error de logica", self)

class Error_entry_none(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)

        #Atributos
        self.title = "ERROR: Entrada vacía"
        self.message = "Por favor coloque información en la entrada..."

        self.warning(
        parent,
        self.title,
        self.message
        )

class Error_invalid_information(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)

        #Atributos
        self.title = "ERROR: Información invalida"
        self.message = "Por favor coloque una información que el programa pueda interpretar"

        self.warning(
        parent,
        self.title,
        self.message
        )

class Error_warning(QMessageBox):
    def __init__(self, title_error, msg_error, parent=None):
        super().__init__(parent)

        #Atributos
        self.title = f"ERROR: {title_error}"
        self.message = f"{msg_error}"

        self.warning(
        parent,
        self.title,
        self.message
        )


class Error_format_incorrect(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)

        #Atributos
        self.title = f"ERROR: Formato o informaciónd el archivo invalida"
        self.message = "Por favor, la información colocada no se puede interpretar bien..."

        self.warning(
        parent,
        self.title,
        self.message
        )

class Error_load_none(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)

        #Atributos
        self.title = f"ERROR: Información no cargada"
        self.message = "Por favor, cargue la información necesaria para esta acción..."

        self.warning(
        parent,
        self.title,
        self.message
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ventana()
    sys.exit(app.exec_())