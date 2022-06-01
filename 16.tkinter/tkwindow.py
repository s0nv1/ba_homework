import tkinter as tk


window = tk.Tk()
# window2 = tk.Tk()

sw = window.winfo_screenwidth()
sh = window.winfo_screenheight()

# 1 - 2 task 
w = [0, sw, 0, sw]
s = [0, 0, sh, sh]
for i in range(4):
    tk.Tk().geometry(f'300x300+{w[i]}+{s[i]}')
window.geometry(f'300x300+{sw // 2}+{sh // 2}')

# 3 task *
# window.geometry(f'{sw}x{sh}+0+0')


# 4 task **
# window.geometry(f'{sw}x{sh // 2}+0+0')


# 5 task ***
# window.geometry(f'{sw // 2}x{sh}+0+0')
# window2.geometry(f'{sw // 2}x{sh}+{sw // 2}+0')


window.mainloop()
