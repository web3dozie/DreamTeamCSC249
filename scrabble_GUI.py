import tkinter as tk
from tkinter import ttk
from scrabble_app import ScrabbleApp


class ScrabbleGUI(tk.Tk):
    def __init__(self, app):
        super().__init__()

        self.execute_button = None
        self.result_label = None
        self.input_entry = None
        self.input_label = None
        self.function_menu = None
        self.function_var = None
        self.function_label = None
        self.logo_label = None
        self.logo_image = None
        self.scrabble_app = app

        self.title("Scrabble App")
        self.geometry("400x400")

        self.create_widgets()

    def create_widgets(self):
        self.logo_image = tk.PhotoImage(file="scrabble_logo.png")

        self.logo_label = ttk.Label(self, image=self.logo_image)
        self.logo_label.pack(pady=10)

        self.function_label = ttk.Label(self, text="Select a function:")
        self.function_label.pack(pady=10)

        self.function_var = tk.StringVar()
        self.function_menu = ttk.Combobox(self, textvariable=self.function_var, values=["Add word", "Remove word", "Check word", "Find words", "Word score"])
        self.function_menu.pack(pady=10)

        self.input_label = ttk.Label(self, text="Enter input:")
        self.input_label.pack(pady=10)

        self.input_entry = ttk.Entry(self)
        self.input_entry.pack(pady=10)

        self.result_label = ttk.Label(self, text="")
        self.result_label.pack(pady=10)

        self.execute_button = ttk.Button(self, text="Execute", command=self.execute_function)
        self.execute_button.pack(pady=10)

    def execute_function(self):
        function = self.function_var.get()
        input_value = self.input_entry.get()

        if function == "Add word":
            self.scrabble_app.add_word(input_value)
            self.result_label.config(text="Word added successfully.")

        elif function == "Remove word":
            self.scrabble_app.remove_word(input_value)
            self.result_label.config(text="Word removed successfully.")

        elif function == "Check word":
            is_valid = self.scrabble_app.is_valid_word(input_value)
            self.result_label.config(text=f"This word is {'valid' if is_valid else 'invalid'}.")

        elif function == "Find words":
            words = self.scrabble_app.find_words_from_letters(input_value)
            self.result_label.config(text=f"Found words: {', '.join(words)}")

        elif function == "Word score":
            score = self.scrabble_app.word_score(input_value)
            self.result_label.config(text=f"The score for this word is {score}.")


if __name__ == "__main__":
    scrabble_app = ScrabbleApp()
    scrabble_gui = ScrabbleGUI(scrabble_app)
    scrabble_gui.mainloop()
