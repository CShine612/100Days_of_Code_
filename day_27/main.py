import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(500, 300)
window.config(padx=20, pady=20)

my_label = tkinter.Label(text="Im a label", font=("Arial", 24, "bold"))
my_label.grid(column=1, row=1)
my_label.config(padx=50, pady=50)


def button_clicked():
    my_label["text"] = input.get()


button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(column=2, row=2)

new_button = tkinter.Button(text="New button", command=button_clicked)
new_button.grid(column=3, row=1)

input = tkinter.Entry()
input.config(width=7)
input.grid(column=4, row=3)

window.mainloop()
