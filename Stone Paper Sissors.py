
import tkinter
import random

def on_button_click(button_text):
    comp_choice = assignnum(compchoice())
    result = Game(button_text, comp_choice)
    mesage=f"Comp chose: {comp_choice} \n You chose: {button_text} \n {result}"
    message_label.config(text=mesage)

def compchoice():
  a=random.randint(1,3)
  return a

def assignnum(a):
  if a==1:
    comp='Stone'
  elif a==2:
    comp='Paper'
  else:
    comp='Scissor'
  return comp

def Game(button_text,comp):
  if button_text==comp:
    return 'It is a tie'
  elif (button_text=='Stone' and comp=='Scissor')  or (button_text=='Paper' and comp=='Stone') or (button_text=='Scissor' and comp=='Paper'):
    return 'You Won'
  else:
    return 'You lost'
root = tkinter.Tk()

root.title("Stone Paper Scissor")

root.geometry("325x340")

w = tkinter.Label(root, text="Stone Paper Scissor", font=("David", 30), fg="red")
w.grid(row=0, column=0, columnspan=3, pady=20)

message_label = tkinter.Label(root, text="", font=("David", 20), fg="blue")
message_label.grid(row=2, column=0, columnspan=3, pady=20)

button1 = tkinter.Button(root, text="Stone",bg='Yellow',fg='Blue',font=("David", 10), command=lambda: on_button_click("Stone"), width=10,height=3)
button1.grid(row=1, column=0, padx=10, pady=10)

button2 = tkinter.Button(root, text="Paper",bg='Yellow',fg='Blue',font=("David", 10), command=lambda: on_button_click("Paper"), width=10,height=3)
button2.grid(row=1, column=1, padx=10, pady=10)

button3 = tkinter.Button(root, text="Scissor", bg='Yellow',fg='Blue',font=("David", 10),command=lambda: on_button_click("Scissor"), width=10,height=3)
button3.grid(row=1, column=2, padx=10, pady=10)

root.mainloop()
