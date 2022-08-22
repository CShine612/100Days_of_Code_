from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Quiz_UI:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}")
        self.score_label.config(bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.check_false)
        self.false_button.grid(column=1, row=2)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.check_true)
        self.true_button.grid(column=0, row=2)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.quiz_text = self.canvas.create_text(150, 125, width=280, text=f"Question Here", fill=THEME_COLOR,
                                                 font=("Arial", 15, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=question_text)
        else:
            self.canvas.itemconfig(self.quiz_text, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_true(self):
        if self.quiz.check_answer("true"):
            self.score += 1
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


    def check_false(self):
        if self.quiz.check_answer("false"):
            self.score += 1
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
