import tkinter as tk
from tkinter import PhotoImage

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quiz")
        self.window.config(background=THEME_COLOR,padx=20,pady=20)
        self.score_label = tk.Label(text="Score: 0", fg="white", font=("Arial", 16, "bold"), bg=THEME_COLOR)
        self.score_label.grid(column=0, row=0)
        self.canvas = tk.Canvas(width=300,height=250,bg="white")
        self.question_bar = self.canvas.create_text(150, 125, text="Question comes here", fill=THEME_COLOR,font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, pady=50, columnspan=2)
        true_image = PhotoImage(file="./images/true.png")
        self.true_button = tk.Button(image=true_image,borderwidth=0,highlightthickness=0)
        self.true_button.grid(column=0, row=2)
        false_image = PhotoImage(file="./images/false.png")
        self.false_button = tk.Button(image=false_image, borderwidth=0, highlightthickness=0)
        self.false_button.grid(column=1, row=2)


        self.window.mainloop()