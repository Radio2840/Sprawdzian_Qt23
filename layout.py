# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1147, 799)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 1121, 471))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.calories_number = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.calories_number.setMaximum(1000.99)
        self.calories_number.setSingleStep(100.0)
        self.calories_number.setObjectName("calories_number")
        self.gridLayout.addWidget(self.calories_number, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 85, 0);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.add_to_list = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.add_to_list.setFont(font)
        self.add_to_list.setStyleSheet("background: rgb(0, 255, 0)")
        self.add_to_list.setObjectName("add_to_list")
        self.gridLayout.addWidget(self.add_to_list, 0, 4, 1, 1)
        self.type_of_food = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.type_of_food.setObjectName("type_of_food")
        self.gridLayout.addWidget(self.type_of_food, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 85, 0);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_3.setStyleSheet("background: rgb(54, 204, 12);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)
        self.line = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 4, 0, 1, 5)
        self.how_many_calories = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.how_many_calories.setText("")
        self.how_many_calories.setObjectName("how_many_calories")
        self.gridLayout.addWidget(self.how_many_calories, 2, 2, 1, 3)
        self.photo = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.photo.setText("")
        self.photo.setObjectName("photo")
        self.gridLayout.addWidget(self.photo, 3, 0, 1, 5)
        self.list_of_food = QtWidgets.QListWidget(parent=self.gridLayoutWidget)
        self.list_of_food.setEnabled(False)
        self.list_of_food.setObjectName("list_of_food")
        self.gridLayout.addWidget(self.list_of_food, 1, 0, 1, 4)
        self.radio_woman = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.radio_woman.setObjectName("radio_woman")
        self.gridLayout.addWidget(self.radio_woman, 5, 1, 1, 1)
        self.radio_man = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.radio_man.setObjectName("radio_man")
        self.gridLayout.addWidget(self.radio_man, 5, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(parent=Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 660, 1111, 131))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 500))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 40, 691, 76))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radio_small_activity = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.radio_small_activity.setObjectName("radio_small_activity")
        self.verticalLayout_2.addWidget(self.radio_small_activity)
        self.radio_medium_activity = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.radio_medium_activity.setObjectName("radio_medium_activity")
        self.verticalLayout_2.addWidget(self.radio_medium_activity)
        self.radio_hight_activity = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.radio_hight_activity.setObjectName("radio_hight_activity")
        self.verticalLayout_2.addWidget(self.radio_hight_activity)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Rodzaj posiłku"))
        self.add_to_list.setText(_translate("Dialog", "Dodaj"))
        self.label_2.setText(_translate("Dialog", "Liczba kalorii"))
        self.label_3.setText(_translate("Dialog", "Liczba spożytych kalorii"))
        self.radio_woman.setText(_translate("Dialog", "Kobieta"))
        self.radio_man.setText(_translate("Dialog", "Mężczyzna"))
        self.groupBox.setTitle(_translate("Dialog", "Jaka aktywność fizyczna?"))
        self.radio_small_activity.setText(_translate("Dialog", "Mała aktywność fizyczna"))
        self.radio_medium_activity.setText(_translate("Dialog", "Średnia aktywność fizyczna"))
        self.radio_hight_activity.setText(_translate("Dialog", "Duża aktywność fizyczna"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
