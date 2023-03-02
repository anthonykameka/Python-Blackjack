# simple true/false quiz game

from question_model import Question

from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question = Question(question_text, question_answer)
    question_bank.append(question)


quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
