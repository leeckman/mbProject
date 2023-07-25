import tkinter as tk

def add_line():
    text = entry.get()
    if text:
        text_area.insert('end', text + '\n')
        entry.delete(0, 'end')

root = tk.Tk()
root.title("Cadavre Exquis")

text_area = tk.Text(root, width=40, height=10)
text_area.pack()

entry = tk.Entry(root, width=30)
entry.pack()

submit_button = tk.Button(root, text="Add Line", command=add_line)
submit_button.pack()

root.mainloop()