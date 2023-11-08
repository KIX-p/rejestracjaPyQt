import random
import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.rezerwuj.clicked.connect(self.wyswietl)
        self.show()


    def wyswietl(self):
        if self.ui.radiointernista.isChecked():
            specjalizacja = "internisty"
            if self.ui.checkBox.isChecked():
                iloscdni = random.randint(0, 14)
                cena = 200
            else:
                iloscdni = random.randint(0, 1000)
                cena = 0
        elif self.ui.radiopediatr.isChecked():
            specjalizacja = "pediatra"
            if self.ui.checkBox.isChecked():
                iloscdni = random.randint(0, 14)
                cena = 200
            else:
                iloscdni = random.randint(0, 1000)
                cena = 0
        else:
            specjalizacja = "dermatologa"
            if self.ui.checkBox.isChecked():
                iloscdni = random.randint(0, 14)
                cena = 200
            else:
                iloscdni = random.randint(0, 1000)
                cena = 0
        self.ui.wynik1.setText("Pomyślnie zarezerwowano wizytę u lekarza " + specjalizacja+ "."+ "Termin wizyty przypada za "+ str(iloscdni)+ "dni " + "Koszt wizyty " + str(cena))
if __name__=="__main__":
    app=QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec())