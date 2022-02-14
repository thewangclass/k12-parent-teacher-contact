import pandas as pd
from student_grade_data import StudentGradeData

FILE_NAME = 'data/test_data.xlsx'


def format_name(student_name, contact):
    try:
        student_nameList = [names.strip() for names in student_name[contact].split(',')]
        return student_nameList[-1] + " " + student_nameList[0]
    except AttributeError:
        print(student_name[contact])


class DataManager:
    def __init__(self):
        self.grades_data = {}
        self.students_list = []

    def get_grades_data(self, spreadsheet, sheet_name):
        df = pd.read_excel(spreadsheet, sheet_name=sheet_name)
        self.grades_data = df.to_dict(orient='records')
        self.create_students_list()
        return self.students_list

    def create_students_list(self):
        self.students_list = []
        for student in self.grades_data:
            student_obj = StudentGradeData(
                student_name=format_name(student, 'Student Name'),
                student_ID=student['Student ID'],
                student_Email=student['Student Email'],
                advisor=student['Advisor'],
                guardian_name=format_name(student, 'Guardian Name'),
                guardian_phone=student['Guardian Phone'],
                guardian_email=student['Guardian Email'],
                grade_average=student['Grade Average']
            )
            self.students_list.append(student_obj)

    def update_grades_contact_attempt(self):
        pass

    # Don't think csv allows formulas to carry over, so this is just in case
    def update_grades(self):
        pass
