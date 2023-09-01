# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:/GIT/PyFlow/PyFlow/UI/Views\VariablesWidget_ui.ui',
# licensing of 'd:/GIT/PyFlow/PyFlow/UI/Views\VariablesWidget_ui.ui' applies.
#
# Created: Tue Jun 11 12:28:18 2019
#      by: PySide6-uic  running on PySide6 5.12.0
#
# WARNING! All changes made in this file will be lost!

import PySide6.QtCore as QtCore
from PySide6.QtCore import QCoreApplication
import PySide6.QtGui as QtGui
import PySide6.QtWidgets as QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(341, 363)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pbNewVar = QtWidgets.QPushButton(Form)
        self.pbNewVar.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pbNewVar.setObjectName("pbNewVar")
        self.horizontalLayout.addWidget(self.pbNewVar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.wListWidget = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wListWidget.sizePolicy().hasHeightForWidth())
        self.wListWidget.setSizePolicy(sizePolicy)
        self.wListWidget.setObjectName("wListWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.wListWidget)
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.gridLayout.setObjectName("gridLayout")
        self.lytListWidget = QtWidgets.QVBoxLayout()
        self.lytListWidget.setContentsMargins(0, 0, 0, 0)
        self.lytListWidget.setObjectName("lytListWidget")
        self.gridLayout.addLayout(self.lytListWidget, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.wListWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None, -1))
        self.label.setText(QCoreApplication.translate("Form", "Create var", None, -1))
        self.pbNewVar.setText(QCoreApplication.translate("Form", "+", None, -1))

