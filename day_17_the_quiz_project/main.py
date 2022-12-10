from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# for loop to iterate over question data
question_bank = []
for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

if not quiz.still_has_questions():
    quiz.final_score()
