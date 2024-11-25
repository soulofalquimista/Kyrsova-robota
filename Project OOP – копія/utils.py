import tkinter as tk

def clear_entries(*entries):
    """Очищення полів вводу"""
    for entry in entries:
        entry.delete(0, tk.END)

def update_listbox(listbox, items):
    """Оновлення списків у Listbox"""
    listbox.delete(0, tk.END)
    for item in items:
        listbox.insert(tk.END, item)
