from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class myPersonalSpace():

	def __init__(self):
		

		self.window = QWidget()
		self.window.setWindowTitle("My Personal Browser")

		self.layout = QVBoxLayout()
		self.horizontal = QHBoxLayout()

		self.urlBar = QTextEdit()
		self.urlBar.setMaximumHeight(30)

		self.goButton = QPushButton("Go")
		self.goButton.setMinimumHeight(30)

		self.backButton = QPushButton("<")
		self.backButton.setMinimumHeight(30)

		self.fwdButton = QPushButton(">")
		self.fwdButton.setMinimumHeight(30)

		self.horizontal.addWidget(self.urlBar)
		self.horizontal.addWidget(self.goButton)
		self.horizontal.addWidget(self.backButton)
		self.horizontal.addWidget(self.fwdButton)

		self.browser = QWebEngineView()

		self.goButton.clicked.connect(lambda: self.navigfunction(self.urlBar.toPlainText()))
		self.backButton.clicked.connect(self.browser.back)
		self.fwdButton.clicked.connect(self.browser.forward)

		self.layout.addLayout(self.horizontal)
		self.layout.addWidget(self.browser)

		self.browser.setUrl(QUrl("https://duckduckgo.com/"))

		self.window.setLayout(self.layout)
		self.window.show()

	def navigfunction(self, url):
		if not url.startswith("http"):
			url = "http://" + url
			self.urlBar.setText(url)
		self.browser.setUrl(QUrl(url))



app = QApplication([])
window =  myPersonalSpace()
app.exec_()