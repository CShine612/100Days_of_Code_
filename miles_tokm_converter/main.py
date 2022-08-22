import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

input = tkinter.Entry()
input.config(width=7)
input.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

equals_label = tkinter.Label(text="is equal to")
equals_label.grid(column=0, row=1)

ans_label = tkinter.Label(text="0")
ans_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

def calculate():
    ans_label.config(text=f"{int(input.get())*1.609}")

button = tkinter.Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

tkinter.mainloop()
