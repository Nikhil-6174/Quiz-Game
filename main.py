from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for x in question_data:
    new_question = Question(x["question"],x["correct_answer"])
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz")
print(f"Your score is {quiz.score}/{quiz.question_number}")










# j = 0

# while j < len(question_bank):
#     print(question_bank[j].text)
#     print(question_bank[j].answer)
#     j += 1

# QuizBrain(question_bank)