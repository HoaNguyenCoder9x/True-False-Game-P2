from data import question_data
from question_model import Question
from quiz_brain import QuizzBrain

question_bank = []
for i in question_data:
    question = i['question']
    answer = i['correct_answer']
    new_q = Question(question, answer)
    question_bank.append(new_q)

quizz = QuizzBrain(question_bank)

while quizz.still_has_question():
    quizz.next_question()

print("You completed the quizz")
print(f"Your final score: {quizz.current_score}/{quizz.question_number}")
