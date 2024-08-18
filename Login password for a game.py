import tkinter
from tkinter import messagebox
import random

def on_button_click(button_text):
    comp_choice = assignnum(compchoice())
    result = Game(button_text, comp_choice)
    message_label.config(text=f"{result}\nComputer chose: {comp_choice}")

def compchoice():
    return random.randint(1, 3)

def assignnum(a):
    if a == 1:
        return 'Stone'
    elif a == 2:
        return 'Paper'
    else:
        return 'Scissor'

def Game(button_text, comp):
    if button_text == comp:
        return 'It is a tie'
    elif (button_text == 'Stone' and comp == 'Scissor')  or \
         (button_text == 'Paper' and comp == 'Stone') or \
         (button_text == 'Scissor' and comp == 'Paper'):
        return 'You Won'
    else:
        return 'You Lost'
      
def check_email(email_entry,emailconform_entry):
  if email_entry==emailconform_entry:
    return True
  else:
    return False
  
def check_password(password_entry,passwordconform_entry):
  if password_entry==passwordconform_entry:
    return True
  else:
    return False

def email_condition(email_entry):
  if email_entry.endswith("@gmail.com"):
    return True
  else:
    return False

def all():
    email = email_entry.get()
    email_confirm = emailconform_entry.get()
    password = password_entry.get()
    password_confirm = passwordconform_entry.get()
    
   
    if email_condition(email):
        if check_email(email, email_confirm) and check_password(password, password_confirm):
            messagebox.showinfo("Success", "Successfully Logged in")
            show_game()
        else:
            messagebox.showerror("Error", "Wrong email or password")
    else:
        messagebox.showerror("Error", "Invalid email format. Must end with '@gmail.com'")

def show_game():
    login_frame.pack_forget()  
    game_frame.pack()  
    
root=tkinter.Tk()
root.title("Email and Password")

root.geometry("450x300")  


login_frame = tkinter.Frame(root)
login_frame.pack(padx=10, pady=10)

email_text = tkinter.Label(login_frame, text="Enter Email:")
email_text.grid(row=0, column=0, padx=10, pady=10)

email_entry = tkinter.Entry(login_frame, width=30)
email_entry.grid(row=0, column=1, padx=10, pady=10)

password_text = tkinter.Label(login_frame, text="Enter Password:")
password_text.grid(row=1, column=0, padx=10, pady=10)

password_entry = tkinter.Entry(login_frame, width=30, show='*')
password_entry.grid(row=1, column=1, padx=10, pady=10)

emailconform_text = tkinter.Label(login_frame, text="Enter Email again:")
emailconform_text.grid(row=2, column=0, padx=10, pady=10)

emailconform_entry = tkinter.Entry(login_frame, width=30)
emailconform_entry.grid(row=2, column=1, padx=10, pady=10)

passwordconform_text = tkinter.Label(login_frame, text="Enter Password again:")
passwordconform_text.grid(row=3, column=0, padx=10, pady=10)

passwordconform_entry = tkinter.Entry(login_frame, width=30, show='*')
passwordconform_entry.grid(row=3, column=1, padx=10, pady=10)

submit_button = tkinter.Button(login_frame, text='Submit', command=all)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

game_frame = tkinter.Frame(root)

w = tkinter.Label(game_frame, text="Stone Paper Scissor", font=("David", 30), fg="red")
w.grid(row=0, column=0, columnspan=3, pady=20)

message_label = tkinter.Label(game_frame, text="", font=("David", 20), fg="blue")
message_label.grid(row=2, column=0, columnspan=3, pady=20)

button1 = tkinter.Button(game_frame, text="Stone", command=lambda: on_button_click("Stone"), width=10)
button1.grid(row=1, column=0, padx=10, pady=10)

button2 = tkinter.Button(game_frame, text="Paper", command=lambda: on_button_click("Paper"), width=10)
button2.grid(row=1, column=1, padx=10, pady=10)

button3 = tkinter.Button(game_frame, text="Scissor", command=lambda: on_button_click("Scissor"), width=10)
button3.grid(row=1, column=2, padx=10, pady=10)


game_frame.pack_forget()

root.mainloop()

