import tkinter as tk

# create the main window
root = tk.Tk()

# create a Text widget with some initial text
text_widget = tk.Text(root, height=10, width=50)
text_widget.insert(tk.END, "Hello, world!\n")

# insert a string at the beginning of the text
text_widget.insert("1.0", "Insert at beginning\n")

# insert a string at the current position
text_widget.insert(tk.INSERT, "Insert at current position")

# delete the first character of the text
text_widget.delete("1.0")

# delete the last character of the text
text_widget.delete(tk.END+"-2c")

# pack the Text widget and start the main loop
text_widget.pack()
root.mainloop()
