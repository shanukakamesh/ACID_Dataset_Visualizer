# Form implementation generated from reading ui file 'ACID_visualizer_UI.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(839, 739)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.listImageNames = QtWidgets.QListView(parent=self.centralwidget)
        self.listImageNames.setTabKeyNavigation(True)
        self.listImageNames.setFlow(QtWidgets.QListView.Flow.LeftToRight)
        self.listImageNames.setProperty("isWrapping", True)
        self.listImageNames.setObjectName("listImageNames")
        self.gridLayout_3.addWidget(self.listImageNames, 0, 1, 2, 1)
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(470, 70))
        self.frame.setMaximumSize(QtCore.QSize(470, 70))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.frame.setObjectName("frame")
        self.lblImageName = QtWidgets.QLabel(parent=self.frame)
        self.lblImageName.setGeometry(QtCore.QRect(10, 40, 87, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblImageName.sizePolicy().hasHeightForWidth())
        self.lblImageName.setSizePolicy(sizePolicy)
        self.lblImageName.setIndent(-1)
        self.lblImageName.setObjectName("lblImageName")
        self.lblImageType = QtWidgets.QLabel(parent=self.frame)
        self.lblImageType.setGeometry(QtCore.QRect(230, 40, 87, 21))
        self.lblImageType.setIndent(-1)
        self.lblImageType.setObjectName("lblImageType")
        self.lblImagePath = QtWidgets.QLabel(parent=self.frame)
        self.lblImagePath.setGeometry(QtCore.QRect(10, 10, 87, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblImagePath.sizePolicy().hasHeightForWidth())
        self.lblImagePath.setSizePolicy(sizePolicy)
        self.lblImagePath.setIndent(-1)
        self.lblImagePath.setObjectName("lblImagePath")
        self.txtImageName = QtWidgets.QLineEdit(parent=self.frame)
        self.txtImageName.setGeometry(QtCore.QRect(80, 40, 131, 21))
        self.txtImageName.setObjectName("txtImageName")
        self.txtImagePath = QtWidgets.QLineEdit(parent=self.frame)
        self.txtImagePath.setGeometry(QtCore.QRect(80, 10, 291, 21))
        self.txtImagePath.setObjectName("txtImagePath")
        self.comboImageType = QtWidgets.QComboBox(parent=self.frame)
        self.comboImageType.setGeometry(QtCore.QRect(300, 40, 68, 21))
        self.comboImageType.setEditable(False)
        self.comboImageType.setPlaceholderText("")
        self.comboImageType.setObjectName("comboImageType")
        self.comboImageType.addItem("")
        self.comboImageType.addItem("")
        self.comboImageType.addItem("")
        self.btnImagePath = QtWidgets.QPushButton(parent=self.frame)
        self.btnImagePath.setGeometry(QtCore.QRect(380, 10, 75, 24))
        self.btnImagePath.setMinimumSize(QtCore.QSize(0, 24))
        self.btnImagePath.setMaximumSize(QtCore.QSize(16777215, 24))
        self.btnImagePath.setObjectName("btnImagePath")
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)
        self.frameAnnotation = QtWidgets.QFrame(parent=self.centralwidget)
        self.frameAnnotation.setMinimumSize(QtCore.QSize(470, 110))
        self.frameAnnotation.setMaximumSize(QtCore.QSize(470, 110))
        self.frameAnnotation.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frameAnnotation.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.frameAnnotation.setObjectName("frameAnnotation")
        self.lblAnnotationPath = QtWidgets.QLabel(parent=self.frameAnnotation)
        self.lblAnnotationPath.setGeometry(QtCore.QRect(10, 30, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblAnnotationPath.sizePolicy().hasHeightForWidth())
        self.lblAnnotationPath.setSizePolicy(sizePolicy)
        self.lblAnnotationPath.setWordWrap(True)
        self.lblAnnotationPath.setIndent(-1)
        self.lblAnnotationPath.setObjectName("lblAnnotationPath")
        self.txtAnnotationPath = QtWidgets.QLineEdit(parent=self.frameAnnotation)
        self.txtAnnotationPath.setGeometry(QtCore.QRect(150, 40, 221, 21))
        self.txtAnnotationPath.setObjectName("txtAnnotationPath")
        self.btnAnnotationPath = QtWidgets.QPushButton(parent=self.frameAnnotation)
        self.btnAnnotationPath.setGeometry(QtCore.QRect(380, 40, 75, 24))
        self.btnAnnotationPath.setObjectName("btnAnnotationPath")
        self.checkBoxCaptioning = QtWidgets.QCheckBox(parent=self.frameAnnotation)
        self.checkBoxCaptioning.setGeometry(QtCore.QRect(40, 10, 101, 21))
        self.checkBoxCaptioning.setObjectName("checkBoxCaptioning")
        self.lblAnnotationPathDetectionSegmentation = QtWidgets.QLabel(parent=self.frameAnnotation)
        self.lblAnnotationPathDetectionSegmentation.setGeometry(QtCore.QRect(10, 70, 141, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblAnnotationPathDetectionSegmentation.sizePolicy().hasHeightForWidth())
        self.lblAnnotationPathDetectionSegmentation.setSizePolicy(sizePolicy)
        self.lblAnnotationPathDetectionSegmentation.setWordWrap(True)
        self.lblAnnotationPathDetectionSegmentation.setIndent(-1)
        self.lblAnnotationPathDetectionSegmentation.setObjectName("lblAnnotationPathDetectionSegmentation")
        self.btnAnnotationPathDetetctionSegmentation = QtWidgets.QPushButton(parent=self.frameAnnotation)
        self.btnAnnotationPathDetetctionSegmentation.setGeometry(QtCore.QRect(380, 80, 75, 24))
        self.btnAnnotationPathDetetctionSegmentation.setObjectName("btnAnnotationPathDetetctionSegmentation")
        self.txtAnnotationPathDetectionSegmentation = QtWidgets.QLineEdit(parent=self.frameAnnotation)
        self.txtAnnotationPathDetectionSegmentation.setGeometry(QtCore.QRect(150, 80, 221, 21))
        self.txtAnnotationPathDetectionSegmentation.setObjectName("txtAnnotationPathDetectionSegmentation")
        self.comboDetectionSegmentation = QtWidgets.QComboBox(parent=self.frameAnnotation)
        self.comboDetectionSegmentation.setGeometry(QtCore.QRect(150, 10, 261, 22))
        self.comboDetectionSegmentation.setObjectName("comboDetectionSegmentation")
        self.comboDetectionSegmentation.addItem("")
        self.comboDetectionSegmentation.addItem("")
        self.comboDetectionSegmentation.addItem("")
        self.gridLayout_3.addWidget(self.frameAnnotation, 1, 0, 1, 1)
        self.gridLayout_3.setRowStretch(0, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.verticalWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.verticalWidget_2.sizePolicy().hasHeightForWidth())
        self.verticalWidget_2.setSizePolicy(sizePolicy)
        self.verticalWidget_2.setMinimumSize(QtCore.QSize(821, 0))
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.verticalWidget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.btnPrevious = QtWidgets.QPushButton(parent=self.verticalWidget_2)
        self.btnPrevious.setObjectName("btnPrevious")
        self.gridLayout.addWidget(self.btnPrevious, 0, 0, 1, 1)
        self.graphicsImageDisplay = QtWidgets.QGraphicsView(parent=self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsImageDisplay.sizePolicy().hasHeightForWidth())
        self.graphicsImageDisplay.setSizePolicy(sizePolicy)
        self.graphicsImageDisplay.setObjectName("graphicsImageDisplay")
        self.gridLayout.addWidget(self.graphicsImageDisplay, 2, 0, 1, 4)
        self.graphicsImageDisplay2 = QtWidgets.QGraphicsView(parent=self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsImageDisplay2.sizePolicy().hasHeightForWidth())
        self.graphicsImageDisplay2.setSizePolicy(sizePolicy)
        self.graphicsImageDisplay2.setMinimumSize(QtCore.QSize(0, 0))
        self.graphicsImageDisplay2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.graphicsImageDisplay2.setObjectName("graphicsImageDisplay2")
        self.gridLayout.addWidget(self.graphicsImageDisplay2, 2, 4, 1, 1)
        self.btnNext = QtWidgets.QPushButton(parent=self.verticalWidget_2)
        self.btnNext.setObjectName("btnNext")
        self.gridLayout.addWidget(self.btnNext, 0, 1, 1, 1)
        self.btnShowImage = QtWidgets.QPushButton(parent=self.verticalWidget_2)
        self.btnShowImage.setObjectName("btnShowImage")
        self.gridLayout.addWidget(self.btnShowImage, 0, 6, 1, 1)
        self.txtCaptions = QtWidgets.QTextBrowser(parent=self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtCaptions.sizePolicy().hasHeightForWidth())
        self.txtCaptions.setSizePolicy(sizePolicy)
        self.txtCaptions.setReadOnly(False)
        self.txtCaptions.setObjectName("txtCaptions")
        self.gridLayout.addWidget(self.txtCaptions, 2, 5, 1, 2)
        self.graphicsViewLegend = QtWidgets.QGraphicsView(parent=self.verticalWidget_2)
        self.graphicsViewLegend.setMinimumSize(QtCore.QSize(0, 40))
        self.graphicsViewLegend.setMaximumSize(QtCore.QSize(16777215, 40))
        self.graphicsViewLegend.setObjectName("graphicsViewLegend")
        self.gridLayout.addWidget(self.graphicsViewLegend, 3, 0, 1, 7)
        self.verticalLayout_3.addWidget(self.verticalWidget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 839, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboImageType.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Visualize ACID Dataset"))
        self.lblImageName.setText(_translate("MainWindow", "Image name"))
        self.lblImageType.setText(_translate("MainWindow", "Image type"))
        self.lblImagePath.setText(_translate("MainWindow", "Image path"))
        self.comboImageType.setItemText(0, _translate("MainWindow", "JPG"))
        self.comboImageType.setItemText(1, _translate("MainWindow", "PNG"))
        self.comboImageType.setItemText(2, _translate("MainWindow", "TIFF"))
        self.btnImagePath.setText(_translate("MainWindow", "Browse"))
        self.lblAnnotationPath.setText(_translate("MainWindow", "Annotation path for captioning"))
        self.btnAnnotationPath.setText(_translate("MainWindow", "Browse"))
        self.checkBoxCaptioning.setText(_translate("MainWindow", "Captioning"))
        self.lblAnnotationPathDetectionSegmentation.setText(_translate("MainWindow", "Annotation path for Instance Segmentation"))
        self.btnAnnotationPathDetetctionSegmentation.setText(_translate("MainWindow", "Browse"))
        self.comboDetectionSegmentation.setItemText(0, _translate("MainWindow", "None"))
        self.comboDetectionSegmentation.setItemText(1, _translate("MainWindow", "Object Detection (VOC Format)"))
        self.comboDetectionSegmentation.setItemText(2, _translate("MainWindow", "Instance Segmentation (COCO Format)"))
        self.btnPrevious.setText(_translate("MainWindow", "Previous Image"))
        self.btnNext.setText(_translate("MainWindow", "Next Image"))
        self.btnShowImage.setText(_translate("MainWindow", "Show Image and Annotations"))
