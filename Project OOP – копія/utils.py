import tkinter as tk

def clear_entries(*entries):
    for entry in entries:
        entry.delete(0, tk.END)

def update_listbox(listbox, items):
    listbox.delete(0, tk.END)
    for item in items:
        listbox.insert(tk.END, item)
