from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6.QtCore import QTimer
import sys


class AddEditForm(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("components/add_edit_coffee/addEditCoffeeForm.ui", self)
        self.id_title_LineEdit.setFocus()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = AddEditForm()
    window.show()
    
    sys.exit(app.exec())
