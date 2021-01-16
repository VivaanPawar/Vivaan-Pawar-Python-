# lv = [ ["Vivaan",8],["Rachit",2],["Shaurya",10],["Besties",1208] ]
# # print (lv)                      
# for item,birthday in lv:
#     print(item,"Birth Date is",birthday)
i = [int,float,"Vivaan",5,23,46,2317,236,7,2,0]

for item in i:
    if str(item).isnumeric() and item>6:
        print(item)