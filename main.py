from data import question_data
from question_model import Question
from quiz_brain import Quiz_Brain

if __name__ == '__main__':
    question_bank = [ Question(x["question"], x["correct_answer"]) for x in question_data]
    quiz_brain  = Quiz_Brain(question_bank)
    print("\n")
    while quiz_brain.still_has_questions():
        quiz_brain.next_question()
    print("You have completed the quiz")
    print(f"your final score was {quiz_brain.get_score()}")
    print("\n\n")

         