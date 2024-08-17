import tkinter

def on_button_click(button_text):
    message_label.config(text=f"You chose {button_text}")

root = tkinter.Tk()

root.geometry("400x400")

button1 = tkinter.Button(root, text="Stone", command=lambda: on_button_click("Stone"), width=20)
button1.grid(row=1, column=0, padx=10, pady=10)
message_label = tkinter.Label(root, text="", font=("David", 20), fg="blue")
message_label.grid(row=2, column=0, columnspan=3, pady=20)

button2 = tkinter.Button(root, text="Paper", command=lambda: on_button_click("Paper"),width=20)
button2.grid(row=1, column=1, padx=10, pady=10)
message_label = tkinter.Label(root, text="", font=("David", 20), fg="blue")
message_label.grid(row=2, column=0, columnspan=3, pady=20)

button3 = tkinter.Button(root, text="Scissor", command=lambda: on_button_click("Scissor"),width=20)
button3.grid(row=1, column=2, padx=10, pady=10)
message_label = tkinter.Label(root, text="", font=("David", 20), fg="blue")
message_label.grid(row=2, column=0, columnspan=3, pady=20)

root.mainloop()
