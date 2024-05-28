import tkinter as tk
from tkinter import filedialog


def show_input_box():
    root = tk.Tk()
    text_area = tk.Text(root)
    text_area.pack()

    def get_text():
        text = text_area.get("1.0", "end-1c")
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w") as file:
                file.write(text)
                file.close()
        root.destroy()

    button = tk.Button(root, text="Save", command=get_text)
    button.pack()

    root.mainloop()


show_input_box()
