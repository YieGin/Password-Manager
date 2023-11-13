from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if len(password) > 0 and len(website) > 0:
        is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered: \nEmail: {email} \npassword: {password} \nIs it ok to save?")
    else:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} / {email} / {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

window = Tk()
window.title("Pomodoro")
window.config(padx=20, pady=20)

# Canvas
canvas = Canvas(width=200, height=200)
logo_img =  PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img )
canvas.grid(column=1, row=0)

# Label
website_label = Label(text="Website")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)
password_label = Label(text="password")
password_label.grid(column=0, row=3)


#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column= 1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column= 1, columnspan=2)
email_entry.insert(0, "islampuma50@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column= 1, columnspan=2)


#BUTTON
generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
