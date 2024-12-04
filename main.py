import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView

from styles.style_main import Ui_MainWindow

from data.interaction_bd import data_acquisition
from components.add_edit_coffee_form import AddEditForm


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        header_names = ["ID", "Название сорта", "Степень обжарки", "Молотый/в зернах", "Описание вкуса",
                        "Цена", "Объем упаковки"]
        self.tableWidget.setHorizontalHeaderLabels(header_names)
        
        self.refreshButton.clicked.connect(self.data_display)
        
        self.data_display()
        
        self.refreshButton.clicked.connect(self.show_dialog_widget)
    
    def data_display(self):
        data = data_acquisition()
        
        self.tableWidget.setRowCount(len(data))
        for row, item_data in enumerate(data):
            for column, cell in enumerate(item_data):
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(cell)))
    
    def show_dialog_widget(self):
        dialog_widget = AddEditForm(self)
        dialog_widget.exec()
        
        self.data_display()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    main_window = MainWindow()
    main_window.show()
    
    sys.exit(app.exec())
