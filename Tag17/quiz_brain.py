class QuizBrain:
    def __init__(self, q_list):
        self.question_number: int = 0
        self.question_list = q_list
        self.score: int = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").capitalize()
        # Call method
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, c_answer):
        if answer == c_answer:
            self.score += 1
        print(f"Your current score is {self.score}/{self.question_number}")


