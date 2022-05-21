from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class StudentTest(TestCase):
    def setUp(self) -> None:
        self.student = StudentReportCard("Samuil", 10)

    def test_init_happy_case(self):
        stud = StudentReportCard("Samuil", 12)
        self.assertEqual("Samuil", stud.student_name)
        self.assertEqual(12, stud.school_year)
        self.assertEqual({}, stud.grades_by_subject)

    def test_init_happy_case_border(self):
        stud = StudentReportCard("Samuil", 1)
        self.assertEqual("Samuil", stud.student_name)
        self.assertEqual(1, stud.school_year)
        self.assertEqual({}, stud.grades_by_subject)

    def test_init_empty_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            StudentReportCard("", 10)
        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

    def test_init_incorrect_school_year_raises(self):
        with self.assertRaises(ValueError) as ex:
            StudentReportCard("Saaaa", 17)
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_add_grade_happy_case(self):
        self.student.add_grade("Maths", 6)
        self.assertEqual({"Maths": [6]}, self.student.grades_by_subject)

    def test_add_grade_when_subject_there_happy_case(self):
        self.student.add_grade("Maths", 6)
        self.student.add_grade("Maths", 6)
        self.assertEqual({"Maths": [6, 6]}, self.student.grades_by_subject)

    def test_average_grade_returns(self):
        self.student.add_grade("Maths", 6)
        self.student.add_grade("Maths", 2)
        x = self.student.average_grade_by_subject()
        self.assertEqual("Maths: 4.00", x)

    def test_average_grade_all_subjects_returns(self):
        self.student.add_grade("Maths", 6)
        self.student.add_grade("Maths", 2)
        self.student.add_grade("Geo", 4)
        x = self.student.average_grade_for_all_subjects()
        self.assertEqual("Average Grade: 4.00", x)

    def test_repr(self):
        self.student.add_grade("Maths", 6)
        self.student.add_grade("Maths", 2)
        self.student.add_grade("Geo", 4)
        self.student.average_grade_by_subject()
        self.student.average_grade_for_all_subjects()
        z = self.student.__repr__()
        self.assertEqual("Name: Samuil\nYear: 10\n----------\nMaths: 4.00\nGeo: 4.00\n----------\nAverage Grade: 4.00", z)
