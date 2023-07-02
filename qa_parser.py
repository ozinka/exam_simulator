import string
import re

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
regular basis to ensure that spending does not exceed the desired amount."""


def parse_question(q_txt: str) -> list:
    q_pattern = get_q_pattern(q_txt)
    answer_pos = q_txt.find(f"A{q_pattern}")
    question = q_txt[:answer_pos]
    answers = parse_answers(q_txt[answer_pos:], q_pattern)
    question_type = get_question_type(question)
    right_answers = get_right_answer(question)
    question = trim_txt(question)
    return [question, answers, question_type, right_answers]


def get_right_answer(q_txt: str) -> list:
    return []

def trim_txt(txt: str) -> string:
    txt = re.sub(r'[^\.](\n)[^A]', " ", txt)
    return txt

def get_q_pattern(q_txt: str) -> str:
    pattern = ''
    if q_txt.find("A) ") >= 0 and q_txt.find("B) ") > 0:
        pattern = ") "
        return pattern
    if q_txt.find("A. ") >= 0 and q_txt.find("B. ") > 0:
        pattern = ". "
        return pattern
    return pattern


def get_question_type(q_txt: str) -> int:  # 0 - Singe chose, 1 - Multi chose
    if q_txt.lower().find(" (select") >= 0:
        return 1
    return 0


def parse_answers(a_txt: str, pattern: str) -> list:
    result = []
    for i in string.ascii_uppercase:
        pos = a_txt.find(f"{i}{pattern}")
        if pos >= 0:
            if a_txt[:pos].strip():
                result.append(a_txt[:pos].strip())
                a_txt = a_txt[pos:]
        else:
            result.append(a_txt.strip())
            break
    return result


if __name__ == "__main__":
    for i in parse_question(example_question)[1]:
        print(i)
        print('-')
