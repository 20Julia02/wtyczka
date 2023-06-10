# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQGIS_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PyQGISDialogBase(object):
    def setupUi(self, PyQGISDialogBase):
        PyQGISDialogBase.setObjectName("PyQGISDialogBase")
        PyQGISDialogBase.resize(563, 437)
        self.zakladki = QtWidgets.QTabWidget(PyQGISDialogBase)
        self.zakladki.setGeometry(QtCore.QRect(10, 10, 541, 431))
        self.zakladki.setObjectName("zakladki")
        self.tab_height_area = QtWidgets.QWidget()
        self.tab_height_area.setObjectName("tab_height_area")
        self.layer_text_label = QtWidgets.QLabel(self.tab_height_area)
        self.layer_text_label.setGeometry(QtCore.QRect(20, 0, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.layer_text_label.setFont(font)
        self.layer_text_label.setObjectName("layer_text_label")
        self.layer_MapLayer = QgsMapLayerComboBox(self.tab_height_area)
        self.layer_MapLayer.setGeometry(QtCore.QRect(10, 50, 160, 31))
        self.layer_MapLayer.setObjectName("layer_MapLayer")
        self.area_radioButton = QtWidgets.QRadioButton(self.tab_height_area)
        self.area_radioButton.setGeometry(QtCore.QRect(20, 190, 95, 20))
        self.area_radioButton.setAutoExclusive(True)
        self.area_radioButton.setObjectName("area_radioButton")
        self.height_radioButton = QtWidgets.QRadioButton(self.tab_height_area)
        self.height_radioButton.setGeometry(QtCore.QRect(20, 160, 95, 20))
        self.height_radioButton.setAutoFillBackground(False)
        self.height_radioButton.setAutoExclusive(True)
        self.height_radioButton.setObjectName("height_radioButton")
        self.calculate_Button = QtWidgets.QPushButton(self.tab_height_area)
        self.calculate_Button.setGeometry(QtCore.QRect(420, 300, 93, 28))
        self.calculate_Button.setObjectName("calculate_Button")
        self.napis_final_difference = QtWidgets.QLabel(self.tab_height_area)
        self.napis_final_difference.setGeometry(QtCore.QRect(170, 230, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.napis_final_difference.setFont(font)
        self.napis_final_difference.setObjectName("napis_final_difference")
        self.calculate_napis = QtWidgets.QLabel(self.tab_height_area)
        self.calculate_napis.setGeometry(QtCore.QRect(20, 120, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.calculate_napis.setFont(font)
        self.calculate_napis.setObjectName("calculate_napis")
        self.result_label = QtWidgets.QLabel(self.tab_height_area)
        self.result_label.setGeometry(QtCore.QRect(150, 270, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.result_label.setFont(font)
        self.result_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.result_label.setText("")
        self.result_label.setTextFormat(QtCore.Qt.AutoText)
        self.result_label.setScaledContents(False)
        self.result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.result_label.setObjectName("result_label")
        self.error_napis = QtWidgets.QLabel(self.tab_height_area)
        self.error_napis.setGeometry(QtCore.QRect(169, 315, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.error_napis.setFont(font)
        self.error_napis.setObjectName("error_napis")
        self.errors_label = QtWidgets.QLabel(self.tab_height_area)
        self.errors_label.setGeometry(QtCore.QRect(29, 349, 481, 41))
        self.errors_label.setObjectName("errors_label")
        self.checkBox_poligon = QtWidgets.QCheckBox(self.tab_height_area)
        self.checkBox_poligon.setEnabled(True)
        self.checkBox_poligon.setGeometry(QtCore.QRect(40, 220, 121, 20))
        self.checkBox_poligon.setObjectName("checkBox_poligon")
        self.zakladki.addTab(self.tab_height_area, "")
        self.tab_loadfile = QtWidgets.QWidget()
        self.tab_loadfile.setObjectName("tab_loadfile")
        self.napis_coordinates_system = QtWidgets.QLabel(self.tab_loadfile)
        self.napis_coordinates_system.setGeometry(QtCore.QRect(20, 90, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.napis_coordinates_system.setFont(font)
        self.napis_coordinates_system.setObjectName("napis_coordinates_system")
        self.radioButton_2000 = QtWidgets.QRadioButton(self.tab_loadfile)
        self.radioButton_2000.setGeometry(QtCore.QRect(20, 170, 95, 20))
        self.radioButton_2000.setObjectName("radioButton_2000")
        self.radioButton_1992 = QtWidgets.QRadioButton(self.tab_loadfile)
        self.radioButton_1992.setGeometry(QtCore.QRect(20, 140, 95, 20))
        self.radioButton_1992.setObjectName("radioButton_1992")
        self.sciezka = QgsFileWidget(self.tab_loadfile)
        self.sciezka.setGeometry(QtCore.QRect(120, 40, 381, 27))
        self.sciezka.setObjectName("sciezka")
        self.napis_source = QtWidgets.QLabel(self.tab_loadfile)
        self.napis_source.setGeometry(QtCore.QRect(20, 10, 60, 16))
        self.napis_source.setObjectName("napis_source")
        self.napis_vector_data = QtWidgets.QLabel(self.tab_loadfile)
        self.napis_vector_data.setGeometry(QtCore.QRect(20, 35, 111, 31))
        self.napis_vector_data.setObjectName("napis_vector_data")
        self.groupBox_choose_zone = QtWidgets.QGroupBox(self.tab_loadfile)
        self.groupBox_choose_zone.setGeometry(QtCore.QRect(40, 200, 171, 141))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_choose_zone.setFont(font)
        self.groupBox_choose_zone.setObjectName("groupBox_choose_zone")
        self.checkBox_zone_5 = QtWidgets.QCheckBox(self.groupBox_choose_zone)
        self.checkBox_zone_5.setGeometry(QtCore.QRect(30, 30, 86, 20))
        self.checkBox_zone_5.setObjectName("checkBox_zone_5")
        self.checkBox_zone_6 = QtWidgets.QCheckBox(self.groupBox_choose_zone)
        self.checkBox_zone_6.setGeometry(QtCore.QRect(30, 60, 86, 20))
        self.checkBox_zone_6.setObjectName("checkBox_zone_6")
        self.checkBox_zone_7 = QtWidgets.QCheckBox(self.groupBox_choose_zone)
        self.checkBox_zone_7.setGeometry(QtCore.QRect(30, 90, 86, 20))
        self.checkBox_zone_7.setObjectName("checkBox_zone_7")
        self.checkBox_zone_8 = QtWidgets.QCheckBox(self.groupBox_choose_zone)
        self.checkBox_zone_8.setGeometry(QtCore.QRect(30, 120, 86, 20))
        self.checkBox_zone_8.setObjectName("checkBox_zone_8")
        self.wybor_testowy = QgsProjectionSelectionWidget(self.tab_loadfile)
        self.wybor_testowy.setGeometry(QtCore.QRect(220, 150, 160, 32))
        self.wybor_testowy.setObjectName("wybor_testowy")
        self.pushButton_add_layer = QtWidgets.QPushButton(self.tab_loadfile)
        self.pushButton_add_layer.setGeometry(QtCore.QRect(390, 350, 113, 32))
        self.pushButton_add_layer.setObjectName("pushButton_add_layer")
        self.zakladki.addTab(self.tab_loadfile, "")

        self.retranslateUi(PyQGISDialogBase)
        self.zakladki.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(PyQGISDialogBase)

    def retranslateUi(self, PyQGISDialogBase):
        _translate = QtCore.QCoreApplication.translate
        PyQGISDialogBase.setWindowTitle(_translate("PyQGISDialogBase", "PyQGIS"))
        self.layer_text_label.setText(_translate("PyQGISDialogBase", "Choose layer:"))
        self.area_radioButton.setText(_translate("PyQGISDialogBase", "Area"))
        self.height_radioButton.setText(_translate("PyQGISDialogBase", "Height"))
        self.calculate_Button.setText(_translate("PyQGISDialogBase", "Calculate"))
        self.napis_final_difference.setText(_translate("PyQGISDialogBase", "Result:"))
        self.calculate_napis.setText(_translate("PyQGISDialogBase", "Calculate:"))
        self.error_napis.setText(_translate("PyQGISDialogBase", "Errors:"))
        self.errors_label.setText(_translate("PyQGISDialogBase", "No errors have been detected"))
        self.checkBox_poligon.setText(_translate("PyQGISDialogBase", "Draw poligon"))
        self.zakladki.setTabText(self.zakladki.indexOf(self.tab_height_area), _translate("PyQGISDialogBase", "Height and area"))
        self.napis_coordinates_system.setText(_translate("PyQGISDialogBase", "Choose file coordinate system:"))
        self.radioButton_2000.setText(_translate("PyQGISDialogBase", "PL2000"))
        self.radioButton_1992.setText(_translate("PyQGISDialogBase", "PL1992"))
        self.napis_source.setText(_translate("PyQGISDialogBase", "Source:"))
        self.napis_vector_data.setText(_translate("PyQGISDialogBase", "vector data"))
        self.groupBox_choose_zone.setTitle(_translate("PyQGISDialogBase", "Choose zone"))
        self.checkBox_zone_5.setText(_translate("PyQGISDialogBase", "5"))
        self.checkBox_zone_6.setText(_translate("PyQGISDialogBase", "6"))
        self.checkBox_zone_7.setText(_translate("PyQGISDialogBase", "7"))
        self.checkBox_zone_8.setText(_translate("PyQGISDialogBase", "8"))
        self.pushButton_add_layer.setText(_translate("PyQGISDialogBase", "Add Layer"))
        self.zakladki.setTabText(self.zakladki.indexOf(self.tab_loadfile), _translate("PyQGISDialogBase", "Load file"))
from qgsfilewidget import QgsFileWidget
from qgsmaplayercombobox import QgsMapLayerComboBox
from qgsprojectionselectionwidget import QgsProjectionSelectionWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PyQGISDialogBase = QtWidgets.QDialog()
    ui = Ui_PyQGISDialogBase()
    ui.setupUi(PyQGISDialogBase)
    PyQGISDialogBase.show()
    sys.exit(app.exec_())
