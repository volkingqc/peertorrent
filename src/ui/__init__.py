# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'peertorrent.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("PeerTorrent")
        MainWindow.setFixedSize(939, 643)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("feather_icons/users.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chatFrame = QtWidgets.QFrame(self.centralwidget)
        self.chatFrame.setGeometry(QtCore.QRect(10, 10, 401, 551))
        self.chatFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chatFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chatFrame.setObjectName("chatFrame")
        self.inputMsg = QtWidgets.QLineEdit(self.chatFrame)
        self.inputMsg.setGeometry(QtCore.QRect(10, 500, 281, 41))
        self.inputMsg.setObjectName("inputMsg")
        self.sendMsg = QtWidgets.QPushButton(self.chatFrame)
        self.sendMsg.setGeometry(QtCore.QRect(300, 500, 91, 41))
        self.sendMsg.setObjectName("sendMsg")
        self.areaMsg = QtWidgets.QTextEdit(self.chatFrame)
        self.areaMsg.setGeometry(QtCore.QRect(10, 60, 381, 431))
        self.areaMsg.setReadOnly(True)
        self.areaMsg.setObjectName("areaMsg")
        self.headMsg = QtWidgets.QLabel(self.chatFrame)
        self.headMsg.setGeometry(QtCore.QRect(20, 10, 371, 41))
        self.headMsg.setAlignment(QtCore.Qt.AlignCenter)
        self.headMsg.setObjectName("headMsg")
        self.transferFrame = QtWidgets.QFrame(self.centralwidget)
        self.transferFrame.setGeometry(QtCore.QRect(420, 10, 511, 551))
        self.transferFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.transferFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.transferFrame.setObjectName("transferFrame")
        self.progBar = QtWidgets.QProgressBar(self.transferFrame)
        self.progBar.setGeometry(QtCore.QRect(10, 510, 491, 31))
        self.progBar.setProperty("value", 0)
        self.progBar.setObjectName("progBar")
        self.headLbl = QtWidgets.QLabel(self.transferFrame)
        self.headLbl.setGeometry(QtCore.QRect(10, 10, 491, 41))
        self.headLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.headLbl.setObjectName("headLbl")
        self.progLbl = QtWidgets.QLabel(self.transferFrame)
        self.progLbl.setGeometry(QtCore.QRect(230, 490, 58, 18))
        self.progLbl.setObjectName("progLbl")
        self.nameLbl = QtWidgets.QLabel(self.transferFrame)
        self.nameLbl.setGeometry(QtCore.QRect(140, 90, 261, 51))
        self.nameLbl.setObjectName("nameLbl")
        self.peerLbl = QtWidgets.QLabel(self.transferFrame)
        self.peerLbl.setGeometry(QtCore.QRect(140, 150, 261, 51))
        self.peerLbl.setObjectName("peerLbl")
        self.uplLbl = QtWidgets.QLabel(self.transferFrame)
        self.uplLbl.setGeometry(QtCore.QRect(140, 210, 261, 51))
        self.uplLbl.setObjectName("uplLbl")
        self.dwnLbl = QtWidgets.QLabel(self.transferFrame)
        self.dwnLbl.setGeometry(QtCore.QRect(140, 270, 261, 51))
        self.dwnLbl.setObjectName("dwnLbl")
        self.saveLbl = QtWidgets.QLabel(self.transferFrame)
        self.saveLbl.setGeometry(QtCore.QRect(140, 330, 261, 51))
        self.saveLbl.setObjectName("saveLbl")
        self.statLbl = QtWidgets.QLabel(self.transferFrame)
        self.statLbl.setGeometry(QtCore.QRect(140, 390, 261, 51))
        self.statLbl.setObjectName("statLbl")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 939, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.magnetBtn = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("feather_icons/link.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.magnetBtn.setIcon(icon1)
        self.magnetBtn.setObjectName("magnetBtn")
        self.torrentBtn = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("feather_icons/file-plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.torrentBtn.setIcon(icon2)
        self.torrentBtn.setVisible(True)
        self.torrentBtn.setObjectName("torrentBtn")
        self.actionStop_Torrent = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("feather_icons/x-octagon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStop_Torrent.setIcon(icon3)
        self.actionStop_Torrent.setObjectName("actionStop_Torrent")
        self.actionStop_Delete_Torrent = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("feather_icons/trash-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStop_Delete_Torrent.setIcon(icon4)
        self.actionStop_Delete_Torrent.setObjectName("actionStop_Delete_Torrent")
        self.menuFile.addAction(self.magnetBtn)
        self.menuFile.addAction(self.torrentBtn)
        self.menuFile.addAction(self.actionStop_Torrent)
        self.menuFile.addAction(self.actionStop_Delete_Torrent)
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar.addAction(self.magnetBtn)
        self.toolBar.addAction(self.torrentBtn)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionStop_Torrent)
        self.toolBar.addAction(self.actionStop_Delete_Torrent)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PeerTorrent"))
        self.inputMsg.setPlaceholderText(_translate("MainWindow", "Send a global message."))
        self.sendMsg.setText(_translate("MainWindow", "Send"))
        self.headMsg.setText(_translate("MainWindow", "Chat\n"
"Please act civil and respectful in the discussions!"))
        self.headLbl.setText(_translate("MainWindow", "PeerTorrent only works single-threaded\n"
"meaning it will download only one torrent at a time."))
        self.progLbl.setText(_translate("MainWindow", "Progress:"))
        self.nameLbl.setText(_translate("MainWindow", "Torrent Name: None"))
        self.peerLbl.setText(_translate("MainWindow", "Peer Count: None"))
        self.uplLbl.setText(_translate("MainWindow", "Upload Speed: None"))
        self.dwnLbl.setText(_translate("MainWindow", "Download Speed: None"))
        self.saveLbl.setText(_translate("MainWindow", "Save Path: None"))
        self.statLbl.setText(_translate("MainWindow", "Status: None"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.magnetBtn.setText(_translate("MainWindow", "Add Torrent Magnet"))
        self.torrentBtn.setText(_translate("MainWindow", "Add Torrent File"))
        self.actionStop_Torrent.setText(_translate("MainWindow", "Stop Torrent (No Delete)"))
        self.actionStop_Delete_Torrent.setText(_translate("MainWindow", "Stop and Delete Torrent"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())