# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/QtUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(792, 572)
        Widget.setStyleSheet("* {\n"
"    color: white;\n"
"    background: transparent;\n"
"    font-size: 14pt;\n"
"    opacity: 0.1;\n"
"}\n"
"#appTitle {\n"
"    font-size: 30px;\n"
"    margin-bottom: 10px;\n"
"    font-weight: bold;\n"
"}\n"
"#Widget {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    background: #17181e;\n"
"}\n"
"QPushButton {\n"
"    color: gainsboro;\n"
"    position: relative;\n"
"    height: 36px;\n"
"    padding: 0 20px;\n"
"    margin: 6px;\n"
"    font-weight: 500;\n"
"    text-transform: uppercase;\n"
"    letter-spacing: 0.15em;\n"
"    border: none;\n"
"    background: #2d313c;\n"
"    border-radius: 3px;\n"
"}\n"
"QPushButton::hover {\n"
"    background: #535865;\n"
"}\n"
"QPushButton:disabled {\n"
"    color: #8a8d9f;\n"
"    background: #1d2029;\n"
"}\n"
"QListWidget {\n"
"    background: #2d313c;\n"
"    border-radius: 3px;\n"
"}\n"
"QListWidget::item {\n"
"    letter-spacing: normal;\n"
"    min-height: 48px;\n"
"    outline: none;\n"
"    position: relative;\n"
"}\n"
"QListWidget::item::hover {\n"
"    background: #3a3e49;\n"
"}\n"
"QListWidget::item:selected {\n"
"    background: #535865;\n"
"}\n"
"QPlainTextEdit {\n"
"    background: #2d313c;\n"
"    border-radius: 3px;\n"
"    padding: 10px;\n"
"    line-height: 40px;\n"
"}\n"
"QLineEdit {\n"
"    background: #2d313c;\n"
"    height: 36px;\n"
"    border: 0;\n"
"    border-radius: 3px;\n"
"    padding-left: 5px;\n"
"}\n"
"QComboBox {\n"
"    background: #2d313c;\n"
"    color: white;\n"
"    height: 36px;\n"
"    border: 0;\n"
"    border-radius: 3px;\n"
"}\n"
"QSpinBox {\n"
"    background: #2d313c;\n"
"    color: white;\n"
"    height: 36px;\n"
"    border: 0;\n"
"    border-radius: 3px;\n"
"    padding-left: 5px;\n"
"}\n"
"QRadioButton {\n"
"    min-height: 32px;\n"
"}\n"
"QMessageBox {\n"
"    background-color: #17181e;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Widget)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.stackedPages = QtWidgets.QStackedWidget(Widget)
        self.stackedPages.setObjectName("stackedPages")
        self.homePage = QtWidgets.QWidget()
        self.homePage.setObjectName("homePage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.homePage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.appTitle = QtWidgets.QLabel(self.homePage)
        self.appTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.appTitle.setObjectName("appTitle")
        self.verticalLayout_2.addWidget(self.appTitle)
        self.bankList = QtWidgets.QListWidget(self.homePage)
        self.bankList.setStyleSheet("")
        self.bankList.setObjectName("bankList")
        self.verticalLayout_2.addWidget(self.bankList)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.enterExamButton = QtWidgets.QPushButton(self.homePage)
        self.enterExamButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enterExamButton.setStyleSheet("")
        self.enterExamButton.setObjectName("enterExamButton")
        self.horizontalLayout_8.addWidget(self.enterExamButton)
        spacerItem = QtWidgets.QSpacerItem(475, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.deleteBankButton = QtWidgets.QPushButton(self.homePage)
        self.deleteBankButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteBankButton.setStyleSheet("color: red")
        self.deleteBankButton.setObjectName("deleteBankButton")
        self.horizontalLayout_8.addWidget(self.deleteBankButton)
        self.editBankButton = QtWidgets.QPushButton(self.homePage)
        self.editBankButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.editBankButton.setObjectName("editBankButton")
        self.horizontalLayout_8.addWidget(self.editBankButton)
        self.addBankButton = QtWidgets.QPushButton(self.homePage)
        self.addBankButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addBankButton.setObjectName("addBankButton")
        self.horizontalLayout_8.addWidget(self.addBankButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.stackedPages.addWidget(self.homePage)
        self.editBankPage = QtWidgets.QWidget()
        self.editBankPage.setObjectName("editBankPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.editBankPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.editBankPage)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.bankName = QtWidgets.QLineEdit(self.editBankPage)
        self.bankName.setObjectName("bankName")
        self.horizontalLayout_2.addWidget(self.bankName)
        self.bankSaveButton = QtWidgets.QPushButton(self.editBankPage)
        self.bankSaveButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bankSaveButton.setObjectName("bankSaveButton")
        self.horizontalLayout_2.addWidget(self.bankSaveButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.questionList = QtWidgets.QListWidget(self.editBankPage)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.questionList.setFont(font)
        self.questionList.setObjectName("questionList")
        self.verticalLayout_3.addWidget(self.questionList)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.homeButton = QtWidgets.QPushButton(self.editBankPage)
        self.homeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.homeButton.setObjectName("homeButton")
        self.horizontalLayout_3.addWidget(self.homeButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.deleteQuestionButton = QtWidgets.QPushButton(self.editBankPage)
        self.deleteQuestionButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteQuestionButton.setStyleSheet("color: red")
        self.deleteQuestionButton.setObjectName("deleteQuestionButton")
        self.horizontalLayout_3.addWidget(self.deleteQuestionButton)
        self.editQuestionButton = QtWidgets.QPushButton(self.editBankPage)
        self.editQuestionButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.editQuestionButton.setObjectName("editQuestionButton")
        self.horizontalLayout_3.addWidget(self.editQuestionButton)
        self.addQuestionButton = QtWidgets.QPushButton(self.editBankPage)
        self.addQuestionButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addQuestionButton.setObjectName("addQuestionButton")
        self.horizontalLayout_3.addWidget(self.addQuestionButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.stackedPages.addWidget(self.editBankPage)
        self.editQuestionPage = QtWidgets.QWidget()
        self.editQuestionPage.setObjectName("editQuestionPage")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.editQuestionPage)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_6 = QtWidgets.QLabel(self.editQuestionPage)
        self.label_6.setStyleSheet("")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.questionType = QtWidgets.QComboBox(self.editQuestionPage)
        self.questionType.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.questionType.setObjectName("questionType")
        self.gridLayout_3.addWidget(self.questionType, 0, 1, 1, 1)
        self.questionText = QtWidgets.QPlainTextEdit(self.editQuestionPage)
        self.questionText.setStyleSheet("")
        self.questionText.setObjectName("questionText")
        self.gridLayout_3.addWidget(self.questionText, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.editQuestionPage)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.editQuestionPage)
        self.label_7.setStyleSheet("")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)
        self.stackedAnswer = QtWidgets.QStackedWidget(self.editQuestionPage)
        self.stackedAnswer.setObjectName("stackedAnswer")
        self.choice = QtWidgets.QWidget()
        self.choice.setObjectName("choice")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.choice)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.radioButtonGroup = QtWidgets.QHBoxLayout()
        self.radioButtonGroup.setObjectName("radioButtonGroup")
        self.newOption = QtWidgets.QLineEdit(self.choice)
        self.newOption.setObjectName("newOption")
        self.radioButtonGroup.addWidget(self.newOption)
        self.addOptionButton = QtWidgets.QPushButton(self.choice)
        self.addOptionButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.addOptionButton.setObjectName("addOptionButton")
        self.radioButtonGroup.addWidget(self.addOptionButton)
        self.verticalLayout_8.addLayout(self.radioButtonGroup)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.stackedAnswer.addWidget(self.choice)
        self.shortAnswer = QtWidgets.QWidget()
        self.shortAnswer.setObjectName("shortAnswer")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.shortAnswer)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.shortAnswerSheet = QtWidgets.QPlainTextEdit(self.shortAnswer)
        self.shortAnswerSheet.setPlaceholderText("")
        self.shortAnswerSheet.setObjectName("shortAnswerSheet")
        self.verticalLayout_9.addWidget(self.shortAnswerSheet)
        self.stackedAnswer.addWidget(self.shortAnswer)
        self.gridLayout_3.addWidget(self.stackedAnswer, 2, 1, 1, 1)
        self.gridLayout_3.setRowStretch(2, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_3)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.backButton = QtWidgets.QPushButton(self.editQuestionPage)
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setObjectName("backButton")
        self.horizontalLayout_11.addWidget(self.backButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)
        self.saveQuestionButton = QtWidgets.QPushButton(self.editQuestionPage)
        self.saveQuestionButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.saveQuestionButton.setObjectName("saveQuestionButton")
        self.horizontalLayout_11.addWidget(self.saveQuestionButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.stackedPages.addWidget(self.editQuestionPage)
        self.enterExamPage = QtWidgets.QWidget()
        self.enterExamPage.setObjectName("enterExamPage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.enterExamPage)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setVerticalSpacing(25)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.enterExamPage)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.bankName_2 = QtWidgets.QLabel(self.enterExamPage)
        self.bankName_2.setText("")
        self.bankName_2.setObjectName("bankName_2")
        self.gridLayout_4.addWidget(self.bankName_2, 0, 1, 1, 1)
        self.examNum = QtWidgets.QSpinBox(self.enterExamPage)
        self.examNum.setProperty("value", 10)
        self.examNum.setObjectName("examNum")
        self.gridLayout_4.addWidget(self.examNum, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.enterExamPage)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 2, 0, 1, 1)
        self.questionNum = QtWidgets.QLabel(self.enterExamPage)
        self.questionNum.setText("")
        self.questionNum.setObjectName("questionNum")
        self.gridLayout_4.addWidget(self.questionNum, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.enterExamPage)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)
        self.gridLayout_4.setColumnStretch(1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.homeButton_2 = QtWidgets.QPushButton(self.enterExamPage)
        self.homeButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.homeButton_2.setObjectName("homeButton_2")
        self.horizontalLayout_9.addWidget(self.homeButton_2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.beginExamButton = QtWidgets.QPushButton(self.enterExamPage)
        self.beginExamButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.beginExamButton.setObjectName("beginExamButton")
        self.horizontalLayout_9.addWidget(self.beginExamButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.stackedPages.addWidget(self.enterExamPage)
        self.examPage = QtWidgets.QWidget()
        self.examPage.setObjectName("examPage")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.examPage)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.examQuestionType = QtWidgets.QLabel(self.examPage)
        self.examQuestionType.setText("")
        self.examQuestionType.setObjectName("examQuestionType")
        self.gridLayout_6.addWidget(self.examQuestionType, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.examPage)
        self.label_11.setObjectName("label_11")
        self.gridLayout_6.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.examPage)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.gridLayout_6.addWidget(self.label_9, 1, 0, 1, 1)
        self.examQuestionText = QtWidgets.QLabel(self.examPage)
        self.examQuestionText.setBaseSize(QtCore.QSize(0, 0))
        self.examQuestionText.setText("")
        self.examQuestionText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.examQuestionText.setObjectName("examQuestionText")
        self.gridLayout_6.addWidget(self.examQuestionText, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.examPage)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_10.setObjectName("label_10")
        self.gridLayout_6.addWidget(self.label_10, 2, 0, 1, 1)
        self.stackedExamAnswer = QtWidgets.QStackedWidget(self.examPage)
        self.stackedExamAnswer.setObjectName("stackedExamAnswer")
        self.examShortAnswer = QtWidgets.QWidget()
        self.examShortAnswer.setObjectName("examShortAnswer")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.examShortAnswer)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.examShortAnswerSheet = QtWidgets.QPlainTextEdit(self.examShortAnswer)
        self.examShortAnswerSheet.setObjectName("examShortAnswerSheet")
        self.verticalLayout_19.addWidget(self.examShortAnswerSheet)
        self.stackedExamAnswer.addWidget(self.examShortAnswer)
        self.examChoice = QtWidgets.QWidget()
        self.examChoice.setObjectName("examChoice")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.examChoice)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.stackedExamAnswer.addWidget(self.examChoice)
        self.gridLayout_6.addWidget(self.stackedExamAnswer, 2, 1, 1, 1)
        self.gridLayout_6.setRowStretch(1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_6)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.homeButton_3 = QtWidgets.QPushButton(self.examPage)
        self.homeButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.homeButton_3.setObjectName("homeButton_3")
        self.horizontalLayout_13.addWidget(self.homeButton_3)
        self.showAnswerButton = QtWidgets.QPushButton(self.examPage)
        self.showAnswerButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.showAnswerButton.setObjectName("showAnswerButton")
        self.horizontalLayout_13.addWidget(self.showAnswerButton)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem7)
        self.currentNum = QtWidgets.QLabel(self.examPage)
        self.currentNum.setObjectName("currentNum")
        self.horizontalLayout_13.addWidget(self.currentNum)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem8)
        self.checkAnswerButton = QtWidgets.QPushButton(self.examPage)
        self.checkAnswerButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkAnswerButton.setObjectName("checkAnswerButton")
        self.horizontalLayout_13.addWidget(self.checkAnswerButton)
        self.nextQuestionButton = QtWidgets.QPushButton(self.examPage)
        self.nextQuestionButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nextQuestionButton.setObjectName("nextQuestionButton")
        self.horizontalLayout_13.addWidget(self.nextQuestionButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_13)
        self.stackedPages.addWidget(self.examPage)
        self.resultPage = QtWidgets.QWidget()
        self.resultPage.setObjectName("resultPage")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.resultPage)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem9)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setVerticalSpacing(25)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.questionWrongNum = QtWidgets.QLabel(self.resultPage)
        self.questionWrongNum.setText("")
        self.questionWrongNum.setObjectName("questionWrongNum")
        self.gridLayout_2.addWidget(self.questionWrongNum, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.resultPage)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.resultPage)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 1, 0, 1, 1)
        self.questionRightNum = QtWidgets.QLabel(self.resultPage)
        self.questionRightNum.setText("")
        self.questionRightNum.setObjectName("questionRightNum")
        self.gridLayout_2.addWidget(self.questionRightNum, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.resultPage)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 2, 0, 1, 1)
        self.questionShowNum = QtWidgets.QLabel(self.resultPage)
        self.questionShowNum.setText("")
        self.questionShowNum.setObjectName("questionShowNum")
        self.gridLayout_2.addWidget(self.questionShowNum, 2, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_2)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem10)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.homeButton_4 = QtWidgets.QPushButton(self.resultPage)
        self.homeButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.homeButton_4.setObjectName("homeButton_4")
        self.horizontalLayout_4.addWidget(self.homeButton_4)
        self.testAgainButton = QtWidgets.QPushButton(self.resultPage)
        self.testAgainButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.testAgainButton.setObjectName("testAgainButton")
        self.horizontalLayout_4.addWidget(self.testAgainButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.stackedPages.addWidget(self.resultPage)
        self.gridLayout.addWidget(self.stackedPages, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Widget)
        self.stackedPages.setCurrentIndex(2)
        self.stackedAnswer.setCurrentIndex(0)
        self.stackedExamAnswer.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.appTitle.setText(_translate("Widget", "Title"))
        self.enterExamButton.setText(_translate("Widget", "進入測驗"))
        self.deleteBankButton.setText(_translate("Widget", "刪除題庫"))
        self.editBankButton.setText(_translate("Widget", "編輯題庫"))
        self.addBankButton.setText(_translate("Widget", "新增題庫"))
        self.label_8.setText(_translate("Widget", "題庫名稱："))
        self.bankSaveButton.setText(_translate("Widget", "儲存"))
        self.homeButton.setText(_translate("Widget", "回首頁"))
        self.deleteQuestionButton.setText(_translate("Widget", "刪除題目"))
        self.editQuestionButton.setText(_translate("Widget", "編輯題目"))
        self.addQuestionButton.setText(_translate("Widget", "新增題目"))
        self.label_6.setText(_translate("Widget", "題目敘述："))
        self.label_5.setText(_translate("Widget", "題目類型："))
        self.label_7.setText(_translate("Widget", "題目答案："))
        self.addOptionButton.setText(_translate("Widget", "新增選項"))
        self.backButton.setText(_translate("Widget", "取消"))
        self.saveQuestionButton.setText(_translate("Widget", "儲存"))
        self.label_2.setText(_translate("Widget", "題庫名稱："))
        self.label.setText(_translate("Widget", "測驗題數："))
        self.label_3.setText(_translate("Widget", "題庫題數："))
        self.homeButton_2.setText(_translate("Widget", "回首頁"))
        self.beginExamButton.setText(_translate("Widget", "開始測驗"))
        self.label_11.setText(_translate("Widget", "題目類型："))
        self.label_9.setText(_translate("Widget", "題目敘述："))
        self.label_10.setText(_translate("Widget", "作答："))
        self.homeButton_3.setText(_translate("Widget", "離開"))
        self.showAnswerButton.setText(_translate("Widget", "偷看答案"))
        self.currentNum.setText(_translate("Widget", "0"))
        self.checkAnswerButton.setText(_translate("Widget", "提交"))
        self.nextQuestionButton.setText(_translate("Widget", "下一題"))
        self.label_4.setText(_translate("Widget", "答對題數："))
        self.label_12.setText(_translate("Widget", "答錯題數："))
        self.label_14.setText(_translate("Widget", "查看答案次數："))
        self.homeButton_4.setText(_translate("Widget", "回首頁"))
        self.testAgainButton.setText(_translate("Widget", "再次測驗"))
