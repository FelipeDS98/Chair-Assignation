import sys
from PySide2 import QtCore, QtGui, QtWidgets, QtXml
from PySide2.QtCore import Qt
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from database import Database
from app_modules import *

class Main(QtWidgets.QMainWindow, Database):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnMinimize.clicked.connect(lambda: UIFunctions.showMinimized(self))
        self.ui.btnMaximize.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        self.ui.btnClose.clicked.connect(lambda: UIFunctions.close(self))
        self.ui.btnRegistrarP.clicked.connect(lambda: UIFunctions.agregar_pasajero(self))
        self.ui.btnRegistrarA.clicked.connect(lambda: UIFunctions.agregar_asignacion(self))
        self.setWindowTitle('CHAIR ASSIGNATION')
        self.GLOBAL_STATE = 0
        self.db = Database()
        self.db.conn()
        UIFunctions.mostrar_pasajeros(self)
        UIFunctions.uiDefinitions(self)
        UIFunctions.checkButtons(self)
        UIFunctions.mostrar_asignaciones(self) 
        UIFunctions.porcentaje(self)       

        def moveWindow(event):
            if self.GLOBAL_STATE == 1:
                self.GLOBAL_STATE = 2
                UIFunctions.maximize_restore(self)

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
                
        self.ui.frameTitle.mouseMoveEvent = moveWindow
        self.show()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())

