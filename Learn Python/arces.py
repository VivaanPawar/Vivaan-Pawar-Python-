# def func(a,b,c,d,e):
#     print (a,b,c,d,e)

# func("Vivaan","Rachit","Shaurya","Besties","Keshav") 


def viv(*args):
    # print(args[0])
    for items in args:
        print(items)


vivp = ["Vivaan","Rachit","Shaurya","Besties","Keshav" ]   
viv(*vivp) 

print (viv())