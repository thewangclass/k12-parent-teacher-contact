class StudentGradeData:

    def __init__(self, student_name, student_ID, student_Email, advisor, guardian_name, guardian_phone, guardian_email,
                 grade_average):
        self.student_name = student_name
        self.student_ID = student_ID
        self.student_Email = student_Email
        self.advisor = advisor
        self.guardian_name = guardian_name
        self.guardian_phone = guardian_phone
        self.guardian_email = guardian_email
        self.grade_average = grade_average
        self.gradeList = {}
        pass
