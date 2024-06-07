# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.cube_wid = QSpinBox(Dialog)
        self.cube_wid.setObjectName(u"cube_wid")

        self.horizontalLayout_4.addWidget(self.cube_wid)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.cube_hei = QSpinBox(Dialog)
        self.cube_hei.setObjectName(u"cube_hei")

        self.horizontalLayout_3.addWidget(self.cube_hei)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_7.addWidget(self.label_2)

        self.verti_corner = QSpinBox(Dialog)
        self.verti_corner.setObjectName(u"verti_corner")

        self.horizontalLayout_7.addWidget(self.verti_corner)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horiz_corner = QSpinBox(Dialog)
        self.horiz_corner.setObjectName(u"horiz_corner")

        self.horizontalLayout.addWidget(self.horiz_corner)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.img_file_in = QLineEdit(Dialog)
        self.img_file_in.setObjectName(u"img_file_in")

        self.horizontalLayout_5.addWidget(self.img_file_in)

        self.open_file_in = QPushButton(Dialog)
        self.open_file_in.setObjectName(u"open_file_in")
        self.open_file_in.setAutoDefault(False)

        self.horizontalLayout_5.addWidget(self.open_file_in)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.img_file_ex = QLineEdit(Dialog)
        self.img_file_ex.setObjectName(u"img_file_ex")

        self.horizontalLayout_6.addWidget(self.img_file_ex)

        self.open_file_ex = QPushButton(Dialog)
        self.open_file_ex.setObjectName(u"open_file_ex")
        self.open_file_ex.setAutoDefault(False)

        self.horizontalLayout_6.addWidget(self.open_file_ex)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Cube Width(mm)", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Cube Height(mm)", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Vertical Corner", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Horizental Corner", None))
        self.open_file_in.setText(QCoreApplication.translate("Dialog", u"Intrinsic Image", None))
        self.open_file_ex.setText(QCoreApplication.translate("Dialog", u"Extrinsic Image", None))
    # retranslateUi

