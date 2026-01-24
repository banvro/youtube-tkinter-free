
import tkinter as tk

app = tk.Tk()
app.geometry('1000x450')
app.title('Learn Entery and Button')
app.config(background = '#57fafa')

def clickbutton():
    print("button clicked...")


ent1 = tk.Entry(app, font = ('Arial', 35), fg = 'green', bg = '#b3fff2', 
            justify = 'left', show = '#', width = 20,
            relief = 'groove', bd = 15
)
ent1.pack(pady = 40)

btn = tk.Button(app, text = 'Click Me', font = ('Arial', 35, 'bold'), 
                fg = '#b3fff2', bg = 'green', relief = 'raised', bd = 15,
                command = clickbutton
)
btn.pack(ipadx = 30)





app.mainloop()