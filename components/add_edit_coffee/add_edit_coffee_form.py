from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QMessageBox, QAbstractButton, QDialogButtonBox
from PyQt6.QtCore import pyqtSlot

from bd.interaction_bd import add_data, edit_data, data_acquisition


class AddEditForm(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("components/add_edit_coffee/addEditCoffeeForm.ui", self)
        
        self.switching_modes()
        
        self.add_edit_CheckBox.stateChanged.connect(self.switching_modes)
        
        self.find_PushButton.clicked.connect(self.search_coffee)
        
        self.buttonBox.clicked.connect(self.on_button_clicked)
    
    @pyqtSlot(QAbstractButton)
    def on_button_clicked(self, button):
        if self.buttonBox.buttonRole(button) == QDialogButtonBox.ButtonRole.AcceptRole:
            self.add_edit_coffee()
    
    def switching_modes(self):
        if self.add_edit_CheckBox.isChecked():
            self.find_PushButton.hide()
            self.id_title_LineEdit.hide()
            self.add_edit_CheckBox.setText("Добавить")
            
            self.variety_name.setText("название сорта")
            self.roast_level.setText("степень обжарки")
            self.grind_type.setText("молотый/в зернах")
            self.taste_description.setPlainText("Описание вкуса...")
            self.price.setText("цена")
            self.package_volume.setText("объем упаковки")
            
            self.id_title_LineEdit.setFocus()
        else:
            self.find_PushButton.show()
            self.id_title_LineEdit.show()
            
            self.add_edit_CheckBox.setText("Изменить")
            
            self.id_title_LineEdit.setText("id / Название")
            
            self.id_title_LineEdit.setFocus()
    
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
    
    def add_edit_coffee(self):
        data_item_coffee = (
            self.variety_name.text(),
            self.roast_level.text(),
            self.grind_type.text(),
            self.taste_description.toPlainText(),
            self.price.text(),
            self.package_volume.text()
        )
        
        if self.add_edit_CheckBox.isChecked():
            add_data(*data_item_coffee)
        else:
            edit_data(self.id_title_LineEdit.text(), *data_item_coffee)
