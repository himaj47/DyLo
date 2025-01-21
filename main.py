from ui_DyLo import *
from Custom_Widgets.Widgets import *
import os
import sys

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_DyLo()
        self.ui.setupUi(self)

        loadJsonStyle(self, self.ui)

        self.show()

        self.ui.pushButton.clicked.connect(self.Load)
        self.ui.pushButton.pressed.connect(self.change_style_sheet)
        self.ui.pushButton.released.connect(self.original_style_sheet)

        self.ui.start_b.clicked.connect(self.go_to_start_page)
        self.ui.sim_b.clicked.connect(self.go_to_sim_page)

    def go_to_start_page(self):
        self.ui.customStackedWidget.setCurrentIndex(0)

    def go_to_sim_page(self):
        self.ui.customStackedWidget.setCurrentIndex(1)

    def Load(self):
        print("Loading Files")

    def change_style_sheet(self):
        self.ui.pushButton.setStyleSheet("""
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
                border-color: rgb(180, 180, 180);
            }
        """)

    def original_style_sheet(self):
        self.ui.pushButton.setStyleSheet("""
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

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())