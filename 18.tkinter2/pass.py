import tkinter as tk


class MyGUI:
    
    def __init__(self):
        self.win = tk.Tk()
        
        # entry and label
        self.lb1 = tk.Label(self.win, text='Email')
        self.ent1 = tk.Entry(self.win)
        self.lb2 = tk.Label(self.win, text='Password')
        self.ent2 = tk.Entry(self.win, show='*')
        self.lb1.grid(row=0, column=0, sticky='e')
        self.ent1.grid(row=0, column=1, sticky='e')
        self.lb2.grid(row=1, column=0)
        self.ent2.grid(row=1, column=1)
        
        # but
        self.but1 = tk.Button(self.win, text='LOG IN', command=self.log_in)
        self.but1.grid(row=2, column=1)
        
        
        self.win.mainloop()
        
    def log_in(self):
        email = self.ent1.get()
        password = self.ent2.get()
        print(email)
        print(password)


root = MyGUI()
