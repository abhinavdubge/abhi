import tkinter as tk
#Main function
def on_button_click(value):
    global current_input
    if value=='x':
        value='*'
    if value == "=":
        try:
            result = str(eval(current_input))
            display_label.config(text=result)
            current_input = result  
        except:
            display_label.config(text="Error")
            current_input = ""
    else:
        if value == "-" and (current_input == "" or current_input[-1] in "+-*/("):
            current_input += value
        else:
            current_input += value
    if value=='clear':
        current_input=''
    display_label.config(text=current_input)

root=tk.Tk()
current_input=""


#GUI title

root.title("Calculator")

#GUI Size

root.geometry("240x350")

#GUI bg colour

root.configure(bg="Lightyellow")


# Response Screen
display_frame = tk.Frame(root, bg="lightblue", height=50, width=100)
display_frame.pack_propagate(False)  
display_frame.pack(fill="x") 

#Response

display_label = tk.Label(display_frame, text="", bg="lightblue", anchor="e", font=("David", 24))
display_label.pack(expand=True, fill="both", padx=10, pady=10)

#For buttons to work and appear

button_frame = tk.Frame(root)
button_frame.pack(fill="both", expand=True)

#Buttons
button1=tk.Button(button_frame, text='1',bg='LightPink',fg='Black',font=("David",18),height=1,width=3,command=lambda:on_button_click("1"))
button1.grid(row=0, column=0, padx=5, pady=5)

button2=tk.Button(button_frame, text='2',bg='LightPink',fg='Black',font=("David",18),height=1,width=3,command=lambda:on_button_click("2"))
button2.grid(row=0, column=1, padx=5, pady=5)

button3=tk.Button(button_frame, text='3',bg='LightPink',fg='Black',font=("David",18),height=1,width=3,command=lambda:on_button_click("3"))
button3.grid(row=0, column=2, padx=5, pady=5)

button4=tk.Button(button_frame, text='+',bg='LightPink',fg='Black',font=("David",18),height=1,width=3,command=lambda:on_button_click("+"))
button4.grid(row=0, column=3, padx=5, pady=5)

button5=tk.Button(button_frame, text='4',bg='LightPink',fg='Black',font=("David",18),height=1,width=3,command=lambda:on_button_click("4"))
button5.grid(row=1, column=0, padx=5, pady=5)

button6=tk.Button(button_frame, text='5',bg='LightPink',fg='Black',font=("David",18),height=1,width=3,command=lambda:on_button_click("5"))
button6.grid(row=1, column=1, padx=5, pady=5)

button7=tk.Button(button_frame, text='6',bg='LightPink',fg='Black',font=("David",18),height=1,width=3,command=lambda:on_button_click("6"))
button7.grid(row=1, column=2, padx=5, pady=5)

button8=tk.Button(button_frame, text='-',bg='LightPink',fg='Black',font=("David",18),height=1,width=3,command=lambda:on_button_click("-"))
button8.grid(row=1, column=3, padx=5, pady=5)

button9=tk.Button(button_frame, text='7',bg='LightPink',fg='Black',font=("David",18),height=1,width=3,command=lambda:on_button_click("7"))
button9.grid(row=2, column=0, padx=5, pady=5)

button10=tk.Button(button_frame, text='8',bg='LightPink',fg='Black',font=("David",18),height=1,width=3,command=lambda:on_button_click("8"))
button10.grid(row=2, column=1, padx=5, pady=5)

button11=tk.Button(button_frame, text='9',bg='LightPink',fg='Black',font=("David",18),height=1,width=3,command=lambda:on_button_click("9"))
button11.grid(row=2, column=2, padx=5, pady=5)

button12=tk.Button(button_frame, text='x',bg='LightPink',fg='Black',font=("David",18),height=1,width=3,command=lambda:on_button_click("x"))
button12.grid(row=2, column=3, padx=5, pady=5)

button13=tk.Button(button_frame, text='0',bg='LightPink',fg='Black',font=("David",18),height=1,width=3,command=lambda:on_button_click("0"))
button13.grid(row=3, column=0, padx=5, pady=5)

button14=tk.Button(button_frame, text='/',bg='LightPink',fg='Black',font=("David",18),height=1,width=3,command=lambda:on_button_click("/"))
button14.grid(row=3, column=1, padx=5, pady=5)

button15=tk.Button(button_frame, text='%',bg='LightPink',fg='Black',font=("David",18),height=1,width=3,command=lambda:on_button_click("%"))
button15.grid(row=3, column=2, padx=5, pady=5)

button16=tk.Button(button_frame, text='=',bg='LightPink',fg='Black',font=("David",18),height=1,width=3,command=lambda:on_button_click("="))
button16.grid(row=3, column=3, padx=5, pady=5)

button17=tk.Button(button_frame,text='clear',bg='LightPink',fg='Black',font=("David",18),height=1,width=3,command=lambda:on_button_click("clear"))
button17.grid(row=4,column=0,padx=10,pady=10)

root.mainloop()
