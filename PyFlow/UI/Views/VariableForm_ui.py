# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:/GIT/PyFlow/PyFlow/UI/Views\VariableForm_ui.ui',
# licensing of 'd:/GIT/PyFlow/PyFlow/UI/Views\VariableForm_ui.ui' applies.
#
# Created: Tue Jun 11 12:28:18 2019
#      by: PySide6-uic  running on PySide6 5.12.0
#
# WARNING! All changes made in this file will be lost!

import PySide6.QtGui as QtGui
import PySide6.QtCore as QtCore
from PySide6.QtCore import QCoreApplication
import PySide6.QtWidgets as QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(228, 30)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        self.labelName = QtWidgets.QLabel(Form)
        self.labelName.setObjectName("labelName")
        self.horizontalLayout.addWidget(self.labelName)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pbKill = QtWidgets.QPushButton(Form)
        self.pbKill.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pbKill.setText("")
        self.pbKill.setObjectName("pbKill")
        self.horizontalLayout.addWidget(self.pbKill)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None, -1))
        self.labelName.setText(QCoreApplication.translate("Form", "var name", None, -1))

