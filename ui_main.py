# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(805, 630)
        MainWindow.setMinimumSize(QSize(800, 630))
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background: transparent;\n"
"}")
        self.MainWidget = QWidget(MainWindow)
        self.MainWidget.setObjectName(u"MainWidget")
        self.MainWidget.setStyleSheet(u"background: transparent;")
        self.horizontalLayout = QHBoxLayout(self.MainWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.MainFrame = QFrame(self.MainWidget)
        self.MainFrame.setObjectName(u"MainFrame")
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.MainFrame.setPalette(palette)
        self.MainFrame.setStyleSheet(u"QLineEdit {\n"
"	font: 12pt \"MS Sans Serif\";\n"
"	border-radius: 8px;\n"
"	border: 1px solid rgb(242, 242, 242);\n"
"	padding-left: 10px;\n"
"	background: rgb(85, 255, 127);\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"	border: 1px solid rgb(229, 229, 229);\n"
"}\n"
"\n"
"QLineEdit::focus {\n"
"	border: 1px solid rgb(180, 180, 180);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: 1px solid rgb(242, 242, 242);\n"
"    height: 15px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::hover:horizontal {\n"
"	border: 1px solid rgb(229, 229, 229);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(193, 193, 193);\n"
"    min-width: 25px;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QScrollBar::handle:hover:horizontal {\n"
"    background: rgb(168, 168, 168);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(95, 99, 104);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"  "
                        "  subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(95, 99, 104);\n"
"    width: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::hover:vertical {\n"
"	border: 1px solid rgb(229, 229, 229);\n"
"}\n"
"\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(193, 193, 193);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
"\n"
"QScrollBar::handle:hover:vertical {\n"
"    background: rgb(168, 168, 168);\n"
"}\n"
""
                        "\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"     background: rgb(95, 99, 104);\n"
"     height: 20px;\n"
"	 border-bottom-left-radius: 7px;\n"
"     border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"	 border: none;\n"
"     background: rgb(95, 99, 104);\n"
"     height: 20px;\n"
"	 border-top-left-radius: 7px;\n"
"     border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
"QCheckBox {\n"
"	font: 12pt \"MS Sans Serif\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	background: rgb(250, 250, 232);\n"
"    border: 2px solid rgb(180, 180, 180);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 8px;\n"
"}"
                        "\n"
"\n"
"QCheckBox::indicator:hover {\n"
"	border: 2px solid rgb(95, 99, 104);\n"
"	background-image: url(://icons/dark/check-alt1.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(95, 99, 104);\n"
"	border: 2px solid rgb(95, 99, 104);\n"
"	background-image: url(://icons/dark/check-alt1.png);\n"
"}\n"
"\n"
"\n"
"QRadioButton {\n"
"	font: 12pt \"MS Sans Serif\";\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"	background: rgb(255, 255, 255);\n"
"    border: 2px solid rgb(180, 180, 180);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    border: 2px solid rgb(95, 99, 104);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(148, 182, 89);\n"
"	border: 2px solid rgb(95, 99, 104);	\n"
"}\n"
"\n"
"QComboBox{\n"
"	font: 12pt \"MS Sans Serif\";\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(180, 180, 180);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
""
                        "	border: 1px solid rgb(95, 99, 104);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgb(95, 99, 104);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/dark/arrow-bottom1.png);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
" }\n"
"\n"
"QComboBox QAbstractItemView {	\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(95, 99, 104);\n"
"}\n"
"\n"
"\n"
"QSlider::groove:hover {\n"
"	border: 1px solid rgb(229, 229, 229);\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"	background: rgb(250, 250, 232);\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	border: 1px solid rgb(242, 242, 242);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    border: none;\n"
"	width: 18px;\n"
"    height: 18px;\n"
"    margin"
                        ": 0px;\n"
"	border-radius: 9px;\n"
"	background: rgb(193, 193, 193);\n"
"}\n"
"\n"
"QSlider::handle:hover:horizontal {\n"
"    background: rgb(168, 168, 168);\n"
"}\n"
"\n"
"QSlider::handle:pressed:horizontal {\n"
"    background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"	background: rgb(250, 250, 232);\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border: 1px solid rgb(242, 242, 242);\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: rgb(193, 193, 193);\n"
"	border: none;\n"
"	width: 18px;\n"
"    height: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"\n"
"QSlider::handle:hover:vertical {\n"
"   background: rgb(168, 168, 168);\n"
"}\n"
"\n"
"QSlider::handle:pressed:vertical {\n"
"    background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"	font: 10pt \"MS Sans Serif\";\n"
"	font-weight: bold;\n"
"	height: 40px;\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	border: 2px solid r"
                        "gb(180, 180, 180);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
" 	border: none;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 2px solid rgb(95, 99, 104);\n"
" }\n"
"\n"
"\n"
"QListWidget {\n"
"	font: 12pt \"MS Sans Serif\";\n"
"	text-align: center;\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(180, 180, 180);\n"
"}")
        self.MainFrame.setFrameShape(QFrame.NoFrame)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.MainFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameTop = QFrame(self.MainFrame)
        self.frameTop.setObjectName(u"frameTop")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameTop.sizePolicy().hasHeightForWidth())
        self.frameTop.setSizePolicy(sizePolicy)
        self.frameTop.setMinimumSize(QSize(0, 0))
        self.frameTop.setMaximumSize(QSize(16777215, 45))
        self.frameTop.setStyleSheet(u"background-color: rgb(222, 225, 230);")
        self.frameTop.setFrameShape(QFrame.NoFrame)
        self.frameTop.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frameTop)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frameTitle = QFrame(self.frameTop)
        self.frameTitle.setObjectName(u"frameTitle")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frameTitle.sizePolicy().hasHeightForWidth())
        self.frameTitle.setSizePolicy(sizePolicy1)
        self.frameTitle.setFrameShape(QFrame.NoFrame)
        self.frameTitle.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frameTitle)

        self.frameButtons = QFrame(self.frameTop)
        self.frameButtons.setObjectName(u"frameButtons")
        sizePolicy1.setHeightForWidth(self.frameButtons.sizePolicy().hasHeightForWidth())
        self.frameButtons.setSizePolicy(sizePolicy1)
        self.frameButtons.setMaximumSize(QSize(120, 16777215))
        self.frameButtons.setFrameShape(QFrame.NoFrame)
        self.frameButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frameButtons)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnMinimize = QPushButton(self.frameButtons)
        self.btnMinimize.setObjectName(u"btnMinimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnMinimize.sizePolicy().hasHeightForWidth())
        self.btnMinimize.setSizePolicy(sizePolicy2)
        self.btnMinimize.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/icons/light/minimize1.png);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(199, 202, 207);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(178, 180, 184);\n"
"}")
        self.btnMinimize.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.btnMinimize)

        self.btnMaximize = QPushButton(self.frameButtons)
        self.btnMaximize.setObjectName(u"btnMaximize")
        sizePolicy2.setHeightForWidth(self.btnMaximize.sizePolicy().hasHeightForWidth())
        self.btnMaximize.setSizePolicy(sizePolicy2)
        self.btnMaximize.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/icons/light/maximize1_3.png);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(199, 202, 207);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(178, 180, 184);\n"
"}")
        self.btnMaximize.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.btnMaximize)

        self.btnClose = QPushButton(self.frameButtons)
        self.btnClose.setObjectName(u"btnClose")
        sizePolicy2.setHeightForWidth(self.btnClose.sizePolicy().hasHeightForWidth())
        self.btnClose.setSizePolicy(sizePolicy2)
        self.btnClose.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/icons/light/close1.png);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(199, 202, 207);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(178, 180, 184);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btnClose)


        self.horizontalLayout_2.addWidget(self.frameButtons)


        self.verticalLayout.addWidget(self.frameTop)

        self.frameContent = QFrame(self.MainFrame)
        self.frameContent.setObjectName(u"frameContent")
        self.frameContent.setStyleSheet(u"background-color: rgb(243, 244, 245);")
        self.frameContent.setFrameShape(QFrame.NoFrame)
        self.frameContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frameContent)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frameFunctions = QFrame(self.frameContent)
        self.frameFunctions.setObjectName(u"frameFunctions")
        sizePolicy.setHeightForWidth(self.frameFunctions.sizePolicy().hasHeightForWidth())
        self.frameFunctions.setSizePolicy(sizePolicy)
        self.frameFunctions.setMinimumSize(QSize(0, 85))
        self.frameFunctions.setMaximumSize(QSize(16777215, 85))
        self.frameFunctions.setFrameShape(QFrame.NoFrame)
        self.frameFunctions.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frameFunctions)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frameB1 = QFrame(self.frameFunctions)
        self.frameB1.setObjectName(u"frameB1")
        self.frameB1.setFrameShape(QFrame.NoFrame)
        self.frameB1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frameB1)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 0)
        self.frame_33 = QFrame(self.frameB1)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.NoFrame)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_35 = QFrame(self.frame_33)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.NoFrame)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_35)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamily(u"MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_4)


        self.horizontalLayout_27.addWidget(self.frame_35)

        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.NoFrame)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_28.setSpacing(10)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.txtPorcentaje = QLabel(self.frame_34)
        self.txtPorcentaje.setObjectName(u"txtPorcentaje")
        font1 = QFont()
        font1.setFamily(u"MS Sans Serif")
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.txtPorcentaje.setFont(font1)
        self.txtPorcentaje.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_28.addWidget(self.txtPorcentaje)

        self.label_3 = QLabel(self.frame_34)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-image: url(:/icons/light/percentage2.png);\n"
"background-position: left;\n"
"background-repeat: no-repeat;")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_28.addWidget(self.label_3)


        self.horizontalLayout_27.addWidget(self.frame_34)


        self.verticalLayout_3.addWidget(self.frame_33)


        self.horizontalLayout_6.addWidget(self.frameB1)

        self.frameB2 = QFrame(self.frameFunctions)
        self.frameB2.setObjectName(u"frameB2")
        self.frameB2.setFrameShape(QFrame.NoFrame)
        self.frameB2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frameB2)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 0)
        self.btnRegistrarP = QPushButton(self.frameB2)
        self.btnRegistrarP.setObjectName(u"btnRegistrarP")
        self.btnRegistrarP.setMaximumSize(QSize(16777215, 37))
        self.btnRegistrarP.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.verticalLayout_4.addWidget(self.btnRegistrarP)


        self.horizontalLayout_6.addWidget(self.frameB2)

        self.frameB3 = QFrame(self.frameFunctions)
        self.frameB3.setObjectName(u"frameB3")
        self.frameB3.setFrameShape(QFrame.NoFrame)
        self.frameB3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frameB3)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 0)
        self.btnRegistrarA = QPushButton(self.frameB3)
        self.btnRegistrarA.setObjectName(u"btnRegistrarA")
        self.btnRegistrarA.setMaximumSize(QSize(16777215, 37))
        self.btnRegistrarA.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.verticalLayout_5.addWidget(self.btnRegistrarA)


        self.horizontalLayout_6.addWidget(self.frameB3)


        self.verticalLayout_2.addWidget(self.frameFunctions)

        self.frameAirplane = QFrame(self.frameContent)
        self.frameAirplane.setObjectName(u"frameAirplane")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frameAirplane.sizePolicy().hasHeightForWidth())
        self.frameAirplane.setSizePolicy(sizePolicy3)
        self.frameAirplane.setMinimumSize(QSize(0, 450))
        self.frameAirplane.setLayoutDirection(Qt.LeftToRight)
        self.frameAirplane.setFrameShape(QFrame.NoFrame)
        self.frameAirplane.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frameAirplane)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 0, 0, 0)
        self.frameAirplane_2 = QFrame(self.frameAirplane)
        self.frameAirplane_2.setObjectName(u"frameAirplane_2")
        sizePolicy3.setHeightForWidth(self.frameAirplane_2.sizePolicy().hasHeightForWidth())
        self.frameAirplane_2.setSizePolicy(sizePolicy3)
        self.frameAirplane_2.setMinimumSize(QSize(0, 450))
        self.frameAirplane_2.setLayoutDirection(Qt.LeftToRight)
        self.frameAirplane_2.setStyleSheet(u"background-image: url(:/icons/images/airplane3.png);\n"
"background-position: left;\n"
"background-repeat: no-repeat;\n"
"")
        self.frameAirplane_2.setFrameShape(QFrame.NoFrame)
        self.frameAirplane_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frameAirplane_2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frameAirplane_2)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(128, 0))
        self.frame.setMaximumSize(QSize(128, 16777215))
        self.frame.setStyleSheet(u"background: transparent;")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.frame)

        self.frame_2 = QFrame(self.frameAirplane_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(250, 460))
        self.frame_2.setMaximumSize(QSize(250, 460))
        self.frame_2.setStyleSheet(u"background: transparent;")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(16777215, 40))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(20, 0, 20, 0)
        self.S1 = QPushButton(self.frame_7)
        self.S1.setObjectName(u"S1")
        self.S1.setMinimumSize(QSize(30, 30))
        self.S1.setMaximumSize(QSize(30, 30))
        self.S1.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(148, 182, 89);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_8.addWidget(self.S1)

        self.S2 = QPushButton(self.frame_7)
        self.S2.setObjectName(u"S2")
        self.S2.setMinimumSize(QSize(30, 30))
        self.S2.setMaximumSize(QSize(30, 30))
        self.S2.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_8.addWidget(self.S2)

        self.S3 = QPushButton(self.frame_7)
        self.S3.setObjectName(u"S3")
        self.S3.setMinimumSize(QSize(30, 30))
        self.S3.setMaximumSize(QSize(30, 30))
        self.S3.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_8.addWidget(self.S3)

        self.S4 = QPushButton(self.frame_7)
        self.S4.setObjectName(u"S4")
        self.S4.setMinimumSize(QSize(30, 30))
        self.S4.setMaximumSize(QSize(30, 30))
        self.S4.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_8.addWidget(self.S4)


        self.verticalLayout_8.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.S5 = QPushButton(self.frame_8)
        self.S5.setObjectName(u"S5")
        self.S5.setMinimumSize(QSize(30, 30))
        self.S5.setMaximumSize(QSize(30, 30))
        self.S5.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_9.addWidget(self.S5)

        self.S6 = QPushButton(self.frame_8)
        self.S6.setObjectName(u"S6")
        self.S6.setMinimumSize(QSize(30, 30))
        self.S6.setMaximumSize(QSize(30, 30))
        self.S6.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_9.addWidget(self.S6)

        self.S7 = QPushButton(self.frame_8)
        self.S7.setObjectName(u"S7")
        self.S7.setMinimumSize(QSize(30, 30))
        self.S7.setMaximumSize(QSize(30, 30))
        self.S7.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_9.addWidget(self.S7)

        self.S8 = QPushButton(self.frame_8)
        self.S8.setObjectName(u"S8")
        self.S8.setMinimumSize(QSize(30, 30))
        self.S8.setMaximumSize(QSize(30, 30))
        self.S8.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_9.addWidget(self.S8)


        self.verticalLayout_8.addWidget(self.frame_8)


        self.verticalLayout_7.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 325))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 5)
        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_9)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.S9 = QPushButton(self.frame_17)
        self.S9.setObjectName(u"S9")
        self.S9.setMinimumSize(QSize(25, 25))
        self.S9.setMaximumSize(QSize(25, 25))
        self.S9.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_17.addWidget(self.S9)

        self.S10 = QPushButton(self.frame_17)
        self.S10.setObjectName(u"S10")
        self.S10.setMinimumSize(QSize(25, 25))
        self.S10.setMaximumSize(QSize(25, 25))
        self.S10.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_17.addWidget(self.S10)

        self.S11 = QPushButton(self.frame_17)
        self.S11.setObjectName(u"S11")
        self.S11.setMinimumSize(QSize(25, 25))
        self.S11.setMaximumSize(QSize(25, 25))
        self.S11.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_17.addWidget(self.S11)


        self.verticalLayout_9.addWidget(self.frame_17)

        self.frame_16 = QFrame(self.frame_9)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.S15 = QPushButton(self.frame_16)
        self.S15.setObjectName(u"S15")
        self.S15.setMinimumSize(QSize(25, 25))
        self.S15.setMaximumSize(QSize(25, 25))
        self.S15.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_16.addWidget(self.S15)

        self.S16 = QPushButton(self.frame_16)
        self.S16.setObjectName(u"S16")
        self.S16.setMinimumSize(QSize(25, 25))
        self.S16.setMaximumSize(QSize(25, 25))
        self.S16.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_16.addWidget(self.S16)

        self.S17 = QPushButton(self.frame_16)
        self.S17.setObjectName(u"S17")
        self.S17.setMinimumSize(QSize(25, 25))
        self.S17.setMaximumSize(QSize(25, 25))
        self.S17.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_16.addWidget(self.S17)


        self.verticalLayout_9.addWidget(self.frame_16)

        self.frame_15 = QFrame(self.frame_9)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.S21 = QPushButton(self.frame_15)
        self.S21.setObjectName(u"S21")
        self.S21.setMinimumSize(QSize(25, 25))
        self.S21.setMaximumSize(QSize(25, 25))
        self.S21.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_15.addWidget(self.S21)

        self.S22 = QPushButton(self.frame_15)
        self.S22.setObjectName(u"S22")
        self.S22.setMinimumSize(QSize(25, 25))
        self.S22.setMaximumSize(QSize(25, 25))
        self.S22.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_15.addWidget(self.S22)

        self.S23 = QPushButton(self.frame_15)
        self.S23.setObjectName(u"S23")
        self.S23.setMinimumSize(QSize(25, 25))
        self.S23.setMaximumSize(QSize(25, 25))
        self.S23.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_15.addWidget(self.S23)


        self.verticalLayout_9.addWidget(self.frame_15)

        self.frame_14 = QFrame(self.frame_9)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.S27 = QPushButton(self.frame_14)
        self.S27.setObjectName(u"S27")
        self.S27.setMinimumSize(QSize(25, 25))
        self.S27.setMaximumSize(QSize(25, 25))
        self.S27.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_14.addWidget(self.S27)

        self.S28 = QPushButton(self.frame_14)
        self.S28.setObjectName(u"S28")
        self.S28.setMinimumSize(QSize(25, 25))
        self.S28.setMaximumSize(QSize(25, 25))
        self.S28.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_14.addWidget(self.S28)

        self.S29 = QPushButton(self.frame_14)
        self.S29.setObjectName(u"S29")
        self.S29.setMinimumSize(QSize(25, 25))
        self.S29.setMaximumSize(QSize(25, 25))
        self.S29.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_14.addWidget(self.S29)


        self.verticalLayout_9.addWidget(self.frame_14)

        self.frame_13 = QFrame(self.frame_9)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.S33 = QPushButton(self.frame_13)
        self.S33.setObjectName(u"S33")
        self.S33.setMinimumSize(QSize(25, 25))
        self.S33.setMaximumSize(QSize(25, 25))
        self.S33.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_13.addWidget(self.S33)

        self.S34 = QPushButton(self.frame_13)
        self.S34.setObjectName(u"S34")
        self.S34.setMinimumSize(QSize(25, 25))
        self.S34.setMaximumSize(QSize(25, 25))
        self.S34.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_13.addWidget(self.S34)

        self.S35 = QPushButton(self.frame_13)
        self.S35.setObjectName(u"S35")
        self.S35.setMinimumSize(QSize(25, 25))
        self.S35.setMaximumSize(QSize(25, 25))
        self.S35.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_13.addWidget(self.S35)


        self.verticalLayout_9.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.S39 = QPushButton(self.frame_12)
        self.S39.setObjectName(u"S39")
        self.S39.setMinimumSize(QSize(25, 25))
        self.S39.setMaximumSize(QSize(25, 25))
        self.S39.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_12.addWidget(self.S39)

        self.S40 = QPushButton(self.frame_12)
        self.S40.setObjectName(u"S40")
        self.S40.setMinimumSize(QSize(25, 25))
        self.S40.setMaximumSize(QSize(25, 25))
        self.S40.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_12.addWidget(self.S40)

        self.S41 = QPushButton(self.frame_12)
        self.S41.setObjectName(u"S41")
        self.S41.setMinimumSize(QSize(25, 25))
        self.S41.setMaximumSize(QSize(25, 25))
        self.S41.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_12.addWidget(self.S41)


        self.verticalLayout_9.addWidget(self.frame_12)

        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(20, -1, 0, -1)
        self.S45 = QPushButton(self.frame_11)
        self.S45.setObjectName(u"S45")
        self.S45.setMinimumSize(QSize(25, 25))
        self.S45.setMaximumSize(QSize(25, 25))
        self.S45.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_11.addWidget(self.S45)

        self.S46 = QPushButton(self.frame_11)
        self.S46.setObjectName(u"S46")
        self.S46.setMinimumSize(QSize(25, 25))
        self.S46.setMaximumSize(QSize(25, 25))
        self.S46.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_11.addWidget(self.S46)

        self.S47 = QPushButton(self.frame_11)
        self.S47.setObjectName(u"S47")
        self.S47.setMinimumSize(QSize(25, 25))
        self.S47.setMaximumSize(QSize(25, 25))
        self.S47.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_11.addWidget(self.S47)


        self.verticalLayout_9.addWidget(self.frame_11)


        self.horizontalLayout_10.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_10)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_10)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.S12 = QPushButton(self.frame_23)
        self.S12.setObjectName(u"S12")
        self.S12.setMinimumSize(QSize(25, 25))
        self.S12.setMaximumSize(QSize(25, 25))
        self.S12.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_23.addWidget(self.S12)

        self.S13 = QPushButton(self.frame_23)
        self.S13.setObjectName(u"S13")
        self.S13.setMinimumSize(QSize(25, 25))
        self.S13.setMaximumSize(QSize(25, 25))
        self.S13.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_23.addWidget(self.S13)

        self.S14 = QPushButton(self.frame_23)
        self.S14.setObjectName(u"S14")
        self.S14.setMinimumSize(QSize(25, 25))
        self.S14.setMaximumSize(QSize(25, 25))
        self.S14.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_23.addWidget(self.S14)


        self.verticalLayout_10.addWidget(self.frame_23)

        self.frame_21 = QFrame(self.frame_10)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.S18 = QPushButton(self.frame_21)
        self.S18.setObjectName(u"S18")
        self.S18.setMinimumSize(QSize(25, 25))
        self.S18.setMaximumSize(QSize(25, 25))
        self.S18.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_21.addWidget(self.S18)

        self.S19 = QPushButton(self.frame_21)
        self.S19.setObjectName(u"S19")
        self.S19.setMinimumSize(QSize(25, 25))
        self.S19.setMaximumSize(QSize(25, 25))
        self.S19.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_21.addWidget(self.S19)

        self.S20 = QPushButton(self.frame_21)
        self.S20.setObjectName(u"S20")
        self.S20.setMinimumSize(QSize(25, 25))
        self.S20.setMaximumSize(QSize(25, 25))
        self.S20.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_21.addWidget(self.S20)


        self.verticalLayout_10.addWidget(self.frame_21)

        self.frame_20 = QFrame(self.frame_10)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.S24 = QPushButton(self.frame_20)
        self.S24.setObjectName(u"S24")
        self.S24.setMinimumSize(QSize(25, 25))
        self.S24.setMaximumSize(QSize(25, 25))
        self.S24.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_20.addWidget(self.S24)

        self.S25 = QPushButton(self.frame_20)
        self.S25.setObjectName(u"S25")
        self.S25.setMinimumSize(QSize(25, 25))
        self.S25.setMaximumSize(QSize(25, 25))
        self.S25.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_20.addWidget(self.S25)

        self.S26 = QPushButton(self.frame_20)
        self.S26.setObjectName(u"S26")
        self.S26.setMinimumSize(QSize(25, 25))
        self.S26.setMaximumSize(QSize(25, 25))
        self.S26.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_20.addWidget(self.S26)


        self.verticalLayout_10.addWidget(self.frame_20)

        self.frame_19 = QFrame(self.frame_10)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.S30 = QPushButton(self.frame_19)
        self.S30.setObjectName(u"S30")
        self.S30.setMinimumSize(QSize(25, 25))
        self.S30.setMaximumSize(QSize(25, 25))
        self.S30.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_19.addWidget(self.S30)

        self.S31 = QPushButton(self.frame_19)
        self.S31.setObjectName(u"S31")
        self.S31.setMinimumSize(QSize(25, 25))
        self.S31.setMaximumSize(QSize(25, 25))
        self.S31.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_19.addWidget(self.S31)

        self.S32 = QPushButton(self.frame_19)
        self.S32.setObjectName(u"S32")
        self.S32.setMinimumSize(QSize(25, 25))
        self.S32.setMaximumSize(QSize(25, 25))
        self.S32.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_19.addWidget(self.S32)


        self.verticalLayout_10.addWidget(self.frame_19)

        self.frame_22 = QFrame(self.frame_10)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.S36 = QPushButton(self.frame_22)
        self.S36.setObjectName(u"S36")
        self.S36.setMinimumSize(QSize(25, 25))
        self.S36.setMaximumSize(QSize(25, 25))
        self.S36.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_22.addWidget(self.S36)

        self.S37 = QPushButton(self.frame_22)
        self.S37.setObjectName(u"S37")
        self.S37.setMinimumSize(QSize(25, 25))
        self.S37.setMaximumSize(QSize(25, 25))
        self.S37.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_22.addWidget(self.S37)

        self.S38 = QPushButton(self.frame_22)
        self.S38.setObjectName(u"S38")
        self.S38.setMinimumSize(QSize(25, 25))
        self.S38.setMaximumSize(QSize(25, 25))
        self.S38.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_22.addWidget(self.S38)


        self.verticalLayout_10.addWidget(self.frame_22)

        self.frame_24 = QFrame(self.frame_10)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.S42 = QPushButton(self.frame_24)
        self.S42.setObjectName(u"S42")
        self.S42.setMinimumSize(QSize(25, 25))
        self.S42.setMaximumSize(QSize(25, 25))
        self.S42.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_24.addWidget(self.S42)

        self.S43 = QPushButton(self.frame_24)
        self.S43.setObjectName(u"S43")
        self.S43.setMinimumSize(QSize(25, 25))
        self.S43.setMaximumSize(QSize(25, 25))
        self.S43.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_24.addWidget(self.S43)

        self.S44 = QPushButton(self.frame_24)
        self.S44.setObjectName(u"S44")
        self.S44.setMinimumSize(QSize(25, 25))
        self.S44.setMaximumSize(QSize(25, 25))
        self.S44.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_24.addWidget(self.S44)


        self.verticalLayout_10.addWidget(self.frame_24)

        self.frame_18 = QFrame(self.frame_10)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, -1, 20, -1)
        self.S48 = QPushButton(self.frame_18)
        self.S48.setObjectName(u"S48")
        self.S48.setMinimumSize(QSize(25, 25))
        self.S48.setMaximumSize(QSize(25, 25))
        self.S48.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_18.addWidget(self.S48)

        self.S49 = QPushButton(self.frame_18)
        self.S49.setObjectName(u"S49")
        self.S49.setMinimumSize(QSize(25, 25))
        self.S49.setMaximumSize(QSize(25, 25))
        self.S49.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_18.addWidget(self.S49)

        self.S50 = QPushButton(self.frame_18)
        self.S50.setObjectName(u"S50")
        self.S50.setMinimumSize(QSize(25, 25))
        self.S50.setMaximumSize(QSize(25, 25))
        self.S50.setStyleSheet(u"QPushButton {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton[Active=true] {\n"
"	background: rgb(95, 99, 104);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: rgb(120, 120, 120);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background: rgb(148, 182, 89);\n"
"}")

        self.horizontalLayout_18.addWidget(self.S50)


        self.verticalLayout_10.addWidget(self.frame_18)


        self.horizontalLayout_10.addWidget(self.frame_10)


        self.verticalLayout_7.addWidget(self.frame_6)


        self.horizontalLayout_7.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frameAirplane_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(422, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setStyleSheet(u"background: transparent;")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.frame_3)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy1.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy1)
        self.frame_25.setMinimumSize(QSize(130, 0))
        self.frame_25.setMaximumSize(QSize(130, 16777215))
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_25.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_3)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy1.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy1)
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_26)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_27)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(20, 0, 50, 0)
        self.txtCedula = QLineEdit(self.frame_27)
        self.txtCedula.setObjectName(u"txtCedula")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.txtCedula.sizePolicy().hasHeightForWidth())
        self.txtCedula.setSizePolicy(sizePolicy4)
        self.txtCedula.setMinimumSize(QSize(0, 0))
        self.txtCedula.setStyleSheet(u"background: rgb(255, 255, 255);")
        self.txtCedula.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_12.addWidget(self.txtCedula)

        self.txtNombre = QLineEdit(self.frame_27)
        self.txtNombre.setObjectName(u"txtNombre")
        sizePolicy4.setHeightForWidth(self.txtNombre.sizePolicy().hasHeightForWidth())
        self.txtNombre.setSizePolicy(sizePolicy4)
        self.txtNombre.setMinimumSize(QSize(0, 0))
        self.txtNombre.setStyleSheet(u"background: rgb(255, 255, 255);")
        self.txtNombre.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_12.addWidget(self.txtNombre)


        self.verticalLayout_11.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_26)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.NoFrame)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_28)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(20, 0, 50, 0)
        self.comboPasajeros = QComboBox(self.frame_28)
        self.comboPasajeros.setObjectName(u"comboPasajeros")
        self.comboPasajeros.setStyleSheet(u"background: rgb(255, 255, 255);")

        self.verticalLayout_13.addWidget(self.comboPasajeros)

        self.frame_30 = QFrame(self.frame_28)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.NoFrame)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.frame_30)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.NoFrame)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_32)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.radioEjecutiva = QRadioButton(self.frame_32)
        self.radioEjecutiva.setObjectName(u"radioEjecutiva")

        self.verticalLayout_14.addWidget(self.radioEjecutiva)

        self.radioEconomica = QRadioButton(self.frame_32)
        self.radioEconomica.setObjectName(u"radioEconomica")

        self.verticalLayout_14.addWidget(self.radioEconomica)


        self.horizontalLayout_26.addWidget(self.frame_32)

        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.NoFrame)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_31)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.radioVentana = QRadioButton(self.frame_31)
        self.radioVentana.setObjectName(u"radioVentana")

        self.verticalLayout_15.addWidget(self.radioVentana)

        self.radioCentro = QRadioButton(self.frame_31)
        self.radioCentro.setObjectName(u"radioCentro")

        self.verticalLayout_15.addWidget(self.radioCentro)

        self.radioPasillo = QRadioButton(self.frame_31)
        self.radioPasillo.setObjectName(u"radioPasillo")

        self.verticalLayout_15.addWidget(self.radioPasillo)


        self.horizontalLayout_26.addWidget(self.frame_31)


        self.verticalLayout_13.addWidget(self.frame_30)


        self.verticalLayout_11.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_26)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_29)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(20, 20, 50, 20)
        self.listaPasajeros = QListWidget(self.frame_29)
        self.listaPasajeros.setObjectName(u"listaPasajeros")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.listaPasajeros.sizePolicy().hasHeightForWidth())
        self.listaPasajeros.setSizePolicy(sizePolicy5)
        self.listaPasajeros.setMinimumSize(QSize(100, 0))
        self.listaPasajeros.setMaximumSize(QSize(16777215, 16777215))
        self.listaPasajeros.setStyleSheet(u"background: rgb(255, 255, 255);")
        self.listaPasajeros.setFrameShape(QFrame.StyledPanel)

        self.verticalLayout_16.addWidget(self.listaPasajeros)


        self.verticalLayout_11.addWidget(self.frame_29)


        self.horizontalLayout_25.addWidget(self.frame_26)


        self.horizontalLayout_7.addWidget(self.frame_3)


        self.verticalLayout_6.addWidget(self.frameAirplane_2)


        self.verticalLayout_2.addWidget(self.frameAirplane)

        self.frameDown = QFrame(self.frameContent)
        self.frameDown.setObjectName(u"frameDown")
        sizePolicy.setHeightForWidth(self.frameDown.sizePolicy().hasHeightForWidth())
        self.frameDown.setSizePolicy(sizePolicy)
        self.frameDown.setMinimumSize(QSize(0, 20))
        self.frameDown.setMaximumSize(QSize(16777215, 20))
        self.frameDown.setStyleSheet(u"background-color: rgb(250, 250, 250);")
        self.frameDown.setFrameShape(QFrame.NoFrame)
        self.frameDown.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frameDown)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frameLabel = QFrame(self.frameDown)
        self.frameLabel.setObjectName(u"frameLabel")
        sizePolicy3.setHeightForWidth(self.frameLabel.sizePolicy().hasHeightForWidth())
        self.frameLabel.setSizePolicy(sizePolicy3)
        self.frameLabel.setFrameShape(QFrame.NoFrame)
        self.frameLabel.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frameLabel)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(15, 0, 0, 0)
        self.label = QLabel(self.frameLabel)
        self.label.setObjectName(u"label")
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setFamily(u"MS Sans Serif")
        font2.setPointSize(6)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"font: 6pt \"MS Sans Serif\";\n"
"color: rgb(135, 135, 135);")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label)


        self.horizontalLayout_4.addWidget(self.frameLabel)

        self.frameSizeGrip = QFrame(self.frameDown)
        self.frameSizeGrip.setObjectName(u"frameSizeGrip")
        sizePolicy3.setHeightForWidth(self.frameSizeGrip.sizePolicy().hasHeightForWidth())
        self.frameSizeGrip.setSizePolicy(sizePolicy3)
        self.frameSizeGrip.setMaximumSize(QSize(20, 20))
        self.frameSizeGrip.setStyleSheet(u"background-image: url(:/icons/dark/size-grip1.png);\n"
"background-position: center;\n"
"background-repeat: no repeat;")
        self.frameSizeGrip.setFrameShape(QFrame.NoFrame)
        self.frameSizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frameSizeGrip)


        self.verticalLayout_2.addWidget(self.frameDown)


        self.verticalLayout.addWidget(self.frameContent)


        self.horizontalLayout.addWidget(self.MainFrame)

        MainWindow.setCentralWidget(self.MainWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.btnMinimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btnMinimize.setText("")
#if QT_CONFIG(tooltip)
        self.btnMaximize.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btnMaximize.setText("")
#if QT_CONFIG(tooltip)
        self.btnClose.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btnClose.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"OCUPACI\u00d3N", None))
        self.txtPorcentaje.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.label_3.setText("")
        self.btnRegistrarP.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR PASAJERO", None))
        self.btnRegistrarA.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR ASIGNACI\u00d3N", None))
        self.S1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.S2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.S3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.S4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.S5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.S6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.S7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.S8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.S9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.S10.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.S11.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.S15.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.S16.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.S17.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.S21.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.S22.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.S23.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.S27.setText(QCoreApplication.translate("MainWindow", u"27", None))
        self.S28.setText(QCoreApplication.translate("MainWindow", u"28", None))
        self.S29.setText(QCoreApplication.translate("MainWindow", u"29", None))
        self.S33.setText(QCoreApplication.translate("MainWindow", u"33", None))
        self.S34.setText(QCoreApplication.translate("MainWindow", u"34", None))
        self.S35.setText(QCoreApplication.translate("MainWindow", u"35", None))
        self.S39.setText(QCoreApplication.translate("MainWindow", u"39", None))
        self.S40.setText(QCoreApplication.translate("MainWindow", u"40", None))
        self.S41.setText(QCoreApplication.translate("MainWindow", u"41", None))
        self.S45.setText(QCoreApplication.translate("MainWindow", u"45", None))
        self.S46.setText(QCoreApplication.translate("MainWindow", u"46", None))
        self.S47.setText(QCoreApplication.translate("MainWindow", u"47", None))
        self.S12.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.S13.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.S14.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.S18.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.S19.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.S20.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.S24.setText(QCoreApplication.translate("MainWindow", u"24", None))
        self.S25.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.S26.setText(QCoreApplication.translate("MainWindow", u"26", None))
        self.S30.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.S31.setText(QCoreApplication.translate("MainWindow", u"31", None))
        self.S32.setText(QCoreApplication.translate("MainWindow", u"32", None))
        self.S36.setText(QCoreApplication.translate("MainWindow", u"36", None))
        self.S37.setText(QCoreApplication.translate("MainWindow", u"37", None))
        self.S38.setText(QCoreApplication.translate("MainWindow", u"38", None))
        self.S42.setText(QCoreApplication.translate("MainWindow", u"42", None))
        self.S43.setText(QCoreApplication.translate("MainWindow", u"43", None))
        self.S44.setText(QCoreApplication.translate("MainWindow", u"44", None))
        self.S48.setText(QCoreApplication.translate("MainWindow", u"48", None))
        self.S49.setText(QCoreApplication.translate("MainWindow", u"49", None))
        self.S50.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.txtCedula.setText("")
        self.txtCedula.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C\u00c9DULA", None))
        self.txtNombre.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.radioEjecutiva.setText(QCoreApplication.translate("MainWindow", u"Ejecutiva", None))
        self.radioEconomica.setText(QCoreApplication.translate("MainWindow", u"Econ\u00f3mica", None))
        self.radioVentana.setText(QCoreApplication.translate("MainWindow", u"Ventana", None))
        self.radioCentro.setText(QCoreApplication.translate("MainWindow", u"Centro", None))
        self.radioPasillo.setText(QCoreApplication.translate("MainWindow", u"Pasillo", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Desarrollado por: Ruby Carolina D\u00edaz D\u00edaz, Juan Diego Fern\u00e1ndez Rivera y Andr\u00e9s Felipe D\u00edaz", None))
    # retranslateUi

