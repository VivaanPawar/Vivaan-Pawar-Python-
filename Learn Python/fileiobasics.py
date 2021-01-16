'''
"r" = open file for reading - deafualt
"w" = Open File For Writing
"x" = Creates file if not exist
"a" = Add More content to file 
"t" = Text mode - deafualt
"b" = Binary Mode
"+" = Open File to update (read and write)
'''
f = open("viv.txt","a")
f.write("Ok So I Am Replacing FIle Content\n line")
f.close()
# content = f.read(135)
# print (content)

# for line in content:
#     print(line)

# for line in f:
#     print(line, end = "\n")
# f.close()