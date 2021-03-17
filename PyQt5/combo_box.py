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
		#CReating Combo Box
		my_combo = qtw.QComboBox(self,
			editable=True,
			insertPolicy=qtw.QComboBox.InsertAtTop)
		#Add Items To COmbo QComboBox
		my_combo.addItem("Pizza",1)
		my_combo.addItem("Burger",2)
		my_combo.addItem("Fries",3)
		my_combo.addItem("Sweets",4)		
		my_combo.addItem("Chicken",5)
		my_combo.addItem("Mutton",6)
		# COmbo Box On Screen
		self.layout().addWidget(my_combo)
		#Creating Button
		my_btn =  qtw.QPushButton("Click Here",
				clicked = lambda: click())
		self.layout().addWidget(my_btn)
		
		self.show()
		
		def click():
			my_label.setText(f"You Chossed {my_combo.currentText()}!")
		
		
app = qtw.QApplication([])
mw = window()

#Run App
app.exec_()
		
