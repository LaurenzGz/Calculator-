from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import calcu_logic as logic

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(328, 432)
        Calculator.setWindowFlags(Qt.FramelessWindowHint)
        Calculator.setAttribute(Qt.WA_NoSystemBackground, True)
        Calculator.setAttribute(Qt.WA_TranslucentBackground, True)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        Calculator.setFont(font)
        Calculator.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.seven = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("7"))
        self.seven.setGeometry(QtCore.QRect(10, 216, 60, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.seven.setFont(font)
        self.seven.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(22, 22, 22, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(22, 22, 22, 150);\n"
"}")
        self.seven.setObjectName("seven")
        self.eight = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("8"))
        self.eight.setGeometry(QtCore.QRect(72, 216, 60, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.eight.setFont(font)
        self.eight.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(22, 22, 22, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(22, 22, 22, 150);\n"
"}")
        self.eight.setObjectName("eight")
        self.four = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("4"))
        self.four.setGeometry(QtCore.QRect(10, 268, 60, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.four.setFont(font)
        self.four.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(22, 22, 22, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(22, 22, 22, 150);\n"
"}")
        self.four.setObjectName("four")
        self.five = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("5"))
        self.five.setGeometry(QtCore.QRect(72, 268, 60, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.five.setFont(font)
        self.five.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(22, 22, 22, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(22, 22, 22, 150);\n"
"}")
        self.five.setObjectName("five")
        self.nine = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("9"))
        self.nine.setGeometry(QtCore.QRect(134, 216, 60, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.nine.setFont(font)
        self.nine.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(22, 22, 22, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(22, 22, 22, 150);\n"
"}")
        self.nine.setObjectName("nine")
        self.six = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("6"))
        self.six.setGeometry(QtCore.QRect(134, 268, 60, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.six.setFont(font)
        self.six.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(22, 22, 22, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(22, 22, 22, 150);\n"
"}")
        self.six.setObjectName("six")
        self.one = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("1"))
        self.one.setGeometry(QtCore.QRect(10, 320, 60, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.one.setFont(font)
        self.one.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(22, 22, 22, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(22, 22, 22, 150);\n"
"}")
        self.one.setObjectName("one")
        self.two = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("2"))
        self.two.setGeometry(QtCore.QRect(72, 320, 60, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.two.setFont(font)
        self.two.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(22, 22, 22, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(22, 22, 22, 150);\n"
"}")
        self.two.setObjectName("two")
        self.three = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("3"))
        self.three.setGeometry(QtCore.QRect(134, 320, 60, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.three.setFont(font)
        self.three.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(22, 22, 22, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(22, 22, 22, 150);\n"
"}")
        self.three.setObjectName("three")
        self.zero = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("0"))
        self.zero.setGeometry(QtCore.QRect(10, 372, 60, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.zero.setFont(font)
        self.zero.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(22, 22, 22, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(22, 22, 22, 150);\n"
"}")
        self.zero.setObjectName("zero")
        self.decimal = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("."))
        self.decimal.setGeometry(QtCore.QRect(72, 372, 60, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.decimal.setFont(font)
        self.decimal.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(22, 22, 22, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(22, 22, 22, 150);\n"
"}")
        self.decimal.setObjectName("decimal")
        self.clear = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("clear"))
        self.clear.setGeometry(QtCore.QRect(258, 216, 60, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 142, 82, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 142, 82, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 142, 82, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 142, 82, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 142, 82, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 142, 82, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 142, 82, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 142, 82, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 142, 82, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.clear.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.clear.setFont(font)
        self.clear.setAutoFillBackground(False)
        self.clear.setStyleSheet("QPushButton{\n"
"    color: rgb(0, 0, 0);\n"
"    background: rgba(231, 142, 82,240);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(231, 142, 82,200);\n"
"}")
        self.clear.setAutoDefault(False)
        self.clear.setDefault(False)
        self.clear.setFlat(False)
        self.clear.setObjectName("clear")
        self.delButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("del"))
        self.delButton.setGeometry(QtCore.QRect(196, 216, 60, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.delButton.setFont(font)
        self.delButton.setStyleSheet("QPushButton{\n"
"    color: rgb(0, 0, 0);\n"
"    background: rgba(231, 142, 82,240);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(231, 142, 82,200);\n"
"}")
        self.delButton.setObjectName("delButton")
        self.division = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("÷"))
        self.division.setGeometry(QtCore.QRect(258, 268, 60, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.division.setFont(font)
        self.division.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(50,50,50, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(50,50,50, 150)\n"
"}")
        self.division.setObjectName("division")
        self.multiplication = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("×"))
        self.multiplication.setGeometry(QtCore.QRect(196, 268, 60, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.multiplication.setFont(font)
        self.multiplication.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(50,50,50, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(50,50,50, 150)\n"
"}")
        self.multiplication.setObjectName("multiplication")
        self.subtraction = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("-"))
        self.subtraction.setGeometry(QtCore.QRect(258, 320, 60, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.subtraction.setFont(font)
        self.subtraction.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(50,50,50, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(50,50,50, 150)\n"
"}")
        self.subtraction.setObjectName("subtraction")
        self.addition = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("+"))
        self.addition.setGeometry(QtCore.QRect(196, 320, 60, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.addition.setFont(font)
        self.addition.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(50,50,50, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(50,50,50, 150)\n"
"}")
        self.addition.setObjectName("addition")
        self.equal = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("="))
        self.equal.setGeometry(QtCore.QRect(258, 372, 60, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.equal.setFont(font)
        self.equal.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(50,50,50, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(50,50,50, 150)\n"
"}")
        self.equal.setObjectName("equal")
        self.left_parenthesis = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("("))
        self.left_parenthesis.setGeometry(QtCore.QRect(10, 152, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.left_parenthesis.setFont(font)
        self.left_parenthesis.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(50,50,50, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(50,50,50, 150)\n"
"}")
        self.left_parenthesis.setObjectName("left_parenthesis")
        self.right_parenthesis = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it(")"))
        self.right_parenthesis.setGeometry(QtCore.QRect(72, 152, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.right_parenthesis.setFont(font)
        self.right_parenthesis.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(50,50,50, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(50,50,50, 150)\n"
"}")
        self.right_parenthesis.setObjectName("right_parenthesis")
        self.ans = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("ans"))
        self.ans.setGeometry(QtCore.QRect(196, 372, 60, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ans.setFont(font)
        self.ans.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(50,50,50, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(50,50,50, 150)\n"
"}")
        self.ans.setObjectName("ans")
        self.sin = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("sin"))
        self.sin.setGeometry(QtCore.QRect(134, 184, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.sin.setFont(font)
        self.sin.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(50,50,50, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(50,50,50, 150)\n"
"}")
        self.sin.setObjectName("sin")
        self.cos = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("cos"))
        self.cos.setGeometry(QtCore.QRect(196, 184, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.cos.setFont(font)
        self.cos.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(50,50,50, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(50,50,50, 150)\n"
"}")
        self.cos.setObjectName("cos")
        self.tan = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("tan"))
        self.tan.setGeometry(QtCore.QRect(258, 184, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.tan.setFont(font)
        self.tan.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(50,50,50, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(50,50,50, 150)\n"
"}")
        self.tan.setObjectName("tan")
        self.pi = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("𝜋"))
        self.pi.setGeometry(QtCore.QRect(134, 372, 60, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pi.setFont(font)
        self.pi.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(22, 22, 22, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(22, 22, 22, 150);\n"
"}")
        self.pi.setObjectName("pi")
        self.sqrt = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("√"))
        self.sqrt.setGeometry(QtCore.QRect(72, 120, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.sqrt.setFont(font)
        self.sqrt.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(50,50,50, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(50,50,50, 150)\n"
"}")
        self.sqrt.setObjectName("sqrt")
        self.log = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("log"))
        self.log.setGeometry(QtCore.QRect(196, 120, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.log.setFont(font)
        self.log.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(50,50,50, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(50,50,50, 150)\n"
"}")
        self.log.setObjectName("log")
        self.ln = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("ln"))
        self.ln.setGeometry(QtCore.QRect(258, 120, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ln.setFont(font)
        self.ln.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(50,50,50, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(50,50,50, 150)\n"
"}")
        self.ln.setObjectName("ln")
        self.e = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("e"))
        self.e.setGeometry(QtCore.QRect(72, 184, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.e.setFont(font)
        self.e.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(50,50,50, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(50,50,50, 150)\n"
"}")
        self.e.setObjectName("e")
        self.arcsin = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("arcsin"))
        self.arcsin.setGeometry(QtCore.QRect(134, 152, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.arcsin.setFont(font)
        self.arcsin.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(50,50,50, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(50,50,50, 150)\n"
"}")
        self.arcsin.setObjectName("arcsin")
        self.arccos = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("arccos"))
        self.arccos.setGeometry(QtCore.QRect(196, 152, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.arccos.setFont(font)
        self.arccos.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(50,50,50, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(50,50,50, 150)\n"
"}")
        self.arccos.setObjectName("arccos")
        self.arctan = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("arctan"))
        self.arctan.setGeometry(QtCore.QRect(258, 152, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.arctan.setFont(font)
        self.arctan.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(50,50,50, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(50,50,50, 150)\n"
"}")
        self.arctan.setObjectName("arctan")
        self.exponent = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("^"))
        self.exponent.setGeometry(QtCore.QRect(134, 120, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.exponent.setFont(font)
        self.exponent.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(50,50,50, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(50,50,50, 150)\n"
"}")
        self.exponent.setObjectName("exponent")
        self.negative = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("﹣"))
        self.negative.setGeometry(QtCore.QRect(10, 184, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.negative.setFont(font)
        self.negative.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(50,50,50, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(50,50,50, 150)\n"
"}")
        self.negative.setObjectName("negative")
        self.degrad = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("degrad"))
        self.degrad.setGeometry(QtCore.QRect(10, 120, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.degrad.setFont(font)
        self.degrad.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(50,50,50, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(50,50,50, 150)\n"
"}")
        self.degrad.setObjectName("degrad")
        self.display = QtWidgets.QLabel(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(20, 35, 288, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.display.setFont(font)
        self.display.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.display.setFrameShadow(QtWidgets.QFrame.Plain)
        self.display.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.display.setObjectName("display")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(10, 25, 308, 85))
        self.background.setStyleSheet("background: rgba(22, 22, 22, 200);")
        self.background.setText("")
        self.background.setObjectName("background")
        self.minimize = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("minimize"))
        self.minimize.setGeometry(QtCore.QRect(268, 0, 25, 25))
        self.minimize.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(22, 22, 22, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(112, 112, 112, 150);\n"
"}")
        self.minimize.setObjectName("minimize")
        self.close = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("close"))
        self.close.setGeometry(QtCore.QRect(293, 0, 25, 25))
        self.close.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgba(22, 22, 22, 220);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background: rgba(232, 17, 35,220)\n"
"}\n"
"")
        self.close.setObjectName("close")
        self.dragFrame = QtWidgets.QFrame(self.centralwidget)
        self.dragFrame.setGeometry(QtCore.QRect(10, 0, 308, 25))
        self.dragFrame.setStyleSheet("background: rgba(0, 0, 0, 200);")
        self.dragFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dragFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dragFrame.setObjectName("dragFrame")
        self.deg = QtWidgets.QLabel(self.centralwidget)
        self.deg.setGeometry(QtCore.QRect(20, 30, 30, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.deg.setFont(font)
        self.deg.setAlignment(QtCore.Qt.AlignCenter)
        self.deg.setObjectName("deg")
        self.rad = QtWidgets.QLabel(self.centralwidget)
        self.rad.setGeometry(QtCore.QRect(60, 30, 30, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.rad.setFont(font)
        self.rad.setAlignment(QtCore.Qt.AlignCenter)
        self.rad.setObjectName("rad")
        self.bgFrame = QtWidgets.QFrame(self.centralwidget)
        self.bgFrame.setGeometry(QtCore.QRect(10, 0, 308, 397))
        self.bgFrame.setStyleSheet("background: rgba(0, 0, 0, 10);")
        self.bgFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bgFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bgFrame.setObjectName("bgFrame")
        self.opDisplay = QtWidgets.QLabel(self.centralwidget)
        self.opDisplay.setEnabled(True)
        self.opDisplay.setGeometry(QtCore.QRect(20, 5, 288, 70))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.opDisplay.setFont(font)
        self.opDisplay.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.opDisplay.setAutoFillBackground(False)
        self.opDisplay.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.opDisplay.setFrameShadow(QtWidgets.QFrame.Plain)
        self.opDisplay.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignTrailing)
        self.opDisplay.setWordWrap(False)
        self.opDisplay.setObjectName("opDisplay")
        self.bgFrame.raise_()
        self.dragFrame.raise_()
        self.background.raise_()
        self.seven.raise_()
        self.eight.raise_()
        self.four.raise_()
        self.five.raise_()
        self.nine.raise_()
        self.six.raise_()
        self.one.raise_()
        self.two.raise_()
        self.three.raise_()
        self.zero.raise_()
        self.decimal.raise_()
        self.clear.raise_()
        self.delButton.raise_()
        self.division.raise_()
        self.multiplication.raise_()
        self.subtraction.raise_()
        self.addition.raise_()
        self.equal.raise_()
        self.left_parenthesis.raise_()
        self.right_parenthesis.raise_()
        self.ans.raise_()
        self.sin.raise_()
        self.cos.raise_()
        self.tan.raise_()
        self.pi.raise_()
        self.sqrt.raise_()
        self.log.raise_()
        self.ln.raise_()
        self.e.raise_()
        self.arcsin.raise_()
        self.arccos.raise_()
        self.arctan.raise_()
        self.exponent.raise_()
        self.negative.raise_()
        self.degrad.raise_()
        self.display.raise_()
        self.opDisplay.raise_()
        self.minimize.raise_()
        self.close.raise_()
        self.deg.raise_()
        self.rad.raise_()
        Calculator.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "MainWindow"))
        self.seven.setText(_translate("Calculator", "7"))
        self.seven.setShortcut(_translate("Calculator", "7"))
        self.eight.setText(_translate("Calculator", "8"))
        self.eight.setShortcut(_translate("Calculator", "8"))
        self.four.setText(_translate("Calculator", "4"))
        self.four.setShortcut(_translate("Calculator", "4"))
        self.five.setText(_translate("Calculator", "5"))
        self.five.setShortcut(_translate("Calculator", "5"))
        self.nine.setText(_translate("Calculator", "9"))
        self.nine.setShortcut(_translate("Calculator", "9"))
        self.six.setText(_translate("Calculator", "6"))
        self.six.setShortcut(_translate("Calculator", "6"))
        self.one.setText(_translate("Calculator", "1"))
        self.one.setShortcut(_translate("Calculator", "1"))
        self.two.setText(_translate("Calculator", "2"))
        self.two.setShortcut(_translate("Calculator", "2"))
        self.three.setText(_translate("Calculator", "3"))
        self.three.setShortcut(_translate("Calculator", "3"))
        self.zero.setText(_translate("Calculator", "0"))
        self.zero.setShortcut(_translate("Calculator", "0"))
        self.decimal.setText(_translate("Calculator", "."))
        self.decimal.setShortcut(_translate("Calculator", "."))
        self.clear.setText(_translate("Calculator", "CLEAR"))
        self.clear.setShortcut(_translate("Calculator", "Shift+Backspace"))
        self.delButton.setText(_translate("Calculator", "DEL"))
        self.delButton.setShortcut(_translate("Calculator", "Backspace"))
        self.division.setText(_translate("Calculator", "÷"))
        self.division.setShortcut(_translate("Calculator", "/"))
        self.multiplication.setText(_translate("Calculator", "×"))
        self.multiplication.setShortcut(_translate("Calculator", "*"))
        self.subtraction.setText(_translate("Calculator", "-"))
        self.subtraction.setShortcut(_translate("Calculator", "-"))
        self.addition.setText(_translate("Calculator", "+"))
        self.addition.setShortcut(_translate("Calculator", "+"))
        self.equal.setText(_translate("Calculator", "="))
        self.equal.setShortcut(_translate("Calculator", "Enter"))
        self.left_parenthesis.setText(_translate("Calculator", "("))
        self.left_parenthesis.setShortcut(_translate("Calculator", "("))
        self.right_parenthesis.setText(_translate("Calculator", ")"))
        self.right_parenthesis.setShortcut(_translate("Calculator", ")"))
        self.ans.setText(_translate("Calculator", "Ans"))
        self.sin.setText(_translate("Calculator", "sin"))
        self.cos.setText(_translate("Calculator", "cos"))
        self.tan.setText(_translate("Calculator", "tan"))
        self.pi.setText(_translate("Calculator", "𝜋"))
        self.sqrt.setText(_translate("Calculator", "√"))
        self.log.setText(_translate("Calculator", "log"))
        self.ln.setText(_translate("Calculator", "ln"))
        self.e.setText(_translate("Calculator", "e"))
        self.e.setShortcut(_translate("Calculator", "e"))
        self.arcsin.setText(_translate("Calculator", "arcsin"))
        self.arccos.setText(_translate("Calculator", "arccos"))
        self.arctan.setText(_translate("Calculator", "arctan"))
        self.exponent.setText(_translate("Calculator", "^"))
        self.exponent.setShortcut(_translate("Calculator", "^"))
        self.negative.setText(_translate("Calculator", "( - )"))
        self.degrad.setText(_translate("Calculator", "deg/rad"))
        self.display.setText(_translate("Calculator", "0"))
        self.display.setStyleSheet("color: rgb(255, 255, 255);")
        self.opDisplay.setText(_translate("Calculator", "0"))
        self.opDisplay.setStyleSheet("color: rgb(255, 255, 255);")
        self.minimize.setText(_translate("Calculator", "—"))
        self.close.setText(_translate("Calculator", "✕"))
        self.deg.setText(_translate("Calculator", "DEG"))
        self.deg.setStyleSheet("color: rgb(255, 255, 255);")
        self.rad.setText(_translate("Calculator", "RAD"))

    def press_it(self, pressed):
        if pressed == "clear":
            logic.clear_all()
            logic.saved_equation = "0"
            self.opDisplay.setText("0")
            self.display.setText("0")
        elif pressed == "del":
            if len(logic.equation) <= 1:
                logic.delete()
                logic.saved_equation = "0"
                self.opDisplay.setText("0")
            else:
                logic.delete()
                self.opDisplay.setText(logic.equation)
        elif pressed == "minimize":
            self.showMinimized()
        elif pressed == "close":
            QtCore.QCoreApplication.instance().quit()
        elif pressed == "degrad":
            if str(self.deg.styleSheet()) == "color: rgb(255, 255, 255);":
                self.rad.setStyleSheet("color: rgb(255, 255, 255);")
                self.deg.setStyleSheet("")
                logic.deg_rad = False
                if logic.saved_equation != "0":
                    logic.equation = logic.saved_equation

            else:
                self.deg.setStyleSheet("color: rgb(255, 255, 255);")
                self.rad.setStyleSheet("")
                logic.deg_rad = True
                if logic.saved_equation != "0":
                    logic.equation = logic.saved_equation

        elif pressed == "1":
            logic.one()
            self.opDisplay.setText(logic.equation)
        elif pressed == "2":
            logic.two()
            self.opDisplay.setText(logic.equation)
        elif pressed == "3":
            logic.three()
            self.opDisplay.setText(logic.equation)
        elif pressed == "4":
            logic.four()
            self.opDisplay.setText(logic.equation)
        elif pressed == "5":
            logic.five()
            self.opDisplay.setText(logic.equation)
        elif pressed == "6":
            logic.six()
            self.opDisplay.setText(logic.equation)
        elif pressed == "7":
            logic.seven()
            self.opDisplay.setText(logic.equation)
        elif pressed == "8":
            logic.eight()
            self.opDisplay.setText(logic.equation)
        elif pressed == "9":
            logic.nine()
            self.opDisplay.setText(logic.equation)
        elif pressed == "0":
            logic.zero()
            self.opDisplay.setText(logic.equation)
        elif pressed == "(":
            logic.parenthesis_open()
            self.opDisplay.setText(logic.equation)
        elif pressed == ")":
            logic.parenthesis_close()
            self.opDisplay.setText(logic.equation)
        elif pressed == "log":
            logic.log()
            self.opDisplay.setText(logic.equation)
        elif pressed == "ln":
            logic.ln()
            self.opDisplay.setText(logic.equation)
        elif pressed == "e":
            logic.e()
            self.opDisplay.setText(logic.equation)
        elif pressed == "√":
            logic.sqrt()
            self.opDisplay.setText(logic.equation)
        elif pressed == "+":
            logic.addition()
            self.opDisplay.setText(logic.equation)
        elif pressed == "-":
            logic.subtraction()
            self.opDisplay.setText(logic.equation)
        elif pressed == "×":
            logic.multiplication()
            self.opDisplay.setText(logic.equation)
        elif pressed == "﹣":
            logic.negative_sign()
            self.opDisplay.setText(logic.equation)
        elif pressed == "÷":
            logic.division()
            self.opDisplay.setText(logic.equation)
        elif pressed == "^":
            logic.exponent()
            self.opDisplay.setText(logic.equation)
        elif pressed == "sin":
            logic.sin()
            self.opDisplay.setText(logic.equation)
        elif pressed == "cos":
            logic.cos()
            self.opDisplay.setText(logic.equation)
        elif pressed == "tan":
            logic.tan()
            self.opDisplay.setText(logic.equation)
        elif pressed == "arcsin":
            logic.arcsin()
            self.opDisplay.setText(logic.equation)
        elif pressed == "arccos":
            logic.arccos()
            self.opDisplay.setText(logic.equation)
        elif pressed == "arctan":
            logic.arctan()
            self.opDisplay.setText(logic.equation)
        elif pressed == ".":
            logic.decimal()
            self.opDisplay.setText(logic.equation)
        elif pressed == "𝜋":
            logic.pi()
            self.opDisplay.setText(logic.equation)
        elif pressed == "=":
            if logic.equation == "":
                return None
            else:
                self.opDisplay.setText(self.opDisplay.text())
                self.display.setText(logic.calculate())
            
        elif pressed == "ans":
            logic.ans()
            self.opDisplay.setText(logic.equation)


class MyWin(QtWidgets.QMainWindow, Ui_Calculator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dragPos = QtCore.QPoint()
        
    def mousePressEvent(self, event):                                
        self.dragPos = event.globalPos()
        
    def mouseMoveEvent(self, event):                              
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    w = MyWin()
    w.show()
    sys.exit(app.exec_())
