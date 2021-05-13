from main import Main
from PySide2 import QtCore, QtGui, QtWidgets, QtXml
from PySide2.QtCore import QSize, QEvent, Qt, QPropertyAnimation
from PySide2.QtGui import QFont, QColor, QIcon, Qt, QCursor
from PySide2.QtWidgets import QSizePolicy, QPushButton, QGraphicsDropShadowEffect, QMessageBox, QSizeGrip
from ui_styles import Style

class UIFunctions(Main):

	def porcentaje(self):
		self.ui.txtPorcentaje.clear()
		x = UIFunctions.sillas_ocupadas(self)
		self.ui.txtPorcentaje.setNum(len(x)*2)

	def sillas_ocupadas(self):
		a = []
		b = []

		for i in range(50):
			exec("a.append(self.ui.S{}.isChecked())".format(i + 1))

		for j in range(len(a)):
			if a[j] is True:
				b.append(j + 1)
		
		return b

	def agregar_pasajero(self):
		self.db.agregar_pasajero(self.ui.txtCedula.text(), self.ui.txtNombre.text())
		UIFunctions.mostrar_pasajeros(self)

	def mostrar_pasajeros(self):
		self.ui.comboPasajeros.clear()

		for row in self.db.mostrar_pasajeros():
			self.ui.comboPasajeros.addItem(str(row[0]) + " - " + row[1])

		self.ui.comboPasajeros.setCurrentIndex(-1)

	def agregar_asignacion(self):
		x = self.ui.comboPasajeros.currentText()
		index = 0

		for i in range(len(x)):
			if x[i] == "-":
				index = i
				
		if (self.ui.radioEjecutiva.isChecked() or self.ui.radioEconomica.isChecked())is True and (self.ui.radioVentana.isChecked() is True or self.ui.radioCentro.isChecked() is True or self.ui.radioPasillo.isChecked() is True):
			if self.ui.radioEjecutiva.isChecked() is True and self.ui.radioVentana.isChecked() is True:
				ejecutivas = [i for i in UIFunctions.sillas_ocupadas(self) if i <= 8]
				pasillos = [2, 3, 6, 7]

				if set([1, 4, 5, 8]).issubset(set(ejecutivas)):
					print("LAS SILLAS DE LAS VENTANAS ESTÁN OCUPADAS.")
				else:
					if self.db.buscar_pasajero(self.ui.comboPasajeros.currentText()[:index-1]) == []:
						for j in range(8):
							if j + 1 not in pasillos and j + 1 not in ejecutivas:
								exec("self.ui.S{}.setChecked(True)".format(j + 1))
								exec("self.ui.S{}.setStyleSheet(Style.btnSelect.replace('COLOR', 'rgb(148, 182, 89)'))".format(j + 1))
								self.db.agregar_asignacion(j + 1, self.ui.comboPasajeros.currentText()[:index-1], 1)
								UIFunctions.mostrar_asignaciones(self)
								UIFunctions.porcentaje(self)
								break
					else:
						print("EL PASAJERO YA ESTÁ REGISTRADO EN ESTE VUELO.")
							

			elif self.ui.radioEjecutiva.isChecked() is True and self.ui.radioCentro.isChecked() is True:
				print("NO ES VÁLIDO.")
			elif self.ui.radioEjecutiva.isChecked() is True and self.ui.radioPasillo.isChecked() is True:
				ejecutivas = [i for i in UIFunctions.sillas_ocupadas(self) if i <= 8]
				ventanas = [1, 4, 5, 8]

				if set([2, 3, 6, 7]).issubset(set(ejecutivas)):
					print("LAS SILLAS DE LOS PASILLOS ESTÁN OCUPADAS.")
				else:
					if self.db.buscar_pasajero(self.ui.comboPasajeros.currentText()[:index-1]) == []:
						for j in range(8):
							if j + 1 not in ventanas and j + 1 not in ejecutivas:
								exec("self.ui.S{}.setChecked(True)".format(j + 1))
								exec("self.ui.S{}.setStyleSheet(Style.btnSelect.replace('COLOR', 'rgb(148, 182, 89)'))".format(j + 1))
								self.db.agregar_asignacion(j + 1, self.ui.comboPasajeros.currentText()[:index-1], 1)
								UIFunctions.mostrar_asignaciones(self)
								UIFunctions.porcentaje(self)
								break
					else:
						print("EL PASAJERO YA ESTÁ REGISTRADO EN ESTE VUELO.")


			elif self.ui.radioEconomica.isChecked() is True and self.ui.radioVentana.isChecked() is True:
				economicas = [i for i in UIFunctions.sillas_ocupadas(self) if 8 < i <= 50]
				pasillos_centro = [10, 11, 12, 13, 16, 17, 18, 19, 22, 23, 24, 25, 28, 29, 30, 31, 34, 35, 36, 37, 40, 41, 42, 43, 46, 47, 48, 49]

				if set([9, 14, 15, 20, 21, 26, 27, 32, 33, 38, 39, 44, 45, 50]).issubset(set(economicas)):
					print("LAS SILLAS DE LAS VENTANAS ESTÁN OCUPADAS.")
				else:
					if self.db.buscar_pasajero(self.ui.comboPasajeros.currentText()[:index-1]) == []:
						for j in range(8, 50):
							if j + 1 not in pasillos_centro and j + 1 not in economicas:
								exec("self.ui.S{}.setChecked(True)".format(j + 1))
								exec("self.ui.S{}.setStyleSheet(Style.btnSelect.replace('COLOR', 'rgb(148, 182, 89)'))".format(j + 1))
								self.db.agregar_asignacion(j + 1, self.ui.comboPasajeros.currentText()[:index-1], 2)
								UIFunctions.mostrar_asignaciones(self)
								UIFunctions.porcentaje(self)
								break
							else:
								print("EL PASAJERO YA ESTÁ REGISTRADO EN ESTE VUELO.")
					else:
						print("EL PASAJERO YA ESTÁ REGISTRADO EN ESTE VUELO.")

			elif self.ui.radioEconomica.isChecked() is True and self.ui.radioCentro.isChecked() is True:
				economicas = [i for i in UIFunctions.sillas_ocupadas(self) if 8 < i <= 50]
				pasillos_ventanas = [9, 11, 12, 14, 15, 17, 18, 20, 21, 23, 24, 26, 27, 29, 30, 32, 33, 35, 36, 38, 39, 41, 42, 44, 45, 47, 48, 50]

				if set([10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49]).issubset(set(economicas)):
					print("LAS SILLAS DEL CENTRO ESTÁN OCUPADAS.")
				else:
					if self.db.buscar_pasajero(self.ui.comboPasajeros.currentText()[:index-1]) == []:
						for j in range(8, 50):
							if j + 1 not in pasillos_ventanas and j + 1 not in economicas:
								exec("self.ui.S{}.setChecked(True)".format(j + 1))
								exec("self.ui.S{}.setStyleSheet(Style.btnSelect.replace('COLOR', 'rgb(148, 182, 89)'))".format(j + 1))
								self.db.agregar_asignacion(j + 1, self.ui.comboPasajeros.currentText()[:index-1], 2)
								UIFunctions.mostrar_asignaciones(self)
								UIFunctions.porcentaje(self)
								break
					else:
						print("EL PASAJERO YA ESTÁ REGISTRADO EN ESTE VUELO.")
							

			elif self.ui.radioEconomica.isChecked() is True and self.ui.radioPasillo.isChecked() is True:
				economicas = [i for i in UIFunctions.sillas_ocupadas(self) if 8 < i <= 50]
				centro_ventanas = [9, 10, 13, 14, 15, 16, 19, 20, 21, 22, 25, 26, 27, 28, 31, 32, 33, 34, 37, 38, 39, 40, 43, 44, 45, 46, 49, 50]

				if set([11, 12, 17, 18, 23, 24, 29, 30, 35, 36, 41, 42, 47, 48]).issubset(set(economicas)):
					print("LAS SILLAS DE LOS PASILLOS ESTÁN OCUPADAS.")
				else:
					if self.db.buscar_pasajero(self.ui.comboPasajeros.currentText()[:index-1]) == []:
						for j in range(8, 50):
							if j + 1 not in centro_ventanas and j + 1 not in economicas:
								exec("self.ui.S{}.setChecked(True)".format(j + 1))
								exec("self.ui.S{}.setStyleSheet(Style.btnSelect.replace('COLOR', 'rgb(148, 182, 89)'))".format(j + 1))
								self.db.agregar_asignacion(j + 1, self.ui.comboPasajeros.currentText()[:index-1], 2)
								UIFunctions.mostrar_asignaciones(self)
								UIFunctions.porcentaje(self)
								break
					else:
						print("EL PASAJERO YA ESTÁ REGISTRADO EN ESTE VUELO.")
							

	def mostrar_asignaciones(self):
		self.ui.listaPasajeros.clear()

		for row in self.db.mostrar_asignaciones():
			self.ui.listaPasajeros.addItem("Cédula: " + str(row[0]) + "\nNombre: " + row[1] + "\nClase: " + str(row[2]) + "\nSilla " + str(row[3]))
	
	def maximize_restore(self):
		if self.GLOBAL_STATE == 0:
			self.GLOBAL_STATE = 1
			self.showMaximized()
			self.ui.btnMaximize.setToolTip("Restore")
			self.ui.btnMaximize.setStyleSheet(Style.btnStandard.replace('ICON', 'url(:/icons/light/restore1_2.png)'))
			self.ui.verticalLayout_6.setContentsMargins(40, 0, 0, 0)
			self.ui.frameSizeGrip.hide()
		elif self.GLOBAL_STATE == 1:
			self.GLOBAL_STATE = 0
			self.showNormal()
			self.ui.btnMaximize.setToolTip("Maximize")
			self.ui.btnMaximize.setStyleSheet(Style.btnStandard.replace('ICON', 'url(:/icons/light/maximize1_3.png)'))
			self.ui.verticalLayout_6.setContentsMargins(10, 0, 0, 0)
			self.ui.frameSizeGrip.show()
		else:
			self.GLOBAL_STATE = 1
			self.showNormal()
			self.move(self.dragPos.x()/2, 0)
			UIFunctions.maximize_restore(self)

			

	def uiDefinitions(self):
		def dobleClickMaximizeRestore(event):
			if event.type() == QEvent.MouseButtonDblClick:
				QtCore.QTimer.singleShot(100, lambda: UIFunctions.maximize_restore(self))

		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_TranslucentBackground)
		self.ui.frameTitle.mouseDoubleClickEvent = dobleClickMaximizeRestore
		self.shadow = QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(15)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QColor(255, 0, 0, 127))
		self.setGraphicsEffect(self.shadow)
		self.sizegrip = QSizeGrip(self.ui.frameSizeGrip)
		self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin: 0px; padding: 0px;")

	def checkButtons(self):
		for i in range(50):
			exec('self.ui.S{}.setCheckable(True)'.format(i+1))

	def mostrar_asignaciones(self):
		self.ui.listaPasajeros.clear()

		for row in self.db.mostrar_asignaciones():
			exec("self.ui.S{}.setChecked(True)".format(row[2]))
			exec("self.ui.S{}.setStyleSheet(Style.btnSelect.replace('COLOR', 'rgb(148, 182, 89)'))".format(row[2]))
			self.ui.listaPasajeros.addItem(row[0] + " - " + row[1] + "\nSILLA: " + str(row[2]))
