import tkinter
from tkinter import messagebox
      
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
        else:
            messagebox.showerror("Error", "Wrong email or password")
    else:
        messagebox.showerror("Error", "Invalid email format. Must end with '@gmail.com'")


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



root.mainloop()

