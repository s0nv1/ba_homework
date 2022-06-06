import tkinter as tk
from tkinter import ttk
import random



class MyGUI:
    
    def __init__(self):
        self.win = tk.Tk()
        self.win.geometry('400x300+500+300')
        self.dic = {
                    'rock': ('scissors', 'lizard'),
                    'paper': ('rock', 'spock'),
                    'scissors': ('paper', 'lizard'),
                    'lizard': ('spock', 'paper'),
                    'spock': ('rock', 'scissors'),
                    }
        # frame
        self.fr1 = ttk.Frame(self.win)
        self.fr2 = ttk.Frame(self.win)
        self.fr3 = ttk.Frame(self.win)
        self.fr1.pack()
        self.fr2.pack()
        self.fr3.pack()
        
        # label fr1
        self.lb1 = ttk.Label(self.fr1, text='0', font=('Arial', 50))
        self.lb2 = ttk.Label(self.fr1, text=':', font=('Arial', 30))
        self.lb3 = ttk.Label(self.fr1, text='0', font=('Arial', 50))
        self.lb1.grid(row=0, column=1)
        self.lb2.grid(row=0, column=2)
        self.lb3.grid(row=0, column=3)
        
        # label fr2
        self.lb0 = ttk.Label(self.fr2, text='START', font=('', 20))
        self.lb0.grid()
        
        # label fr3
        self.but1 = ttk.Button(self.fr3, text='ROCK', command=lambda: self.start_game('rock'))
        self.but2 = ttk.Button(self.fr3, text='PAPER', command=lambda: self.start_game('paper'))
        self.but3 = ttk.Button(self.fr3, text='SCISSORS', command=lambda: self.start_game('scissors'))
        self.but4 = ttk.Button(self.fr3, text='LIZARD', command=lambda: self.start_game('lizard'))
        self.but5 = ttk.Button(self.fr3, text='SPOCK', command=lambda: self.start_game('spock'))
        self.but1.grid()
        self.but2.grid()
        self.but3.grid()
        self.but4.grid()
        self.but5.grid()
        
        
        self.win.mainloop()
    
    def start_game(self, choice):
        pc_choice = random.choice(list(self.dic.keys()))
        if pc_choice in self.dic[choice]:
            self.lb0['text'] = 'WON'
            self.lb1['text'] = int(self.lb1['text']) + 1
        elif choice in self.dic[pc_choice]:
            self.lb0['text'] = 'LOST'
            self.lb3['text'] = int(self.lb3['text']) + 1
        else:
            self.lb0['text'] = 'DRAW'


root = MyGUI()

















