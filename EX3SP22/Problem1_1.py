# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Problem1.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(842, 691)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gb_Input = QtWidgets.QGroupBox(Form)
        self.gb_Input.setObjectName("gb_Input")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gb_Input)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.layout_GridInput = QtWidgets.QGridLayout()
        self.layout_GridInput.setObjectName("layout_GridInput")
        self.label_Frequency = QtWidgets.QLabel(self.gb_Input)
        self.label_Frequency.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Frequency.setObjectName("label_Frequency")
        self.layout_GridInput.addWidget(self.label_Frequency, 4, 0, 1, 1)
        self.LE_Magnitude = QtWidgets.QLineEdit(self.gb_Input)
        self.LE_Magnitude.setObjectName("LE_Magnitude")
        self.layout_GridInput.addWidget(self.LE_Magnitude, 3, 1, 1, 1)
        self.label_Magnitude = QtWidgets.QLabel(self.gb_Input)
        self.label_Magnitude.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Magnitude.setObjectName("label_Magnitude")
        self.layout_GridInput.addWidget(self.label_Magnitude, 3, 0, 1, 1)
        self.LE_L = QtWidgets.QLineEdit(self.gb_Input)
        self.LE_L.setObjectName("LE_L")
        self.layout_GridInput.addWidget(self.LE_L, 0, 1, 1, 1)
        self.LE_Phase = QtWidgets.QLineEdit(self.gb_Input)
        self.LE_Phase.setObjectName("LE_Phase")
        self.layout_GridInput.addWidget(self.LE_Phase, 5, 1, 1, 1)
        self.label_Phase = QtWidgets.QLabel(self.gb_Input)
        self.label_Phase.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Phase.setObjectName("label_Phase")
        self.layout_GridInput.addWidget(self.label_Phase, 5, 0, 1, 1)
        self.LE_R = QtWidgets.QLineEdit(self.gb_Input)
        self.LE_R.setObjectName("LE_R")
        self.layout_GridInput.addWidget(self.LE_R, 1, 1, 1, 1)
        self.label_R = QtWidgets.QLabel(self.gb_Input)
        self.label_R.setAlignment(QtCore.Qt.AlignCenter)
        self.label_R.setObjectName("label_R")
        self.layout_GridInput.addWidget(self.label_R, 1, 0, 1, 1)
        self.LE_C = QtWidgets.QLineEdit(self.gb_Input)
        self.LE_C.setObjectName("LE_C")
        self.layout_GridInput.addWidget(self.LE_C, 2, 1, 1, 1)
        self.label_C = QtWidgets.QLabel(self.gb_Input)
        self.label_C.setAlignment(QtCore.Qt.AlignCenter)
        self.label_C.setObjectName("label_C")
        self.layout_GridInput.addWidget(self.label_C, 2, 0, 1, 1)
        self.label_L = QtWidgets.QLabel(self.gb_Input)
        self.label_L.setAlignment(QtCore.Qt.AlignCenter)
        self.label_L.setObjectName("label_L")
        self.layout_GridInput.addWidget(self.label_L, 0, 0, 1, 1)
        self.LE_Frequency = QtWidgets.QLineEdit(self.gb_Input)
        self.LE_Frequency.setObjectName("LE_Frequency")
        self.layout_GridInput.addWidget(self.LE_Frequency, 4, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_GridInput.addItem(spacerItem, 0, 2, 1, 1)
        self.PB_Calculate = QtWidgets.QPushButton(self.gb_Input)
        self.PB_Calculate.setObjectName("PB_Calculate")
        self.layout_GridInput.addWidget(self.PB_Calculate, 6, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.layout_GridInput)
        self.verticalLayout.addWidget(self.gb_Input)

        self.retranslateUi(Form)
        self.PB_Calculate.clicked.connect(Form.Calculate_Click)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.gb_Input.setTitle(_translate("Form", "Input"))
        self.label_Frequency.setText(_translate("Form", "Frequency"))
        self.LE_Magnitude.setText(_translate("Form", "20"))
        self.label_Magnitude.setText(_translate("Form", "Magnitude"))
        self.LE_L.setToolTip(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.LE_L.setText(_translate("Form", "20"))
        self.LE_Phase.setText(_translate("Form", "0"))
        self.label_Phase.setText(_translate("Form", "Phase"))
        self.LE_R.setText(_translate("Form", "10"))
        self.label_R.setText(_translate("Form", "R"))
        self.LE_C.setText(_translate("Form", ".05"))
        self.label_C.setText(_translate("Form", "C"))
        self.label_L.setText(_translate("Form", "L"))
        self.LE_Frequency.setText(_translate("Form", "3.18"))
        self.PB_Calculate.setText(_translate("Form", "Calculate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
