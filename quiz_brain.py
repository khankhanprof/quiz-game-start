class quizbrain:
    def __init__(self,quesbank):
        self.quesbank=quesbank
        self.quesnumber=0
        self.score=0

    def exhaust(self):
        return self.quesnumber<len(self.quesbank)

    def nextquestion(self):
        question=self.quesbank[self.quesnumber]
        self.quesnumber+=1
        userans=input(f"Q{self.quesnumber}.{question.ques}(True/False)")
        self.checkans(userans,question.ans)

    def checkans(self,userans,currentans):
        if userans.lower()==currentans.lower():
            print("correct")
            self.score+=1
        else:
            print("incorrect")
        print(f"score:{self.score}/{self.quesnumber}")



