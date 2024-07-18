import unittest
from student import Student
from datetime import timedelta
from unittest.mock import patch

class TestStudent(unittest.TestCase):

    def setUp(self):
        print('setUP')
        self.student = Student('Joe', 'Bloggs')
        

    def tearDown(self):
        print('tearDown')
    
    def test_full_name(self):
        self.assertEqual(self.student.full_name, 'Joe Bloggs')

    def test_alert_santa(self):
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)
    
    def test_email(self):

        self.assertEqual(self.student.email, 'joe.bloggs@email.com')

    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(5)
        self.assertEqual(self.student.end_date, old_end_date + timedelta(days = 5))
    
    def course_schedule_success(self):
        with patch('students.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_sechedule()
            self.assertEqual(schedule, 'Success')
    
    
    def course_schedule_fail(self):
        with patch('students.requests.get') as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_sechedule()
            self.assertEqual(schedule, "Something went wrong with the request.")

if __name__== '__main__':
    unittest.main()