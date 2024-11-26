import tkinter as tk
from tkinter import messagebox

def copy_prompt(text_widget):
    prompt = text_widget.get("1.0", tk.END).strip()
    if not prompt:
        messagebox.showwarning("Błąd", "Pole promptu jest puste! Wygeneruj najpierw prompt.")
        return
    root = text_widget.winfo_toplevel()
    root.clipboard_clear()
    root.clipboard_append(prompt)
    root.update()
    messagebox.showinfo("Skopiowano", "Prompt został skopiowany do schowka.")
