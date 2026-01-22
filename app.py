
import tkinter as tk

app = tk.Tk()

app.geometry('1000x500')
app.title("This is my title")
app.config(background = '#36f525')


lbl = tk.Label(app, text = 'Hellow word',
            font = ('Arial', 40, 'bold'),
            fg = 'white',
            bg = 'green'
    )

lbl.pack(fill = 'x', pady = 20, ipady = 30)




app.mainloop()