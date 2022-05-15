from unittest import TestCase, main

from project.student import Student


class StudentTest(TestCase):
    def setUp(self) -> None:
        self.student = Student("Tina")

    def test_init_with_course_is_none(self):
        self.assertEqual("Tina", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_init_with_courses(self):
        self.student.courses = {"course_name": ["notes"]}
        self.assertEqual("Tina", self.student.name)
        self.assertEqual({"course_name": ["notes"]}, self.student.courses)

    def test_if_course_already_in_update_notes(self):
        stud = Student("Tina", {"maths": ["x", "y"]})
        x = stud.enroll("maths", ["x", "y"])
        self.assertEqual("Course already added. Notes have been updated.", x)
        self.assertEqual({"maths": ["x", "y", "x", "y"]}, stud.courses)

    def test_if_course_is_new_and_add_course_notes_is_yes(self):
        stud = Student("Tina", {"maths": ["x", "y"]})
        x = stud.enroll("Coding", ["x", "y"], "")
        self.assertEqual("Course and course notes have been added.", x)
        self.assertEqual({"maths": ["x", "y"], "Coding": ["x", "y"]}, stud.courses)

    def test_if_course_is_new_and_add_course_notes_is_empty(self):
        stud = Student("Tina", {"maths": ["x", "y"]})
        x = stud.enroll("Coding", ["x", "y"], "Y")
        self.assertEqual("Course and course notes have been added.", x)
        self.assertEqual({"maths": ["x", "y"], "Coding": ["x", "y"]}, stud.courses)

    def test_if_course_gets_added(self):
        stud = Student("Tina", {"maths": ["x", "y"]})
        x = stud.enroll("Coding", ["x", "y"], "N")
        self.assertEqual("Course has been added.", x)
        self.assertEqual({"maths": ["x", "y"], "Coding": []}, stud.courses)

    def test_add_notes_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("course_name", "notes")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_happy_case(self):
        stud = Student("Tina", {"maths": ["x", "y"]})
        stud.add_notes("maths", "x")
        self.assertEqual(["x", "y", "x"], stud.courses["maths"])

    def test_remove_course_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("course_name")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_remove_course_happy_case(self):
        stud = Student("Tina", {"maths": ["x", "y"]})
        stud.leave_course("maths")
        self.assertEqual({}, stud.courses)
