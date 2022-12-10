class QuizBrain:
    def __init__(self, question_list):
        """Initialize asking the questions and it's methods
        question_list(list of objects): a list of Question objects"""
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        """Ask the next question and update question number"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False)?: "
        )
        self.check_answer(answer, current_question.answer)

    def still_has_questions(self):
        """Returns True if still have questions left. False otherwise"""
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"The correct answer was: {question_answer}")
        print(f"The current score is: {self.score}/{self.question_number}")

    def final_score(self):
        """Prints out the final score"""
        print("You've completed the quiz.")
        print(f"The final score is: {self.score}/{self.question_number}")
