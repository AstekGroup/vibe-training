
import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculette")

        self.total = tk.StringVar()
        self.entry = tk.Entry(master, textvariable=self.total, font=('Arial', 20), bd=10, insertwidth=4, width=14, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            self.create_button(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        self.create_button('C', 5, 0, columnspan=4)


    def create_button(self, text, row, col, columnspan=1):
        button = tk.Button(self.master, text=text, padx=20, pady=20, font=('Arial', 20), command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, columnspan=columnspan, sticky="nsew")

    def on_button_click(self, char):
        if char == 'C':
            self.total.set('')
        elif char == '=':
            try:
                result = eval(self.total.get())
                self.total.set(str(result))
            except:
                self.total.set('Erreur')
        else:
            self.total.set(self.total.get() + char)

if __name__ == '__main__':
    root = tk.Tk()
    my_gui = Calculator(root)
    root.mainloop()
