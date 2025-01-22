from ui_DyLo import *
from Custom_Widgets.Widgets import *
import os
import sys

import command_executor as cmd

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
        self.ui.create_b.clicked.connect(self.create_package)
        self.ui.package_name.setPlaceholderText("__enter package name__")
        self.ui.lineEdit.setPlaceholderText("__path of your workspace__")
        self.ui.browse_b.clicked.connect(self.browse_directories)
        self.ui.listWidget.itemClicked.connect(self.selected_build_type)

        self.workspace_path = ""
        self.package_name = ""
        self.build_type = ""

        self.cmd = []
        self.exec = cmd.CommandExecutor()

    def selected_build_type(self, type):
        self.build_type = type.text()

    def browse_directories(self):
        self.workspace_path = QFileDialog.getExistingDirectory(self, "Select a Directory", options=QFileDialog.ShowDirsOnly | QFileDialog.DontUseNativeDialog)
        if self.workspace_path:
            self.ui.lineEdit.setText(self.workspace_path)

    def create_package(self):
        self.package_name = self.ui.package_name.text()
        print(f"workspace path = {self.ui.lineEdit.text()}")
        print(f"package name = {self.package_name}")
        print(f"build type = {self.build_type}")

        path = self.workspace_path + "/src"
        os.makedirs(path, exist_ok=True)

        self.cmd = ["ros2", "pkg", "create", self.package_name, "--build-type", self.build_type]
        res = self.exec.run_command(self.cmd, path)
        print("success = " + str(res["success"]))

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