# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ex-1.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        # self.initUI()


    def setupUi(self, MainWindow):
        digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        operator = ["+", "-", "*", "/"]
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(273, 420)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_calc = QtWidgets.QLabel(self.centralwidget)
        self.label_calc.setGeometry(QtCore.QRect(10, 10, 254, 60))
        self.label_calc.setMaximumSize(QtCore.QSize(16777215, 16777211))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setStrikeOut(False)
        self.label_calc.setFont(font)
        self.label_calc.setAutoFillBackground(True)
        self.label_calc.setFrameShape(QtWidgets.QFrame.Box)
        self.label_calc.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_calc.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_calc.setObjectName("label_calc")
        self.button_clear = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_button("AC"))
        self.button_clear.setGeometry(QtCore.QRect(10, 90, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_clear.setFont(font)
        self.button_clear.setObjectName("button_clear")
        self.button_del = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.delete())
        self.button_del.setGeometry(QtCore.QRect(78, 90, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_del.setFont(font)
        self.button_del.setObjectName("button_del")
        self.button_mod = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_button("%"))
        self.button_mod.setGeometry(QtCore.QRect(145, 90, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_mod.setFont(font)
        self.button_mod.setMouseTracking(False)
        self.button_mod.setObjectName("button_mod")
        self.button_div = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_button("/"))
        self.button_div.setGeometry(QtCore.QRect(214, 90, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_div.setFont(font)
        self.button_div.setObjectName("button_div")
        self.button_7 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_button("7"))
        self.button_7.setGeometry(QtCore.QRect(10, 150, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_7.setFont(font)
        self.button_7.setObjectName("button_7")
        self.button_9 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_button("9"))
        self.button_9.setGeometry(QtCore.QRect(145, 150, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_9.setFont(font)
        self.button_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_9.setStyleSheet("")
        self.button_9.setObjectName("button_9")
        self.button_8 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_button("8"))
        self.button_8.setGeometry(QtCore.QRect(78, 150, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_8.setFont(font)
        self.button_8.setObjectName("button_8")
        self.button_multy = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_button("*"))
        self.button_multy.setGeometry(QtCore.QRect(214, 150, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_multy.setFont(font)
        self.button_multy.setObjectName("button_multy")
        self.button_4 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_button("4"))
        self.button_4.setGeometry(QtCore.QRect(10, 211, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_4.setFont(font)
        self.button_4.setObjectName("button_4")
        self.button_minus = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_button("-"))
        self.button_minus.setGeometry(QtCore.QRect(214, 211, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_minus.setFont(font)
        self.button_minus.setObjectName("button_minus")
        self.button_6 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_button("6"))
        self.button_6.setGeometry(QtCore.QRect(145, 211, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_6.setFont(font)
        self.button_6.setStyleSheet("")
        self.button_6.setObjectName("button_6")
        self.button_5 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_button("5"))
        self.button_5.setGeometry(QtCore.QRect(78, 211, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_5.setFont(font)
        self.button_5.setObjectName("button_5")
        self.button_1 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_button("1"))
        self.button_1.setGeometry(QtCore.QRect(10, 270, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_1.setFont(font)
        self.button_1.setObjectName("button_1")
        self.button_3 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_button("3"))
        self.button_3.setGeometry(QtCore.QRect(145, 270, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_3.setFont(font)
        self.button_3.setObjectName("button_3")
        self.button_2 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_button("2"))
        self.button_2.setGeometry(QtCore.QRect(78, 270, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_2.setFont(font)
        self.button_2.setObjectName("button_2")
        self.button_plus = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_button("+"))
        self.button_plus.setGeometry(QtCore.QRect(214, 270, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_plus.setFont(font)
        self.button_plus.setObjectName("button_plus")
        self.button_plus_minus = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.plus_minus())
        self.button_plus_minus.setGeometry(QtCore.QRect(10, 330, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_plus_minus.setFont(font)
        self.button_plus_minus.setObjectName("button_plus_minus")
        self.button_0 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_button("0"))
        self.button_0.setGeometry(QtCore.QRect(78, 330, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_0.setFont(font)
        self.button_0.setObjectName("button_0")
        self.button_equal = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.equal())
        self.button_equal.setGeometry(QtCore.QRect(214, 330, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_equal.setFont(font)
        self.button_equal.setObjectName("button_equal")
        self.button_dot = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.dot())
        self.button_dot.setGeometry(QtCore.QRect(145, 330, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_dot.setFont(font)
        self.button_dot.setObjectName("button_dot")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 273, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def key_bind(self, event):
        if event.key() == Qt.Key_Enter:
            self.equal()
            print("yeah")
        elif event.key() == Qt.key_1:
            self.press_button()

    def equal(self):
        screen = self.label_calc.text()
        try:
            ans = eval(screen)
            ans = str(ans)
            self.label_calc.setText(ans[:11])
        except ZeroDivisionError:
            self.label_calc.setText("Math error")
        except SyntaxError:
            self.label_calc.setText("Syntax error")
        except TypeError:
            self.label_calc.setText("Type error")
        except:
            self.label_calc.setText("Error")


    def plus_minus(self):
        screen = self.label_calc.text()
        if "-" in screen:
            self.label_calc.setText(F"{abs(int(screen))}")
            screen = str(screen)
        else:
            self.label_calc.setText(F"-{screen}")

    def dot(self):
        screen = self.label_calc.text()

        if screen[-1] == ".":
            pass
        else:
            self.label_calc.setText(F"{screen}.")
    
    def delete(self):
        screen = self.label_calc.text()
        if len(screen) <= 1:
            self.label_calc.setText("0")   
        else: 
            screen = screen[:-1]
            self.label_calc.setText(F"{screen}")
    
    def press_button(self, pressed):
        error = ["Math error", "Syntax error", "Math error", "Error"]
        operators = ["+", "-", "*", "/", "%"]
        screen = self.label_calc.text()
        if pressed == "AC":
            self.label_calc.setText("0")
        elif screen == error[0 or 1 or 2 or 3]:
            self.label_calc.setText("")
            self.label_calc.setText(F"{self.label_calc.text()}{pressed}")
        elif pressed == operators[0 or 1 or 2 or 3 or 4]:
            self.label_calc.setText(F"{self.label_calc.text()}{pressed}")
        else:
            if self.label_calc.text() == "0":
                self.label_calc.setText("")
            self.label_calc.setText(F"{self.label_calc.text()}{pressed}")
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calc"))
        self.label_calc.setText(_translate("MainWindow", "0"))
        self.button_clear.setText(_translate("MainWindow", "AC"))
        self.button_del.setText(_translate("MainWindow", "<<"))
        self.button_mod.setText(_translate("MainWindow", "%"))
        self.button_div.setText(_translate("MainWindow", "/"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_multy.setText(_translate("MainWindow", "*"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_minus.setText(_translate("MainWindow", "-"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_plus.setText(_translate("MainWindow", "+"))
        self.button_plus_minus.setText(_translate("MainWindow", "+/-"))
        self.button_0.setText(_translate("MainWindow", "0"))
        self.button_equal.setText(_translate("MainWindow", "="))
        self.button_dot.setText(_translate("MainWindow", "."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
