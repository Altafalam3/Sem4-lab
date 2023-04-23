import tkinter as tk
root = tk.Tk()
text_var = tk.DoubleVar()

spin_box = tk.Spinbox(
root,
from_=0.6,
to=50.0,
increment=.01,
textvariable=text_var
)
spin_box.pack()
root.mainloop()