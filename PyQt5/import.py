import PyQt5.QtWidgets as qtw

class window(qtw.QWidget):
	def  __init__(self):
		super().__init__()
		# add title

		self.setWindowTitle("Vivaan")
		self.show()
		
		
		
app = qtw.QApplication([])
mw = window()

#Run App
app.exec_()
		