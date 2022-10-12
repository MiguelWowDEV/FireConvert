# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyqtgraph import PlotWidget

import recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(601, 588)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_toggle = QFrame(self.centralwidget)
        self.menu_toggle.setObjectName(u"menu_toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_toggle.sizePolicy().hasHeightForWidth())
        self.menu_toggle.setSizePolicy(sizePolicy)
        self.menu_toggle.setMinimumSize(QSize(0, 0))
        self.menu_toggle.setMaximumSize(QSize(81, 16777215))
        self.menu_toggle.setStyleSheet(u"background-color: rgb(33, 33, 33);")
        self.menu_toggle.setFrameShape(QFrame.StyledPanel)
        self.menu_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.menu_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_content = QFrame(self.menu_toggle)
        self.btn_content.setObjectName(u"btn_content")
        self.btn_content.setFrameShape(QFrame.StyledPanel)
        self.btn_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.btn_content)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_icon = QFrame(self.btn_content)
        self.frame_icon.setObjectName(u"frame_icon")
        self.frame_icon.setMaximumSize(QSize(16777215, 74))
        self.frame_icon.setStyleSheet(u"background-color: rgb(50, 50, 50);")
        self.frame_icon.setFrameShape(QFrame.StyledPanel)
        self.frame_icon.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_icon)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, -1, -1, -1)
        self.toolButton_4 = QToolButton(self.frame_icon)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setStyleSheet(u"border: none;\n"
"")
        icon = QIcon()
        icon.addFile(u":/iconos/icons/Comet_icon-icons.com_54192.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_4.setIcon(icon)
        self.toolButton_4.setIconSize(QSize(52, 52))

        self.horizontalLayout_4.addWidget(self.toolButton_4)


        self.verticalLayout_3.addWidget(self.frame_icon)

        self.btns_main = QFrame(self.btn_content)
        self.btns_main.setObjectName(u"btns_main")
        self.btns_main.setFrameShape(QFrame.StyledPanel)
        self.btns_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.btns_main)
        self.verticalLayout_4.setSpacing(38)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 20, -1, -1)
        self.btn_convert = QToolButton(self.btns_main)
        self.btn_convert.setObjectName(u"btn_convert")
        self.btn_convert.setStyleSheet(u"border: none;\n"
"background-color: rgb(255, 133, 76);\n"
"border-radius: 9px;")
        icon1 = QIcon()
        icon1.addFile(u":/iconos/icons/thermometer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_convert.setIcon(icon1)
        self.btn_convert.setIconSize(QSize(45, 45))

        self.verticalLayout_4.addWidget(self.btn_convert)

        self.btn_graph = QToolButton(self.btns_main)
        self.btn_graph.setObjectName(u"btn_graph")
        self.btn_graph.setStyleSheet(u"border: none;\n"
"background-color: rgb(255, 133, 76);\n"
"border-radius: 9px;")
        icon2 = QIcon()
        icon2.addFile(u":/iconos/icons/bar-chart-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_graph.setIcon(icon2)
        self.btn_graph.setIconSize(QSize(45, 45))

        self.verticalLayout_4.addWidget(self.btn_graph)


        self.verticalLayout_3.addWidget(self.btns_main, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.line_3 = QFrame(self.btn_content)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        self.frame_support = QFrame(self.btn_content)
        self.frame_support.setObjectName(u"frame_support")
        sizePolicy.setHeightForWidth(self.frame_support.sizePolicy().hasHeightForWidth())
        self.frame_support.setSizePolicy(sizePolicy)
        self.frame_support.setMaximumSize(QSize(16777215, 74))
        self.frame_support.setFrameShape(QFrame.StyledPanel)
        self.frame_support.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_support)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.support = QToolButton(self.frame_support)
        self.support.setObjectName(u"support")
        self.support.setStyleSheet(u"border: none;\n"
"background-color: rgb(255, 133, 76);\n"
"border-radius: 9px;")
        icon3 = QIcon()
        icon3.addFile(u":/iconos/icons/box.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.support.setIcon(icon3)
        self.support.setIconSize(QSize(45, 45))

        self.horizontalLayout_5.addWidget(self.support)


        self.verticalLayout_3.addWidget(self.frame_support)


        self.verticalLayout_2.addWidget(self.btn_content)


        self.horizontalLayout.addWidget(self.menu_toggle)

        self.body_app = QFrame(self.centralwidget)
        self.body_app.setObjectName(u"body_app")
        self.body_app.setFrameShape(QFrame.StyledPanel)
        self.body_app.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.body_app)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.body_app)
        self.header.setObjectName(u"header")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy1)
        self.header.setMaximumSize(QSize(16777215, 54))
        self.header.setStyleSheet(u"background-color: rgb(36, 36, 36);")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header_title = QLabel(self.header)
        self.header_title.setObjectName(u"header_title")
        font = QFont()
        font.setFamily(u"Bahnschrift SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.header_title.setFont(font)
        self.header_title.setStyleSheet(u"color: white;\n"
"font-size: 25px;")
        self.header_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.header_title)

        self.line = QFrame(self.header)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.page_title = QLabel(self.header)
        self.page_title.setObjectName(u"page_title")
        self.page_title.setFont(font)
        self.page_title.setStyleSheet(u"color: white;\n"
"font-size: 20px;")
        self.page_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.page_title)


        self.verticalLayout.addWidget(self.header)

        self.content = QFrame(self.body_app)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.content)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(self.content)
        self.pages.setObjectName(u"pages")
        self.pages.setStyleSheet(u"border: none;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"background-color: rgb(42, 42, 42);\n"
"border: none;")
        self.verticalLayout_5 = QVBoxLayout(self.page)
        self.verticalLayout_5.setSpacing(11)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, 0, 0)
        self.convert_frame = QFrame(self.page)
        self.convert_frame.setObjectName(u"convert_frame")
        self.convert_frame.setFrameShape(QFrame.StyledPanel)
        self.convert_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.convert_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 12, 10, 0)
        self.frame_options = QFrame(self.convert_frame)
        self.frame_options.setObjectName(u"frame_options")
        self.frame_options.setStyleSheet(u"border-radius: 7px;\n"
"background-color: rgb(255, 147, 69);")
        self.frame_options.setFrameShape(QFrame.StyledPanel)
        self.frame_options.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_options)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame = QFrame(self.frame_options)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Bahnschrift SemiBold")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color:white;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label)

        self.btn_load_text = QPushButton(self.frame)
        self.btn_load_text.setObjectName(u"btn_load_text")
        self.btn_load_text.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_load_text.setStyleSheet(u"QPushButton {\n"
"border: 4px solid rgb(202, 97, 44);\n"
"color: white;\n"
"font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border: none;\n"
"background-color: rgb(202, 97, 44);\n"
"\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/iconos/icons/file-text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_load_text.setIcon(icon4)
        self.btn_load_text.setIconSize(QSize(30, 30))

        self.verticalLayout_6.addWidget(self.btn_load_text)


        self.horizontalLayout_7.addWidget(self.frame)

        self.frame_3 = QFrame(self.frame_options)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(1, 0))
        self.frame_3.setMaximumSize(QSize(13, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.line_4 = QFrame(self.frame_3)
        self.line_4.setObjectName(u"line_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy2)
        self.line_4.setMinimumSize(QSize(0, 0))
        self.line_4.setMaximumSize(QSize(5, 16777215))
        self.line_4.setStyleSheet(u"border: none;\n"
"background-color: rgb(59, 59, 59);")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_4)


        self.horizontalLayout_7.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame_options)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color:white;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.btn_history = QPushButton(self.frame_2)
        self.btn_history.setObjectName(u"btn_history")
        self.btn_history.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_history.setStyleSheet(u"QPushButton {\n"
"border: 4px solid rgb(202, 97, 44);\n"
"color: white;\n"
"font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border: none;\n"
"background-color: rgb(202, 97, 44);\n"
"\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/iconos/icons/cloud.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_history.setIcon(icon5)
        self.btn_history.setIconSize(QSize(30, 30))

        self.verticalLayout_7.addWidget(self.btn_history)


        self.horizontalLayout_7.addWidget(self.frame_2)


        self.horizontalLayout_6.addWidget(self.frame_options)


        self.verticalLayout_5.addWidget(self.convert_frame)

        self.convert_content = QFrame(self.page)
        self.convert_content.setObjectName(u"convert_content")
        self.convert_content.setFrameShape(QFrame.StyledPanel)
        self.convert_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.convert_content)
        self.verticalLayout_8.setSpacing(56)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.convert_content)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(65)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setContentsMargins(10, 0, 10, 0)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(142, 16777215))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 20px;")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setMinimumSize(QSize(0, 25))
        self.label_4.setMaximumSize(QSize(235, 117))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 20px;")

        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)

        self.temp_a = QLineEdit(self.frame_4)
        self.temp_a.setObjectName(u"temp_a")
        self.temp_a.setMaximumSize(QSize(198, 16777215))
        self.temp_a.setStyleSheet(u"border-bottom: 2px solid rgb(255, 136, 56);\n"
"background-color: rgb(38, 38, 38);\n"
"color: white;\n"
"font-size: 16px;")
        self.temp_a.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.temp_a, 1, 0, 1, 1)

        self.combox_temp_1 = QComboBox(self.frame_4)
        self.combox_temp_1.addItem("")
        self.combox_temp_1.addItem("")
        self.combox_temp_1.addItem("")
        self.combox_temp_1.setObjectName(u"combox_temp_1")
        self.combox_temp_1.setStyleSheet(u"color: white;\n"
"background-color: rgb(38, 38, 38);\n"
"font-size: 17px;\n"
"padding-left: 15px;\n"
"")

        self.gridLayout.addWidget(self.combox_temp_1, 2, 0, 1, 1)

        self.combox_temp_2 = QComboBox(self.frame_4)
        self.combox_temp_2.addItem("")
        self.combox_temp_2.addItem("")
        self.combox_temp_2.addItem("")
        self.combox_temp_2.setObjectName(u"combox_temp_2")
        self.combox_temp_2.setStyleSheet(u"color: white;\n"
"background-color: rgb(38, 38, 38);\n"
"font-size: 17px;\n"
"padding-left: 15px;\n"
"")

        self.gridLayout.addWidget(self.combox_temp_2, 2, 1, 1, 1, Qt.AlignVCenter)


        self.verticalLayout_8.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.convert_content)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 65))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(15, 0, 15, 0)
        self.calculate = QPushButton(self.frame_5)
        self.calculate.setObjectName(u"calculate")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.calculate.sizePolicy().hasHeightForWidth())
        self.calculate.setSizePolicy(sizePolicy4)
        self.calculate.setCursor(QCursor(Qt.PointingHandCursor))
        self.calculate.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 85, 51, 255), stop:1 rgba(255, 192, 129, 255));\n"
"color: white;\n"
"font-size: 20px;\n"
"border-top-right-radius: 9px;")

        self.horizontalLayout_10.addWidget(self.calculate)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.line_2 = QFrame(self.convert_content)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line_2)


        self.verticalLayout_5.addWidget(self.convert_content)

        self.result_frame = QFrame(self.page)
        self.result_frame.setObjectName(u"result_frame")
        sizePolicy1.setHeightForWidth(self.result_frame.sizePolicy().hasHeightForWidth())
        self.result_frame.setSizePolicy(sizePolicy1)
        self.result_frame.setMaximumSize(QSize(16777215, 90))
        self.result_frame.setFrameShape(QFrame.StyledPanel)
        self.result_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.result_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_result = QLabel(self.result_frame)
        self.label_result.setObjectName(u"label_result")
        self.label_result.setStyleSheet(u"color: white;\n"
"font-size: 20px;")
        self.label_result.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_result)


        self.verticalLayout_5.addWidget(self.result_frame)

        self.pages.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"background-color: rgb(42, 42, 42);")
        self.verticalLayout_9 = QVBoxLayout(self.page_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.options_graph = QFrame(self.page_2)
        self.options_graph.setObjectName(u"options_graph")
        self.options_graph.setFrameShape(QFrame.StyledPanel)
        self.options_graph.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.options_graph)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_load_files = QFrame(self.options_graph)
        self.frame_load_files.setObjectName(u"frame_load_files")
        sizePolicy.setHeightForWidth(self.frame_load_files.sizePolicy().hasHeightForWidth())
        self.frame_load_files.setSizePolicy(sizePolicy)
        self.frame_load_files.setMinimumSize(QSize(0, 0))
        self.frame_load_files.setMaximumSize(QSize(268, 16777215))
        self.frame_load_files.setLayoutDirection(Qt.LeftToRight)
        self.frame_load_files.setFrameShape(QFrame.StyledPanel)
        self.frame_load_files.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_load_files)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 0, 5, 9)
        self.label_5 = QLabel(self.frame_load_files)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(178, 16777215))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: white;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_5)

        self.load_graph = QPushButton(self.frame_load_files)
        self.load_graph.setObjectName(u"load_graph")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.load_graph.sizePolicy().hasHeightForWidth())
        self.load_graph.setSizePolicy(sizePolicy5)
        self.load_graph.setMaximumSize(QSize(351, 55))
        self.load_graph.setCursor(QCursor(Qt.PointingHandCursor))
        self.load_graph.setLayoutDirection(Qt.LeftToRight)
        self.load_graph.setStyleSheet(u"background-color: rgb(255, 146, 103);\n"
"color: white;\n"
"font-size: 20px;\n"
"border-radius: 12px;\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/iconos/icons/file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.load_graph.setIcon(icon6)
        self.load_graph.setIconSize(QSize(30, 30))

        self.verticalLayout_11.addWidget(self.load_graph)


        self.verticalLayout_10.addWidget(self.frame_load_files, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.options_graph)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(21)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setContentsMargins(0, 15, 0, 6)
        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: white;")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.action_graph = QPushButton(self.frame_7)
        self.action_graph.setObjectName(u"action_graph")
        sizePolicy4.setHeightForWidth(self.action_graph.sizePolicy().hasHeightForWidth())
        self.action_graph.setSizePolicy(sizePolicy4)
        self.action_graph.setMaximumSize(QSize(202, 54))
        self.action_graph.setCursor(QCursor(Qt.PointingHandCursor))
        self.action_graph.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 85, 51, 255), stop:1 rgba(255, 192, 129, 255));\n"
"color: white;\n"
"font-size: 20px;\n"
"border-top-right-radius: 9px;\n"
"border-bottom-left-radius: 9px;")

        self.gridLayout_2.addWidget(self.action_graph, 0, 1, 2, 1)

        self.select_graph = QComboBox(self.frame_7)
        self.select_graph.addItem("")
        self.select_graph.addItem("")
        self.select_graph.setObjectName(u"select_graph")
        self.select_graph.setMaximumSize(QSize(151, 16777215))
        self.select_graph.setStyleSheet(u"color: white;\n"
"font-size: 18px;\n"
"background-color: rgb(38, 38, 38)")

        self.gridLayout_2.addWidget(self.select_graph, 1, 0, 1, 1)


        self.verticalLayout_10.addWidget(self.frame_7)


        self.verticalLayout_9.addWidget(self.options_graph)

        self.graphicsView = PlotWidget(self.page_2)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setStyleSheet(u"background-color: rgb(57, 57, 57);\n"
"border-radius: 9px;")

        self.verticalLayout_9.addWidget(self.graphicsView)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"background-color: rgb(42, 42, 42);\n"
"border: none;")
        self.verticalLayout_12 = QVBoxLayout(self.page_3)
        self.verticalLayout_12.setSpacing(13)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.page_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.warning_version = QLabel(self.frame_6)
        self.warning_version.setObjectName(u"warning_version")
        self.warning_version.setStyleSheet(u"color: white;\n"
"font-size: 30px;")
        self.warning_version.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.warning_version)


        self.verticalLayout_12.addWidget(self.frame_6)

        self.pages.addWidget(self.page_3)

        self.horizontalLayout_3.addWidget(self.pages)


        self.verticalLayout.addWidget(self.content)


        self.horizontalLayout.addWidget(self.body_app)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_convert.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_graph.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.support.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.header_title.setText(QCoreApplication.translate("MainWindow", u"FireConvert v1.0-beta", None))
        self.page_title.setText(QCoreApplication.translate("MainWindow", u"Conversi\u00f3n", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Importar temperaturas", None))
        self.btn_load_text.setText(QCoreApplication.translate("MainWindow", u"Importar Archivo", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Historial de operaciones", None))
        self.btn_history.setText(QCoreApplication.translate("MainWindow", u"Historial", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Temperatura A", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Temperatura a convertir", None))
        self.combox_temp_1.setItemText(0, QCoreApplication.translate("MainWindow", u"Kelvin", None))
        self.combox_temp_1.setItemText(1, QCoreApplication.translate("MainWindow", u"Celsius", None))
        self.combox_temp_1.setItemText(2, QCoreApplication.translate("MainWindow", u"Farenheit", None))

        self.combox_temp_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Kelvin", None))
        self.combox_temp_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Celsius", None))
        self.combox_temp_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Farenheit", None))

        self.calculate.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.label_result.setText(QCoreApplication.translate("MainWindow", u"Prueba alguna temperatura :)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cargar datos", None))
        self.load_graph.setText(QCoreApplication.translate("MainWindow", u"Leer temperaturas", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Tipo de curva", None))
        self.action_graph.setText(QCoreApplication.translate("MainWindow", u"Graficar", None))
        self.select_graph.setItemText(0, QCoreApplication.translate("MainWindow", u"Calentamiento", None))
        self.select_graph.setItemText(1, QCoreApplication.translate("MainWindow", u"Enfriamiento", None))

        self.warning_version.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Sistema de soporte para la beta 1.5 <br/><br/>Proximamente...</p></body></html>", None))
    # retranslateUi

