# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qttest.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import hashlib

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(552, 404)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(29, 18, 391, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(450, 80, 77, 83))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget1)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.widget2 = QtWidgets.QWidget(Form)
        self.widget2.setGeometry(QtCore.QRect(31, 300, 391, 22))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.widget3 = QtWidgets.QWidget(Form)
        self.widget3.setGeometry(QtCore.QRect(31, 50, 391, 222))
        self.widget3.setObjectName("widget3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.comboBox = QtWidgets.QComboBox(self.widget3)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        # self.comboBox.currentIndexChanged.connect(self.onComboBoxChanged)

        self.horizontalLayout_3.addWidget(self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        # self.comboBox_2.currentIndexChanged.connect(self.onComboBox2Changed)
        self.horizontalLayout_3.addWidget(self.comboBox_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tableWidget = QtWidgets.QTableWidget(self.widget3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "主KEY:"))
        self.pushButton.setText(_translate("Form", "增加資料"))
        self.pushButton_2.setText(_translate("Form", "減少資料"))
        self.pushButton_3.setText(_translate("Form", "轉換"))
        self.label_2.setText(_translate("Form", "結果 :"))
        self.comboBox.setItemText(0, _translate("Form", "Cloud pay"))
        self.comboBox.setItemText(1, _translate("Form", "Spay"))
        self.comboBox_2.setItemText(0, _translate("Form", "TEST"))
        self.comboBox_2.setItemText(1, _translate("Form", "UAT"))
        self.comboBox_2.setItemText(2, _translate("Form", "PROD"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "key"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "value"))
        
    
    # def onComboBoxChanged(self):
    #     print(self.comboBox.currentText())

    # def onComboBox2Changed(self):
    #     print(self.comboBox_2.currentText())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()


    arr = []
    strdict = {}
    project =''
    env =''
    cluodpay_list = ['merchantNo','identifiedCode','merchantOrderNo','notifyUrl','amount']
    spay_list = ['userNo','orderNo','amount']

    # 增加資料
    def add():
        print('add_btn')
        rowPosition = ui.tableWidget.rowCount()
        ui.tableWidget.insertRow(rowPosition)

    def delete():
        print('delete')
        # 刪除當前所選欄位
        # rowIndex = ui.tableWidget.currentRow()
        # ui.tableWidget.removeRow(rowIndex)

        # 刪除最後一欄位
        rowPosition = ui.tableWidget.rowCount()
        ui.tableWidget.removeRow(rowPosition-1)

    # 轉換
    def srech_value():
        try:
            global arr
            global strdict
            i = ui.tableWidget.rowCount()
            for i in range(i) :
                key = ui.tableWidget.item(i,0).text()
                value = ui.tableWidget.item(i,1).text()
                strdict[key] = value 

            sortDict = sorted(strdict.items())
            # print(sortDict)
            for item in sortDict:
                arr.append(item[0])
                arr.append('=')
                arr.append(item[1])
                arr.append('&')
            # print(arr)

            # 主key
            mainkey = ui.lineEdit.text()
            ans = ''.join(arr).replace(' ','')[:-1]
            print(ans)

            finalAns = f'{ans}&key={mainkey}'
            print(finalAns)

            turn_md5 = hashlib.md5(finalAns.encode('utf-8')).hexdigest().upper() 
            print(turn_md5)

            ui.lineEdit_2.setText(turn_md5)
            arr.clear()
        except:
            mbox = QtWidgets.QMessageBox(Form)  
            mbox.information(Form, 'info', 'Value 沒填入')
            print('error')

    def onComboBoxChanged():
        global project
        project = ui.comboBox.currentText()
        print(project)
        if project == 'Cloud pay':
            ui.tableWidget.setRowCount(0)
            for i in range(5):
                # rowPosition = ui.tableWidget.rowCount()
                ui.tableWidget.insertRow(i)
                ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(cluodpay_list[i]))
                
        elif project == 'Spay':
            ui.tableWidget.setRowCount(0)
            for i in range(3):
                # rowPosition = ui.tableWidget.rowCount()
                ui.tableWidget.insertRow(i)
                ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(spay_list[i]))
        else:
            return
        
        

    def onComboBox2Changed():
        global env
        env = ui.comboBox_2.currentText()
        print(env)

    # 監聽當combobox改變執行方法
    ui.comboBox.currentIndexChanged.connect(onComboBoxChanged)
    ui.comboBox_2.currentIndexChanged.connect(onComboBox2Changed)

    # 案扭動作
    ui.pushButton.clicked.connect(add)
    ui.pushButton_2.clicked.connect(delete)
    ui.pushButton_3.clicked.connect(srech_value)



    sys.exit(app.exec_())
