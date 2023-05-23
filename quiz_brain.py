class Quiz_Brain:
    def __init__(self, question_list) -> None:
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        user_answer = input(f"{self.question_number + 1}. {self.question_list[self.question_number].text} (True/False)?: ")
        self.check_answer(self.question_list[self.question_number].answer, user_answer)
        self.question_number += 1
        print(f"Your current score is {self.get_score()}\n\n")
    
    def still_has_questions(self) -> bool:
        return self.question_number < (len(self.question_list) - 1)
    
    def check_answer(self, answer, user_answer):
        if answer.lower() == user_answer.lower():
            self.score += 1
            print("Yu got it right!")
        else:
            print(f"You got it wrong! Correct answer was {answer}")
    
    def get_score(self):
        return f"{self.score}/{self.question_number}"