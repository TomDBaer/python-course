from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_question = Question(text=question['text'], answer=question['answer'])
    question_bank.append(new_question)

brain = QuizBrain(question_bank)

while brain.still_has_questions():
    brain.next_question()

print("You completed the quiz")
print(f"Your final score was: {brain.score}/{len(brain.question_list)}")