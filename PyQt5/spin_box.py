import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class window(qtw.QWidget):
	def  __init__(self):
		super().__init__()
		# add title

		self.setWindowTitle("Vivaan")
		self.setLayout(qtw.QVBoxLayout())
		#Creat Label
		my_label = qtw.QLabel("Choose Something")
		#Changing Font Syle
		my_label.setFont(qtg.QFont('Helvetica', 22))
		self.layout().addWidget(my_label)
		#CReating spin Box
		my_spin = qtw.QSpinBox(self,
			value=10,
			maximum=100,
			minimum=0,
			singleStep=3)
		# spin Box On Screen
		self.layout().addWidget(my_spin)
		#Creating Button
		my_btn =  qtw.QPushButton("Click Here",
				clicked = lambda: click())
		self.layout().addWidget(my_btn)
		
		self.show()
		
		def click():
			my_label.setText(f"You Chossed {my_spin.value()}!")
		
		
app = qtw.QApplication([])
mw = window()

#Run App
app.exec_()
		
