import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView

from bd.interaction_bd import data_acquisition


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        self.refreshButton.clicked.connect(self.data_display)
        
        self.data_display()
    
    def data_display(self):
        data = data_acquisition()
        
        self.tableWidget.setRowCount(len(data))
        for row, item_data in enumerate(data):
            for column, cell in enumerate(item_data):
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(cell)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    main_window = MainWindow()
    main_window.show()
    
    sys.exit(app.exec())
