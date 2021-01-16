task =1

def vivfun(task):
  if task==1:
    print("You have chosen to add") 
    vivmenu()
  elif task==2:
    print("You haev chosen to subsctract")
    vivmenu()
  elif task ==3:
    print("You have chosen to multiply")
    vivmenu()
  elif task ==4:
    print("You have chosen to divide")
    vivmenu()
  elif task ==5:
    print("You Quit")
    exit()
  else:
    print ("Chose from (1-5)")  
    
def vivmenu():
  print("Please chose what you want to do. Input the number displaying against the task")
  print("1. Add")
  print("2. Substract")
  print("3. multiply")
  print("4. divide")
  print("5. Quite")
  task=int(input ("Please enter the task number \n" ))
  vivfun(task)

task=vivmenu()
while task != 5:
  vivmenu()


    



