import tkinter as tk
from tkinter import messagebox

# Sample product data
products = {}
cart = {}

def add_product():
    name = product_name_entry.get()
    price = product_price_entry.get()
    if name and price.isdigit():
        products[name] = int(price)
        update_product_display()
        product_name_entry.delete(0, tk.END)
        product_price_entry.delete(0, tk.END)

def add_to_cart(product):
    if product in cart:
        cart[product] += 1
    else:
        cart[product] = 1
    update_cart_display()

def remove_from_cart(product):
    if product in cart:
        cart[product] -= 1
        if cart[product] == 0:
            del cart[product]
    update_cart_display()

def update_cart_display():
    cart_text.set("\n".join([f"{item} x{cart[item]} - ${cart[item] * products[item]}" for item in cart]))

def update_product_display():
    for widget in frame.winfo_children():
        widget.destroy()
    tk.Label(frame, text="Products", font=("Arial", 14, "bold")).pack()
    for product, price in products.items():
        tk.Button(frame, text=f"{product} - ${price}", command=lambda p=product: add_to_cart(p)).pack(fill='x')

def checkout():
    if not cart:
        messagebox.showinfo("Checkout", "Your cart is empty!")
        return
    total = sum(products[item] * cart[item] for item in cart)
    messagebox.showinfo("Checkout", f"Total amount: ${total}\nThank you for your purchase!")
    cart.clear()
    update_cart_display()

# GUI Setup
root = tk.Tk()
root.title("E-Commerce Store")
root.geometry("400x600")

# Product Input
tk.Label(root, text="Add Product", font=("Arial", 12, "bold")).pack()
product_name_entry = tk.Entry(root)
product_name_entry.pack()
tk.Label(root, text="Price").pack()
product_price_entry = tk.Entry(root)
product_price_entry.pack()
tk.Button(root, text="Add Product", command=add_product).pack()

# Product List
frame = tk.Frame(root)
frame.pack(pady=10)

# Cart Display
cart_text = tk.StringVar()
kart_label = tk.Label(root, textvariable=cart_text, font=("Arial", 12), justify="left")
kart_label.pack(pady=10)

# Checkout Button
tk.Button(root, text="Checkout", command=checkout, bg="green", fg="white").pack()

root.mainloop()
