l = 10 # Global

def function1(n):
    # l = 5 #Local
    m = 8 #Local
    global l
    l = l + 45
    print(l, m)
    print(n, "I have printed")

function1("This is me")
# print(m)

x = 89
def viv():
    x = 20
    def vivaan():
        global x
        x = 88
    print("before calling vivaan()", x)
    vivaan()
    print("after calling vivaan()", x)

viv()
print(x)





  
