
# ===========================================================================================
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar

p1, p2 = 'player1', 'player2'
z = 0
sX, sO = 0, 0
player = 'X'


def playAgain():
    global stop_game
    stop_game = False
    enableAllButton()
    for i in range(3):
        for j in range(3):
            states[i][j] = 0
            b[i][j].configure(text='', bg='powder blue')


def score():
    global player, Z, sX, sO, root
    won = Z  # states [i] [o]
    nextPlay.config(state=DISABLED)
    if won == 'X':
        sX += 1
        scoreX.config(text="{}[X]: {}".format(p1, sX))
    elif won == 'O':
        sO += 1
        scoreO.config(text="{}[O]: {}".format(p1, sX))
    # if score three game over
    if sX == 3 or sO == 3:
        stop_game = True
        Winner = messagebox.askyesno("Game Over",
                                     "Highest score:\n\t{}\n\t{}\nDo You Want to Play Again??".format(
                                         scoreX.cget('text'), scoreO.cget('text')))
        if Winner == True:
            playAgain()
            sX, sO = 0, 0
            scoreX.config(text="{}[X]: {}".format(p1, sX))
            scoreO.config(text="{}[O]: {}".format(p1, sX))
        elif Winner == False:
            exiting = messagebox.showinfo("Come Soon",
                                          "Hope You All enjoyed the game.\n game is exiting")
            root.destroy


def disableAllButton():
    for i in range(3):
        for j in range(3):
            b[i][j].config(state=DISABLED)


def enableAllButton():
    for i in range(3):
        for j in range(3):
            b[i][j].config(state=NORMAL)


def getName():
    global player, p1, p2, player1E, player2E
    p1 = player1E.get()
    p2 = player2E.get()
    print("Player1 : ", p1, "player2: ", p2)
    scoreX.config(text="{}[X]: 0".format(p1))
    scoreO.config(text="{}[X]: 0".format(p2))
    root.deiconify()
    mainWindow.destroy()


def load():
    global i, progress, loadingLabel
    loadingLabel = Label(mainWindow, text='', font=(
        'arial', 10, 'bold'), fg='blue')
    loadingLabel.place(x=400, y=420)
    progress = Progressbar(mainWindow, orient=HORIZONTAL, length=250,
                           mode='determinate')
    progress.place(x=150, y=420)
    if i <= 10:
        txt = str(10 * i) + '%'
        loadingLabel.config(text=txt)
        loadingLabel.after(1000, load)
        progress['value'] = int(10 * i)
        i += 1
    if progress['value'] == 100:
        getName()
# ====================================Two players mode========================================


def mode2():
    global player1E, player2E
    mode.destroy()
    singleMode.destroy()
    twoMode.destroy()
    player1 = Label(mainWindow, text="Player 1 Name:", bg='red',
                    font=('arial', 10), fg='white')
    player1.place(x=200, y=330)
    player1E = Entry(mainWindow, fg='blue', highlightbackground='blue',
                     highlightthickness=2, width=30)
    player1E.place(x=310, y=330)

    player2 = Label(mainWindow, text="Player 2 Name:", bg='red',
                    font=('arial', 10), fg='white')
    player2.place(x=200, y=360)
    player2E = Entry(mainWindow, fg='blue', highlightbackground='blue',
                     highlightthickness=2, width=30)
    player2E.place(x=310, y=360)

    submit = Button(mainWindow, text="Play Game", bg='Blue', fg='white',
                    width=15, command=load)
    submit.place(x=280, y=390)

# ==================================Exit Game=================================================


def exitWindow(e):
    try:
        mainWindow.wm_attributes('-topmost', False)
        msg = messagebox.askyesno(title='Exit Game',
                                  message='Do You Realy Wanna Exit The Game??')

    except:
        msg = messagebox.askyesno(title='Exit Game',
                                  message='Do You Realy Wanna Exit The Game??')
    if msg == True:
        sys.exit(root.destroy())
# ===========================Def=============================================================


def callback(r, c):
    global player
    if player == 'X' and states[r][c] == 0 and stop_game == False:
        b[r][c].configure(text='X', fg='blue', bg='white')
        states[r][c] = 'X'
        player = 'O'
    if player == 'O' and states[r][c] == 0 and stop_game == False:
        b[r][c].configure(text='O', fg='orange', bg='black')
        states[r][c] = 'O'
        player = 'X'
    check_for_winner()
# =============================Check For Winner==============================================


def check_for_winner():
    global stop_game, Z

    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] != 0:
            b[i][0].configure(bg='grey')
            b[i][1].configure(bg='grey')
            b[i][2].configure(bg='grey')
            stop_game = True
            Z = states[i][0]  # counting winning score

            winner = messagebox.showinfo("Winner", states[i][0] + 'Won')
            disableAllButton()
            score()
            break

        elif states[0][i] == states[1][i] == states[2][i] != 0:
            b[0][i].configure(bg='grey')
            b[1][i].configure(bg='grey')
            b[2][i].configure(bg='grey')
            stop_game = True
            Z = states[0][i]  # Counting winner score

            winner = messagebox.showinfo("Winner", states[1][i] + 'Won!')
            disableAllButton()
            score()
            break

        elif states[2][0] == states[1][1] == states[0][2] != 0:
            b[2][0].configure(bg='grey')
            b[1][1].configure(bg='grey')
            b[0][2].configure(bg='grey')
            stop_game = True
            Z = states[2][0]  # Counting winner score

            winner = messagebox.showinfo("Winner", states[1][1] + 'Won!')
            disableAllButton()
            score()
            break

    nextPlay.config(text="PLAY AGAIN", bg='red', state=NORMAL)


# ===================game deisgned============================================================
root = Tk()
root.title('Tic Tac Toe')
root.resizable(0, 0)

# ==================================image of the game=========================================
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(
    file='/home/vivaan/Documents/Programming/Python/Images/Image.gif'))
root.bind('<Escape>', exitWindow)  # Escape key to exit
bg = PhotoImage(
    file="/home/vivaan/Documents/Programming/Python/Images/Image.gif")
bgImage = Label(root, image=bg).place(x=-60, y=0)

# ================================Buttons=====================================================
b = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
# ==============================Text Buttons==================================================
states = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(3):
    for j in range(3):
        b[i][j] = Button(font=('Verdana', 60), width=3, bg='powder blue',
                         command=lambda r=i, c=j: callback(r, c))
        b[i][j].grid(row=i, column=j)

# =============================Writting name of both players==================================
mainWindow = Toplevel(root)
mainWindow.title("TIC TAC TOE")
mainWindow.resizable(0, 0)
mainWindow.config(bg='green')
mainWindow.bind('<Escape>', exitWindow)

# ====================================EXTRA DESIGNS===========================================
height = 450
width = 580
x = (root.winfo_screenwidth()//2) - (width // 2)
y = (root.winfo_screenheight()//2) - (height // 2)
mainWindow.geometry("{}x{}+{}+{}".format(width, height, x, y))
mainWindow.overrideredirect(1)
mainWindow.wm_attributes('-topmost', True)

# ===============================More UI design===============================================
bgImage = Label(mainWindow, image=bg).place(x=-30, y=0)

devBy = Label(mainWindow, text="TIC TAC TOE",
              font=('mistral', 10, 'bold'), fg='blue', bg='powder blue', width=150)
devBy.pack(side=TOP)
# =========================Choosing single or double player===================================
mode = Label(mainWindow, text='CHOOSE MODE', bg='blue', fg='goldenrod1',
             font=('impact', 12,), width=20)
mode.place(x=180, y=220)
# ===============================Hover Affect for multiplayer=================================


def onButtonT(e):
    twoMode['bg'] = 'goldenrod3'


def leaveButtonT(e):
    twoMode['bg'] = 'goldenrod1'

# ===============================Hover Affect For single player===============================


def onButtonS(e):
    singleMode['bg'] = 'goldenrod3'


def leaveButtonS(e):
    singleMode['bg'] = 'goldenrod1'


# =============================Single Player mode=============================================
singleMode = Button(mainWindow, text='Single Player', bg='goldenrod1', width=20,
                    activebackground='goldenrod3', activeforeground='blue')
singleMode.place(x=190, y=250)
singleMode.bind('<Enter>', onButtonS)
singleMode.bind('<Leave>', leaveButtonS)
# ==========================Two Player Mod ===================================================
twoMode = Button(mainWindow, text='Two player', bg='goldenrod1', width=20,
                 activebackground='goldenrod3', activeforeground='blue', command=mode2)
twoMode.place(x=190, y=280)
twoMode.bind('<Enter>', onButtonT)
twoMode.bind('<Leave>', leaveButtonT)
# ================================play again button===========================================
nextPlay = Button(root, text="", width=10, bd=0, command=playAgain)
nextPlay.grid(row=4, column=1)

scoreX = Label(root, text="Score X:", font=('mistral', 12))
scoreX.grid(row=4, column=0)

scoreO = Label(root, text="Score O:", font=('mistral', 12))
scoreO.grid(row=4, column=2)
stop_game = False

copyri8 = Label(root, text="Developed by Vivaan Pawar",
                font=('mistral', 12, 'bold'), fg='blue', bg='powder blue', width=70)
copyri8.grid(row=5, columnspan=3)
root.withdraw()

# =====================================END====================================================
root.mainloop()
