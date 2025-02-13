from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


# Function to load tasks from a file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []


# Function to save tasks to a file
def save_tasks():
    with open("tasks.txt", "w") as file:
        tasks = lb.get(0, END)
        for task in tasks:
            file.write(task + "\n")


# Add task to the listbox
def task_enter():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
        save_tasks()
    else:
        messagebox.showwarning("WARNING", "PLEASE ENTER SOME TASK.")


# Delete selected task from the listbox
def delete_entry():
    try:
        lb.delete(ANCHOR)
        save_tasks()  # Save tasks after deletion
    except:
        messagebox.showwarning("WARNING", "PLEASE SELECT A TASK TO DELETE.")


# Create main window
window = Tk()
window.geometry("500x450+520+200")
window.title("YATHARTH's PYTHON PROGRAMME")
window.resizable(width=False, height=False)

# Set up the background image
canvas = Canvas(window, width=500, height=450)
canvas.pack(fill=BOTH, expand=True)

try:
    image = Image.open("todolist.jpg")
    image = image.resize((window.winfo_screenwidth(), window.winfo_screenheight()), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
except FileNotFoundError:
    messagebox.showerror("Error", "Background image 'todolist.jpg' not found!")

# Frame for tasks
frame = Frame(canvas, bg="#223441")
frame.pack(pady=10)

# Listbox for tasks
lb = Listbox(
    frame,
    width=25,
    height=8,
    font=("times 20"),
    bd=0,
    fg="#ffffff",
    bg="#2b2b2b",
    highlightthickness=0,
    selectbackground="#4caf50",
    activestyle="none",
)
lb.pack(side=LEFT, fill=BOTH)

# Scrollbar
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

# Load tasks from file into the Listbox
task_list = load_tasks()
for item in task_list:
    lb.insert(END, item)

# Entry widget for adding tasks
my_entry = Entry(
    window,
    font=("Times", 24),
    bd=2,
    relief=SOLID
)
my_entry.pack(pady=20)

# Button frame
Button_frame = Frame(window, bg="#223441")
Button_frame.pack(pady=20)

# Add Task Button
addtask_btn = Button(
    Button_frame,
    text="ADD TASK",
    font=("Times 14"),
    bg="#c5f776",
    padx=20,
    pady=10,
    command=task_enter
)
addtask_btn.pack(fill=BOTH, expand=True, side=LEFT)

# Delete Task Button
delTask_btn = Button(
    Button_frame,
    text="DELETE TASK",
    font=("Times 14"),
    bg="#ff8b61",
    padx=20,
    pady=10,
    command=delete_entry
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

window.mainloop()
