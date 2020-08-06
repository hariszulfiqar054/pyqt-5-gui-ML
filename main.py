

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    selected_algo = 'logistic regression'
    gender = 'Male'
    embark = 'S'
    pClass = '1'
    siblings = '1'

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(767, 831)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.img_label = QtWidgets.QLabel(self.centralwidget)
        self.img_label.setGeometry(QtCore.QRect(0, 0, 951, 441))
        self.img_label.setText("")
        self.img_label.setPixmap(QtGui.QPixmap("titanic.jpg"))
        self.img_label.setObjectName("img_label")
        self.header_label = QtWidgets.QLabel(self.centralwidget)
        self.header_label.setGeometry(QtCore.QRect(270, 450, 261, 17))
        self.header_label.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.header_label.setFont(font)
        self.header_label.setObjectName("header_label")
        self.regression = QtWidgets.QRadioButton(self.centralwidget)
        self.regression.setGeometry(QtCore.QRect(20, 550, 151, 23))
        self.regression.setObjectName("regression")
        self.random_forest = QtWidgets.QRadioButton(self.centralwidget)
        self.random_forest.setGeometry(QtCore.QRect(200, 550, 121, 23))
        self.random_forest.setObjectName("random_forest")
        self.decision_tree = QtWidgets.QRadioButton(self.centralwidget)
        self.decision_tree.setGeometry(QtCore.QRect(360, 550, 111, 23))
        self.decision_tree.setObjectName("decision_tree")
        self.knn = QtWidgets.QRadioButton(self.centralwidget)
        self.knn.setGeometry(QtCore.QRect(500, 550, 81, 23))
        self.knn.setObjectName("knn")
        self.gnb = QtWidgets.QRadioButton(self.centralwidget)
        self.gnb.setGeometry(QtCore.QRect(590, 550, 171, 23))
        self.gnb.setObjectName("gnb")
        self.select_algo = QtWidgets.QLabel(self.centralwidget)
        self.select_algo.setGeometry(QtCore.QRect(220, 489, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.select_algo.setFont(font)
        self.select_algo.setObjectName("select_algo")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 630, 100, 33))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Male")
        self.comboBox.addItem("Female")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(330, 630, 100, 33))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("S")
        self.comboBox_2.addItem("C")
        self.comboBox_2.addItem("Q")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(610, 630, 100, 33))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("1")
        self.comboBox_3.addItem("2")
        self.comboBox_3.addItem("3")
        self.sex_label = QtWidgets.QLabel(self.centralwidget)
        self.sex_label.setGeometry(QtCore.QRect(60, 600, 71, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sex_label.setFont(font)
        self.sex_label.setObjectName("sex_label")
        self.embark_label = QtWidgets.QLabel(self.centralwidget)
        self.embark_label.setGeometry(QtCore.QRect(330, 600, 111, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.embark_label.setFont(font)
        self.embark_label.setObjectName("embark_label")
        self.p_class_label = QtWidgets.QLabel(self.centralwidget)
        self.p_class_label.setGeometry(QtCore.QRect(610, 600, 91, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.p_class_label.setFont(font)
        self.p_class_label.setObjectName("p_class_label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(320, 720, 113, 33))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.sibling_label = QtWidgets.QLabel(self.centralwidget)
        self.sibling_label.setGeometry(QtCore.QRect(330, 690, 81, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sibling_label.setFont(font)
        self.sibling_label.setObjectName("sibling_label")
        self.predict_btn = QtWidgets.QPushButton(self.centralwidget)
        self.predict_btn.setGeometry(QtCore.QRect(180, 770, 391, 33))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.predict_btn.setFont(font)
        self.predict_btn.setObjectName("predict_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # setting methods for radio btns
        self.regression.toggled.connect(
            lambda: self.selectAlgo('logistic regression'))
        self.decision_tree.toggled.connect(
            lambda: self.selectAlgo('decision tree'))
        self.random_forest.toggled.connect(
            lambda: self.selectAlgo('random forest'))
        self.knn.toggled.connect(lambda: self.selectAlgo('knn'))
        self.gnb.toggled.connect(lambda: self.selectAlgo('gnb'))
        self.regression.setChecked(
            True if self.selectAlgo == 'logistic regression' else False)

        # setting methods for sex
        self.comboBox.activated[str].connect(self.onChangeSex)

        # setting methods for embark
        self.comboBox_2.activated[str].connect(self.onChangeEmbarked)

        # setting methods for
        self.comboBox_3.activated[str].connect(self.onChangePClass)

        # on Click Predict
        self.predict_btn.clicked.connect(self.onClickPredict)

    # Selected Algo Method
    def selectAlgo(self, algo):
        self.selected_algo = algo

    # Change Sex
    def onChangeSex(self, sex):
        self.gender = sex

    # Change Embark
    def onChangeEmbarked(self, embark):
        self.embark = embark

    # Change Pclass
    def onChangePClass(self, pclass):
        self.pClass = pclass

    def onClickPredict(self):
        print(self.lineEdit.text())
        self.lineEdit.setText("")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header_label.setText(_translate(
            "MainWindow", "Titanic Disaster Prediction"))
        self.regression.setText(_translate(
            "MainWindow", "Logistic Regression"))
        self.random_forest.setText(_translate("MainWindow", "Random Forest"))
        self.decision_tree.setText(_translate("MainWindow", "Decision Tree"))
        self.knn.setText(_translate("MainWindow", "KNN"))
        self.gnb.setText(_translate("MainWindow", "Gaussain Naive Bayes"))
        self.select_algo.setText(_translate(
            "MainWindow", "Select The Algorithm you want to run"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Male"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Female"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "S"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "C"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Q"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "3"))
        self.sex_label.setText(_translate("MainWindow", "Select Sex"))
        self.embark_label.setText(_translate("MainWindow", "Select Embarked"))
        self.p_class_label.setText(_translate("MainWindow", "Select P-Class"))
        self.sibling_label.setText(_translate("MainWindow", "Enter Siblings"))
        self.predict_btn.setText(_translate("MainWindow", "Press to Predict"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
