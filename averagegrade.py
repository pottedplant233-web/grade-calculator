from statistics import mean
import re

def main():

    print(round(float(percentage(unit(), quiz()))))
def unit():
    unit_exam_grades = []
    while True:
        try:
            grade = input("unit exam grade(or done): ")
            matches_unit = re.search(r'^(?:[0-9]|[1-9][0-9]|100)$', grade)
            if matches_unit:
                unit_exam_grades.append(int(matches_unit.group()))
            elif grade.lower() == 'done':
                yes_no = input('Move to quiz?y/n:').strip()
                if yes_no.lower() == 'y':
                    average_unit = mean(unit_exam_grades)
                    return average_unit
                elif yes_no.lower() == 'n':
                    continue
                else:
                    continue

        except ValueError:
            pass
def quiz():
    quiz_grades = []
    while True:
        try:
            quiz_grade = input("quiz grade(or done): ").strip()
            matches_quiz = re.search(r'^(?:[0-9]|[1-9][0-9]|100)$', quiz_grade)
            if matches_quiz:
                quiz_grades.append(int(matches_quiz.group()))
            elif quiz_grade.lower() == 'done':
                yes_no_2 = input('Calculate avg?y/n:')
                if yes_no_2 == 'y':
                    average_quiz = mean(quiz_grades)
                    return average_quiz
                elif yes_no_2 == 'n':
                    continue
        except ValueError:
            pass

def percentage(x, y):
    percentage_wheighted = (x * 0.6 + y * 0.4)
    return percentage_wheighted

if __name__ == '__main__':
    main()




