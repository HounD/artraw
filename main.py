#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui


class Artraw(QtGui.QWidget):

	def __init__(self):
		super(Artraw, self).__init__()

		self.initUI()


	def initUI(self):

		self.setGeometry(300, 300, 300, 220)
		self.setWindowTitle('Artraw')

		self.show()


if __name__ == '__main__':
    
    app = QtGui.QApplication(sys.argv)
    ex = Artraw()    
    
    sys.exit(app.exec_())
