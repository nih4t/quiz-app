import tkinter as tk
from tkinter.constants import DISABLED, NORMAL

from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quiz")
        self.window.config(background=THEME_COLOR,padx=20,pady=20)
        self.score_label = tk.Label(text="Score: 0", fg="white", font=("Arial", 16, "bold"), bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        self.canvas = tk.Canvas(width=300,height=250,bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question comes here", font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, pady=50, columnspan=2)
        true_image = tk.PhotoImage(file="./images/true.png")
        self.true_button = tk.Button(image=true_image,borderwidth=0, command=self.clicked_true,highlightthickness=0)
        self.true_button.grid(column=0, row=2)
        false_image = tk.PhotoImage(file="./images/false.png")
        self.false_button = tk.Button(image=false_image,command=self.clicked_false, borderwidth=0, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.true_button.config(state=NORMAL)
        self.false_button.config(state=NORMAL)
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached end of the quiz. \n\n"
                                                            f"Your score: {self.quiz.score}")
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)
            self.score_label.config(fg=THEME_COLOR)

    def clicked_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def clicked_false(self):
        self.give_feedback(self.quiz.check_answer("False"))


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.true_button.config(state=DISABLED)
        self.false_button.config(state=DISABLED)

        self.canvas.update()
        self.window.after(1000, self.get_next_question())


