import csv

class Trivia():
    def __init__(self):
        pass
        # self.questions = []
    @staticmethod
    def load_solo_questions(file_path):
        trivia_questions = []
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                question = row[0]
                answer = row[1]
                trivia_questions.append({'question': question, 'answer': answer})
        return trivia_questions
    @staticmethod
    def load_multiple_questions(file_path):
        trivia_questions = []
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                question = row[0]
                correct_answer = row[1]
                wrong_answers = row[2:]  # Extract wrong answer choices
                trivia_questions.append({'question': question, 'correct_answer': correct_answer, 'wrong_answers': wrong_answers})
        return trivia_questions