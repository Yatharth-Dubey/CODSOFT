from tkinter import *
from PIL import Image, ImageTk
import random
import string

##########################################
# MAIN WINDOW
window = Tk()
window.geometry("700x300")
window.title("YATHARTH's PASSWORD_GENERATOR")

# BACKGROUND IMAGE
try:
    bg_image = Image.open("password.jpg")
    bg_image = bg_image.resize((700, 500), Image.Resampling.LANCZOS)
    bg = ImageTk.PhotoImage(bg_image)

    bg_label = Label(window, image=bg)
    bg_label.place(x=0, y=0, relheight=1, relwidth=1)
except FileNotFoundError:
    print("Background image 'password.jpg' not found!")

# WINDOW ICON
try:
    img = Image.open("password_generator.jpg")
    icon = ImageTk.PhotoImage(img)
    window.iconphoto(True, icon)
except FileNotFoundError:
    print("Icon image 'password_generator.jpg' not found!")

# PASSWORD TEXT BOX
password = Text(window)
password.place(x=150, y=148, height=70, width=400)
password.config(bg="lightgreen", fg="blue", bd=10, relief="solid", font=("Courier", 13))
##############################################################


# DROPDOWN LISTS
# Complexity List
complexity_option = ["EASY", "MEDIUM", "HARD", "HARDEST"]
com_var = StringVar(window)
com_var.set(complexity_option[3])

w = OptionMenu(window, com_var, *complexity_option)
w.config(bg="black", fg="yellow", font=("Courier", 15))
w.place(x=10, y=150)
menu = w["menu"]
menu.config(bg="lightyellow", fg="blue", font=("Arial", 12))

# Length Option
length_option = [6, 9, 12]
len_var = IntVar(window)
len_var.set(length_option[0])

l = OptionMenu(window, len_var, *length_option)
l.config(bg="black", fg="yellow", font=("Courier", 15))
l.place(x=580, y=150)
menu2 = l["menu"]
menu2.config(bg="lightyellow", fg="blue", font=("Arial", 12))
########################################################


# PASSWORD GENERATION FUNCTION
def generate_password(length, complexity):
    """
    Generates a password based on length and complexity.
    - EASY: Lowercase letters with at least one number.
    - MEDIUM: Lowercase and uppercase letters with numbers.
    - HARD: Letters, numbers, and at least one special character.
    - HARDEST: Letters, numbers, and multiple special characters.
    """
    char_set = string.ascii_lowercase
    password = []

    # Add complexity-specific characters
    if complexity == "EASY":
        char_set += string.digits
        password.append(random.choice(string.digits))
    elif complexity == "MEDIUM":
        char_set += string.ascii_uppercase + string.digits
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.digits))
    elif complexity == "HARD":
        char_set += string.ascii_uppercase + string.digits + string.punctuation
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.digits))
        password.append(random.choice(string.punctuation))
    elif complexity == "HARDEST":
        char_set += string.ascii_uppercase + string.digits + string.punctuation
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.digits))
        password.append(random.choice(string.punctuation))
        password.append(random.choice(string.punctuation))

    # Fill the rest of the password with random choices from the character set
    while len(password) < length:
        password.append(random.choice(char_set))

    # Shuffle to randomize the order
    random.shuffle(password)

    # Return as a string
    return ''.join(password)


########################################
# SUBMIT BUTTON FUNCTION
def submit():
    complexity = com_var.get()
    length = len_var.get()

    # Generate the password based on selected options
    generated_password = generate_password(length, complexity)

    # Display the password in the text box
    password.delete(1.0, END)  # Clear previous text
    password.insert(END, generated_password)

    print(f"Generated Password: {generated_password}")

# SUBMIT BUTTON
button = Button(window, text="SUBMIT", command=submit)
button.config(bg="tomato", fg="green", font=("Courier", 15))
button.place(x=295, y=240)
########################################

# MAIN LOOP
window.mainloop()
