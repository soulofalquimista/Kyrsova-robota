import tkinter as tk
from tkinter import messagebox, LabelFrame

root = tk.Tk()
root.title("Mineral Fertilizer Trading System")
root.geometry("600x400")
root.configure(bg="#f0f4f7")

# Стиль для кнопок
button_style = {
    "font": ("Arial", 10, "bold"),
    "bg": "#4CAF50",
    "fg": "white",
    "activebackground": "#45a049",
    "width": 15,
}

# Дані
products = []
customers = []

# Функція додавання продукту
def add_product():
    name = product_name_entry.get()
    try:
        price = float(product_price_entry.get())
        quantity = int(product_quantity_entry.get())
        if price <= 0 or quantity <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid price and quantity.")
        return

    products.append((name, price, quantity))
    product_listbox.insert(tk.END, f"{name} - Price: {price} USD, Quantity: {quantity}")
    product_name_entry.delete(0, tk.END)
    product_price_entry.delete(0, tk.END)
    product_quantity_entry.delete(0, tk.END)

# Функція додавання клієнта
def add_customer():
    name = customer_name_entry.get()
    contact = customer_contact_entry.get()
    customers.append((name, contact))
    customer_listbox.insert(tk.END, f"Customer: {name}, Contact: {contact}")
    customer_name_entry.delete(0, tk.END)
    customer_contact_entry.delete(0, tk.END)

# Функція обробки продажу
def process_sale():
    # Перевірка вибору продукту
    selected_product_index = product_listbox.curselection()
    if not selected_product_index:
        messagebox.showwarning("Warning", "Please select a product.")
        return
    selected_product_index = selected_product_index[0]

    # Перевірка вибору клієнта
    selected_customer_index = customer_listbox.curselection()
    if not selected_customer_index:
        messagebox.showwarning("Warning", "Please select a customer.")
        return
    selected_customer_index = selected_customer_index[0]

    # Отримання кількості
    try:
        quantity_to_sell = int(sale_quantity_entry.get())
        if quantity_to_sell <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive quantity.")
        return

    # Отримання деталей продукту
    product_name, product_price, product_quantity = products[selected_product_index]

    if quantity_to_sell > product_quantity:
        messagebox.showerror("Insufficient Stock", "Not enough quantity available.")
        return

    # Отримання деталей клієнта
    customer_name, customer_contact = customers[selected_customer_index]

    # Оновлення продукту
    new_quantity = product_quantity - quantity_to_sell
    products[selected_product_index] = (product_name, product_price, new_quantity)
    product_listbox.delete(selected_product_index)
    product_listbox.insert(selected_product_index, f"{product_name} - Price: {product_price} USD, Quantity: {new_quantity}")

    # Додавання запису до історії продажів
    total_price = product_price * quantity_to_sell
    sales_history_listbox.insert(tk.END, f"{customer_name} bought {quantity_to_sell} {product_name} for {total_price:.2f} USD")

    sale_quantity_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Sale processed successfully!")

# Фрейм для продуктів
product_frame = LabelFrame(root, text="Add Product", font=("Arial", 12, "bold"), bg="#f0f4f7")
product_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

import tkinter as tk
from tkinter import messagebox, LabelFrame

root = tk.Tk()
root.title("Mineral Fertilizer Trading System")
root.geometry("700x500")
root.configure(bg="#f0f4f7")

# Стиль для кнопок
button_style = {
    "font": ("Arial", 10, "bold"),
    "bg": "#4CAF50",
    "fg": "white",
    "activebackground": "#45a049",
    "width": 15,
}

# Дані
products = []
customers = []

# Функція додавання продукту
def add_product():
    name = product_name_entry.get()
    try:
        price = float(product_price_entry.get())
        quantity = int(product_quantity_entry.get())
        if price <= 0 or quantity <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid price and quantity.")
        return

    products.append((name, price, quantity))
    product_listbox.insert(tk.END, f"{name} - Price: {price} USD, Quantity: {quantity}")
    product_name_entry.delete(0, tk.END)
    product_price_entry.delete(0, tk.END)
    product_quantity_entry.delete(0, tk.END)

# Функція додавання клієнта
def add_customer():
    name = customer_name_entry.get()
    contact = customer_contact_entry.get()
    customers.append((name, contact))
    customer_listbox.insert(tk.END, f"Customer: {name}, Contact: {contact}")
    customer_name_entry.delete(0, tk.END)
    customer_contact_entry.delete(0, tk.END)

# Функція обробки продажу
def process_sale():
    # Перевірка вибору продукту
    selected_product_index = product_listbox.curselection()
    if not selected_product_index:
        messagebox.showwarning("Warning", "Please select a product.")
        return
    selected_product_index = selected_product_index[0]

    # Перевірка вибору клієнта
    selected_customer_index = customer_listbox.curselection()
    if not selected_customer_index:
        messagebox.showwarning("Warning", "Please select a customer.")
        return
    selected_customer_index = selected_customer_index[0]

    # Отримання кількості
    try:
        quantity_to_sell = int(sale_quantity_entry.get())
        if quantity_to_sell <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive quantity.")
        return

    # Отримання деталей продукту
    product_name, product_price, product_quantity = products[selected_product_index]

    if quantity_to_sell > product_quantity:
        messagebox.showerror("Insufficient Stock", "Not enough quantity available.")
        return

    # Отримання деталей клієнта
    customer_name, customer_contact = customers[selected_customer_index]

    # Оновлення продукту
    new_quantity = product_quantity - quantity_to_sell
    if new_quantity == 0:
        messagebox.showinfo("Product Sold Out", f"The product '{product_name}' is now sold out!")
        products.pop(selected_product_index)
        product_listbox.delete(selected_product_index)
    else:
        products[selected_product_index] = (product_name, product_price, new_quantity)
        product_listbox.delete(selected_product_index)
        product_listbox.insert(selected_product_index, f"{product_name} - Price: {product_price} USD, Quantity: {new_quantity}")

    # Додавання запису до історії продажів
    total_price = product_price * quantity_to_sell
    sales_history_listbox.insert(tk.END, f"{customer_name} bought {quantity_to_sell} {product_name} for {total_price:.2f} USD")
    product_sales_history_listbox.insert(tk.END, f"{product_name}: {quantity_to_sell} units sold to {customer_name}")

    sale_quantity_entry.delete(0, tk.END)

# Фрейм для продуктів
product_frame = LabelFrame(root, text="Add Product", font=("Arial", 12, "bold"), bg="#f0f4f7")
product_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

tk.Label(product_frame, text="Name:", bg="#f0f4f7").grid(row=0, column=0, padx=5, pady=5, sticky="w")
product_name_entry = tk.Entry(product_frame, width=20)
product_name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(product_frame, text="Price:", bg="#f0f4f7").grid(row=1, column=0, padx=5, pady=5, sticky="w")
product_price_entry = tk.Entry(product_frame, width=20)
product_price_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(product_frame, text="Quantity:", bg="#f0f4f7").grid(row=2, column=0, padx=5, pady=5, sticky="w")
product_quantity_entry = tk.Entry(product_frame, width=20)
product_quantity_entry.grid(row=2, column=1, padx=5, pady=5)

add_product_button = tk.Button(product_frame, text="Add Product", command=add_product, **button_style)
add_product_button.grid(row=3, column=0, columnspan=2, pady=10)

# Фрейм для клієнтів
customer_frame = LabelFrame(root, text="Add Customer", font=("Arial", 12, "bold"), bg="#f0f4f7")
customer_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nw")

tk.Label(customer_frame, text="Name:", bg="#f0f4f7").grid(row=0, column=0, padx=5, pady=5, sticky="w")
customer_name_entry = tk.Entry(customer_frame, width=20)
customer_name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(customer_frame, text="Contact:", bg="#f0f4f7").grid(row=1, column=0, padx=5, pady=5, sticky="w")
customer_contact_entry = tk.Entry(customer_frame, width=20)
customer_contact_entry.grid(row=1, column=1, padx=5, pady=5)

add_customer_button = tk.Button(customer_frame, text="Add Customer", command=add_customer, **button_style)
add_customer_button.grid(row=2, column=0, columnspan=2, pady=10)

# Фрейм для продажу
sale_frame = LabelFrame(root, text="Process Sale", font=("Arial", 12, "bold"), bg="#f0f4f7")
sale_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nw")

tk.Label(sale_frame, text="Select Product:", bg="#f0f4f7").grid(row=0, column=0, padx=5, pady=5, sticky="w")
product_listbox = tk.Listbox(sale_frame, height=4, width=25, exportselection=False)
product_listbox.grid(row=1, column=0, padx=5, pady=5)

tk.Label(sale_frame, text="Select Customer:", bg="#f0f4f7").grid(row=0, column=1, padx=5, pady=5, sticky="w")
customer_listbox = tk.Listbox(sale_frame, height=4, width=25, exportselection=False)
customer_listbox.grid(row=1, column=1, padx=5, pady=5)

tk.Label(sale_frame, text="Quantity:", bg="#f0f4f7").grid(row=2, column=0, padx=5, pady=5, sticky="w")
sale_quantity_entry = tk.Entry(sale_frame, width=10)
sale_quantity_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

process_sale_button = tk.Button(sale_frame, text="Process Sale", command=process_sale, **button_style)
process_sale_button.grid(row=3, column=0, columnspan=2, pady=10)

# Фрейм для історії продажів
history_frame = LabelFrame(root, text="Sales History", font=("Arial", 12, "bold"), bg="#f0f4f7")
history_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nw")

sales_history_listbox = tk.Listbox(history_frame, height=8, width=60)
sales_history_listbox.grid(row=0, column=0, padx=5, pady=5)

# Фрейм для історії продажу продуктів
product_history_frame = LabelFrame(root, text="Product Sales History", font=("Arial", 12, "bold"), bg="#f0f4f7")
product_history_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nw")

product_sales_history_listbox = tk.Listbox(product_history_frame, height=8, width=60)
product_sales_history_listbox.grid(row=0, column=0, padx=5, pady=5)

# Основний цикл
root.mainloop()