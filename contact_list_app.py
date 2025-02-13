from tkinter import *
from PIL import Image, ImageTk
import pygame
from tkinter import messagebox
import os

pygame.mixer.init()

# Initialize main window
window = Tk()
window.title("YATHARTH's CONTACT LIST APP")
window.geometry("500x500")

bg_label = None
bg_image1 = None
bg_image2 = None


# Function to save contact
def save_func(name_entry, number_entry, email_entry, address_entry):
    name = name_entry.get().strip()
    number = number_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()
    
    if name and number:
        with open("contact_info.txt", "a") as file:
            file.write(f"{name},{number},{email},{address}\n")
        messagebox.showinfo("Success", "Contact Saved!")
        name_entry.delete(0, END)
        number_entry.delete(0, END)
        email_entry.delete(0, END)
        address_entry.delete(0, END)
    else:
        messagebox.showerror("Error", "Name and Phone Number are required!")


# Function to validate phone number
def validate_phone(input_text):
    return input_text.isdigit() and len(input_text) <= 10


# Function to add contact
def add_btn_clicked():
    add_btn_window = Toplevel(window)
    add_btn_window.title("ADD CONTACT")
    add_btn_window.geometry("350x350")

    Label(add_btn_window, text="Name", font=("Arial", 10)).place(x=20, y=20)
    text_name = Entry(add_btn_window)
    text_name.place(x=120, y=20, width=200, height=20)

    Label(add_btn_window, text="Phone", font=("Arial", 10)).place(x=20, y=60)
    validate_cmd = add_btn_window.register(validate_phone)
    text_number = Entry(add_btn_window, validate="key", validatecommand=(validate_cmd, "%P"))
    text_number.place(x=120, y=60, width=200, height=20)

    Label(add_btn_window, text="Email", font=("Arial", 10)).place(x=20, y=100)
    text_email = Entry(add_btn_window)
    text_email.place(x=120, y=100, width=200, height=20)

    Label(add_btn_window, text="Address", font=("Arial", 10)).place(x=20, y=140)
    text_address = Entry(add_btn_window)
    text_address.place(x=120, y=140, width=200, height=20)

    Button(add_btn_window, text="Save", bg="sky blue", font=("Arial", 10), 
           command=lambda: save_func(text_name, text_number, text_email, text_address)).place(x=140, y=190)


# Function to view contacts
def view_btn_clicked():
    view_btn_window = Toplevel(window)
    view_btn_window.title("VIEW CONTACTS")
    view_btn_window.geometry("400x400")

    text_area = Text(view_btn_window, width=50, height=20)
    text_area.pack(pady=20)

    if os.path.exists("contact_info.txt"):
        with open("contact_info.txt", "r") as file:
            contacts = file.readlines()
            if contacts:
                text_area.insert(END, "Name, Phone, Email, Address\n")
                text_area.insert(END, "-" * 40 + "\n")
                for contact in contacts:
                    text_area.insert(END, contact)
            else:
                text_area.insert(END, "No contacts found.")
    else:
        text_area.insert(END, "No contacts found.")


# Function to search contacts
def search_contact():
    search_window = Toplevel(window)
    search_window.title("SEARCH CONTACT")
    search_window.geometry("350x200")

    Label(search_window, text="Enter Name or Phone Number:", font=("Arial", 10)).pack(pady=10)
    search_entry = Entry(search_window, width=30)
    search_entry.pack(pady=5)

    result_label = Label(search_window, text="", font=("Arial", 10))
    result_label.pack(pady=10)

    def perform_search():
        query = search_entry.get().strip().lower()
        found = False

        if os.path.exists("contact_info.txt"):
            with open("contact_info.txt", "r") as file:
                for line in file:
                    if query in line.lower():
                        result_label.config(text=f"Contact Found: {line.strip()}", fg="green")
                        found = True
                        break

        if not found:
            result_label.config(text="Contact Not Found", fg="red")

    Button(search_window, text="Search", command=perform_search, bg="light green").pack(pady=5)


# Function to delete contacts
def delete_contact():
    delete_window = Toplevel(window)
    delete_window.title("DELETE CONTACT")
    delete_window.geometry("350x200")

    Label(delete_window, text="Enter Name to Delete:", font=("Arial", 10)).pack(pady=10)
    delete_entry = Entry(delete_window, width=30)
    delete_entry.pack(pady=5)

    def perform_delete():
        name_to_delete = delete_entry.get().strip().lower()
        deleted = False

        if os.path.exists("contact_info.txt"):
            with open("contact_info.txt", "r") as file:
                lines = file.readlines()

            with open("contact_info.txt", "w") as file:
                for line in lines:
                    if not line.lower().startswith(name_to_delete + ","):
                        file.write(line)
                    else:
                        deleted = True

        if deleted:
            messagebox.showinfo("Success", "Contact Deleted!")
        else:
            messagebox.showerror("Error", "Contact Not Found!")

    Button(delete_window, text="Delete", command=perform_delete, bg="red", fg="white").pack(pady=5)


# Function to change image
def change_image():
    global bg_image2, bg_label

    try:
        bg_image2 = Image.open("contact_list.jpg").resize((500, 500), Image.Resampling.LANCZOS)
        bg_image2 = ImageTk.PhotoImage(bg_image2)

        bg_label.config(image=bg_image2)
        bg_label.image = bg_image2

        Label(window, text="Select an Option", font=("Arial", 12)).place(x=150, y=70, width=200, height=40)

        Button(window, text="Add Contact", bg="sky blue", command=add_btn_clicked).place(x=200, y=130, width=120, height=40)
        Button(window, text="View Contacts", bg="sky blue", command=view_btn_clicked).place(x=200, y=180, width=120, height=40)
        Button(window, text="Search Contact", bg="sky blue", command=search_contact).place(x=200, y=230, width=120, height=40)
        Button(window, text="Delete Contact", bg="red", fg="white", command=delete_contact).place(x=200, y=280, width=120, height=40)

    except Exception as e:
        print("Error loading contact_list.jpg:", e)


# Function to display welcome screen
def welcome():
    global bg_label, bg_image1

    try:
        pygame.mixer.music.load("contact_music.mp3")
        pygame.mixer.music.play(-1)
    except Exception as e:
        print("Error playing music:", e)

    try:
        bg_image1 = Image.open("contact_list1.jpg").resize((500, 500), Image.Resampling.LANCZOS)
        bg_image1 = ImageTk.PhotoImage(bg_image1)

        bg_label = Label(window, image=bg_image1)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = bg_image1

        window.after(2000, change_image)
    except Exception as e:
        print("Error loading contact_list1.jpg:", e)


welcome()
window.mainloop()
