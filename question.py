import string
import re
import json
from dataclasses import dataclass, field, asdict

example_question = """A company has many AWS accounts that individual business groups own. One of the accounts was
recently compromised. The attacker launched a large number of instances, resulting in a high bill for that
account.
The company addressed the security breach, but a solutions architect needs to develop a solution to
prevent excessive spending in all accounts. Each business group wants to retain full control of its AWS
account.
Which solution should the solutions architect recommend to meet these requirements?
A) Use AWS Organizations. Add each AWS account to the management account. Create an SCP that uses
the ec2:instanceType condition key to prevent the launch of high-cost instance types in each account.
B) Attach a new customer-managed IAM policy to an IAM group in each account. Configure the policy to use
the ec2:instanceType condition key to prevent the launch of high-cost instance types. Place all the
existing IAM users in each group.
C) Turn on billing alerts for each AWS account. Create Amazon CloudWatch alarms that send an Amazon
Simple Notification Service (Amazon SNS) notification to the account administrator whenever the account
exceeds a designated spending threshold.
D) Turn on AWS Cost Explorer in each account. Review the Cost Explorer reports for each account on a
regular basis to ensure that spending does not exceed the desired amount.

Correct Answer: CD """


@dataclass
class Question:
    question: str = ''
    answers: list = field(default_factory=list)
    question_type: bool = 0
    right_answer: str = ''


class ParsedQuestion:
    parsed_question = Question()

    def __init__(self, raw_text: str = None):
        if raw_text:
            a_pattern = self.get_a_pattern(raw_text)  # Defining Answers pattern
            explanation = self.get_explanation(raw_text) # Looking for Explanation
            right_answers = self.get_right_answer(raw_text) # Looking for Right Answers
            question = self.remove_right_answers(raw_text, right_answers)
            answers_pos = question.find(f"A{a_pattern}")

            self.parsed_question.question = question[:answers_pos]
            self.parsed_question.answers = self.parse_answers(question[answers_pos:], a_pattern, right_answers)
            self.parsed_question.question_type = self.get_question_type(self.parsed_question.question)
            self.parsed_question.question = self.trim_txt(self.parsed_question.question)
            self.parsed_question.explanation = explanation

    # Split to lines, check if line contains "answer:" than delete line and join back into long string
    @staticmethod
    def remove_right_answers(q_txt: str, right_answers: list) -> str:
        if right_answers:
            q_txt = '\n'.join([_ for _ in q_txt.splitlines() if _.lower().find('answer:') < 0])
        return q_txt

    @staticmethod
    def get_right_answer(raw_text: str) -> list:
        res = []
        for i in raw_text.splitlines():
            if i.lower().find('answer:') >= 0:
                for ans in [*i[i.find(':'):].strip()]:
                    if ans in string.ascii_uppercase:
                        res.append(ans)
        return res

    @staticmethod
    def trim_txt(txt: str) -> string:
        txt = re.sub(r'[^\.](\n)[^A]', " ", txt)
        return txt.strip()

    @staticmethod
    def get_a_pattern(raw_text: str) -> str:
        pattern = ''
        if raw_text.find("A) ") >= 0 and raw_text.find("B) ") > 0:
            pattern = ") "
            return pattern
        if raw_text.find("A. ") >= 0 and raw_text.find("B. ") > 0:
            pattern = ". "
            return pattern
        return pattern

    @staticmethod
    def get_question_type(q_txt: str) -> int:  # 0 - Singe chose, 1 - Multi chose
        if q_txt.lower().find(" (select") >= 0:
            return 1
        return 0

    @staticmethod
    def parse_answers(a_txt: str, pattern: str, right_answers: list) -> list:
        result = []
        for _ in string.ascii_uppercase:
            pos_start = a_txt.find(f"{_}{pattern}")
            pos_end = a_txt.find(f"{_}{pattern}", pos_start + 1)
            if pos_end >= 0:
                if q := a_txt[:pos_end].strip():
                    result.append([q, 1 if _ in right_answers else 0])
                    a_txt = a_txt[pos_end:]
            else:
                result.append([a_txt.strip(), 1 if _ in right_answers else 0])
                break
        return result

    @staticmethod
    def get_explanation(self, raw_text):
        lines = raw_text.splitlines()
        for i in range(len(lines)):
            if lines[i].lower().find('Explanation:') >= 0:
                return ' '.join(lines[i:]).strip()
        return ''


if __name__ == "__main__":
    with open('pdf/saa-c03.2023-jan-08.txt') as f:
        text = f.read()
    questions_pattern = re.compile(r'\b(?:NEW QUESTION\s+\d+)')
    questions_txt_lst = questions_pattern.split(text)[1:]
    questions = [ParsedQuestion(i).parsed_question for i in questions_txt_lst]

    for i in questions:
        print(i.__dict__)
        print('-' * 20)

    exit()
