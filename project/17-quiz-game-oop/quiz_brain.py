class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
    
    def still_has_question(self):
        return self.question_number < len(self.question_list)
        ## Code could be simplified as above
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question.text} (True/False)?")