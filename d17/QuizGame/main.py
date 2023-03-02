from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = [] #list of question objects



for key in question_data:
    text = key["question"]
    answer = key["correct_answer"]
    question = Question(answer=answer, text=text)
    question_bank.append(question)


quizbrain = QuizBrain(question_bank)
while quizbrain.still_has_questions():
    quizbrain.next_question()

print("You have completed the quiz")
print(f"Your final score is {quizbrain.score}/{quizbrain.question_no}")
#Requirement
#Loop through List and ask user to answer
#get the answer from user and check with correct answer
#return success or failure
#Question No and True/False in the question

