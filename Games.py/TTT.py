from tkinter import *


root = Tk()
root.title("Tic Tac Toe")


def callback(r, c):
    global player

    if player == "X" and states[r][c] == 0 and stop_game == False:
        b[r][c].configure(text="X", fg="blue", bg="white")
        states[r][c] = "X"
        player = "O"
    if player == "O" and states[r][c] == 0 and stop_game == False:
        b[r][c].configure(text="O", fg="orange", bg="black")
        states[r][c] = "O"
        player = "X"
    check_for_winner()


def check_for_winner():
    global stop_game
    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] != 0:
            b[i][0].config(bg="grey")
            b[i][1].config(bg="grey")
            b[i][2].config(bg="grey")
            stop_game = True
    for g in range(3):
        if states[0][i] == states[1][i] == states[2][i] != 0:
            b[3][i].config(bg="grey")
            b[4][i].config(bg="grey")
            b[5][i].config(bg="grey")
            stop_game = True
        if states[0][0] == states[1][1] == states[2][2] != 0:
            b[i][6].config(bg="grey")
            b[i][7].config(bg="grey")
            b[i][8].config(bg="grey")
            stop_game = True
        if states[2][0] == states[1][1] == states[0][2] != 0:
            b[9][i].config(bg="grey")
            b[10][i].config(bg="grey")
            b[11][i].config(bg="grey")
            stop_game = True


b = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
states = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
for i in range(3):
    for j in range(3):
        b[i][j] = Button(font=("Arial", 60), width=4, bg="powder blue",
                         command=lambda r=i, c=j: callback(r, c))
        b[i][j].grid(row=i, column=j)
player = "X"
stop_game = False
root.mainloop()
