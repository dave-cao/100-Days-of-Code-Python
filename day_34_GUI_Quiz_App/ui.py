import tkinter as tk

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # images
        y_button_img = tk.PhotoImage(file="./images/true.png")
        x_button_img = tk.PhotoImage(file="./images/false.png")

        # score label
        self.score_label = tk.Label(
            text="Score: 0", font=("Courier", 10), bg=THEME_COLOR, fg="white"
        )
        self.score_label.grid(column=1, row=0)

        # middle question section
        self.canvas = tk.Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question text",
            fill=THEME_COLOR,
            font=("Courier", 20, "italic"),
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # buttons
        self.y_button = tk.Button(
            image=y_button_img, highlightthickness=0, command=self.pressed_y
        )
        self.y_button.grid(column=0, row=2)
        self.x_button = tk.Button(
            image=x_button_img, highlightthickness=0, command=self.pressed_x
        )
        self.x_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You've reached the end of the quiz"
            )
            self.y_button.config(state="disabled")
            self.x_button.config(state="disabled")

    def pressed_y(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def pressed_x(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
