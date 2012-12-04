import sys, time, threading
from PyQt4 import QtGui, QtCore
from gui import Ui_MainWindow
from xmpp import *

class GStatusSetter(QtGui.QMainWindow):
	def __init__(self):
		super(GStatusSetter, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.show()
		self.thread = None
		self.ui.start.clicked.connect(self.start)
		self.ui.stop.clicked.connect(self.stop)

	def start(self):
		self.enabled = True
		self.interval = int(self.ui.interval.text())
		self.index = 0
		self.statuses = self.ui.statuses.toPlainText().split('\n')
		if self.thread == None:
			self.thread = threading.Thread(target=self.run)
			self.thread.start()

	def run(self):
		while self.enabled:
			self.setStatus(self.statuses[self.index])
			self.index = (self.index + 1) % len(self.statuses)
			time.sleep(self.interval)
		self.thread = None
	
	def stop(self):
		self.enabled = False

	def setStatus(self, statusmsg):
		client = Client(server='gmail.com', debug=[])
		if not client.connect(server=('talk.google.com', 5222)):
			raise IOError('Cannot connect to server')
		if not client.auth(self.ui.username.text(), self.ui.password.text(), 'gmail.com'):
			raise IOError('Authentication failed')
		client.send(Iq('set', 'google:shared-status', payload=[
					Node('show', payload=['dnd']),
					Node('status', payload=[statusmsg])
					]))
		client.disconnect()

if __name__ == '__main__':
	qApp = QtGui.QApplication(sys.argv)
	gs = GStatusSetter()
	sys.exit(qApp.exec_())
