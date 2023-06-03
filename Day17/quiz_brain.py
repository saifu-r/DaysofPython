class QuizBrain:
    def __init__(self, question_list):
        self.question_number= 0
        self.question_list= question_list
        self.score= 0

    def next_question(self):
        current_question= self.question_list[self.question_number]
        self.question_number+=1
        user_answer= input(f"Q.{self.question_number} {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        return self.question_number!=12


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower()== correct_answer.lower():
            print("You got it right! ")
            self.score+= 1
        else:
            print("That's a wrong answer.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}\n\n")

    def final_statement(self):
        print("Your have completed the quiz.")
        print(f"Your final score was {self.score}/12")

