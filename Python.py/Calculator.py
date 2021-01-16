print ("WELCOME TO THE VIVAAN'S PYTHON CALCULATER")
NUM1=1
NUM2=2
NUM1=input ("TELL NUMBER 1  ")
NUM2=input ("TELL NUMBER 2  ")
NUMBERS=input ("WHAT OPREATOIN DO YOU WANT TO DO WITH THEASE NUMBERS ? (+,-,*,/)  ")
if NUM1==(""):
    print ("YOUR NUMBER 1 IS BEING CONSIDERD AS 0")
    NUM1=0
if NUMBERS==("+"):
    RESULT= int(NUM1)+ int(NUM2)or(NUM1)+int(NUM2)
    print (RESULT)
elif NUMBERS==("-"):
    RESULT= int(NUM1)- int(NUM2)or(NUM1)-int(NUM2)
    print (RESULT)    
elif NUMBERS==("*"):
    RESULT= int(NUM1)* int(NUM2)or(NUM1)*int(NUM2)
    print (RESULT)
elif NUMBERS==("/"):
    RESULT= int(NUM1)/ int(NUM2)or(NUM1)/int(NUM2)
    print (RESULT)    

