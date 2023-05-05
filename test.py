# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qttest.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import hashlib
import random
import time

import requests
import json


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(950, 404)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(560, 20, 351, 301))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 220, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
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
        self.widget3.setGeometry(QtCore.QRect(32, 50, 391, 222))
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
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_2)
        self.comboBox_3 = QtWidgets.QComboBox(self.widget3)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_3)
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
        self.pushButton_4.setText(_translate("Form", "API Requests"))
        self.label.setText(_translate("Form", "主KEY:"))
        self.pushButton.setText(_translate("Form", "增加資料"))
        self.pushButton_2.setText(_translate("Form", "減少資料"))
        self.pushButton_3.setText(_translate("Form", "取得sign"))
        self.label_2.setText(_translate("Form", "sign :"))
        self.comboBox.setItemText(0, _translate("Form", "Cloud pay"))
        self.comboBox.setItemText(1, _translate("Form", "Spay"))
        self.comboBox_2.setItemText(0, _translate("Form", "TEST"))
        self.comboBox_2.setItemText(1, _translate("Form", "UAT"))
        self.comboBox_2.setItemText(2, _translate("Form", "PROD"))
        self.comboBox_3.setItemText(0, _translate("Form", "玩家提現(無回調)"))
        self.comboBox_3.setItemText(1, _translate("Form", "玩家提現(回調)"))
        self.comboBox_3.setItemText(2, _translate("Form", "玩家充值(获取在线支付地址)"))
        self.comboBox_3.setItemText(3, _translate("Form", "订单查询"))
        self.comboBox_3.setItemText(4, _translate("Form", "提现订单查询"))
        self.comboBox_3.setItemText(5, _translate("Form", "商户访客获取令牌"))
        self.comboBox_3.setItemText(6, _translate("Form", "商户端访客充值"))
        self.comboBox_3.setItemText(7, _translate("Form", "商户端访客验证后充值"))
        self.comboBox_3.setItemText(8, _translate("Form", "商户端访客余额查询"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "key"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "value"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()


    
    action_list=[
        {'action_name':'玩家提現(無回調)','item_number':4,'value':['merchantNo','merchantOrderNo','amount','userMobile'],'web_action':'post','api':'/api/partner/orders'},
        {'action_name':'玩家提現(回調)','item_number':5,'value':['merchantNo','merchantOrderNo','amount','userMobile','notifyUrl'],'web_action':'post','api':'/api/partner/orders-withNotify'},
        {'action_name':'玩家充值(获取在线支付地址)','item_number':4,'value':['merchantNo','merchantOrderNo','notifyUrl','amount'],'web_action':'post','api':'/api/partner/online-pay'}, 
        {'action_name':'订单查询','item_number':2,'value':['merchantOrderNo','merchantNo'],'web_action':'get','api':'/api/partner/orders-recharge'},
        {'action_name':'提现订单查询','item_number':2,'value':['merchantOrderNo','merchantNo'],'web_action':'get','api':'/api/partner/orders-withdraw'},
        {'action_name':'商户访客获取令牌','item_number':2,'value':['merchantNo','identifiedCode'],'web_action':'post','api':'/api/partner/visitor/token'},
        {'action_name':'商户端访客充值','item_number':5,'value':['merchantNo','identifiedCode','merchantOrderNo','notifyUrl','amount'],'web_action':'post','api':'/api/partner/visitor/online-pay'},
        {'action_name':'商户端访客验证后充值','item_number':5,'value':['merchantNo','identifiedCode','merchantOrderNo','notifyUrl','amount'],'web_action':'post','api':'/api/partner/visitor/online-pay/validated'},
        {'action_name':'商户端访客余额查询','item_number':2,'value':['merchantNo','identifiedCode'],'web_action':'get','api':'/api/partner/visitor/userInfo'},
                 ]
    
    env_list=[{'test':'http://api.cloudpayPartner.tyche'},{'uat':'https://partner.uat888.com/'}]

    

    arr = []
    strdict = {}
    mainkey = ''
    action ='玩家提現(無回調)'
    envstr ='TEST'
    envurl ='http://api.cloudpayPartner.tyche'
    timestamp = ''
    sign = ''
    api_method='post'
    finalAns= ''
    

    

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

    def remove_data():
            global arr
            global strdict
            global sign
            global mainkey
            global finalAns
            finalAns =''
            strdict ={}
            arr.clear()
            sign=''
            mainkey =''
            ui.textBrowser.clear()


    # 轉換
    def srech_value():
        try:
            global arr
            global strdict
            global sign
            global mainkey
            
            arr.clear()
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
            # print(f'字元{arr}')

            # 主key
            mainkey = ui.lineEdit.text()
            ans = ''.join(arr).replace(' ','')[:-1]
            # print(ans)

            finalAns = f'{ans}&key={mainkey}'
            print(f'組合字串:{finalAns}')

            sign = hashlib.md5(finalAns.encode('utf-8')).hexdigest().upper() 
            print(f'sign:{sign}')

            ui.lineEdit_2.setText(sign)
            # 清空
            # finalAns =''
            strdict ={}
            arr.clear()
        except:
            mbox = QtWidgets.QMessageBox(Form)  
            mbox.information(Form, 'info', 'Value 沒填入')
            print('error')

    # action
    def onComboBoxChanged():
        global action
        global arr
        global timestamp
        global sign
        global mainkey
        global api_method
        merchantNo = 'MSN2023042416823040844899JzZXEte'
        action = ui.comboBox_3.currentText()
        print(action)

        # 玩家提現(無回調)
        if action == action_list[0]['action_name']:
            remove_data()
            ui.lineEdit.setText('')
            print(f'sign:{sign}')
            ui.lineEdit_2.setText('')
            timestamp = int(time.time())
            amount = random.randrange(10, 101)*10
            print(f'merchantOrderNo:{timestamp}')
            # 取得GET還是POST
            api_method = action_list[0]['web_action']
            print(f'api_method={api_method}')
            ui.tableWidget.setRowCount(0)
            for i in range(action_list[0]['item_number']):
                # rowPosition = ui.tableWidget.rowCount()
                ui.tableWidget.insertRow(i)
                ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(action_list[0]['value'][i]))
            ui.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(f'{merchantNo}'))
            ui.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(f'{timestamp}'))
            ui.tableWidget.setItem(2, 1, QtWidgets.QTableWidgetItem(f'{amount}'))
            
        
        # 玩家提現(回調)
        elif action == action_list[1]['action_name']:
            remove_data()
            ui.lineEdit.setText('')
            print(f'sign:{sign}')
            ui.lineEdit_2.setText('')
            timestamp = int(time.time())
            notifyUrl = 'https://timer.uat888.com/'
            amount = random.randrange(10, 101)*10
            print(f'merchantOrderNo:{timestamp}')
            # 取得GET還是POST
            api_method = action_list[1]['web_action']
            print(f'api_method={api_method}')
            ui.tableWidget.setRowCount(0)
            for i in range(action_list[1]['item_number']):
                # rowPosition = ui.tableWidget.rowCount()
                ui.tableWidget.insertRow(i)
                ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(action_list[1]['value'][i]))
            ui.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(f'{merchantNo}'))
            ui.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(f'{timestamp}'))
            ui.tableWidget.setItem(2, 1, QtWidgets.QTableWidgetItem(f'{amount}'))
            ui.tableWidget.setItem(4, 1, QtWidgets.QTableWidgetItem(f'{notifyUrl}'))
        
        
        # 玩家充值(获取在线支付地址)
        elif action == action_list[2]['action_name']:
            remove_data()
            ui.lineEdit.setText('')
            ui.lineEdit_2.setText('')
            timestamp = int(time.time())
            amount = random.randrange(10, 101)*10
            notifyUrl = 'https://timer.uat888.com/'
            print(f'merchantOrderNo:{timestamp}')
            # 取得GET還是POST
            api_method = action_list[2]['web_action']
            print(f'api_method={api_method}')
            ui.tableWidget.setRowCount(0)
            for i in range(action_list[2]['item_number']):
                # rowPosition = ui.tableWidget.rowCount()
                ui.tableWidget.insertRow(i)
                ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(action_list[2]['value'][i]))
            ui.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(f'{merchantNo}'))
            ui.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(f'{timestamp}'))
            ui.tableWidget.setItem(2, 1, QtWidgets.QTableWidgetItem(f'{notifyUrl}'))
            ui.tableWidget.setItem(3, 1, QtWidgets.QTableWidgetItem(f'{amount}'))

        # 订单查询
        elif action == action_list[3]['action_name']:
            remove_data()
            ui.lineEdit.setText('')
            ui.lineEdit_2.setText('')
            timestamp = int(time.time())
            print(f'merchantOrderNo:{timestamp}')
            # 取得GET還是POST
            api_method = action_list[3]['web_action']
            print(f'api_method={api_method}')
            ui.tableWidget.setRowCount(0)
            for i in range(action_list[3]['item_number']):
                # rowPosition = ui.tableWidget.rowCount()
                ui.tableWidget.insertRow(i)
                ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(action_list[3]['value'][i]))
        
        # 提现订单查询
        elif action == action_list[4]['action_name']:
            remove_data()
            ui.lineEdit.setText('')
            ui.lineEdit_2.setText('')
            timestamp = int(time.time())
            print(f'merchantOrderNo:{timestamp}')
            # 取得GET還是POST
            api_method = action_list[4]['web_action']
            print(f'api_method={api_method}')
            ui.tableWidget.setRowCount(0)
            for i in range(action_list[4]['item_number']):
                # rowPosition = ui.tableWidget.rowCount()
                ui.tableWidget.insertRow(i)
                ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(action_list[4]['value'][i]))

        # 商户访客获取令牌
        elif action == action_list[5]['action_name']:
            remove_data()
            ui.lineEdit.setText('')
            ui.lineEdit_2.setText('')
            timestamp = int(time.time())
            identifiedCode = f'IDC{timestamp}'
            print(f'merchantOrderNo:{timestamp}')
            # 取得GET還是POST
            api_method = action_list[5]['web_action']
            print(f'api_method={api_method}')
            ui.tableWidget.setRowCount(0)
            for i in range(action_list[5]['item_number']):
                # rowPosition = ui.tableWidget.rowCount()
                ui.tableWidget.insertRow(i)
                ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(action_list[5]['value'][i]))
            ui.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(f'{merchantNo}'))
            ui.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(f'{identifiedCode}'))

        # 商户端访客充值
        elif action == action_list[6]['action_name']:
            remove_data()
            ui.lineEdit.setText('')
            ui.lineEdit_2.setText('')
            timestamp = int(time.time())
            identifiedCode = f'IDC{timestamp}'
            notifyUrl = 'https://timer.uat888.com/'
            amount = random.randrange(10, 101)*10
            print(f'merchantOrderNo:{timestamp}')
            # 取得GET還是POST
            api_method = action_list[6]['web_action']
            print(f'api_method={api_method}')
            ui.tableWidget.setRowCount(0)
            for i in range(action_list[6]['item_number']):
                # rowPosition = ui.tableWidget.rowCount()
                ui.tableWidget.insertRow(i)
                ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(action_list[6]['value'][i]))
            ui.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(f'{merchantNo}'))
            ui.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(f'{identifiedCode}'))
            ui.tableWidget.setItem(2, 1, QtWidgets.QTableWidgetItem(f'{timestamp}'))
            ui.tableWidget.setItem(3, 1, QtWidgets.QTableWidgetItem(f'{notifyUrl}'))
            ui.tableWidget.setItem(4, 1, QtWidgets.QTableWidgetItem(f'{amount}'))

        # 商户端访客验证后充值
        elif action == action_list[7]['action_name']:
            remove_data()
            ui.lineEdit.setText('')
            ui.lineEdit_2.setText('')
            timestamp = int(time.time())
            amount = random.randrange(10, 101)*10
            identifiedCode = f'IDC{timestamp}'
            notifyUrl = 'https://timer.uat888.com/'
            print(f'merchantOrderNo:{timestamp}')
            # 取得GET還是POST
            api_method = action_list[7]['web_action']
            print(f'api_method={api_method}')
            ui.tableWidget.setRowCount(0)
            for i in range(action_list[7]['item_number']):
                # rowPosition = ui.tableWidget.rowCount()
                ui.tableWidget.insertRow(i)
                ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(action_list[7]['value'][i]))
            ui.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(f'{merchantNo}'))
            ui.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(f'{identifiedCode}'))
            ui.tableWidget.setItem(2, 1, QtWidgets.QTableWidgetItem(f'{timestamp}'))
            ui.tableWidget.setItem(3, 1, QtWidgets.QTableWidgetItem(f'{notifyUrl}'))
            ui.tableWidget.setItem(4, 1, QtWidgets.QTableWidgetItem(f'{amount}'))

        # 商户端访客余额查询
        elif action == action_list[8]['action_name']:
            remove_data()
            ui.lineEdit.setText('')
            ui.lineEdit_2.setText('')
            timestamp = int(time.time())
            identifiedCode = f'IDC{timestamp}'
            amount = random.randrange(10, 101)*10
            print(f'merchantOrderNo:{timestamp}')
            # 取得GET還是POST
            api_method = action_list[8]['web_action']
            print(f'api_method={api_method}')
            ui.tableWidget.setRowCount(0)
            for i in range(action_list[8]['item_number']):
                # rowPosition = ui.tableWidget.rowCount()
                ui.tableWidget.insertRow(i)
                ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(action_list[8]['value'][i]))
            ui.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(f'{merchantNo}'))
            ui.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(f'{identifiedCode}'))
        else:
            return
        
        
    # env
    def onComboBox2Changed():
        global envstr
        global envurl
        envstr = ui.comboBox_2.currentText()
        # print(envstr)
        if envstr == 'TEST':
            envurl = env_list[0]['test']
            print(envurl)
        elif envstr == 'UAT':
            envurl = env_list[1]['uat']
            print(envurl)
        else:
            print('err')

    
    def send_api():
        global envurl
        global sign
        send_api_dict={}
        i = ui.tableWidget.rowCount()
        for i in range(i) :
                key = ui.tableWidget.item(i,0).text()
                value = ui.tableWidget.item(i,1).text()
                send_api_dict[key] = value
        api_sign = ui.lineEdit_2.text()
        send_api_dict["sign"] = api_sign
        print(f'send_api:{send_api_dict}')

       
        json_data = json.dumps(send_api_dict)
        print(json_data)
        headers = {'Content-Type': 'application/json'}

        if action == action_list[0]['action_name']:
            api_url = action_list[0]["api"]
            print(f'action={action}')
        elif action == action_list[1]['action_name']:
            api_url = action_list[1]["api"]
            print(f'action={action}')
        elif action == action_list[2]['action_name']:
            api_url = action_list[2]["api"]
            print(f'action={action}')
        elif action == action_list[3]['action_name']:
            api_url = action_list[3]["api"]
            print(f'action={action}')
        elif action == action_list[4]['action_name']:
            api_url = action_list[4]["api"]
            print(f'action={action}')
        elif action == action_list[5]['action_name']:
            api_url = action_list[5]["api"]
            print(f'action={action}')
        elif action == action_list[6]['action_name']:
            api_url = action_list[6]["api"]
            print(f'action={action}')
        elif action == action_list[7]['action_name']:
            api_url = action_list[7]["api"]
            print(f'action={action}')
        else:
            api_url = action_list[8]["api"]
        # print(api_url)
        print(f"{envurl}{api_url}")
        url = f"{envurl}{api_url}"

        # 判斷用post還是get
        if api_method == 'post':
            r = requests.post(url,data=json_data,headers=headers)
            print("POST")
            api_response = r.json()
            ui.textBrowser.insertPlainText(f'{api_response}')
        elif api_method == 'get':
            payload = send_api_dict
            r = requests.get(url,params=payload)
            print("GET")
            api_response = r.json()
            ui.textBrowser.insertPlainText(f'{api_response}')
        else:
            print('not have api method !!')
        
        # print(api_response)
    
    # 開啟後預設值
    timestamp = int(time.time())
    merchantNo = 'MSN2023042416823040844899JzZXEte'
    amount = random.randrange(10, 101)*10
    for i in range(4):
                # rowPosition = ui.tableWidget.rowCount()
                ui.tableWidget.insertRow(i)
                ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(action_list[0]['value'][i]))
    ui.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(f'{merchantNo}'))
    ui.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(f'{timestamp}'))
    ui.tableWidget.setItem(2, 1, QtWidgets.QTableWidgetItem(f'{amount}'))

    # 監聽當combobox改變執行方法
    ui.comboBox_3.currentIndexChanged.connect(onComboBoxChanged)
    ui.comboBox_2.currentIndexChanged.connect(onComboBox2Changed)

    # 案扭動作
    ui.pushButton.clicked.connect(add) 
    ui.pushButton_2.clicked.connect(delete)
    ui.pushButton_3.clicked.connect(srech_value)
    ui.pushButton_4.clicked.connect(send_api)



    sys.exit(app.exec_())
