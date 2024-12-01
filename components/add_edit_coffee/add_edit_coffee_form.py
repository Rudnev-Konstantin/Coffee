from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
import sys

from bd.interaction_bd import add_data, data_acquisition


class AddEditForm(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("components/add_edit_coffee/addEditCoffeeForm.ui", self)
        self.id_title_LineEdit.setFocus()
        
        self.add_edit_CheckBox.stateChanged.connect(self.switching_modes)
        self.switching_modes()
        
        self.find_PushButton.clicked.connect(self.search_coffee)
    
    def switching_modes(self):
        if self.add_edit_CheckBox.isChecked():
            self.find_PushButton.hide()
            self.add_edit_CheckBox.setText("Добавить")
            
            self.variety_name.setText("название сорта")
            self.roast_level.setText("степень обжарки")
            self.grind_type.setText("молотый/в зернах")
            self.taste_description.setPlainText("Описание вкуса...")
            self.price.setText("цена")
            self.package_volume.setText("объем упаковки")
            
            self.id_title_LineEdit.setText("id / Название")
        else:
            self.find_PushButton.show()
            self.add_edit_CheckBox.setText("Изменить")
            
            self.id_title_LineEdit.setText("id / Название")
    
    def search_coffee(self):
        coffee_data = data_acquisition(self.id_title_LineEdit.text())
        
        if not coffee_data:
            QMessageBox.warning(self, "Не удалось найти", "Не удалось найти id или название кофе.")
            self.id_title_LineEdit.setText("id / Название")
            return
        
        data_line_edit = [self.variety_name, self.roast_level, self.grind_type,
                          self.taste_description, self.price, self.package_volume]
        for i, coffee_item in enumerate(coffee_data[1:]):
            data_line_edit[i].setText(str(coffee_item))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = AddEditForm()
    window.show()
    
    sys.exit(app.exec())
