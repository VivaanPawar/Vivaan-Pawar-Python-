print("WELCOME TO VIVAAN PYTHON CALENDAR")
import calendar
year = int(input("ENTER THE YEAR:  ") )
month=int(input("ENTER THE MONTH:  ") ) 

vivaancal=calendar.month(year,month)
print(vivaancal)
