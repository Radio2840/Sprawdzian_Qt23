import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6.uic.properties import QtGui

from layout import Ui_Dialog


class MyForm(QDialog):
    sum_of_calories = 0
    men_table = [1900, 2200, 2500]
    women_table = [1700, 1900, 2100]
    how_many_percent = 0

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.setWindowTitle("Kalkulaor kalorii")
        self.ui.add_to_list.clicked.connect(self.buton_clicked)

    def buton_clicked(self):
        self.ui.how_many_calories.setText(str(self.sum_of_calories))
        self.add_to_list()
        self.calories_eficiencies()
    def add_to_list(self):
        food_text = self.ui.type_of_food.text()
        food_calories = self.ui.calories_number.value()
        food_with_calories_str = str(food_text)+" "+str(food_calories)
        self.sum_of_calories += food_calories
        self.ui.list_of_food.addItem(food_with_calories_str)
        self.ui.how_many_calories.setText(str(self.sum_of_calories))
    def calories_eficiencies(self):
        is_woman = self.ui.radio_woman.isChecked()
        is_man = self.ui.radio_man.isChecked()
        activity_small = self.ui.radio_small_activity.isChecked()
        activity_medium = self.ui.radio_medium_activity.isChecked()
        activity_hight = self.ui.radio_hight_activity.isChecked()
        activity_tables = [activity_small, activity_medium, activity_hight]
        photo_one = QPixmap("1.jpg")
        photo_two = QPixmap("2.jpg")
        photo_three = QPixmap("3.jpg")
        photo_one = photo_one.scaled(500, 500)
        photo_two = photo_two.scaled(500, 500)
        photo_three = photo_three.scaled(500, 500)


        if is_woman:
            for i in range(3):
                if activity_tables[i]:
                    self.how_many_percent = (self.sum_of_calories*100)/self.women_table[i]
        elif is_man:
            for i in range(3):
                if activity_tables[i]:
                    self.how_many_percent = (self.sum_of_calories*100)/self.men_table[i]
        else:
            pass
        if self.how_many_percent <= 80:
            self.ui.how_many_calories.setStyleSheet("color: rgb(0, 255, 0);")
            self.ui.photo.setPixmap(photo_one)
        elif self.how_many_percent > 80 and self.how_many_percent <= 100:
            self.ui.how_many_calories.setStyleSheet("color: rgb(0, 0, 0);")
            self.ui.photo.setPixmap(photo_two)
        elif self.how_many_percent > 100:
            self.ui.how_many_calories.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.photo.setPixmap(photo_three)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec())