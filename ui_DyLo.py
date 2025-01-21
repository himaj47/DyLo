# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DyLoWZvKKf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomStackedWidget

import resources_rc

class Ui_DyLo(object):
    def setupUi(self, DyLo):
        if not DyLo.objectName():
            DyLo.setObjectName(u"DyLo")
        DyLo.resize(958, 667)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        DyLo.setFont(font)
        DyLo.setMouseTracking(False)
        DyLo.setStyleSheet(u"*{\n"
"	background-color: rgb(246, 245, 244);\n"
"	padding: 0;\n"
"	margin: 0;\n"
"}\n"
"\n"
"left_menu_container{\n"
"	padding: 0;\n"
"	margin: 0;\n"
"}\n"
"\n"
"QPushButton{\n"
"	text-align: left;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"        background-color: rgb(153, 193, 241);\n"
"    }")
        self.centralwidget = QWidget(DyLo)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout_8 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_bar_widget = QWidget(self.centralwidget)
        self.top_bar_widget.setObjectName(u"top_bar_widget")
        self.top_bar_widget.setStyleSheet(u"background-color: rgb(119, 118, 123);")
        self.horizontalLayout_9 = QHBoxLayout(self.top_bar_widget)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(80, 5, 0, 5)
        self.label_3 = QLabel(self.top_bar_widget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"text-font-color: white;\n"
"")

        self.horizontalLayout_9.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.frame_2 = QFrame(self.top_bar_widget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setBaseSize(QSize(0, 0))
        self.frame_2.setStyleSheet(u"border: none")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_11.setSpacing(9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.minimize = QPushButton(self.frame_2)
        self.minimize.setObjectName(u"minimize")
        icon = QIcon()
        icon.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize.setIcon(icon)

        self.horizontalLayout_11.addWidget(self.minimize, 0, Qt.AlignHCenter)

        self.maximize = QPushButton(self.frame_2)
        self.maximize.setObjectName(u"maximize")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.maximize.sizePolicy().hasHeightForWidth())
        self.maximize.setSizePolicy(sizePolicy1)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize.setIcon(icon1)

        self.horizontalLayout_11.addWidget(self.maximize, 0, Qt.AlignHCenter)

        self.close = QPushButton(self.frame_2)
        self.close.setObjectName(u"close")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close.setIcon(icon2)

        self.horizontalLayout_11.addWidget(self.close, 0, Qt.AlignHCenter)


        self.horizontalLayout_9.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.top_bar_widget, 0, Qt.AlignTop)

        self.main_widget = QWidget(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.main_widget.sizePolicy().hasHeightForWidth())
        self.main_widget.setSizePolicy(sizePolicy2)
        self.horizontalLayout_10 = QHBoxLayout(self.main_widget)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.left_body_container = QWidget(self.main_widget)
        self.left_body_container.setObjectName(u"left_body_container")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.left_body_container.sizePolicy().hasHeightForWidth())
        self.left_body_container.setSizePolicy(sizePolicy3)
        self.left_body_container.setFont(font)
        self.left_body_container.setMouseTracking(True)
        self.left_body_layout = QVBoxLayout(self.left_body_container)
        self.left_body_layout.setSpacing(0)
        self.left_body_layout.setObjectName(u"left_body_layout")
        self.left_body_layout.setContentsMargins(7, 0, 0, 7)
        self.left_menu_container = QWidget(self.left_body_container)
        self.left_menu_container.setObjectName(u"left_menu_container")
        self.left_menu_container.setStyleSheet(u"background-color: rgb(222, 221, 218);\n"
"")
        self.horizontalLayout = QHBoxLayout(self.left_menu_container)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_sub_container = QWidget(self.left_menu_container)
        self.left_sub_container.setObjectName(u"left_sub_container")
        self.verticalLayout_3 = QVBoxLayout(self.left_sub_container)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.start_frame = QFrame(self.left_sub_container)
        self.start_frame.setObjectName(u"start_frame")
        sizePolicy3.setHeightForWidth(self.start_frame.sizePolicy().hasHeightForWidth())
        self.start_frame.setSizePolicy(sizePolicy3)
        self.start_frame.setMinimumSize(QSize(0, 42))
        self.start_frame.setSizeIncrement(QSize(0, 0))
        self.start_frame.setBaseSize(QSize(0, 0))
        self.start_frame.setStyleSheet(u"hover {\n"
"	background-color: rgb(153, 193, 241);\n"
"}")
        self.start_frame.setFrameShape(QFrame.StyledPanel)
        self.start_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.start_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.start_b = QPushButton(self.start_frame)
        self.start_b.setObjectName(u"start_b")
        sizePolicy3.setHeightForWidth(self.start_b.sizePolicy().hasHeightForWidth())
        self.start_b.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.start_b.setFont(font2)
        self.start_b.setMouseTracking(True)
        self.start_b.setAutoFillBackground(False)
        self.start_b.setStyleSheet("""
            QPushButton {
                color: rgb(154, 153, 150);
                font: bold;
            }
            QPushButton:hover {
                background-color: rgb(98, 160, 234);
                color: white;
            }
        """)
        self.start_b.setIconSize(QSize(16, 16))
        self.start_b.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.start_b)


        self.verticalLayout_3.addWidget(self.start_frame)

        self.sim_frame = QFrame(self.left_sub_container)
        self.sim_frame.setObjectName(u"sim_frame")
        self.sim_frame.setMinimumSize(QSize(0, 42))
        self.sim_frame.setFrameShape(QFrame.StyledPanel)
        self.sim_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.sim_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.sim_b = QPushButton(self.sim_frame)
        self.sim_b.setObjectName(u"sim_b")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.sim_b.sizePolicy().hasHeightForWidth())
        self.sim_b.setSizePolicy(sizePolicy4)
        self.sim_b.setFont(font2)
        self.sim_b.setStyleSheet("""
            QPushButton {
                color: rgb(154, 153, 150);
                font: bold;
            }
            QPushButton:hover {
                background-color: rgb(98, 160, 234);
                color: white;
            }
        """)

        self.horizontalLayout_3.addWidget(self.sim_b)


        self.verticalLayout_3.addWidget(self.sim_frame)

        self.ros2_control_frame = QFrame(self.left_sub_container)
        self.ros2_control_frame.setObjectName(u"ros2_control_frame")
        self.ros2_control_frame.setMinimumSize(QSize(0, 42))
        self.ros2_control_frame.setFrameShape(QFrame.StyledPanel)
        self.ros2_control_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.ros2_control_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ros_control_b = QPushButton(self.ros2_control_frame)
        self.ros_control_b.setObjectName(u"ros_control_b")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.ros_control_b.sizePolicy().hasHeightForWidth())
        self.ros_control_b.setSizePolicy(sizePolicy5)
        self.ros_control_b.setFont(font2)
        self.ros_control_b.setStyleSheet("""
            QPushButton {
                color: rgb(154, 153, 150);
                font: bold;
            }
            QPushButton:hover {
                background-color: rgb(98, 160, 234);
                color: white;
            }
        """)

        self.horizontalLayout_4.addWidget(self.ros_control_b)


        self.verticalLayout_3.addWidget(self.ros2_control_frame)

        self.config_frame = QFrame(self.left_sub_container)
        self.config_frame.setObjectName(u"config_frame")
        self.config_frame.setMinimumSize(QSize(0, 42))
        self.config_frame.setFrameShape(QFrame.StyledPanel)
        self.config_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.config_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.config_file_b = QPushButton(self.config_frame)
        self.config_file_b.setObjectName(u"config_file_b")
        sizePolicy4.setHeightForWidth(self.config_file_b.sizePolicy().hasHeightForWidth())
        self.config_file_b.setSizePolicy(sizePolicy4)
        self.config_file_b.setFont(font2)
        self.config_file_b.setStyleSheet("""
            QPushButton {
                color: rgb(154, 153, 150);
                font: bold;
            }
            QPushButton:hover {
                background-color: rgb(98, 160, 234);
                color: white;
            }
        """)

        self.horizontalLayout_5.addWidget(self.config_file_b)


        self.verticalLayout_3.addWidget(self.config_frame)

        self.help_frame = QFrame(self.left_sub_container)
        self.help_frame.setObjectName(u"help_frame")
        self.help_frame.setMinimumSize(QSize(0, 42))
        self.help_frame.setFrameShape(QFrame.StyledPanel)
        self.help_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.help_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.help_b = QPushButton(self.help_frame)
        self.help_b.setObjectName(u"help_b")
        sizePolicy4.setHeightForWidth(self.help_b.sizePolicy().hasHeightForWidth())
        self.help_b.setSizePolicy(sizePolicy4)
        self.help_b.setFont(font2)
        self.help_b.setStyleSheet("""
            QPushButton {
                color: rgb(154, 153, 150);
                font: bold;
            }
            QPushButton:hover {
                background-color: rgb(98, 160, 234);
                color: white;
            }
        """)

        self.horizontalLayout_6.addWidget(self.help_b)


        self.verticalLayout_3.addWidget(self.help_frame)


        self.horizontalLayout.addWidget(self.left_sub_container)


        self.left_body_layout.addWidget(self.left_menu_container, 0, Qt.AlignLeft)

        self.frame = QFrame(self.left_body_container)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer = QSpacerItem(20, 344, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.left_body_layout.addWidget(self.frame)


        self.horizontalLayout_10.addWidget(self.left_body_container)

        self.main_body = QWidget(self.main_widget)
        self.main_body.setObjectName(u"main_body")
        sizePolicy6 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy6)
        self.main_body_layout = QHBoxLayout(self.main_body)
        self.main_body_layout.setSpacing(0)
        self.main_body_layout.setObjectName(u"main_body_layout")
        self.main_body_layout.setContentsMargins(0, 0, 0, 0)
        self.customStackedWidget = QCustomStackedWidget(self.main_body)
        self.customStackedWidget.setObjectName(u"customStackedWidget")
        self.startPage = QWidget()
        self.startPage.setObjectName(u"startPage")
        self.verticalLayout_6 = QVBoxLayout(self.startPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, 7, -1)
        self.label = QLabel(self.startPage)
        self.label.setObjectName(u"label")
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setPointSize(16)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"background-color: rgb(98, 160, 234);\n"
"color: white;\n"
"padding: 5px;\n"
"border-width: 2px;")

        self.verticalLayout_6.addWidget(self.label, 0, Qt.AlignTop)

        self.pushButton = QPushButton(self.startPage)
        self.pushButton.setObjectName(u"pushButton")
        font4 = QFont()
        font4.setFamily(u"Manjari")
        self.pushButton.setFont(font4)
        self.pushButton.setStyleSheet("""
            QPushButton {
                background-color: rgb(222, 221, 218);
                border-style: outset;
                border-width: 2px;
                border-color: rgb(119, 118, 123);
                padding-top: 8px;
                padding-bottom: 4px;
                padding-left: 25px;
                padding-right: 25px;
            }
            QPushButton:hover {
                background-color: rgb(180, 180, 180);
            }
        """)

        self.verticalLayout_6.addWidget(self.pushButton, 0, Qt.AlignRight)

        self.customStackedWidget.addWidget(self.startPage)
        self.Simulation = QWidget()
        self.Simulation.setObjectName(u"Simulation")
        self.verticalLayout_5 = QVBoxLayout(self.Simulation)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.Simulation)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)

        self.verticalLayout_5.addWidget(self.label_2, 0, Qt.AlignTop)

        self.customStackedWidget.addWidget(self.Simulation)

        self.main_body_layout.addWidget(self.customStackedWidget)


        self.horizontalLayout_10.addWidget(self.main_body)


        self.verticalLayout.addWidget(self.main_widget)


        self.horizontalLayout_8.addLayout(self.verticalLayout)

        DyLo.setCentralWidget(self.centralwidget)

        self.retranslateUi(DyLo)

        self.customStackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DyLo)
    # setupUi

    def retranslateUi(self, DyLo):
        DyLo.setWindowTitle(QCoreApplication.translate("DyLo", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("DyLo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#ffffff;\">Nav2 Setup Assistant</span></p></body></html>", None))
        self.minimize.setText("")
        self.maximize.setText("")
        self.close.setText("")
        self.start_b.setText(QCoreApplication.translate("DyLo", u"  Start", None))
        self.sim_b.setText(QCoreApplication.translate("DyLo", u"  Simulation", None))
        self.ros_control_b.setText(QCoreApplication.translate("DyLo", u"  ROS2 Control", None))
        self.config_file_b.setText(QCoreApplication.translate("DyLo", u"  Configuration files  ", None))
        self.help_b.setText(QCoreApplication.translate("DyLo", u"  Help", None))
        self.label.setText(QCoreApplication.translate("DyLo", u"Welcome to Nav2 Setup Assistant", None))
        self.pushButton.setText(QCoreApplication.translate("DyLo", u"Load Files", None))
        self.label_2.setText(QCoreApplication.translate("DyLo", u"Simulations", None))
    # retranslateUi

