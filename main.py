import tkinter


def miles_to_km():
    miles = int(entry_input.get())
    km = int(miles * 1.609)
    kilometer_result_label.config(text= km)


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

entry_input = tkinter.Entry(width=7)
entry_input.grid(column=1, row=0)

mile_label = tkinter.Label(text="Miles")
mile_label.grid(column=2, row=0)

new_label = tkinter.Label(text="is equal to")
new_label.grid(column=0, row=1)

kilometer_result_label = tkinter.Label(text="0")
kilometer_result_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

button = tkinter.Button(text="Calculate", command= miles_to_km)
button.grid(column=1, row=2)

window.mainloop()