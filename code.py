import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x600")
        self.resizable(False, False)
        self.configure(bg="#2e2e2e")

        self.expression = ""
        self.display_var = tk.StringVar()

        self._create_widgets()

    def _create_widgets(self):
        self._create_display()
        self._create_buttons()

    def _create_display(self):
        display_frame = tk.Frame(self, bg="#2e2e2e")
        display_frame.pack(expand=True, fill="both")

        display = tk.Entry(display_frame, textvariable=self.display_var, font=("Arial", 48), bg="#2e2e2e", fg="white", bd=0, justify="right")
        display.pack(expand=True, fill="both", padx=10, pady=20)

    def _create_buttons(self):
        buttons_frame = tk.Frame(self, bg="#2e2e2e")
        buttons_frame.pack(expand=True, fill="both")

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0, 4)
        ]

        for (text, row, col, *span) in buttons:
            self._create_button(text, row, col, span[0] if span else 1, buttons_frame)

    def _create_button(self, text, row, col, span, parent):
        if text == '=':
            btn = tk.Button(parent, text=text, font=("Arial", 24), command=self._calculate, bg="#ff9500", fg="white", bd=0)
        elif text == 'C':
            btn = tk.Button(parent, text=text, font=("Arial", 24), command=self._clear, bg="#d4d4d2", fg="black", bd=0)
        elif text in ['/', '*', '-', '+']:
            btn = tk.Button(parent, text=text, font=("Arial", 24), command=lambda t=text: self._on_button_click(t), bg="#ff9500", fg="white", bd=0)
        else:
            btn = tk.Button(parent, text=text, font=("Arial", 24), command=lambda t=text: self._on_button_click(t), bg="#505050", fg="white", bd=0)
        
        btn.grid(row=row, column=col, columnspan=span, sticky="nsew", padx=5, pady=5)
        parent.grid_columnconfigure(col, weight=1)
        parent.grid_rowconfigure(row, weight=1)

    def _on_button_click(self, char):
        self.expression += str(char)
        self.display_var.set(self.expression)

    def _clear(self):
        self.expression = ""
        self.display_var.set("")

    def _calculate(self):
        try:
            result = str(eval(self.expression))
            self.display_var.set(result)
            self.expression = result
        except:
            self.display_var.set("Error")
            self.expression = ""

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
