from tkinter import *
from tkinter.messagebox import showinfo
from itertools import permutations

N = 0
button_number = 0
player_1 = []
player_2 = []
        

class game_board:
    def __init__(self, number, x, y, color):
        self.number = number
        self.x = x
        self.y = y
        self.color = color
        
    def show(self):
        #Create one Tic Tac Toe Game Board
        b1 = Button(window, text = "", width = 3, height = 1, font = "times 12", bg = self.color)
        b1.place(x = self.x, y = self.y)
        b2 = Button(window, text = "", width = 3, height = 1, font = "times 12", bg = self.color)
        b2.place(x = self.x + 40, y = self.y)
        b3 = Button(window, text = "", width = 3, height = 1, font = "times 12", bg = self.color)
        b3.place(x = self.x + 80, y = self.y)
        b4 = Button(window, text = "", width = 3, height = 1, font = "times 12", bg = self.color)
        b4.place(x = self.x, y = self.y + 35)
        b5 = Button(window, text = "", width = 3, height = 1, font = "times 12", bg = self.color)
        b5.place(x = self.x + 40, y = self.y + 35)
        b6 = Button(window, text = "", width = 3, height = 1, font = "times 12", bg = self.color)
        b6.place(x = self.x + 80, y = self.y + 35)
        b7 = Button(window, text = "", width = 3, height = 1, font = "times 12", bg = self.color)
        b7.place(x = self.x, y = self.y + 70)
        b8 = Button(window, text = "", width = 3, height = 1, font = "times 12", bg = self.color)
        b8.place(x = self.x + 40, y = self.y + 70)
        b9 = Button(window, text = "", width = 3, height = 1, font = "times 12", bg = self.color)
        b9.place(x = self.x + 80, y = self.y + 70)
        
        buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
        
        #What happens when a button is clicked
        def click(i):
            global N
            global button_number
            global fields, rects
            global player_1, player_2
            global l4
        
            #restrict players to play on specific fields
            if (self.number != button_number+1) and N != 0:
                if (button_number+1 in player_1) or (button_number+1 in player_2):
                    pass
                else:
                    showinfo("Info", "Not Possible!\nPlay in the highlighted field.")
                    return
            else:
                pass
            
            button_number = i
        
            #show who plays next
            if N%2 == 0:
                buttons[i].config(text = "X")
                l4.config(text = " It's your turn: " + str(e2.get()))
            else:
                buttons[i].config(text = "O")
                l4.config(text = " It's your turn: " + str(e1.get()))
            

            #disable button after clicking or add remove-ability with right click
            buttons[i].config(command = "")
            #buttons[i].bind("<Button-3>", rightclick)
            

            #cases who wins!
            if (b1["text"] == b2["text"] == b3["text"] != "") or (b4["text"] == b5["text"] == b6["text"] != "") or (b7["text"] == b8["text"] == b9["text"] != ""):
                if N%2 == 0:
                    fields[self.number-1].player1_won()
                    player_1.append(self.number)
                else:
                    fields[self.number-1].player2_won()
                    player_2.append(self.number)
                    
            if (b1["text"] == b4["text"] == b7["text"] != "") or (b2["text"] == b5["text"] == b8["text"] != "") or (b3["text"] == b6["text"] == b9["text"] != ""):
                if N%2 == 0:
                    fields[self.number-1].player1_won()
                    player_1.append(self.number)
                else:
                    fields[self.number-1].player2_won()
                    player_2.append(self.number)
                    
            if (b1["text"] == b5["text"] == b9["text"] != "") or (b3["text"] == b5["text"] == b7["text"] != ""):
                if N%2 == 0:
                    fields[self.number-1].player1_won()
                    player_1.append(self.number)
                else:
                    fields[self.number-1].player2_won()
                    player_2.append(self.number)

 
            set1 = permutations([1,2,3])
            set2 = permutations([4,5,6])
            set3 = permutations([7,8,9])
            set4 = permutations([1,4,7])
            set5 = permutations([2,5,8])
            set6 = permutations([3,6,9])
            set7 = permutations([1,5,9])
            set8 = permutations([3,5,7])

            #check the whole game board for winning cases
            for i in set1,set2,set3,set4,set5,set6,set7,set8:
                for j in list(i):
                    plyr_1 = all(elem in player_1 for elem in j)
                    plyr_2 = all(elem in player_2 for elem in j)
                    if plyr_1 == True:
                        showinfo("Game Over", "Player 1 has won!")
                        break
                    elif plyr_2 == True:
                        showinfo("Game Over", "Player 2 has won!")
                        break
                    else:
                        pass
        
        
            #highlight the next field to play
            w.itemconfig(rects[self.number-1], outline = "")
            
            if (button_number+1 in player_1) or (button_number+1 in player_2):
                showinfo("Info", "This field is already gone.\nChoose your field freely!")
            else:
                w.itemconfig(rects[button_number], outline = "black")
        
            #increase play counter by 1
            N += 1

        #Assign each button the respective command
        b1.config(command = lambda: click(0))
        b2.config(command = lambda: click(1))
        b3.config(command = lambda: click(2))
        b4.config(command = lambda: click(3))
        b5.config(command = lambda: click(4))
        b6.config(command = lambda: click(5))
        b7.config(command = lambda: click(6))
        b8.config(command = lambda: click(7))
        b9.config(command = lambda: click(8))
        
    #Layouts for winning cases
    def player1_won(self):
        b1 = Button(window, text = "\ ", width = 3, height = 1, font = "times 12", bg = "red")
        b1.place(x = self.x, y = self.y)
        b2 = Button(window, text = "", width = 3, height = 1, font = "times 12", bg = "red")
        b2.place(x = self.x + 40, y = self.y)
        b3 = Button(window, text = "/ ", width = 3, height = 1, font = "times 12", bg = "red")
        b3.place(x = self.x + 80, y = self.y)
        b4 = Button(window, text = "", width = 3, height = 1, font = "times 12", bg = "red")
        b4.place(x = self.x, y = self.y + 35)
        b5 = Button(window, text = "X", width = 3, height = 1, font = "times 12", bg = "red")
        b5.place(x = self.x + 40, y = self.y + 35)
        b6 = Button(window, text = "", width = 3, height = 1, font = "times 12", bg = "red")
        b6.place(x = self.x + 80, y = self.y + 35)
        b7 = Button(window, text = "/", width = 3, height = 1, font = "times 12", bg = "red")
        b7.place(x = self.x, y = self.y + 70)
        b8 = Button(window, text = "", width = 3, height = 1, font = "times 12", bg = "red")
        b8.place(x = self.x + 40, y = self.y + 70)
        b9 = Button(window, text = "\ ", width = 3, height = 1, font = "times 12", bg = "red")
        b9.place(x = self.x + 80, y = self.y + 70)

    def player2_won(self):
        b1 = Button(window, text = "/", width = 3, height = 1, font = "times 12", bg = "red")
        b1.place(x = self.x, y = self.y)
        b2 = Button(window, text = "---", width = 3, height = 1, font = "times 12", bg = "red")
        b2.place(x = self.x + 40, y = self.y)
        b3 = Button(window, text = "\ ", width = 3, height = 1, font = "times 12", bg = "red")
        b3.place(x = self.x + 80, y = self.y)
        b4 = Button(window, text = "|", width = 3, height = 1, font = "times 12", bg = "red")
        b4.place(x = self.x, y = self.y + 35)
        b5 = Button(window, text = "O", width = 3, height = 1, font = "times 12", bg = "red")
        b5.place(x = self.x + 40, y = self.y + 35)
        b6 = Button(window, text = "|", width = 3, height = 1, font = "times 12", bg = "red")
        b6.place(x = self.x + 80, y = self.y + 35)
        b7 = Button(window, text = "\ ", width = 3, height = 1, font = "times 12", bg = "red")
        b7.place(x = self.x, y = self.y + 70)
        b8 = Button(window, text = "---", width = 3, height = 1, font = "times 12", bg = "red")
        b8.place(x = self.x + 40, y = self.y + 70)
        b9 = Button(window, text = "/", width = 3, height = 1, font = "times 12", bg = "red")
        b9.place(x = self.x + 80, y = self.y + 70)
        
        

#Create window
window = Tk()
window.title("Mega Tic Tac Toe")
window.geometry("682x600+300+30")

w = Canvas(window, width=682, height=600)
w.place(x = 0, y = 0)

default_bg_color = window.cget("bg")
rect1 = w.create_rectangle(137, 152, 267, 270, fill = default_bg_color, outline = "")
rect2 = w.create_rectangle(268, 152, 398, 270, fill = default_bg_color, outline = "")
rect3 = w.create_rectangle(399, 152, 529, 270, fill = default_bg_color, outline = "")
rect4 = w.create_rectangle(137, 272, 267, 390, fill = default_bg_color, outline = "")
rect5 = w.create_rectangle(268, 272, 398, 390, fill = default_bg_color, outline = "")
rect6 = w.create_rectangle(399, 272, 529, 390, fill = default_bg_color, outline = "")
rect7 = w.create_rectangle(137, 392, 267, 510, fill = default_bg_color, outline = "")
rect8 = w.create_rectangle(268, 392, 398, 510, fill = default_bg_color, outline = "")
rect9 = w.create_rectangle(399, 392, 529, 510, fill = default_bg_color, outline = "")

rects = [rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9]

#fixme!!
def start_button():
    #enable all buttons?
    l4.config(text = " It's your turn: " + str(e1.get()))
    l4.focus_set()

#fixme!!
def reset_button():
    global N
    player_1.clear()
    player_2.clear()
    N = 0
    for i in range(9):
        fields[i].color = "gray"
        fields[i].show()
    for i in range(9):
        w.itemconfig(rects[i], outline = "")
    

#Create layout
l1 = Label(window, text = "Welcome to Mega Tic Tac Toe!", font = "times 15 bold")
l1.grid(row = 0, column = 2, columnspan = 10, pady = 10, sticky="NW")
l2 = Label(window, text = " Player 1 = ", font = "times 12")
l2.grid(row = 1, column = 0)
e1 = Entry(window)
e1.grid(row = 1, column = 1)
l3 = Label(window, text = " Player 2 = ", font = "times 12")
l3.grid(row = 2, column = 0)
e2 = Entry(window)
e2.grid(row = 2, column = 1)
l4 = Label(window, text = " It's your turn: ", width = 30, font = "times 12")
l4.grid(row = 2, column = 3, columnspan = 3, pady = 4, sticky = "W")
start = Button(window, text = "Start", width = 8, height = 1, font = "times 12", command = start_button)
start.grid(row = 1, column = 3, columnspan = 3)
reset = Button(window, text = "Reset", width = 8, height = 1, font = "times 12", command = reset_button)
reset.grid(row = 1, column = 6, columnspan = 6)
l5 = Label(window, text = " ")
l5.grid(row = 3, column = 0)


#Create game board
g1 = game_board(1, 145, 160, "gray")
g2 = game_board(2, 275, 160, "gray")
g3 = game_board(3, 405, 160, "gray")
g4 = game_board(4, 145, 280, "gray")
g5 = game_board(5, 275, 280, "gray")
g6 = game_board(6, 405, 280, "gray")
g7 = game_board(7, 145, 400, "gray")
g8 = game_board(8, 275, 400, "gray")
g9 = game_board(9, 405, 400, "gray")

fields = [g1, g2, g3, g4, g5, g6, g7, g8, g9]

for i in range(9):
    fields[i].show()


#Keep window open
window.mainloop()