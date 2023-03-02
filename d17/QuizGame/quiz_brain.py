# create a class QuizBrain
# question number initialize
# accept list from main class
# implement the next_question method

class QuizBrain:
    def __init__(self, question_list):
        self.question_no = 0
        self.question_list = question_list
        self.score = 0

    # still_has_question : true or false if there are more questions
    def still_has_questions(self):
        size = len(self.question_list)
        if self.question_no < size:
            return True
        else:
            # print("You have completed the quiz")
            # print(f"Your final score was:{self.score}/{self.question_no}")
            return False

    def check_answer(self, user_answer, exp_answer):

        if user_answer.lower() == exp_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("That is wrong")
        print(f"The correct answer is {exp_answer}")
        print(f"Your score is {self.score}/{self.question_no}\n")

    def next_question(self):
        question = self.question_list[self.question_no]
        answer = input(f"Q.{self.question_no + 1}: {question.text} (True/False)?: ")
        self.question_no += 1
        self.check_answer(answer, question.answer)


# create New method check_answer
# check if the question list answer and answer from user matches
# keep track of the score
 