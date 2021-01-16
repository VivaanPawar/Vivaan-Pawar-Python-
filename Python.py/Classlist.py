print ("Hi")
classmate = ["Arav","Ahaan","Ananaya","Arnav","Bhaumik","Jhanvey","Prisa","Prince","Rachit","Shaurya","Vivaan"]
for x in classmate:
         print (x)
ask= str(input("What Do You Want To Do:\n"))          
if ask ==  ("add"or"ADD"):
    a = str(input("Tell the name that you want to add:\n"))            
    classmate.append(a)
    for x in classmate:
        print (x)
else:
    b = str(input("Tell the name that you want to remove\n"))
    classmate.remove(b)
    for x in classmate:
         print (x)





                       
                       

            
            
            
            


            




