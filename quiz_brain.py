#TODO: asking the questions
#TODO: checking if the answer was correct
#TODO: checking if we're the end of the quiz

class QuizzBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.current_score = 0

    def next_question(self):
        current_quesiton = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_quesiton.text}. (True/False)?: ")
        self.check_answer(user_answer, current_quesiton.answer)

    def still_has_question(self):
        return len(self.question_list) > self.question_number

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.current_score += 1
        else:
            print("You're Wrong")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score: {self.current_score}/{self.question_number}")
        print("\n")
