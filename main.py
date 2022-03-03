from question_model import question
from data import question_data
from quiz_brain import quizbrain
#initialize the data with constructor
#ask question
#move to next question
#check correctness
#score calculation
quesbank = []
for i in question_data:
    qtext = i["question"]
    qans = i['correct_answer']
    userques = question(qtext, qans)
    quesbank.append(userques)

quiz=quizbrain(quesbank)

while quiz.exhaust():
    quiz.nextquestion()
