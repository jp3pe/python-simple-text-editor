import tkinter as tk
from tkinter import filedialog

def save_text(text):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            file.write(text)

def open_text():
    file_path = filedialog.askopenfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "r") as file:
            return file.read()

def add_button(root, text_area, text, command):
    button = tk.Button(root, text=text, command=command)
    button.grid(row=1, column=0 if text == "Open" else 1)

def draw_gui():
    root = tk.Tk()
    text_area = tk.Text(root)
    text_area.grid(row=0, column=0, columnspan=2)
    add_button(root, text_area, "Save", lambda: save_text(text_area.get("1.0", "end-1c")))
    add_button(root, text_area, "Open", lambda: [text_area.delete("1.0", tk.END), text_area.insert(tk.END, open_text())])
    root.mainloop()

draw_gui()