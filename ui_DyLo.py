# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fros_loadergnSHZz.ui'
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
        DyLo.resize(1070, 716)
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


        self.verticalLayout.addWidget(self.top_bar_widget)

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
        self.start_b.setStyleSheet(u"QPushButton {\n"
"	color: rgb(154, 153, 150);\n"
"	font: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(98, 160, 234);\n"
"	color: white;\n"
"}")
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
        self.sim_b.setStyleSheet(u"QPushButton {\n"
"	color: rgb(154, 153, 150);\n"
"	font: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(98, 160, 234);\n"
"	color: white;\n"
"}")

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
        self.ros_control_b.setStyleSheet(u"QPushButton {\n"
"	color: rgb(154, 153, 150);\n"
"	font: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(98, 160, 234);\n"
"	color: white;\n"
"}")

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
        self.config_file_b.setStyleSheet(u"QPushButton {\n"
"	color: rgb(154, 153, 150);\n"
"	font: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(98, 160, 234);\n"
"	color: white;\n"
"}")

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
        self.help_b.setStyleSheet(u"QPushButton {\n"
"	color: rgb(154, 153, 150);\n"
"	font: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(98, 160, 234);\n"
"	color: white;\n"
"}")

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

        self.widget = QWidget(self.startPage)
        self.widget.setObjectName(u"widget")
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy7.setHorizontalStretch(10)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy7)
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(-1, -1, 0, -1)
        self.nav2_logo_frame = QFrame(self.widget)
        self.nav2_logo_frame.setObjectName(u"nav2_logo_frame")
        self.nav2_logo_frame.setStyleSheet(u".QFrame {\n"
"	border: none\n"
"}")
        self.nav2_logo_frame.setFrameShape(QFrame.StyledPanel)
        self.nav2_logo_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.nav2_logo_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.gridLayout.addWidget(self.nav2_logo_frame, 0, 2, 1, 1, Qt.AlignRight)

        self.main_content = QWidget(self.widget)
        self.main_content.setObjectName(u"main_content")
        sizePolicy6.setHeightForWidth(self.main_content.sizePolicy().hasHeightForWidth())
        self.main_content.setSizePolicy(sizePolicy6)
        self.main_content.setAcceptDrops(False)
        self.main_content.setStyleSheet(u"margin-bottom: 10px;\n"
"margin-left: 0px;")
        self.verticalLayout_11 = QVBoxLayout(self.main_content)
        self.verticalLayout_11.setSpacing(9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.workspace_frame = QFrame(self.main_content)
        self.workspace_frame.setObjectName(u"workspace_frame")
        self.workspace_frame.setStyleSheet(u".QFrame {\n"
"	border: 1.5px solid rgb(192, 191, 188);\n"
"}")
        self.workspace_frame.setFrameShape(QFrame.StyledPanel)
        self.workspace_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.workspace_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_5 = QLabel(self.workspace_frame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setMinimumSize(QSize(0, 0))
        font4 = QFont()
        font4.setFamily(u"Ubuntu")
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"background-color: rgb(222, 221, 218);\n"
"padding-top: 3px;\n"
"padding-bottom: 3px;\n"
"border-radius: 4px;")

        self.verticalLayout_8.addWidget(self.label_5, 0, Qt.AlignVCenter)

        self.widget_2 = QWidget(self.workspace_frame)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy3.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy3)
        self.widget_2.setStyleSheet(u".QWidget {\n"
"	border: 1.5px solid rgb(192, 191, 188);\n"
"	border-radius: 6px;\n"
"}")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lineEdit = QLineEdit(self.widget_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 27))
        self.lineEdit.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"background-color: white;\n"
"height: 26;")

        self.horizontalLayout_7.addWidget(self.lineEdit)

        self.browse_b = QPushButton(self.widget_2)
        self.browse_b.setObjectName(u"browse_b")
        font5 = QFont()
        font5.setFamily(u"Manjari")
        self.browse_b.setFont(font5)
        self.browse_b.setStyleSheet(u"QPushButton{\n"
"	padding-top: 5px;\n"
"	padding-bottom: 5px;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color: rgb(222, 221, 218);\n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border-color: rgb(119, 118, 123);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(180, 180, 180);\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_7.addWidget(self.browse_b, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_8.addWidget(self.widget_2)


        self.verticalLayout_11.addWidget(self.workspace_frame)

        self.frame_5 = QFrame(self.main_content)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        font6 = QFont()
        font6.setFamily(u"Ubuntu")
        self.frame_5.setFont(font6)
        self.frame_5.setStyleSheet(u".QFrame {\n"
"	border: 1.5px solid rgb(192, 191, 188);\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"background-color: rgb(222, 221, 218);\n"
"padding-top: 3px;\n"
"padding-bottom: 3px;\n"
"border-radius: 4px;")

        self.verticalLayout_9.addWidget(self.label_6, 0, Qt.AlignVCenter)

        self.package_name = QLineEdit(self.frame_5)
        self.package_name.setObjectName(u"package_name")
        sizePolicy5.setHeightForWidth(self.package_name.sizePolicy().hasHeightForWidth())
        self.package_name.setSizePolicy(sizePolicy5)
        self.package_name.setMinimumSize(QSize(0, 27))
        self.package_name.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"background-color: white;\n"
"height: 27px;")

        self.verticalLayout_9.addWidget(self.package_name)

        self.separator_package_build_type = QWidget(self.frame_5)
        self.separator_package_build_type.setObjectName(u"separator_package_build_type")
        sizePolicy3.setHeightForWidth(self.separator_package_build_type.sizePolicy().hasHeightForWidth())
        self.separator_package_build_type.setSizePolicy(sizePolicy3)
        self.verticalLayout_10 = QVBoxLayout(self.separator_package_build_type)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalSpacer_2 = QSpacerItem(28, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)


        self.verticalLayout_9.addWidget(self.separator_package_build_type)

        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"background-color: rgb(222, 221, 218);\n"
"padding-top: 3px;\n"
"padding-bottom: 3px;\n"
"border-radius: 4px;")

        self.verticalLayout_9.addWidget(self.label_7)

        self.listWidget = QListWidget(self.frame_5)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy3.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy3)
        self.listWidget.setMinimumSize(QSize(0, 10))
        self.listWidget.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"background-color: white;")
        self.listWidget.setFrameShape(QFrame.WinPanel)
        self.listWidget.setAlternatingRowColors(False)
        self.listWidget.setLayoutMode(QListView.SinglePass)
        self.listWidget.setViewMode(QListView.ListMode)
        self.listWidget.setModelColumn(0)
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setSelectionRectVisible(True)

        self.verticalLayout_9.addWidget(self.listWidget)

        self.create_b = QPushButton(self.frame_5)
        self.create_b.setObjectName(u"create_b")
        font7 = QFont()
        font7.setFamily(u"Manjari")
        font7.setPointSize(13)
        self.create_b.setFont(font7)
        self.create_b.setStyleSheet(u"QPushButton{\n"
"	padding-top: 5px;\n"
"	padding-bottom: 5px;\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	background-color: rgb(222, 221, 218);\n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border-color: rgb(119, 118, 123);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(180, 180, 180);\n"
"}\n"
"\n"
"\n"
"")

        self.verticalLayout_9.addWidget(self.create_b, 0, Qt.AlignLeft)


        self.verticalLayout_11.addWidget(self.frame_5)

        self.frame_5.raise_()
        self.workspace_frame.raise_()

        self.gridLayout.addWidget(self.main_content, 0, 1, 1, 1, Qt.AlignTop)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout_6.addWidget(self.widget)

        self.pushButton = QPushButton(self.startPage)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font5)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(222, 221, 218);\n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border-color: rgb(119, 118, 123);\n"
"	padding-top: 8px;\n"
"	padding-bottom: 4px;\n"
"	padding-left: 25px;\n"
"	padding-right: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(180, 180, 180);\n"
"}")

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
        self.listWidget.setCurrentRow(-1)


        QMetaObject.connectSlotsByName(DyLo)
    # setupUi

    def retranslateUi(self, DyLo):
        DyLo.setWindowTitle(QCoreApplication.translate("DyLo", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("DyLo", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#ffffff;\">FROS Loader</span></p></body></html>", None))
        self.minimize.setText("")
        self.maximize.setText("")
        self.close.setText("")
        self.start_b.setText(QCoreApplication.translate("DyLo", u"  Start", None))
        self.sim_b.setText(QCoreApplication.translate("DyLo", u"  Simulation", None))
        self.ros_control_b.setText(QCoreApplication.translate("DyLo", u"  ROS2 Control", None))
        self.config_file_b.setText(QCoreApplication.translate("DyLo", u"  Configuration files  ", None))
        self.help_b.setText(QCoreApplication.translate("DyLo", u"  Help", None))
        self.label.setText(QCoreApplication.translate("DyLo", u"Welcome to FROS Loader", None))
        self.label_5.setText(QCoreApplication.translate("DyLo", u"Select your Workspace", None))
        self.browse_b.setText(QCoreApplication.translate("DyLo", u"Browse", None))
        self.label_6.setText(QCoreApplication.translate("DyLo", u"Create a Package", None))
        self.package_name.setText("")
        self.label_7.setText(QCoreApplication.translate("DyLo", u"Select Build Type", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("DyLo", u"ament_cmake", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("DyLo", u"ament_python", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.create_b.setText(QCoreApplication.translate("DyLo", u"Create", None))
        self.pushButton.setText(QCoreApplication.translate("DyLo", u"Load Files", None))
        self.label_2.setText(QCoreApplication.translate("DyLo", u"Simulations", None))
    # retranslateUi

