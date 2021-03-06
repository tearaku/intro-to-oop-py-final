from ast import literal_eval
from Model.question import Choice, MultipleChoice, ChoiceOption, Question, ShortAnswer
from typing import List, Dict

from Model.question_type import QuestionType


# TODO: validating & cleaning user input
class QuestionFactory():
    def __init__(self) -> None:
        pass
    def createQuestion(self, qDes: str, qAns: str) -> Question:
        pass

class ShortAnswerFactory(QuestionFactory):
    # Expected input format:
    # qDes: the question string itself
    # qAns: the answer string itself
    def createQuestion(self, qDes: str, qAns: str) -> Question:
        return ShortAnswer(qDes, qAns)

class ChoiceFactory(QuestionFactory):
    # Expected input format:
    # qDes: str evaluated w/ ast into dict{"question": ..., "options": ["option1", "option2", "option3"]}
    # qAns: str evaluated w/ ast into List[bool], only 1 True
    def createQuestion(self, qDes: str, qAns: str) -> Question:
        # Parsing inputs
        qDict = literal_eval(qDes)
        qAnsStat = literal_eval(qAns)
        # Creating ChoiceOption
        qOptList: List[ChoiceOption] = []
        for optStr, isAns in zip(qDict["options"], qAnsStat):
            qOptList.append(ChoiceOption(optStr, isAns))
        return Choice(qDict["question"], qOptList)

class MultipleChoiceFactory(QuestionFactory):
    # Expected input format:
    # qDes: str evaluated w/ ast into dict{"question": ..., "options": ["option1", "option2", "option3"]}
    # qAns: str evaluated w/ ast into List[bool], may contain multiple True
    def createQuestion(self, qDes: str, qAns: str) -> Question:
        # Parsing inputs
        qDict = literal_eval(qDes)
        qAnsStat = literal_eval(qAns)
        # Creating ChoiceOption
        qOptList: List[ChoiceOption] = []
        for optStr, isAns in zip(qDict["options"], qAnsStat):
            qOptList.append(ChoiceOption(optStr, isAns))
        return MultipleChoice(qDict["question"], qOptList)
