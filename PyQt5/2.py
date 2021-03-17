import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class window(qtw.QWidget):
	def  __init__(self):
		super().__init__()
		# add title

		self.setWindowTitle("Vivaan")
		self.setLayout(qtw.QVBoxLayout())
		#Creat Label
		my_label = qtw.QLabel("Hello World! What IS You'r Name")
		#Changing Font Syle
		my_label.setFont(qtg.QFont('Helvetica', 22))
		self.layout().addWidget(my_label)
		#CReating Entry Box
		my_entry = qtw.QLineEdit()
		my_entry.setObjectName("entry")
		my_entry.setText("Name..")
		self.layout().addWidget(my_entry)
		#Creating Button
		my_btn =  qtw.QPushButton("Click Here",
				clicked = lambda: click())
		self.layout().addWidget(my_btn)
		
		self.show()
		
		def click():
			my_label.setText(f"Hello{my_entry.text()}!")
			#Clearing Text Box
			my_entry.setText("Name..")
		
		
app = qtw.QApplication([])
mw = window()

#Run App
app.exec_()
		
