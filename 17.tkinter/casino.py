import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
import random





class MyGUI:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('BEETROOT CASINO')
        self.win.geometry('800x600+500+300')
        self.win.maxsize(800, 600)
        self.win.minsize(800, 600)
        # image 
        self.di = {1: PhotoImage(file='image/logo.png'),
                    2: PhotoImage(file='image/beet.png'),
                    3: PhotoImage(file='image/bug.png'),
                    4: PhotoImage(file='image/man.png'),
                    5: PhotoImage(file='image/tesla.png'),
                    6: PhotoImage(file='image/mach.png'),
                    7: PhotoImage(file='image/dice.png')
                }
        self.background_image=tk.PhotoImage(file='image/bt.png')
        self.background_label = tk.Label(self.win, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.res_but = tk.PhotoImage(file='image/restart.png')
        self.quit_but = tk.PhotoImage(file='image/quit.png')
        self.spin_but = tk.PhotoImage(file='image/spin.png')
        # Style
        self.s = ttk.Style()                     
        self.s.configure('Wild.TRadiobutton', 
                            background='orange',
                            foreground='black'
                            )
        self.l = ttk.Style()
        self.l.configure('TLabel', background='orange', foreground='black')
        self.st = ttk.Style()
        self.st.map('TButton',
                    foreground=[('!active', 'purple'),
                               ('pressed', 'orange'),
                               ('active', 'red')],
                    background=[
                               ('pressed', 'brown'),
                               ('active', 'orange')]
                    )
        # var 
        self.var = tk.IntVar()
        self.var.set(25)
        
        # frame
        self.fr1 = ttk.Frame(self.win)
        self.fr2 = ttk.Frame(self.win)
        self.fr3 = ttk.Frame(self.win)
        self.fr4 = ttk.Frame(self.win)
        self.fr5 = ttk.Frame(self.win)
        self.fr1.grid()
        self.fr2.grid()
        self.fr3.grid()
        self.fr4.grid()
        self.fr5.grid()
        
        # labels
        self.fot_lb = PhotoImage(file='image/beet.png')
        self.lb1 = ttk.Label(self.fr1, 
                            text='$', 
                            font=('', 100), 
                            width=2, 
                            anchor='center', 
                            image=self.fot_lb,
                            borderwidth=5,
                            )
        self.lb2 = ttk.Label(self.fr1, 
                            text='$', 
                            font=('', 100), 
                            width=2, 
                            anchor='center', 
                            image=self.fot_lb,
                            borderwidth=5
                            )
        self.lb3 = ttk.Label(self.fr1, 
                            text='$', 
                            font=('', 100), 
                            width=2, 
                            anchor='center', 
                            image=self.fot_lb,
                            borderwidth=5
                            )
        
        self.win.grid_rowconfigure(0, weight=1)
        self.win.grid_columnconfigure(0, weight=1)
        
        # labels grid
        self.lb1.grid(column=0, row=0)
        self.lb2.grid(column=1, row=0)
        self.lb3.grid(column=2, row=0)
        
        # balance
        self.bal = ttk.Label(self.fr2, text='Balance:', font=('', 20),width=8, style='TLabel')
        self.counter = ttk.Label(self.fr2, text='10000', font=('', 20),width=6, style='TLabel')
        self.bal.grid(column=1, row=2, sticky='ew')
        self.counter.grid(column=2, row=2, sticky='ew')
        
        self.bt1 = ttk.Button(self.fr3, 
                                text='$SPIN$', 
                                command=self.spin_game, 
                                width=50, 
                                image=self.spin_but,
                                style='TButton'
                                )
        self.bt1.grid(columnspan=1)

        self.bt2 = ttk.Button(self.fr5, 
                                text='quit', 
                                command=self.win.destroy, 
                                image=self.quit_but,
                                style='TButton'
                                )
        self.bt2.grid( column=1, row=4)

        self.bt3 = ttk.Button(self.fr5, 
                                text='', 
                                command=self.reset_all, 
                                image=self.res_but,
                                style='TButton'
                                )
        self.bt3.grid( column=0, row=4)
        
        self.r1 = ttk.Radiobutton(self.fr4, 
                                    text='25$', 
                                    variable=self.var, 
                                    value=25, 
                                    width=4, 
                                    style='Wild.TRadiobutton'
                                    )
        self.r2 = ttk.Radiobutton(self.fr4, 
                                    text='50$', 
                                    variable=self.var, 
                                    value=50, width=4, 
                                    style='Wild.TRadiobutton'
                                    )
        self.r3 = ttk.Radiobutton(self.fr4, 
                                    text='100$', 
                                    variable=self.var, 
                                    value=100, width=4, 
                                    style='Wild.TRadiobutton'
                                    )
        self.r1.grid(row=0, column=0, sticky='n')
        self.r2.grid(row=0, column=1, sticky='ew')
        self.r3.grid(row=0, column=2, sticky='s')
        
        self.win.mainloop()
        
    def reset_all(self):
        self.win.destroy()
        win = MyGUI()
    
    def spin_game(self):
        sim = []
        for i in range(3):
            sim.append(random.randint(1, 7))
        self.lb1['image'] = self.di[sim[0]]
        self.lb2['image'] = self.di[sim[1]]
        self.lb3['image'] = self.di[sim[2]] 
        if sim[0] == sim[1] == sim[2]:
            self.counter['text'] = str(int(self.counter['text']) + self.var.get() * 1)
        else:
            self.counter['text'] = str(int(self.counter['text']) - self.var.get())
        if int(self.counter['text']) <= 0:
            self.counter['text'] = 'LOSER'
            self.bt1.state(['disabled'])


if __name__ == '__main__':
    win = MyGUI()
    
