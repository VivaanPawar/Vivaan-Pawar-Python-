import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class window(qtw.QWidget):
	def  __init__(self):
		super().__init__()
		# add title

		self.setWindowTitle("Vivaan")
		self.setLayout(qtw.QVBoxLayout())
		#Creat Label
		my_label = qtw.QLabel("Write Something")
		#Changing Font Syle
		my_label.setFont(qtg.QFont('Helvetica', 22))
		self.layout().addWidget(my_label)
		#CReating text Box
		my_text = qtw.QTextEdit(self,
			lineWrapMode=qtw.QTextEdit,
			lineWrapColumnOrWidth=50,
			placeholderText="Type Here...",
			readOnly=False)
		# text Box On Screen
		self.layout().addWidget(my_text)
		#Creating Button
		my_btn =  qtw.QPushButton("Click Here",
				clicked = lambda: click())
		self.layout().addWidget(my_btn)
		
		self.show()
		
		def click():
			my_label.setText(f"You Wrote {my_text.toPlainText()}!")
		
		
app = qtw.QApplication([])
mw = window()

#Run App
app.exec_()
		
