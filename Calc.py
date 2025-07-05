import tkinter as tk
from tkinter import ttk
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jcreeper's Calculator")
        self.geometry("400x600")
        self.resizable(False, False)
        self.configure(bg="#2e2e2e")

        self.expression = ""
        self.create_widgets()

        self.bind("<Key>", self.key_input)
        self.bind("<Return>", lambda event: self.on_button_click('='))
        self.bind("<BackSpace>", lambda event: self.backspace())
        self.bind("<Escape>", lambda event: self.clear())

    def create_widgets(self):
        self.entry = tk.Entry(self, font=("Arial", 24), borderwidth=5, relief=tk.FLAT, bg="#1e1e1e", fg="white", justify='right')
        self.entry.pack(padx=10, pady=20, fill=tk.X)

        btn_frame = tk.Frame(self, bg="#2e2e2e")
        btn_frame.pack()

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+'),
        ]

        for row in buttons:
            row_frame = tk.Frame(btn_frame, bg="#2e2e2e")
            row_frame.pack(expand=True, fill='both')
            for btn_text in row:
                btn = tk.Button(row_frame, text=btn_text, font=("Arial", 20), fg="white", bg="#3a3a3a",
                                relief=tk.RAISED, borderwidth=1, activebackground="#505050",
                                command=lambda x=btn_text: self.on_button_click(x))
                btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)

        sci_frame = tk.LabelFrame(self, text="Scientific", font=("Arial", 14), bg="#2e2e2e", fg="white")
        sci_frame.pack(padx=10, pady=10, fill='both')

        sci_buttons = [
            ('sin', 'cos', 'tan', 'sqrt'),
            ('log', 'ln', '^', '%'),
        ]

        for row in sci_buttons:
            row_frame = tk.Frame(sci_frame, bg="#2e2e2e")
            row_frame.pack(expand=True, fill='both')
            for btn_text in row:
                btn = tk.Button(row_frame, text=btn_text, font=("Arial", 16), fg="white", bg="#4a4a4a",
                                relief=tk.RAISED, borderwidth=1, activebackground="#505050",
                                command=lambda x=btn_text: self.on_scientific_click(x))
                btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)

    def on_button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.expression))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
                self.expression = result
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)

    def on_scientific_click(self, func):
        try:
            if func == 'sin':
                value = math.sin(math.radians(float(self.entry.get())))
            elif func == 'cos':
                value = math.cos(math.radians(float(self.entry.get())))
            elif func == 'tan':
                value = math.tan(math.radians(float(self.entry.get())))
            elif func == 'sqrt':
                value = math.sqrt(float(self.entry.get()))
            elif func == 'log':
                value = math.log10(float(self.entry.get()))
            elif func == 'ln':
                value = math.log(float(self.entry.get()))
            elif func == '^':
                self.expression += '**'
                self.entry.insert(tk.END, '^')
                return
            elif func == '%':
                value = float(self.entry.get()) / 100
            else:
                return

            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(value))
            self.expression = str(value)
        except Exception:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")
            self.expression = ""

    def key_input(self, event):
        allowed_keys = '0123456789+-*/.^%'
        if event.char in allowed_keys:
            self.expression += event.char
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)
        elif event.keysym == 'Return':
            self.on_button_click('=')
        elif event.keysym == 'BackSpace':
            self.backspace()
        elif event.keysym == 'Escape':
            self.clear()

    def backspace(self):
        self.expression = self.expression[:-1]
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
