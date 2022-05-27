import json
from bot_create import cursor
from handlers import tests

user_data = {}
user_task = {}
user_numoftests = {}
subject_list = ["Math", "OOP", "ASD"]

class MyClass:
    num2 = int(0)
    num3 = int(0)
    numoftest = int(0)
    numoftests = int(0)
    subject = ""

async def count_tests(line):
    sql = "SELECT * FROM teachers_tests WHERE test_subject = %s"
    MyClass.numoftests = cursor.execute(sql, line)

async def get_info():
    sql = "SELECT * FROM teachers_tests WHERE test_owner = %s AND test_subject = %s AND test_name = %s"
    cursor.execute(sql, (0, MyClass.subject, "Тест " + str(MyClass.numoftest + 1)))
    for row in cursor:
        json_string = row["test_info"]
    # parse x:
    json_string_decoded = json.loads(json_string)
    # the result is a Python dictionary:
    tests.answerstring = json_string_decoded["answerstring"]
    tests.numofquestions = json_string_decoded["numofquestions"]
    tests.question = json_string_decoded["question"]
    tests.question_value = json_string_decoded["question_value"]
    tests.answervarA = json_string_decoded["answervarA"]
    tests.answervarB = json_string_decoded["answervarB"]
    tests.answervarC = json_string_decoded["answervarC"]
    tests.answervarD = json_string_decoded["answervarD"]